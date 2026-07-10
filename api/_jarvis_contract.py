from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler
from typing import Any


APP_VERSION = "2026-07-07-vercel-jarvis-chat-files-voice-disabled"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_OPENROUTER_MODEL = ""
DEFAULT_DAILY_BUDGET = 5.00
DEFAULT_RUN_BUDGET = 1.99
DEFAULT_HARD_STOP = 1.99

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
    return os.getenv("MODEL_PROVIDER", "none").strip().lower() or "none"


def env_float(name: str) -> tuple[float | None, str | None]:
    value = os.getenv(name, "").strip()
    if not value:
        return None, None
    try:
        return float(value), None
    except ValueError:
        return None, name


def budget_payload(provider_allowed: bool = False) -> dict[str, Any]:
    daily_name = "OPENROUTER_DAILY_BUDGET_USD"
    run_name = "OPENROUTER_RUN_BUDGET_USD"
    hard_stop_name = "OPENROUTER_RUN_HARD_STOP_USD"
    daily, invalid_daily = env_float(daily_name)
    run, invalid_run = env_float(run_name)
    hard_stop, invalid_hard_stop = env_float(hard_stop_name)
    invalid = [name for name in [invalid_daily, invalid_run, invalid_hard_stop] if name]
    if invalid:
        return {
            "status": "invalid_budget_env",
            "invalid": invalid,
            "provider_calls_allowed": False,
            "over_cap_behavior": "stop_and_request_owner_approval",
        }

    missing = [
        name
        for name, value in [
            (daily_name, daily),
            (run_name, run),
            (hard_stop_name, hard_stop),
        ]
        if value is None
    ]
    if provider_allowed and missing:
        return {
            "status": "approval_required",
            "reason": "budget_env_missing_for_provider_route",
            "missing": missing,
            "provider_calls_allowed": False,
            "over_cap_behavior": "stop_and_request_owner_approval",
        }

    daily = daily if daily is not None else DEFAULT_DAILY_BUDGET
    run = run if run is not None else DEFAULT_RUN_BUDGET
    hard_stop = hard_stop if hard_stop is not None else DEFAULT_HARD_STOP
    over_cap = daily > DEFAULT_DAILY_BUDGET or run >= 2.0 or hard_stop >= 2.0
    return {
        "status": "blocked_over_cap" if over_cap else ("ready_for_approved_provider_call" if provider_allowed else "ready_disabled"),
        "daily_budget_usd": daily,
        "run_budget_usd": run,
        "run_hard_stop_usd": hard_stop,
        "actual_spend_usd": 0.0,
        "provider_calls_allowed": bool(provider_allowed and not over_cap),
        "over_cap_behavior": "stop_and_request_owner_approval",
    }


def packet(
    kind: str,
    status: str,
    payload: dict[str, Any] | None = None,
    runtime_update: dict[str, Any] | None = None,
) -> dict[str, Any]:
    runtime = {
        "hosting": "vercel_serverless",
        "model_provider": model_provider(),
        "provider_calls": 0,
        "external_writeback": 0,
        "default_runtime": "guarded_openrouter_review_packet",
    }
    if runtime_update:
        runtime.update(runtime_update)
    return {
        "kind": kind,
        "status": status,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "runtime": runtime,
        "budget": budget_payload(provider_allowed=bool(runtime.get("provider_calls"))),
        "payload": payload or {},
    }


def provider_requested(body: dict[str, Any]) -> bool:
    return bool(body.get("owner_approval") and body.get("provider_approval"))


def openrouter_model() -> str:
    return os.getenv("OPENROUTER_MODEL", "").strip() or DEFAULT_OPENROUTER_MODEL


def provider_ready(body: dict[str, Any]) -> tuple[bool, str]:
    if model_provider() != "openrouter":
        return False, "model_provider_not_openrouter"
    if not provider_requested(body):
        return False, "owner_and_provider_approval_required"
    if not os.getenv("OPENROUTER_API_KEY", "").strip():
        return False, "openrouter_api_key_missing"
    if not openrouter_model():
        return False, "openrouter_model_required"
    budget = budget_payload(provider_allowed=True)
    if budget["status"] != "ready_for_approved_provider_call":
        return False, f"budget_not_ready:{budget['status']}"
    return True, "ready"


def architecture_context(kind: str, body: dict[str, Any]) -> dict[str, Any]:
    architecture = str(body.get("architecture") or ("control" if kind == "agent_orchestra" else "service"))
    if kind == "agent_orchestra" or architecture == "control":
        return {
            "architecture": "Architecture 2 - Agent Control",
            "langgraph_lane": "agent_orchestra",
            "crewai_roles": ["af_tools", "af_context", "af_manager", "af_review", "af_knowledge", "af_publisher"],
            "kb_contract": "Return facts, interpretation, gaps, next action, and KB update candidates only after review.",
        }
    return {
        "architecture": "Architecture 1 - PRD/ICP Service",
        "langgraph_lane": "prd_icp_flow",
        "crewai_roles": ["af_context", "af_research", "af_manager", "af_review"],
        "kb_contract": "Return PRD/ICP output blocks, evidence gaps, owner questions, and KB update candidates only after review.",
    }


def attachment_summary(body: dict[str, Any]) -> list[dict[str, Any]]:
    attachments = body.get("attachments") if isinstance(body.get("attachments"), list) else []
    summary = []
    for attachment in attachments[:6]:
        if not isinstance(attachment, dict):
            continue
        summary.append(
            {
                "name": str(attachment.get("name") or "")[:260],
                "mime_type": str(attachment.get("mime_type") or "unknown")[:120],
                "size": int(attachment.get("size") or 0),
                "transfer_mode": str(attachment.get("transfer_mode") or "metadata_only")[:40],
                "text_excerpt": str(attachment.get("text_excerpt") or "")[:900],
            }
        )
    return summary


def prompt_attachment_context(body: dict[str, Any]) -> str:
    attachments = attachment_summary(body)
    if not attachments:
        return "No files attached."
    lines = []
    for index, attachment in enumerate(attachments, start=1):
        text = attachment["text_excerpt"][:1200] if attachment["transfer_mode"] == "text_excerpt" else ""
        lines.append(
            f"{index}. {attachment['name']} ({attachment['mime_type']}, {attachment['size']} bytes, {attachment['transfer_mode']})"
            + (f"\nExcerpt:\n{text}" if text else "")
        )
    return "\n".join(lines)


def prompt_conversation_context(body: dict[str, Any]) -> str:
    conversation = body.get("conversation") if isinstance(body.get("conversation"), list) else []
    if not conversation:
        return "No prior chat context supplied."
    lines = []
    for message in conversation[-6:]:
        if not isinstance(message, dict):
            continue
        lines.append(
            f"{str(message.get('role') or 'user')[:20]} via {str(message.get('source') or '')[:80]}: {str(message.get('text') or '')[:700]}"
        )
    return "\n".join(lines) or "No prior chat context supplied."


def openrouter_prompt(kind: str, body: dict[str, Any]) -> list[dict[str, str]]:
    context = architecture_context(kind, body)
    request = str(body.get("request") or body.get("transcript") or "")[:4000]
    system = (
        "You are ArchFlow Jarvis running server-side under explicit owner/provider approval. "
        "Follow the ArchFlow LangGraph lane and CrewAI role contract. "
        "Never claim durable writeback, Notion sync, GitHub updates, customer validation, or raw private-source processing. "
        "Return concise structured Markdown with FACT, INTERPRETATION, GAP, NEXT, and KB_UPDATE_CANDIDATES."
    )
    user = (
        f"Runtime architecture: {context['architecture']}\n"
        f"LangGraph lane: {context['langgraph_lane']}\n"
        f"CrewAI roles: {', '.join(context['crewai_roles'])}\n"
        f"KB contract: {context['kb_contract']}\n\n"
        f"Recent chat context:\n{prompt_conversation_context(body)}\n\n"
        f"Attached files:\n{prompt_attachment_context(body)}\n\n"
        f"User request:\n{request}"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def call_openrouter(kind: str, body: dict[str, Any]) -> dict[str, Any]:
    ready, reason = provider_ready(body)
    if not ready:
        return {"provider_executed": False, "reason": reason}
    payload = {
        "model": openrouter_model(),
        "messages": openrouter_prompt(kind, body),
        "temperature": float(os.getenv("OPENROUTER_TEMPERATURE", "0.2")),
        "max_tokens": int(os.getenv("OPENROUTER_MAX_TOKENS", "900")),
    }
    request = urllib.request.Request(
        OPENROUTER_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json",
            "HTTP-Referer": os.getenv("OPENROUTER_HTTP_REFERER", "https://archflowautomate.vercel.app"),
            "X-Title": os.getenv("OPENROUTER_APP_TITLE", "ArchFlow Jarvis"),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=int(os.getenv("OPENROUTER_TIMEOUT_SECONDS", "35"))) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        return {"provider_executed": False, "reason": f"openrouter_http_{exc.code}", "detail": detail}
    except Exception as exc:  # noqa: BLE001
        return {"provider_executed": False, "reason": f"openrouter_error:{type(exc).__name__}"}
    choice = (data.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    return {
        "provider_executed": True,
        "model": data.get("model") or payload["model"],
        "reply": str(message.get("content") or "").strip(),
        "usage": data.get("usage") or {},
    }


def provider_packet(kind: str, body: dict[str, Any], fallback_payload: dict[str, Any]) -> dict[str, Any]:
    provider = call_openrouter(kind, body)
    context = architecture_context(kind, body)
    payload = {
        **fallback_payload,
        "architecture_runtime": context,
        "provider_result": {
            key: value
            for key, value in provider.items()
            if key not in {"detail"}
        },
        "writeback": "disabled_until_review_and_explicit_durable_write_approval",
    }
    if provider.get("provider_executed"):
        return packet(
            kind,
            "provider_response_created",
            payload,
            {
                "provider_calls": 1,
                "default_runtime": "openrouter_guarded_langgraph_crewai_packet",
                "model": provider.get("model", openrouter_model()),
            },
        )
    return packet(kind, "review_packet_created", payload)


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
            "voice": "disabled_text_chat_only",
            "file_transfer": "bounded_chat_attachments_no_persistence",
            "writeback": "disabled",
            "deployment": "vercel_guarded_openrouter_review_contract",
        },
    )


def chat_payload(body: dict[str, Any]) -> dict[str, Any]:
    request = str(body.get("request") or body.get("transcript") or "")[:900]
    architecture = str(body.get("architecture") or "service")
    return provider_packet(
        "chat",
        body,
        {
            "reply": "Jarvis Vercel API received the request. Provider calls require owner/provider approval; writeback remains disabled.",
            "request_excerpt": request,
            "lane": body.get("lane", "chat"),
            "architecture": architecture,
            "conversation_count": len(body.get("conversation") if isinstance(body.get("conversation"), list) else []),
            "attachment_count": len(attachment_summary(body)),
            "attachments": attachment_summary(body),
            "architecture_contract": (
                "Architecture 1: PRD/ICP service output"
                if architecture == "service"
                else "Architecture 2: controlled agent/workflow system"
            ),
        },
    )


def prd_icp_payload(body: dict[str, Any]) -> dict[str, Any]:
    return provider_packet(
        "prd-icp-flow",
        body,
        {
            "lane": "prd_icp_flow",
            "architecture": body.get("architecture", "service"),
            "request_excerpt": str(body.get("request") or "")[:900],
            "attachment_count": len(attachment_summary(body)),
            "attachments": attachment_summary(body),
            "output_blocks": PRD_BLOCKS,
            "required_outputs": [
                "suggested backlog",
                "missing-info questions",
                "review gates",
            ],
            "provider_state": "available_only_with_owner_provider_approval_and_budget_guard",
            "deployment": "vercel_serverless_review_packet",
        },
    )


def agent_orchestra_payload(body: dict[str, Any]) -> dict[str, Any]:
    return provider_packet(
        "agent-orchestra",
        body,
        {
            "lane": "agent_orchestra",
            "architecture": body.get("architecture", "system"),
            "request_excerpt": str(body.get("request") or "")[:900],
            "attachment_count": len(attachment_summary(body)),
            "attachments": attachment_summary(body),
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


def voice_payload(body: dict[str, Any]) -> dict[str, Any]:
    return packet(
        "voice-chat",
        "disabled",
        {
            "reply": "Voice mode is disabled. Use /api/chat with text and attachments.",
            "transcript_excerpt": str(body.get("transcript") or body.get("request") or "")[:900],
            "raw_audio_storage": "disabled",
        },
    )
