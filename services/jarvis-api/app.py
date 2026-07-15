#!/usr/bin/env python3
"""Provider-disabled OpenRouter Jarvis API contract for ArchFlow.

This service is intentionally conservative. It can answer health/config
requests and create review packets. Provider execution stays disabled until a
server-enforced single-use approval nonce and durable spend ledger exist. It
never writes Notion/WikiLLM/GitHub or stores raw transcripts.
"""

from __future__ import annotations

import os
import hmac
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


APP_VERSION = "2026-07-13-owner-auth-model-routing-blocked-ledger"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_DAILY_BUDGET = 5.00
DEFAULT_RUN_BUDGET = 1.99
DEFAULT_HARD_STOP = 1.99
LOCAL_ORIGIN_REGEX = r"^http://(127\.0\.0\.1|localhost):\d+$"
DEFAULT_ALLOWED_MODELS = [
    "openai/gpt-5.6-luna",
    "anthropic/claude-sonnet-5",
    "qwen/qwen3.7-plus",
    "deepseek/deepseek-v4-flash",
]
CURATED_MODELS = [
    {"id": "openai/gpt-5.6-luna", "label": "GPT-5.6 Luna", "provider": "OpenAI", "tier": "frontier", "context_length": 1_050_000},
    {"id": "anthropic/claude-sonnet-5", "label": "Claude Sonnet 5", "provider": "Anthropic", "tier": "frontier", "context_length": 1_000_000},
    {"id": "qwen/qwen3.7-plus", "label": "Qwen3.7 Plus", "provider": "Qwen", "tier": "economy", "context_length": 1_000_000},
    {"id": "deepseek/deepseek-v4-flash", "label": "DeepSeek V4 Flash", "provider": "DeepSeek", "tier": "economy", "context_length": 1_048_576},
]

REQUIRED_ROLE_IDS = [
    "lead_integrator",
    "dashboard_workflow_owner",
    "technical_reviewer",
    "pm_reviewer",
    "product_icp_reviewer",
    "model_efficiency_observer",
    "prd_icp_advisor",
    "safety_reviewer",
    "bounded_executor",
    "af_tools",
    "af_knowledge",
    "af_publisher",
    "af_review",
    "crewai_workers",
]

PRD_BLOCKS = [
    "Meeting Summary",
    "Product Context",
    "Stakeholders",
    "ICP",
    "Pains/JTBD",
    "Existing Workflow",
    "Proposed Workflow",
    "Requirements",
    "Decisions",
    "Questions",
    "Risks",
    "Next Tasks",
    "Backlog",
    "Success Metrics",
]


class JarvisAttachment(BaseModel):
    id: str = Field(default="", max_length=120)
    name: str = Field(default="", max_length=260)
    mime_type: str = Field(default="unknown", max_length=120)
    size: int = Field(default=0, ge=0)
    transfer_mode: Literal["metadata_only", "text_excerpt"] = "metadata_only"
    text_excerpt: str = Field(default="", max_length=6000)


class JarvisMessage(BaseModel):
    role: Literal["user", "assistant", "system"] = "user"
    source: str = Field(default="", max_length=160)
    time: str = Field(default="", max_length=80)
    text: str = Field(default="", max_length=1400)


class JarvisRequest(BaseModel):
    request: str = Field(default="", max_length=12000)
    lane: str = "general"
    architecture: Literal["service", "control"] = "service"
    approved_test_input: bool = False
    source_refs: list[str] = Field(default_factory=list)
    conversation: list[JarvisMessage] = Field(default_factory=list, max_length=8)
    attachments: list[JarvisAttachment] = Field(default_factory=list, max_length=6)
    owner_approval: bool = False
    provider_approval: bool = False
    model_id: str = Field(default="", max_length=180)


class RoleConfig(BaseModel):
    id: str
    title: str = ""
    objective: str = ""
    responsibility: str = ""
    tools: str = ""
    modelRoute: str = "Codex operator"
    budgetMode: str = "local only"
    outputArtifact: str = ""
    reviewGate: str = "AF Review"
    status: str = "review"
    handoffTarget: str = "Lead Integrator"


class RoleUpdateRequest(BaseModel):
    roles: list[RoleConfig]
    owner_approval: bool = False


class VoiceRequest(BaseModel):
    transcript: str = Field(default="", max_length=12000)
    architecture: Literal["service", "control"] = "service"
    owner_approval: bool = False
    provider_approval: bool = False
    auto_speak: bool = False


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def pydantic_payload(model: BaseModel) -> dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


def env_float(name: str) -> float | None:
    value = os.getenv(name, "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=f"invalid_budget_env:{name}") from exc


def model_provider() -> str:
    return os.getenv("MODEL_PROVIDER", "none").strip().lower() or "none"


def env_enabled(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def allowed_models() -> list[str]:
    configured = [value.strip() for value in os.getenv("OPENROUTER_ALLOWED_MODELS", "").split(",") if value.strip()]
    return configured or list(DEFAULT_ALLOWED_MODELS)


def requested_model(request_model: JarvisRequest | VoiceRequest) -> str:
    return str(getattr(request_model, "model_id", "") or os.getenv("OPENROUTER_MODEL", "")).strip()


def owner_authorized(request: Request) -> bool:
    expected = os.getenv("JARVIS_OWNER_TOKEN", "").strip()
    if not expected:
        return False
    authorization = request.headers.get("authorization", "")
    scheme, _, supplied = authorization.partition(" ")
    return scheme.lower() == "bearer" and bool(supplied) and hmac.compare_digest(supplied.strip(), expected)


def budget_state(provider_requested: bool = False) -> dict[str, Any]:
    provider = model_provider()
    budget_prefix = "OPENAI" if provider == "openai" else "OPENROUTER"
    daily_name = f"{budget_prefix}_DAILY_BUDGET_USD"
    run_name = f"{budget_prefix}_RUN_BUDGET_USD"
    hard_stop_name = f"{budget_prefix}_RUN_HARD_STOP_USD"
    daily = env_float(daily_name)
    run = env_float(run_name)
    hard_stop = env_float(hard_stop_name)

    missing = [
        name
        for name, value in [
            (daily_name, daily),
            (run_name, run),
            (hard_stop_name, hard_stop),
        ]
        if value is None
    ]

    if provider_requested and missing:
        return {
            "status": "approval_required",
            "reason": "budget_env_missing_for_provider_route",
            "missing": missing,
            "over_cap_behavior": "stop_and_request_owner_approval",
        }

    daily = daily if daily is not None else DEFAULT_DAILY_BUDGET
    run = run if run is not None else DEFAULT_RUN_BUDGET
    hard_stop = hard_stop if hard_stop is not None else DEFAULT_HARD_STOP

    over_cap = daily > DEFAULT_DAILY_BUDGET or hard_stop >= 2.00 or run >= 2.00
    status = "blocked_over_cap" if over_cap else "ready_disabled"
    if provider_requested and not over_cap:
        status = "blocked_durable_nonce_and_spend_ledger_required"
    return {
        "status": status,
        "daily_budget_usd": daily,
        "run_budget_usd": run,
        "run_hard_stop_usd": hard_stop,
        "actual_spend_usd": None,
        "spend_tracking": "not_durable_across_process_restarts",
        "over_cap_behavior": "stop_and_request_owner_approval",
        "provider_calls_allowed": False,
    }


def provider_ready(provider_requested: bool, owner_is_authorized: bool, model: str) -> tuple[bool, str]:
    if model_provider() != "openrouter":
        return False, "model_provider_not_openrouter"
    if not env_enabled("JARVIS_ENABLE_PROVIDER_CALLS"):
        return False, "provider_calls_not_enabled_server_side"
    if not os.getenv("JARVIS_OWNER_TOKEN", "").strip():
        return False, "owner_auth_not_configured"
    if not owner_is_authorized:
        return False, "owner_auth_required"
    if not provider_requested:
        return False, "per_request_provider_acknowledgement_required"
    if not os.getenv("OPENROUTER_API_KEY", "").strip():
        return False, "openrouter_api_key_missing"
    if not model:
        return False, "openrouter_model_required"
    if model not in allowed_models():
        return False, "model_not_in_server_allowlist"
    return False, "durable_nonce_and_spend_ledger_required"


def architecture_context(kind: str, request: JarvisRequest | VoiceRequest) -> dict[str, Any]:
    architecture = getattr(request, "architecture", "service")
    if kind == "agent-orchestra" or architecture == "control":
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


def attachment_summary(attachments: list[JarvisAttachment]) -> list[dict[str, Any]]:
    return [
        {
            "name": attachment.name,
            "mime_type": attachment.mime_type,
            "size": attachment.size,
            "transfer_mode": attachment.transfer_mode,
            "text_excerpt": attachment.text_excerpt[:900],
        }
        for attachment in attachments[:6]
    ]


def prompt_attachment_context(request: JarvisRequest | VoiceRequest) -> str:
    attachments = getattr(request, "attachments", []) or []
    if not attachments:
        return "No files attached."
    lines = []
    for index, attachment in enumerate(attachments[:6], start=1):
        text = attachment.text_excerpt[:1200] if attachment.transfer_mode == "text_excerpt" else ""
        lines.append(
            f"{index}. {attachment.name} ({attachment.mime_type}, {attachment.size} bytes, {attachment.transfer_mode})"
            + (f"\nExcerpt:\n{text}" if text else "")
        )
    return "\n".join(lines)


def prompt_conversation_context(request: JarvisRequest | VoiceRequest) -> str:
    messages = getattr(request, "conversation", []) or []
    if not messages:
        return "No prior chat context supplied."
    return "\n".join(
        f"{message.role} via {message.source}: {message.text[:700]}"
        for message in messages[-6:]
    )


def openrouter_prompt(kind: str, request: JarvisRequest | VoiceRequest) -> list[dict[str, str]]:
    context = architecture_context(kind, request)
    raw_request = getattr(request, "request", "") or getattr(request, "transcript", "")
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
        f"Recent chat context:\n{prompt_conversation_context(request)}\n\n"
        f"Attached files:\n{prompt_attachment_context(request)}\n\n"
        f"User request:\n{str(raw_request)[:4000]}"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def call_openrouter(kind: str, request_model: JarvisRequest | VoiceRequest, owner_is_authorized: bool) -> dict[str, Any]:
    provider_requested = bool(getattr(request_model, "provider_approval", False))
    model = requested_model(request_model)
    ready, reason = provider_ready(provider_requested, owner_is_authorized, model)
    if not ready:
        return {"provider_executed": False, "reason": reason, "requested_model": model}
    payload = {
        "model": model,
        "messages": openrouter_prompt(kind, request_model),
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


def default_roles() -> list[dict[str, str]]:
    titles = {
        "lead_integrator": "Lead Integrator",
        "dashboard_workflow_owner": "Dashboard Workflow Owner",
        "technical_reviewer": "Technical Reviewer",
        "pm_reviewer": "PM Reviewer",
        "product_icp_reviewer": "Product/ICP Reviewer",
        "model_efficiency_observer": "Model-Efficiency Observer",
        "prd_icp_advisor": "PRD/ICP Advisor",
        "safety_reviewer": "Safety Reviewer",
        "bounded_executor": "Bounded Worker",
        "af_tools": "AF Tools",
        "af_knowledge": "AF Knowledge",
        "af_publisher": "AF Publisher",
        "af_review": "AF Review",
        "crewai_workers": "CrewAI Role Workers",
    }
    return [
        {
            "id": role_id,
            "title": titles[role_id],
            "objective": "Operate within the approved static/local dashboard boundary.",
            "responsibility": "Create or review public-safe packets; no provider calls or writeback by default.",
            "tools": "Codex, dashboard packets, validation scripts",
            "modelRoute": "Codex operator" if role_id != "model_efficiency_observer" else "OpenRouter gated",
            "budgetMode": "local only" if role_id != "model_efficiency_observer" else "stop before 1.99 USD",
            "outputArtifact": "review packet",
            "reviewGate": "AF Review",
            "status": "review",
            "handoffTarget": "Lead Integrator",
        }
        for role_id in REQUIRED_ROLE_IDS
    ]


def packet(
    kind: str,
    status: str,
    payload: dict[str, Any],
    runtime_update: dict[str, Any] | None = None,
) -> dict[str, Any]:
    runtime = {
        "model_provider": model_provider(),
        "provider_calls": 0,
        "external_writeback": 0,
        "crewai_level_3": "proof_passed_not_default_runtime",
        "default_runtime": "guarded_openrouter_review_packet",
    }
    if runtime_update:
        runtime.update(runtime_update)
    return {
        "kind": kind,
        "status": status,
        "created_at": now_utc(),
        "runtime": runtime,
        "budget": budget_state(provider_requested=bool(runtime.get("provider_calls"))),
        "payload": payload,
    }


def provider_packet(
    kind: str,
    request_model: JarvisRequest | VoiceRequest,
    payload: dict[str, Any],
    owner_is_authorized: bool = False,
) -> dict[str, Any]:
    provider = call_openrouter(kind, request_model, owner_is_authorized)
    full_payload = {
        **payload,
        "architecture_runtime": architecture_context(kind, request_model),
        "provider_result": {key: value for key, value in provider.items() if key != "detail"},
        "writeback": "disabled_until_review_and_explicit_durable_write_approval",
    }
    if provider.get("provider_executed"):
        return packet(
            kind,
            "provider_response_created",
            full_payload,
            {
                "provider_calls": 1,
                "default_runtime": "openrouter_guarded_langgraph_crewai_packet",
                "model": provider.get("model", requested_model(request_model)),
            },
        )
    return packet(kind, "review_packet_created", full_payload)


def approval_block(reason: str) -> dict[str, Any]:
    return packet(
        "approval-required",
        "approval_required",
        {
            "reason": reason,
            "next_step": "Stop and ask owner approval before provider call, backend write, raw transcript use, Telegram send, or full test-cycle execution.",
        },
    )


app = FastAPI(title="ArchFlow Jarvis API", version=APP_VERSION)

allowed_origin = os.getenv("JARVIS_API_ALLOWED_ORIGIN", "").strip()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed_origin] if allowed_origin else [],
    allow_origin_regex=None if allowed_origin else LOCAL_ORIGIN_REGEX,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.middleware("http")
async def enforce_origin(request: Request, call_next):
    if allowed_origin and request.method not in {"GET", "OPTIONS"}:
        origin = request.headers.get("origin")
        if origin and origin != allowed_origin:
            return JSONResponse(status_code=403, content={"detail": "origin_not_allowed"})
    return await call_next(request)


@app.get("/health")
@app.get("/api/health")
def health() -> dict[str, Any]:
    return packet(
        "health",
        "ok",
        {
            "service": "jarvis-api",
            "version": APP_VERSION,
            "model_provider": model_provider(),
            "provider_enabled": False,
            "provider_switch_requested": env_enabled("JARVIS_ENABLE_PROVIDER_CALLS"),
            "provider_key_configured": bool(os.getenv("OPENROUTER_API_KEY", "").strip()),
            "owner_auth_configured": bool(os.getenv("JARVIS_OWNER_TOKEN", "").strip()),
            "allowed_models": allowed_models(),
            "provider_calls": "blocked_until_server_nonce_and_durable_spend_ledger_exist",
            "spend_tracking": "not_implemented_provider_execution_disabled",
            "langgraph": "controller_contract",
            "crewai": "proof_passed_not_default_runtime",
            "voice": "disabled_text_chat_only",
            "file_transfer": "bounded_chat_attachments_no_persistence",
            "writeback": "disabled",
        },
    )


@app.get("/api/models")
def models() -> dict[str, Any]:
    allowed = set(allowed_models())
    return packet(
        "model-catalog",
        "ok",
        {
            "curated": [{**model, "allowed": model["id"] in allowed} for model in CURATED_MODELS],
            "allowed_model_ids": sorted(allowed),
            "live_catalog_url": "https://openrouter.ai/api/v1/models",
            "catalog_policy": "search_is_public; execution remains disabled until server nonce and durable spend enforcement exist",
            "snapshot_date": "2026-07-13",
        },
    )


@app.post("/api/chat")
def chat(request: JarvisRequest, http_request: Request) -> dict[str, Any]:
    return provider_packet(
        "chat",
        request,
        {
            "reply": "Jarvis API received the request. Provider calls require owner/provider approval; writeback remains disabled.",
            "request_excerpt": request.request[:900],
            "lane": request.lane,
            "architecture": request.architecture,
            "conversation_count": len(request.conversation),
            "attachment_count": len(request.attachments),
            "attachments": attachment_summary(request.attachments),
            "architecture_contract": (
                "Architecture 1: PRD/ICP service output"
                if request.architecture == "service"
                else "Architecture 2: controlled agent/workflow system"
            ),
        },
        owner_authorized(http_request),
    )


@app.get("/api/config/roles")
def get_roles() -> dict[str, Any]:
    return packet("role-config", "ok", {"roles": default_roles()})


@app.post("/api/config/roles/update")
def update_roles(request: RoleUpdateRequest) -> dict[str, Any]:
    return packet(
        "role-config-update",
        "review_packet_created",
        {
            "roles": [pydantic_payload(role) for role in request.roles],
            "write_policy": "browser/API role updates are candidates only until Codex review writes source files",
        },
    )


@app.get("/api/lanes/prd-icp")
@app.post("/api/lanes/prd-icp")
def prd_icp_lane(http_request: Request, request: JarvisRequest | None = None) -> dict[str, Any]:
    request = request or JarvisRequest(lane="prd_icp_flow")
    return provider_packet(
        "prd-icp-flow",
        request,
        {
            "lane": "prd_icp_flow",
            "architecture": request.architecture,
            "request_excerpt": request.request[:900],
            "attachment_count": len(request.attachments),
            "attachments": attachment_summary(request.attachments),
            "output_blocks": PRD_BLOCKS,
            "required_outputs": ["suggested Jira/GitLab backlog", "missing-info questions", "review gates"],
            "test_cycle": "blocked_until_owner_approval",
        },
        owner_authorized(http_request),
    )


@app.get("/api/lanes/agent-orchestra")
@app.post("/api/lanes/agent-orchestra")
def agent_orchestra_lane(http_request: Request, request: JarvisRequest | None = None) -> dict[str, Any]:
    request = request or JarvisRequest(lane="agent_orchestra")
    return provider_packet(
        "agent-orchestra",
        request,
        {
            "lane": "agent_orchestra",
            "architecture": request.architecture,
            "request_excerpt": request.request[:900],
            "attachment_count": len(request.attachments),
            "attachments": attachment_summary(request.attachments),
            "stages": ["Intake", "Role Assignment", "Active Work", "QA Gate", "Docs/Reports", "Git/Deploy", "Notion/Memory", "Final Decision"],
            "roles": default_roles(),
        },
        owner_authorized(http_request),
    )


@app.get("/api/reports/daily-form")
def daily_form() -> dict[str, Any]:
    return packet("daily-form", "ok", {"template": "docs/reporting-daily-weekly-template.md", "scope": "daily"})


@app.get("/api/reports/weekly-form")
def weekly_form() -> dict[str, Any]:
    return packet("weekly-form", "ok", {"template": "docs/reporting-daily-weekly-template.md", "scope": "weekly"})


@app.get("/api/reports/whole-block")
def whole_block_report() -> dict[str, Any]:
    return packet("whole-block-report", "ok", {"template": "docs/reporting-daily-weekly-template.md", "scope": "E1-E7 whole block"})


@app.post("/api/test-runs/meeting-prd")
def meeting_prd_test(request: JarvisRequest) -> dict[str, Any]:
    if not request.owner_approval:
        return approval_block("meeting_prd_test_cycle_requires_owner_approval")
    return packet(
        "meeting-prd-test",
        "review_packet_created",
        {
            "input_ref": "docs/testmeeting.md",
            "source_link": "approved public discovery-call video link",
            "note": "Full execution still requires approved runtime and public/private source boundary review.",
        },
    )


@app.post("/api/voice/transcribe")
def voice_transcribe(request: VoiceRequest) -> dict[str, Any]:
    return packet(
        "voice-transcribe",
        "disabled",
        {"reason": "voice_mode_disabled_use_text_chat_and_file_attachments", "raw_audio_storage": "disabled"},
    )


@app.post("/api/voice/chat")
def voice_chat(request: VoiceRequest) -> dict[str, Any]:
    return packet(
        "voice-chat",
        "disabled",
        {
            "reply": "Voice mode is disabled. Use /api/chat with text and attachments.",
            "transcript_excerpt": request.transcript[:900],
            "raw_audio_storage": "disabled",
        },
    )


@app.post("/api/voice/tts")
def voice_tts(request: VoiceRequest) -> dict[str, Any]:
    return packet(
        "voice-tts",
        "disabled",
        {
            "text_excerpt": request.transcript[:900],
            "tts_runtime": "disabled_text_chat_only",
        },
    )
