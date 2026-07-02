# Dashboard Local Jarvis Stack Manual

Status: Prompt 2.1 local operating manual

## Purpose

This manual explains how the ArchFlow dashboard relates to local Jarvis runtime pieces before any Railway migration or provider-backed activation.

## What Works Now

- The dashboard is a static/browser-local operating surface.
- Screen 1, PRD/ICP Flow, can collect a Jarvis request and stage PRD/ICP review packets.
- Screen 2, Agent Orchestra, can display stages, roles, gates, and browser-local role packets.
- The `jarvis-api` FastAPI service contract exists under `services/jarvis-api/`.
- CrewAI Level 3 direct runtime has deterministic local proof status `proof_passed_not_default_runtime`.
- OpenRouter is disabled.
- Provider calls and dashboard-driven writeback are not active.

## Screen 1 - PRD/ICP Flow

Screen 1 is for turning approved meeting, interview, or research input into a PRD/ICP packet.

Expected output blocks:

- Meeting Summary
- Product Context
- Stakeholders
- ICP
- Pains/JTBD
- Existing Workflow
- Proposed Workflow
- Requirements
- Decisions
- Questions
- Risks
- Next Tasks
- Backlog
- Success Metrics

If a backend is available, Screen 1 should call `/api/lanes/prd-icp`.

If no backend is available, Screen 1 must keep the request as a browser-local packet and must not imply provider execution or file writeback.

## Screen 2 - Agent Orchestra

Screen 2 is for local execution coordination.

It shows:

- Intake
- Role Assignment
- Active Work
- QA Gate
- Docs/Reports
- Git/Deploy
- Notion/Memory
- Final Decision

Role config can include:

- objective;
- responsibility;
- tools;
- model route;
- budget mode;
- output artifact;
- review gate;
- status;
- handoff target.

If a backend is available, Screen 2 should call `/api/lanes/agent-orchestra`.

If no backend is available, Screen 2 must preserve browser-local role packets only.

## Local Backend

The local backend contract is `services/jarvis-api/`.

Expected endpoints:

- `/health`
- `/api/chat`
- `/api/config/roles`
- `/api/config/roles/update`
- `/api/lanes/prd-icp`
- `/api/lanes/agent-orchestra`
- `/api/reports/daily-form`
- `/api/reports/weekly-form`
- `/api/reports/whole-block`
- `/api/test-runs/meeting-prd`
- `/api/voice/transcribe`
- `/api/voice/chat`
- `/api/voice/tts`

FastAPI dependencies are not proven installed in the current local runtime. Do not claim live backend proof until the service starts and `/health` responds.

## LangGraph And CrewAI

LangGraph is the default controller for routing, state, gates, lane execution, and review stops.

CrewAI roles are orchestration units. They should run through LangGraph by default.

Current CrewAI direct-runtime state:

- proof status: `proof_passed_not_default_runtime`;
- deterministic local proof only;
- not default runtime;
- not provider-backed runtime;
- no external writeback;
- zero provider spend.

## OpenRouter

OpenRouter remains disabled.

Activation requires:

- owner approval;
- server-side secret storage only;
- fresh pricing/model verification;
- provider-call ledger;
- live budget guard;
- AF Review;
- daily cap `5.00` USD;
- run hard stop `1.99` USD;
- stop and ask approval if missing or over cap.

Browser JavaScript must never receive provider keys.

## Voice/STT/TTS

Target local voice path:

1. Browser `MediaRecorder`.
2. `/api/voice/transcribe`.
3. Local STT service such as faster-whisper.
4. Editable transcript preview.
5. `/api/voice/chat`.
6. LangGraph route and review gate.
7. `/api/voice/tts`.
8. Local TTS service such as Kokoro, with Piper fallback.
9. Dashboard playback.

If STT fails, use manual transcript.

If TTS fails, keep text output.

Raw audio and raw transcript persistence remain off by default.

## Local Test Sequence

Use this sequence after code or docs changes:

1. Public safety scan.
2. Python syntax compile for `services/jarvis-api/app.py`.
3. Regenerate dashboard data.
4. Parse dashboard JSON.
5. Dashboard JavaScript syntax check.
6. Workflow validation.
7. Runtime guard.
8. Dashboard static smoke.

Add `/health` only after backend dependencies are installed and service start is approved.

## Owner Decisions

These decisions remain explicit gates:

1. Approve or defer the full PRD/ICP test cycle.
2. Approve or defer FastAPI dependency install and runtime proof.
3. Approve or defer OpenRouter server-side activation and budget ledger.
4. Approve or defer Railway, Telegram, production/Figma sync, and dashboard-driven writeback.

## Railway Migration Gate

Railway migration is not ready until:

- local `jarvis-api` starts and passes `/health`;
- all endpoint contracts return expected gated packets;
- auth and allowed origins are defined;
- secrets live in approved secret storage;
- provider budget guard is live or provider mode remains disabled;
- voice persistence policy is explicit;
- AF Review passes;
- owner approves deployment.

## Failure Interpretation

- Backend unavailable: use browser-local packets.
- FastAPI missing: dependency gate, not dashboard failure.
- OpenRouter disabled: expected safe state.
- Budget missing: stop and request approval.
- Telegram not configured: record deferred status.
- Notion dashboard writeback missing: expected; operator connector updates are separate.
