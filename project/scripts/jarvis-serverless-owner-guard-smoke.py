#!/usr/bin/env python3
"""Verify fail-closed request handling and immutable zero-effect packets."""

from __future__ import annotations

import io
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
API_ROOT = REPO_ROOT / "api"
sys.path.insert(0, str(API_ROOT))

import _jarvis_contract as contract  # noqa: E402


class BodyProbe:
    def __init__(self, body: bytes, content_length: str | None = None) -> None:
        self.headers = {"content-length": content_length if content_length is not None else str(len(body))}
        self.rfile = io.BytesIO(body)


def main() -> int:
    failures: list[str] = []

    valid = BodyProbe(b'{"request":"bounded"}')
    if contract.read_json_body(valid).get("request") != "bounded":  # type: ignore[arg-type]
        failures.append("valid JSON body did not parse")

    for probe in (
        BodyProbe(b"[]"),
        BodyProbe(b"not-json"),
        BodyProbe(b"{}", "invalid"),
        BodyProbe(b"", str(contract.MAX_BODY_BYTES + 1)),
    ):
        try:
            contract.read_json_body(probe)  # type: ignore[arg-type]
        except contract.InvalidRequestBody:
            continue
        failures.append("invalid body did not fail closed")

    events: list[str] = []

    class Stub:
        headers: dict[str, str] = {}

        def route(self, _method: str, _body: contract.ServerRequest) -> dict[str, object]:
            events.append("route")
            return contract.packet("test", "ok")

    def deny(_handler: object) -> SimpleNamespace:
        events.append("authenticate")
        return SimpleNamespace(authorized=False, status=401, error="authentication_required")

    def read(_handler: object) -> dict[str, object]:
        events.append("read")
        return {}

    def send(_handler: object, _payload: object, status: int = 200) -> None:
        events.append(f"send:{status}")

    with (
        mock.patch.object(contract, "authorize_admin_handler", side_effect=deny),
        mock.patch.object(contract, "read_json_body", side_effect=read),
        mock.patch.object(contract, "send_json", side_effect=send),
    ):
        contract.JsonHandler.do_POST(Stub())  # type: ignore[arg-type]
    if events != ["authenticate", "send:401"]:
        failures.append(f"authentication/body order drifted: {events}")

    attempted = contract.ServerRequest(
        {
            "request": "attempted effect",
            "execute": True,
            "authorize": True,
            "external_write": True,
        },
        contract.ADMIN_REQUEST_CONTEXT,
    )
    packets = (
        contract.chat_payload(attempted),
        contract.prd_icp_payload(attempted),
        contract.agent_orchestra_payload(attempted),
    )
    for response in packets:
        runtime = response.get("runtime", {})
        if runtime.get("provider_calls") != 0:
            failures.append("packet reported a provider call")
        if runtime.get("network_calls") != 0:
            failures.append("packet reported a network call")
        if runtime.get("external_writeback") != 0 or runtime.get("external_actions") != 0:
            failures.append("packet reported an external effect")

    catalog = contract.models_payload().get("payload", {})
    if catalog.get("providers") != [] or catalog.get("models") != []:
        failures.append("catalog exposed a provider or model")
    if len(contract.default_roles()) != 21:
        failures.append("role projection does not contain 21 roles")

    if failures:
        print("jarvis_serverless_guard_smoke=failed failures=" + "; ".join(failures))
        return 1
    print(
        "jarvis_serverless_guard_smoke=ok "
        "auth_before_body_read=1 invalid_body_fail_closed=1 roles=21 "
        "providers=0 models=0 provider_calls=0 network_calls=0 writeback=0 external_actions=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
