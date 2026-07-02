#!/usr/bin/env python3
"""Provider-disabled Jarvis API contract for the ArchFlow dashboard.

This service is intentionally conservative. It can answer health/config
requests and create review packets, but it does not call OpenRouter, write
Notion/WikiLLM/GitHub, store raw transcripts, or run the full PRD/ICP test
cycle without explicit owner approval and a live budget guard.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


APP_VERSION = "2026-07-02-jarvis-dashboard-mvp"
DEFAULT_DAILY_BUDGET = 5.00
DEFAULT_RUN_BUDGET = 1.99
DEFAULT_HARD_STOP = 1.99

REQUIRED_ROLE_IDS = [
    "jesus",
    "lol",
    "ronaldinho",
    "messi",
    "ronaldo",
    "yushchenko",
    "theory",
    "security",
    "actor",
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


class JarvisRequest(BaseModel):
    request: str = Field(default="", max_length=12000)
    lane: str = "general"
    architecture: Literal["service", "control"] = "service"
    approved_test_input: bool = False
    source_refs: list[str] = Field(default_factory=list)
    owner_approval: bool = False
    provider_approval: bool = False


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
    handoffTarget: str = "Jesus"


class RoleUpdateRequest(BaseModel):
    roles: list[RoleConfig]
    owner_approval: bool = False


class VoiceRequest(BaseModel):
    transcript: str = Field(default="", max_length=12000)
    owner_approval: bool = False
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


def budget_state(provider_requested: bool = False) -> dict[str, Any]:
    daily = env_float("OPENROUTER_DAILY_BUDGET_USD")
    run = env_float("OPENROUTER_RUN_BUDGET_USD")
    hard_stop = env_float("OPENROUTER_RUN_HARD_STOP_USD")

    missing = [
        name
        for name, value in [
            ("OPENROUTER_DAILY_BUDGET_USD", daily),
            ("OPENROUTER_RUN_BUDGET_USD", run),
            ("OPENROUTER_RUN_HARD_STOP_USD", hard_stop),
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
    return {
        "status": "blocked_over_cap" if over_cap else "ready_disabled",
        "daily_budget_usd": daily,
        "run_budget_usd": run,
        "run_hard_stop_usd": hard_stop,
        "actual_spend_usd": 0.00,
        "over_cap_behavior": "stop_and_request_owner_approval",
        "provider_calls_allowed": False,
    }


def default_roles() -> list[dict[str, str]]:
    titles = {
        "jesus": "Lead Integrator",
        "lol": "Dashboard UI/UX",
        "ronaldinho": "Technical Reviewer",
        "messi": "PM Closeout",
        "ronaldo": "Product/ICP Reviewer",
        "yushchenko": "Budget Reviewer",
        "theory": "PRD/ICP Theory",
        "security": "Security Reviewer",
        "actor": "Bounded Worker",
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
            "modelRoute": "Codex operator" if role_id != "yushchenko" else "OpenRouter gated",
            "budgetMode": "local only" if role_id != "yushchenko" else "stop before 1.99 USD",
            "outputArtifact": "review packet",
            "reviewGate": "AF Review",
            "status": "review",
            "handoffTarget": "Jesus",
        }
        for role_id in REQUIRED_ROLE_IDS
    ]


def packet(kind: str, status: str, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": kind,
        "status": status,
        "created_at": now_utc(),
        "runtime": {
            "model_provider": model_provider(),
            "provider_calls": 0,
            "external_writeback": 0,
            "crewai_level_3": "proof_passed_not_default_runtime",
            "default_runtime": "langgraph_controlled_static_packet",
        },
        "budget": budget_state(provider_requested=model_provider() != "none"),
        "payload": payload,
    }


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
if allowed_origin:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[allowed_origin],
        allow_credentials=False,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )


@app.middleware("http")
async def enforce_origin(request: Request, call_next):
    if allowed_origin and request.method not in {"GET", "OPTIONS"}:
        origin = request.headers.get("origin")
        if origin and origin != allowed_origin:
            raise HTTPException(status_code=403, detail="origin_not_allowed")
    return await call_next(request)


@app.get("/health")
def health() -> dict[str, Any]:
    return packet(
        "health",
        "ok",
        {
            "service": "jarvis-api",
            "version": APP_VERSION,
            "openrouter": "disabled_until_explicit_owner_approval",
            "langgraph": "controller_contract",
            "crewai": "proof_passed_not_default_runtime",
            "voice": "local_ui_only",
            "writeback": "disabled",
        },
    )


@app.post("/api/chat")
def chat(request: JarvisRequest) -> dict[str, Any]:
    if model_provider() != "none" and not request.provider_approval:
        return approval_block("provider_route_requested_without_approval")
    return packet(
        "chat",
        "review_packet_created",
        {
            "reply": "Jarvis API received the request. Provider calls and writeback remain disabled; this is a review packet.",
            "request_excerpt": request.request[:900],
            "lane": request.lane,
            "architecture": request.architecture,
            "architecture_contract": (
                "Architecture 1: PRD/ICP service output"
                if request.architecture == "service"
                else "Architecture 2: controlled agent/workflow system"
            ),
        },
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
def prd_icp_lane(request: JarvisRequest | None = None) -> dict[str, Any]:
    request = request or JarvisRequest(lane="prd_icp_flow")
    return packet(
        "prd-icp-flow",
        "review_packet_created",
        {
            "lane": "prd_icp_flow",
            "architecture": request.architecture,
            "request_excerpt": request.request[:900],
            "output_blocks": PRD_BLOCKS,
            "required_outputs": ["suggested Jira/GitLab backlog", "missing-info questions", "review gates"],
            "test_cycle": "blocked_until_owner_approval",
        },
    )


@app.get("/api/lanes/agent-orchestra")
@app.post("/api/lanes/agent-orchestra")
def agent_orchestra_lane(request: JarvisRequest | None = None) -> dict[str, Any]:
    request = request or JarvisRequest(lane="agent_orchestra")
    return packet(
        "agent-orchestra",
        "review_packet_created",
        {
            "lane": "agent_orchestra",
            "architecture": request.architecture,
            "request_excerpt": request.request[:900],
            "stages": ["Intake", "Role Assignment", "Active Work", "QA Gate", "Docs/Reports", "Git/Deploy", "Notion/Memory", "Final Decision"],
            "roles": default_roles(),
        },
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
    if not request.owner_approval:
        return approval_block("voice_transcription_requires_owner_approval_and_storage_policy")
    return packet("voice-transcribe", "review_packet_created", {"transcript_excerpt": request.transcript[:900]})


@app.post("/api/voice/chat")
def voice_chat(request: VoiceRequest) -> dict[str, Any]:
    return packet(
        "voice-chat",
        "review_packet_created",
        {
            "reply": "Voice transcript received as text only. Raw audio is not stored and provider calls remain disabled.",
            "transcript_excerpt": request.transcript[:900],
        },
    )


@app.post("/api/voice/tts")
def voice_tts(request: VoiceRequest) -> dict[str, Any]:
    return packet(
        "voice-tts",
        "browser_tts_only",
        {
            "text_excerpt": request.transcript[:900],
            "tts_runtime": "browser_speech_synthesis_or_later_approved_provider",
        },
    )
