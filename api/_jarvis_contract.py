from __future__ import annotations

import json
from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from typing import Any

from _auth_contract import authorize_admin_handler


APP_VERSION = "3.0.0-provider-disabled"
SCHEMA_VERSION = "3.0"
MAX_BODY_BYTES = 65_536
REPO_ROOT = Path(__file__).resolve().parents[1]
ROLE_CATALOG_PATH = REPO_ROOT / "project" / "database" / "role-catalog.json"

ADAPTERS = (
    {"id": "review_packet", "state": "available"},
    {"id": "role_projection", "state": "available"},
    {"id": "browser_local_handoff", "state": "available"},
    {"id": "provider_execution", "state": "disabled"},
    {"id": "external_writeback", "state": "disabled"},
)
STAGES = {"research", "define", "plan", "review", "handoff"}


@dataclass(frozen=True)
class TrustedRequestContext:
    authenticated_admin: bool


PUBLIC_REQUEST_CONTEXT = TrustedRequestContext(authenticated_admin=False)
ADMIN_REQUEST_CONTEXT = TrustedRequestContext(authenticated_admin=True)


@dataclass(frozen=True)
class ServerRequest(Mapping[str, Any]):
    """A JSON payload paired with authority established by the server handler."""

    payload: Mapping[str, Any]
    context: TrustedRequestContext

    def __getitem__(self, key: str) -> Any:
        return self.payload[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self.payload)

    def __len__(self) -> int:
        return len(self.payload)


class InvalidRequestBody(ValueError):
    pass


def _created_at() -> str:
    return datetime.now(timezone.utc).isoformat()


def _runtime_boundary() -> dict[str, Any]:
    return {
        "execution_mode": "provider_disabled",
        "provider_calls": 0,
        "network_calls": 0,
        "external_writeback": 0,
        "external_actions": 0,
    }


def packet(
    kind: str,
    status: str,
    payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Create a schema-stable review packet with immutable zero-effect bounds."""

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": kind,
        "status": status,
        "created_at": _created_at(),
        "runtime": _runtime_boundary(),
        "payload": dict(payload or {}),
    }


def _text(value: Any, limit: int) -> str:
    if value is None:
        return ""
    return str(value).strip()[:limit]


def _stage(value: Any) -> str:
    candidate = _text(value, 32).lower()
    return candidate if candidate in STAGES else "research"


def attachment_summary(body: ServerRequest) -> list[dict[str, Any]]:
    supplied = body.get("attachments")
    attachments = supplied if isinstance(supplied, list) else []
    summary: list[dict[str, Any]] = []
    for item in attachments[:6]:
        if not isinstance(item, Mapping):
            continue
        try:
            size = max(0, min(int(item.get("size") or 0), 100_000_000))
        except (TypeError, ValueError):
            size = 0
        summary.append(
            {
                "name": _text(item.get("name"), 200),
                "media_type": _text(item.get("mime_type") or item.get("media_type"), 100),
                "size": size,
                "handling": "metadata_only",
            }
        )
    return summary


def _review_contract(body: ServerRequest) -> dict[str, Any]:
    return {
        "state": "draft_review_packet",
        "stage": _stage(body.get("stage")),
        "objective": _text(body.get("objective") or body.get("request"), 1_200),
        "public_reference": _text(body.get("public_reference"), 500),
        "evidence_boundary": _text(body.get("evidence_boundary"), 1_200),
        "requested_output": _text(body.get("requested_output"), 600),
        "reviewer_role": _text(body.get("reviewer_role"), 120),
        "constraints": _text(body.get("constraints"), 1_200),
        "next_gate": "human_review_required",
    }


def _review_payload(
    body: ServerRequest,
    *,
    lane: str,
    sections: tuple[str, ...],
    include_roles: bool = False,
) -> dict[str, Any]:
    supplied_conversation = body.get("conversation")
    conversation = supplied_conversation if isinstance(supplied_conversation, list) else []
    result: dict[str, Any] = {
        "adapter": "review_packet",
        "lane": lane,
        "contract": _review_contract(body),
        "sections": list(sections),
        "conversation_items": min(len(conversation), 50),
        "attachments": attachment_summary(body),
        "result_state": "unexecuted_candidate",
    }
    if include_roles:
        result["roles"] = default_roles()
    return result


def default_roles() -> list[dict[str, Any]]:
    """Project the generated 21-role catalog without adding runtime authority."""

    try:
        catalog = json.loads(ROLE_CATALOG_PATH.read_text(encoding="utf-8"))
        roles = catalog.get("roles", [])
    except (OSError, json.JSONDecodeError):
        roles = []

    projection: list[dict[str, Any]] = []
    for role in roles:
        if not isinstance(role, Mapping) or not role.get("id"):
            continue
        projection.append(
            {
                "id": _text(role.get("id"), 120),
                "title": _text(role.get("title") or role.get("id"), 160),
                "mode": _text(role.get("mode"), 200),
                "status": "available_for_planning",
                "public_skill_packages": [
                    _text(value, 120)
                    for value in (role.get("public_skill_packages") or [])
                    if isinstance(value, str)
                ],
                "method_checklists": [
                    _text(value, 160)
                    for value in (role.get("method_checklists") or [])
                    if isinstance(value, str)
                ],
                "forbidden_actions": [
                    _text(value, 200)
                    for value in (role.get("forbidden_actions") or [])
                    if isinstance(value, str)
                ],
            }
        )
    return projection


def health_payload() -> dict[str, Any]:
    return packet(
        "compatibility-health",
        "ok",
        {
            "service": "knowledge-operator-compatibility-api",
            "version": APP_VERSION,
            "contract": "review_packets_only",
            "post_authentication": "required_before_body_read",
            "catalog_projection": "public_read_only",
        },
    )


def models_payload() -> dict[str, Any]:
    return packet(
        "adapter-catalog",
        "provider_disabled",
        {
            "providers": [],
            "models": [],
            "adapters": [dict(adapter) for adapter in ADAPTERS],
        },
    )


def role_config_payload() -> dict[str, Any]:
    return packet(
        "role-catalog",
        "read_only",
        {
            "roles": default_roles(),
            "projection": "planning_only",
        },
    )


def chat_payload(body: ServerRequest) -> dict[str, Any]:
    return packet(
        "generic-review",
        "review_packet_created",
        _review_payload(
            body,
            lane="communication",
            sections=("objective", "evidence", "constraints", "review", "handoff"),
        ),
    )


def prd_icp_payload(body: ServerRequest) -> dict[str, Any]:
    return packet(
        "definition-review",
        "review_packet_created",
        _review_payload(
            body,
            lane="research_define",
            sections=("research", "definition", "acceptance_checks", "gaps", "review"),
        ),
    )


def agent_orchestra_payload(body: ServerRequest) -> dict[str, Any]:
    return packet(
        "coordination-review",
        "review_packet_created",
        _review_payload(
            body,
            lane="plan_review_handoff",
            sections=("role_selection", "task_contracts", "verification", "handoff"),
            include_roles=True,
        ),
    )


def read_json_body(handler: BaseHTTPRequestHandler) -> dict[str, Any]:
    raw_length = handler.headers.get("content-length") or "0"
    try:
        length = int(raw_length)
    except (TypeError, ValueError) as exc:
        raise InvalidRequestBody("invalid_request_body") from exc
    if length < 0 or length > MAX_BODY_BYTES:
        raise InvalidRequestBody("invalid_request_body")
    if length == 0:
        return {}
    raw = handler.rfile.read(length)
    if len(raw) != length:
        raise InvalidRequestBody("invalid_request_body")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InvalidRequestBody("invalid_request_body") from exc
    if not isinstance(value, dict):
        raise InvalidRequestBody("invalid_request_body")
    return value


def send_json(handler: BaseHTTPRequestHandler, payload: Mapping[str, Any], status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store, max-age=0")
    handler.send_header("Pragma", "no-cache")
    handler.send_header("Vary", "Cookie, Origin")
    handler.send_header("X-Content-Type-Options", "nosniff")
    handler.send_header("X-Frame-Options", "DENY")
    handler.end_headers()
    handler.wfile.write(body)


class JsonHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self) -> None:
        send_json(self, packet("compatibility-options", "ok"))

    def do_GET(self) -> None:
        request = ServerRequest({}, PUBLIC_REQUEST_CONTEXT)
        send_json(self, self.route("GET", request))

    def do_POST(self) -> None:
        authorization = authorize_admin_handler(self)
        if not authorization.authorized:
            send_json(self, {"error": authorization.error}, status=authorization.status)
            return
        try:
            body = read_json_body(self)
        except InvalidRequestBody:
            send_json(self, {"error": "invalid_request_body"}, status=400)
            return
        request = ServerRequest(body, ADMIN_REQUEST_CONTEXT)
        send_json(self, self.route("POST", request))

    def log_message(self, format: str, *args: Any) -> None:
        return

    def route(self, method: str, body: ServerRequest) -> dict[str, Any]:
        return packet("compatibility-api", "ok", {"method": method})
