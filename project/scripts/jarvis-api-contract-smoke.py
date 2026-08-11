#!/usr/bin/env python3
"""Smoke-test the generic provider-disabled compatibility API in-process."""

from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
API_ROOT = REPO_ROOT / "api"
sys.path.insert(0, str(API_ROOT))

import _jarvis_contract as contract  # noqa: E402


API_FILES = (
    API_ROOT / "_jarvis_contract.py",
    API_ROOT / "health.py",
    API_ROOT / "models.py",
    API_ROOT / "chat.py",
    API_ROOT / "config" / "roles.py",
    API_ROOT / "lanes" / "prd-icp.py",
    API_ROOT / "lanes" / "agent-orchestra.py",
)
EXPECTED_ADAPTERS = (
    ("review_packet", "available"),
    ("role_projection", "available"),
    ("browser_local_handoff", "available"),
    ("provider_execution", "disabled"),
    ("external_writeback", "disabled"),
)


def import_file(path: Path) -> None:
    name = "contract_smoke_" + "_".join(path.relative_to(API_ROOT).parts).replace("-", "_").replace(".", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path.relative_to(REPO_ROOT)}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(name, None)


def assert_zero_effects(label: str, payload: dict[str, object], failures: list[str]) -> None:
    runtime = payload.get("runtime")
    if not isinstance(runtime, dict):
        failures.append(f"{label}: runtime boundary missing")
        return
    expected = {
        "execution_mode": "provider_disabled",
        "provider_calls": 0,
        "network_calls": 0,
        "external_writeback": 0,
        "external_actions": 0,
    }
    if runtime != expected:
        failures.append(f"{label}: runtime boundary drifted")


def assert_auth_before_body_read(failures: list[str]) -> None:
    events: list[str] = []

    class Stub:
        headers: dict[str, str] = {}

        def route(self, method: str, body: contract.ServerRequest) -> dict[str, object]:
            events.append("route")
            return contract.packet("test", "ok", {"method": method})

    denied = Stub()

    def deny(_handler: object) -> SimpleNamespace:
        events.append("authenticate")
        return SimpleNamespace(authorized=False, status=401, error="authentication_required")

    def forbidden_read(_handler: object) -> dict[str, object]:
        events.append("read")
        raise AssertionError("body read before authentication")

    def capture_send(_handler: object, _payload: object, status: int = 200) -> None:
        events.append(f"send:{status}")

    with (
        mock.patch.object(contract, "authorize_admin_handler", side_effect=deny),
        mock.patch.object(contract, "read_json_body", side_effect=forbidden_read),
        mock.patch.object(contract, "send_json", side_effect=capture_send),
    ):
        contract.JsonHandler.do_POST(denied)  # type: ignore[arg-type]
    if events != ["authenticate", "send:401"]:
        failures.append(f"denied request order drifted: {events}")

    events.clear()
    accepted = Stub()

    def allow(_handler: object) -> SimpleNamespace:
        events.append("authenticate")
        return SimpleNamespace(authorized=True, status=200, error="")

    def read(_handler: object) -> dict[str, object]:
        events.append("read")
        return {"request": "bounded test"}

    original_route = accepted.route

    def route(method: str, body: contract.ServerRequest) -> dict[str, object]:
        if not body.context.authenticated_admin:
            failures.append("authenticated handler did not create trusted context")
        return original_route(method, body)

    accepted.route = route  # type: ignore[method-assign]
    with (
        mock.patch.object(contract, "authorize_admin_handler", side_effect=allow),
        mock.patch.object(contract, "read_json_body", side_effect=read),
        mock.patch.object(contract, "send_json", side_effect=capture_send),
    ):
        contract.JsonHandler.do_POST(accepted)  # type: ignore[arg-type]
    if events != ["authenticate", "read", "route", "send:200"]:
        failures.append(f"accepted request order drifted: {events}")


def main() -> int:
    failures: list[str] = []

    for path in API_FILES:
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")
        import_file(path)

    contract_source = (API_ROOT / "_jarvis_contract.py").read_text(encoding="utf-8")
    tree = ast.parse(contract_source)
    forbidden_imports = {"urllib", "requests", "httpx", "socket"}
    imported = {
        alias.name.split(".", 1)[0]
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    if imported & forbidden_imports:
        failures.append("compatibility contract imports a network client")

    function_names = {node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    forbidden_functions = {
        "provider_" + "ready",
        "provider_" + "packet",
        "call_" + "openrouter",
        "openrouter_" + "prompt",
        "budget_" + "payload",
        "voice_" + "payload",
    }
    if function_names & forbidden_functions:
        failures.append("compatibility contract retains an execution-era function")

    forbidden_fragments = (
        "url" + "open",
        "OPEN" + "ROUTER",
        "api_" + "key",
        "voi" + "ce",
        "Architecture" + " 1",
        "Architecture" + " 2",
        "own" + "er",
        "bud" + "get",
        "sp" + "end",
        "context_" + "length",
        "model_" + "id",
        "snapshot_" + "date",
    )
    lowered = contract_source.lower()
    for fragment in forbidden_fragments:
        if fragment.lower() in lowered:
            failures.append(f"retired contract fragment remains: {fragment}")

    public_request = contract.ServerRequest({}, contract.PUBLIC_REQUEST_CONTEXT)
    attempted_controls = contract.ServerRequest(
        {
            "request": "Prepare a bounded review",
            "execute": True,
            "authorize": True,
            "external_write": True,
            "stage": "define",
        },
        contract.ADMIN_REQUEST_CONTEXT,
    )
    responses = {
        "health": contract.health_payload(),
        "models": contract.models_payload(),
        "roles": contract.role_config_payload(),
        "chat": contract.chat_payload(attempted_controls),
        "definition": contract.prd_icp_payload(attempted_controls),
        "coordination": contract.agent_orchestra_payload(attempted_controls),
        "base": contract.JsonHandler.route(object(), "GET", public_request),
    }
    for label, response in responses.items():
        if response.get("schema_version") != "3.0":
            failures.append(f"{label}: schema version drifted")
        assert_zero_effects(label, response, failures)

    catalog = responses["models"].get("payload", {})
    if not isinstance(catalog, dict) or catalog.get("providers") != [] or catalog.get("models") != []:
        failures.append("provider-disabled catalog is not empty")
    adapters = catalog.get("adapters", []) if isinstance(catalog, dict) else []
    adapter_pairs = tuple((item.get("id"), item.get("state")) for item in adapters if isinstance(item, dict))
    if adapter_pairs != EXPECTED_ADAPTERS:
        failures.append("adapter names or states drifted")

    roles = responses["roles"].get("payload", {})
    role_items = roles.get("roles", []) if isinstance(roles, dict) else []
    if len(role_items) != 21:
        failures.append(f"role projection expected 21, received {len(role_items)}")

    serialized_review = str(responses["chat"])
    for control in ("'execute': True", "'authorize': True", "'external_write': True"):
        if control in serialized_review:
            failures.append("request control field leaked into the review packet")

    assert_auth_before_body_read(failures)

    if failures:
        print("jarvis_api_contract_smoke=failed failures=" + "; ".join(failures))
        return 1
    print(
        "jarvis_api_contract_smoke=ok "
        "api_files=7 roles=21 providers=0 models=0 adapters=5 "
        "auth_before_body_read=1 provider_calls=0 network_calls=0 writeback=0 external_actions=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
