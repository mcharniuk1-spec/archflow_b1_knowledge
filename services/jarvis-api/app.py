#!/usr/bin/env python3
"""Local, provider-disabled Jarvis review-packet compatibility API.

The service validates bounded public-safe inputs and returns schema 3.0 review
packets. It has no outbound adapter, durable persistence, secret input, or
external-action route. The hosted administrator boundary remains in ``api/auth``.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


SCHEMA_VERSION = "3.0"
APP_VERSION = "3.0.0"
REPO_ROOT = Path(__file__).resolve().parents[2]
ROLE_CATALOG_PATH = REPO_ROOT / "project" / "database" / "role-catalog.json"
LOCAL_ORIGIN_PATTERN = re.compile(r"^http://(?:127\.0\.0\.1|localhost):\d+$")
MAX_BODY_BYTES = 65_536


class Attachment(BaseModel):
    """Bounded attachment metadata; binary file transfer is unsupported."""

    name: str = Field(default="", max_length=260)
    content_type: str = Field(default="unknown", max_length=120)
    size: int = Field(default=0, ge=0, le=20_000_000)
    transfer_mode: Literal["metadata_only", "text_excerpt"] = "metadata_only"
    text_excerpt: str = Field(default="", max_length=6000)


class Message(BaseModel):
    role: Literal["user", "assistant", "system"] = "user"
    text: str = Field(default="", max_length=2000)


class ReviewRequest(BaseModel):
    """Compatible public input for chat and lane packet preparation."""

    request: str = Field(default="", max_length=12_000)
    objective: str = Field(default="", max_length=4000)
    decision: str = Field(default="", max_length=2000)
    allowed_evidence: list[str] = Field(default_factory=list, max_length=32)
    excluded_evidence: list[str] = Field(default_factory=list, max_length=32)
    requested_output: str = Field(default="", max_length=2000)
    reviewer: str = Field(default="", max_length=300)
    constraints: list[str] = Field(default_factory=list, max_length=24)
    stop_conditions: list[str] = Field(default_factory=list, max_length=24)
    source_refs: list[str] = Field(default_factory=list, max_length=32)
    conversation: list[Message] = Field(default_factory=list, max_length=8)
    attachments: list[Attachment] = Field(default_factory=list, max_length=6)


class RoleCandidate(BaseModel):
    id: str = Field(min_length=1, max_length=120)
    state: Literal["proposed", "inactive"] = "proposed"
    note: str = Field(default="", max_length=500)


class RoleUpdateRequest(BaseModel):
    roles: list[RoleCandidate] = Field(default_factory=list, max_length=21)


def _read_canonical_roles() -> list[dict[str, Any]]:
    """Read and validate the single public 21-role catalog."""

    try:
        raw = json.loads(ROLE_CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=500, detail="role_catalog_unavailable") from exc

    roles = raw.get("roles") if isinstance(raw, dict) else None
    if not isinstance(roles, list) or len(roles) != 21:
        raise HTTPException(status_code=500, detail="role_catalog_contract_failed")
    role_ids = [role.get("id") for role in roles if isinstance(role, dict)]
    if len(role_ids) != 21 or any(not isinstance(role_id, str) or not role_id for role_id in role_ids):
        raise HTTPException(status_code=500, detail="role_catalog_contract_failed")
    if len(set(role_ids)) != 21:
        raise HTTPException(status_code=500, detail="role_catalog_contract_failed")
    return roles


def _public_role(role: dict[str, Any]) -> dict[str, Any]:
    """Project functional responsibility without private runtime state."""

    return {
        "id": role["id"],
        "title": role.get("title", role["id"]),
        "lane": role.get("lane", "maker"),
        "purpose": role.get("purpose", ""),
        "outputs": list(role.get("outputs", [])),
        "permission_mode": role.get("permission_mode", "read_draft_only"),
        "reviewer_route": list(role.get("reviewer_route", [])),
        "forbidden_actions": list(role.get("forbidden_actions", [])),
    }


def _attachment_summary(attachments: list[Attachment]) -> list[dict[str, Any]]:
    return [
        {
            "name": attachment.name,
            "content_type": attachment.content_type,
            "size": attachment.size,
            "transfer_mode": attachment.transfer_mode,
            "text_excerpt": attachment.text_excerpt[:900],
        }
        for attachment in attachments
    ]


def _bounded_payload(request: ReviewRequest) -> dict[str, Any]:
    objective = request.objective.strip() or request.request.strip()
    return {
        "objective": objective[:4000],
        "decision": request.decision.strip(),
        "allowed_evidence": request.allowed_evidence,
        "excluded_evidence": request.excluded_evidence,
        "requested_output": request.requested_output.strip(),
        "reviewer": request.reviewer.strip(),
        "constraints": request.constraints,
        "stop_conditions": request.stop_conditions,
        "source_refs": request.source_refs,
        "conversation_count": len(request.conversation),
        "attachments": _attachment_summary(request.attachments),
    }


def _packet(
    kind: str,
    status: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": kind,
        "status": status,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "execution_mode": "provider_disabled",
            "provider_calls": 0,
            "network_calls": 0,
            "external_writeback": 0,
            "external_actions": 0,
        },
        "payload": payload or {},
    }


app = FastAPI(title="ArchFlow Jarvis Compatibility API", version=APP_VERSION)

allowed_origin = os.getenv("JARVIS_API_ALLOWED_ORIGIN", "").strip().rstrip("/")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed_origin] if allowed_origin else [],
    allow_origin_regex=None if allowed_origin else LOCAL_ORIGIN_PATTERN.pattern,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


def _harden_response(response: Response) -> Response:
    response.headers["Cache-Control"] = "no-store, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Vary"] = "Origin"
    return response


@app.middleware("http")
async def enforce_configured_origin(request: Request, call_next):
    """Enforce an exact configured browser origin on mutating requests."""

    if request.method not in {"GET", "HEAD", "OPTIONS"}:
        origin = request.headers.get("origin", "").rstrip("/")
        if allowed_origin and origin != allowed_origin:
            return _harden_response(
                JSONResponse(status_code=403, content={"detail": "origin_not_allowed"})
            )
        if not allowed_origin and origin and not LOCAL_ORIGIN_PATTERN.fullmatch(origin):
            return _harden_response(
                JSONResponse(status_code=403, content={"detail": "origin_not_allowed"})
            )
        raw_length = request.headers.get("content-length")
        if raw_length:
            try:
                length = int(raw_length)
            except ValueError:
                return _harden_response(
                    JSONResponse(status_code=400, content={"detail": "invalid_content_length"})
                )
            if length < 0 or length > MAX_BODY_BYTES:
                return _harden_response(
                    JSONResponse(status_code=413, content={"detail": "request_too_large"})
                )
    response = await call_next(request)
    return _harden_response(response)


@app.get("/health")
@app.get("/api/health")
def health() -> dict[str, Any]:
    roles = _read_canonical_roles()
    return _packet(
        "compatibility-health",
        "ok",
        {
            "service": "jarvis-review-packet-api",
            "version": APP_VERSION,
            "role_catalog_count": len(roles),
            "providers": [],
            "models": [],
            "outbound_adapter": "absent",
            "durable_storage": "absent",
        },
    )


@app.get("/api/models")
def models() -> dict[str, Any]:
    """Legacy discovery route: execution choices are intentionally empty."""

    return _packet(
        "adapter-catalog",
        "provider_disabled",
        {"providers": [], "models": [], "selection": "unavailable"},
    )


@app.post("/api/chat")
def chat(request: ReviewRequest) -> dict[str, Any]:
    payload = _bounded_payload(request)
    payload.update(
        {
            "handoff_target": "/project/dashboard/#communication",
            "next_step": "Review the packet, fill its missing boundaries, and assign an independent reviewer.",
        }
    )
    return _packet("generic-review", "review_packet_created", payload)


@app.get("/api/config/roles")
def get_roles() -> dict[str, Any]:
    roles = [_public_role(role) for role in _read_canonical_roles()]
    return _packet(
        "role-catalog",
        "read_only",
        {"roles": roles, "count": len(roles), "source": "project/database/role-catalog.json"},
    )


@app.post("/api/config/roles/update")
def propose_role_update(request: RoleUpdateRequest) -> dict[str, Any]:
    canonical_ids = {role["id"] for role in _read_canonical_roles()}
    requested_ids = [role.id for role in request.roles]
    if len(set(requested_ids)) != len(requested_ids):
        raise HTTPException(status_code=422, detail="duplicate_role_id")
    unknown = sorted(set(requested_ids) - canonical_ids)
    if unknown:
        raise HTTPException(status_code=422, detail={"unknown_role_ids": unknown})
    return _packet(
        "role-configuration-candidate",
        "review_packet_created",
        {
            "roles": [
                {"id": role.id, "state": role.state, "note": role.note}
                for role in request.roles
            ],
            "write_policy": "candidate_only_no_source_or_runtime_mutation",
        },
    )


@app.get("/api/lanes/prd-icp")
@app.post("/api/lanes/prd-icp")
def requirements_lane(request: ReviewRequest | None = None) -> dict[str, Any]:
    payload = _bounded_payload(request or ReviewRequest())
    payload.update(
        {
            "purpose": "Turn approved evidence into requirement and audience candidates without treating them as approved truth.",
            "role_ids": [
                "source_and_context_operator",
                "requirements_and_market_research",
                "action_validator",
                "independent_reviewer",
            ],
            "expected_outputs": [
                "evidence capsule",
                "requirement candidates",
                "acceptance checks",
                "contradictions and gaps",
                "independent verdict",
            ],
        }
    )
    return _packet("definition-review", "review_packet_created", payload)


@app.get("/api/lanes/agent-orchestra")
@app.post("/api/lanes/agent-orchestra")
def task_role_lane(request: ReviewRequest | None = None) -> dict[str, Any]:
    payload = _bounded_payload(request or ReviewRequest())
    payload.update(
        {
            "purpose": "Prepare the smallest responsible role and handoff plan for review.",
            "stages": ["research", "define", "act", "review", "remember"],
            "role_ids": [
                "goal_and_architecture_operator",
                "source_and_context_operator",
                "task_and_handoff_planner",
                "action_validator",
                "independent_reviewer",
                "integrator",
            ],
            "activation": "proposal_only",
        }
    )
    return _packet("coordination-review", "review_packet_created", payload)
