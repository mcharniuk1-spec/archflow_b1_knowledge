from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler
from typing import Any


APP_VERSION = "2026-07-03-vercel-jarvis-provider-disabled"

PRD_BLOCKS = [
    "Product context",
    "ICP and buyer",
    "Problem statement",
    "User stories",
    "Functional requirements",
    "Non-functional requirements",
    "Acceptance criteria",
    "Evidence and gaps",
    "Backlog",
    "Review gates",
]


def model_provider() -> str:
    return os.getenv("MODEL_PROVIDER", "openrouter").strip().lower() or "openrouter"


def packet(kind: str, status: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "kind": kind,
        "status": status,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "hosting": "vercel_serverless",
            "model_provider": model_provider(),
            "provider_calls": 0,
            "external_writeback": 0,
            "default_runtime": "provider_disabled_review_packet",
        },
        "budget": {
            "status": "ready_disabled",
            "daily_budget_usd": float(os.getenv("OPENROUTER_DAILY_BUDGET_USD", "5.00")),
            "run_budget_usd": float(os.getenv("OPENROUTER_RUN_BUDGET_USD", "1.99")),
            "run_hard_stop_usd": float(os.getenv("OPENROUTER_RUN_HARD_STOP_USD", "1.99")),
            "actual_spend_usd": 0.0,
            "provider_calls_allowed": False,
        },
        "payload": payload or {},
    }


def approval_block(reason: str) -> dict[str, Any]:
    return packet(
        "approval-block",
        "approval_required",
        {
            "reason": reason,
            "provider_calls": "disabled_until_explicit_owner_approval_and_budget_guard",
            "writeback": "disabled",
        },
    )


def default_roles() -> list[dict[str, str]]:
    return [
        {
            "id": "af_tools",
            "name": "AF Tools",
            "role": "source and tooling analyst",
            "status": "configured",
        },
        {
            "id": "af_context",
            "name": "AF Context",
            "role": "context digest and evidence labels",
            "status": "configured",
        },
        {
            "id": "af_manager",
            "name": "AF Manager",
            "role": "PRD and task orchestration",
            "status": "configured",
        },
        {
            "id": "af_review",
            "name": "AF Review",
            "role": "safety, evidence, and approval gate",
            "status": "required",
        },
    ]


def read_json_body(handler: BaseHTTPRequestHandler) -> dict[str, Any]:
    length = int(handler.headers.get("content-length") or 0)
    if length <= 0:
        return {}
    raw = handler.rfile.read(length).decode("utf-8", errors="replace")
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {"request": raw[:900]}


def send_json(handler: BaseHTTPRequestHandler, payload: dict[str, Any], status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Cache-Control", "no-store, max-age=0")
    handler.send_header("Access-Control-Allow-Origin", os.getenv("JARVIS_API_ALLOWED_ORIGIN", "*"))
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
    handler.end_headers()
    handler.wfile.write(body)


class JsonHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self) -> None:
        send_json(self, {"status": "ok"})

    def do_GET(self) -> None:
        send_json(self, self.route("GET", {}))

    def do_POST(self) -> None:
        send_json(self, self.route("POST", read_json_body(self)))

    def log_message(self, format: str, *args: Any) -> None:
        return

    def route(self, method: str, body: dict[str, Any]) -> dict[str, Any]:
        return packet("jarvis-api", "ok", {"method": method, "body": body})


def health_payload() -> dict[str, Any]:
    return packet(
        "health",
        "ok",
        {
            "service": "jarvis-api",
            "version": APP_VERSION,
            "model_provider": model_provider(),
            "provider_calls": "disabled_until_explicit_owner_approval_and_budget_guard",
            "langgraph": "controller_contract",
            "crewai": "proof_passed_not_default_runtime",
            "voice": "browser_text_only",
            "writeback": "disabled",
            "deployment": "vercel_provider_disabled_contract",
        },
    )


def chat_payload(body: dict[str, Any]) -> dict[str, Any]:
    request = str(body.get("request") or body.get("transcript") or "")[:900]
    architecture = str(body.get("architecture") or "service")
    return packet(
        "chat",
        "review_packet_created",
        {
            "reply": "Jarvis Vercel API received the request. Provider calls and writeback remain disabled; this is a review packet.",
            "request_excerpt": request,
            "lane": body.get("lane", "chat"),
            "architecture": architecture,
            "architecture_contract": (
                "Architecture 1: PRD/ICP service output"
                if architecture == "service"
                else "Architecture 2: controlled agent/workflow system"
            ),
        },
    )


def prd_icp_payload(body: dict[str, Any]) -> dict[str, Any]:
    return packet(
        "prd-icp-flow",
        "review_packet_created",
        {
            "lane": "prd_icp_flow",
            "architecture": body.get("architecture", "service"),
            "request_excerpt": str(body.get("request") or "")[:900],
            "output_blocks": PRD_BLOCKS,
            "required_outputs": [
                "suggested backlog",
                "missing-info questions",
                "review gates",
            ],
            "provider_state": "disabled_until_owner_approval_and_budget_guard",
            "deployment": "vercel_serverless_review_packet",
        },
    )


def agent_orchestra_payload(body: dict[str, Any]) -> dict[str, Any]:
    return packet(
        "agent-orchestra",
        "review_packet_created",
        {
            "lane": "agent_orchestra",
            "architecture": body.get("architecture", "system"),
            "request_excerpt": str(body.get("request") or "")[:900],
            "stages": [
                "Intake",
                "Role Assignment",
                "Active Work",
                "QA Gate",
                "Docs/Reports",
                "Git/Deploy",
                "Notion/Memory",
                "Final Decision",
            ],
            "roles": default_roles(),
        },
    )
