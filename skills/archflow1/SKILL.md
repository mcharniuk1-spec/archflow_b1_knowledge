---
name: archflow1
description: Local ArchFlow Jarvis stack operating contract for dashboard, jarvis-api, LangGraph, CrewAI, voice services, OpenRouter budget gates, and later Railway migration.
---

# Archflow1

## Purpose

Use `archflow1` when running, reviewing, or extending the local ArchFlow Jarvis stack from the dashboard.

This skill is a local operating contract, not proof that the full runtime is live.

## Stack Topology

Layer order:

1. Dashboard local UI: static browser surface under `project/dashboard/`.
2. `jarvis-api`: FastAPI backend contract under `services/jarvis-api/`.
3. LangGraph controller: routing, state, gates, lane execution, and review stops.
4. CrewAI roles: role/team structure orchestrated through LangGraph by default.
5. Optional voice services:
   - `stt-faster-whisper` for speech-to-text;
   - `tts-kokoro` for text-to-speech;
   - Piper as a lower-complexity fallback.
6. OpenRouter: server-side only, disabled unless owner-approved budget and ledger gates pass.
7. Railway: later deployment target after local proof, auth, secrets, budget, and review gates pass.

## Expected Local Endpoints

If `jarvis-api` is running, expected endpoints are:

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

Default port for local proof should be documented by the run. Do not assume a live backend unless `/health` responds.

## Env Names

Use placeholder names only in public files:

- `OPENROUTER_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `TELEGRAM_TARGET_LABEL`
- `JARVIS_API_ALLOWED_ORIGIN`
- `MODEL_PROVIDER`
- `MODEL_ROUTING_PROFILE`
- `OPENROUTER_DAILY_BUDGET_USD`
- `OPENROUTER_RUN_BUDGET_USD`
- `OPENROUTER_RUN_HARD_STOP_USD`

Real values belong only in ignored local env files or approved provider secret stores.

## OpenRouter Budget Contract

OpenRouter is disabled by default.

Owner approval is required before activation. Activation also requires:

- server-side secret access only;
- fresh model/pricing check;
- provider call ledger;
- live budget guard;
- AF Review;
- `5.00` USD daily hard cap;
- per-run budget under `2.00` USD;
- `1.99` USD run hard-stop threshold;
- over-cap behavior: stop and ask approval.

Browser JavaScript must never receive provider keys.

## Voice Path

Approved local voice flow:

1. Browser captures audio through explicit user action.
2. `MediaRecorder` creates a local audio packet.
3. `/api/voice/transcribe` sends audio to an approved local STT service.
4. Editable transcript preview is shown before sending.
5. `/api/voice/chat` sends approved transcript text into Jarvis.
6. LangGraph routes the request.
7. CrewAI role workers are used only through LangGraph-controlled gates unless separately approved.
8. `/api/voice/tts` returns audio from approved local TTS.
9. Dashboard plays audio only after explicit user action or explicit auto-speak toggle.

Raw audio and raw transcripts are non-persistent by default.

## Fallback Behavior

If backend is unavailable:

- dashboard keeps text chat and browser-local review packets;
- Screen 1 can stage PRD/ICP packets;
- Screen 2 can export role config packets;
- no local file write is implied.

If STT fails:

- use manual transcript entry.

If TTS fails:

- show text response and keep speaker playback disabled.

If model provider is disabled:

- return deterministic local packet or stop for approval.

If budget is missing or exceeded:

- stop and ask owner approval.

## LangGraph / CrewAI Levels

Level 1: role configuration and static packets.

Level 2: LangGraph-wrapped execution with review stops.

Level 3: direct CrewAI runtime proof.

Current CrewAI Level 3 state:

- `proof_passed_not_default_runtime`;
- deterministic local direct runtime only;
- zero provider calls;
- zero external writeback;
- zero spend;
- not default runtime;
- not provider-backed runtime.

CrewAI must not become default runtime without owner approval.

## Dashboard Screen Mapping

Screen 1, PRD/ICP Flow:

- direct Jarvis request surface;
- PRD/ICP output blocks;
- owner-gated meeting/test input path;
- local backend route `/api/lanes/prd-icp` when available;
- browser-local packet fallback when unavailable.

Screen 2, Agent Orchestra:

- role cards/config panels;
- task stages;
- QA/report/Git/Notion/memory/final-decision gates;
- backend route `/api/lanes/agent-orchestra` when available;
- browser-local role packet fallback when unavailable.

## Local Health Check Sequence

Run the smallest check that matches the change:

1. `python3 scripts/public_safety_scan.py`
2. `python3 -m py_compile services/jarvis-api/app.py`
3. `python3 project/scripts/generate-dashboard-data.py`
4. dashboard JSON parse
5. `node --check project/dashboard/app.js`
6. workflow validation
7. runtime guard
8. dashboard static smoke
9. `/health` only when `jarvis-api` dependencies are installed and the service is started with owner approval.

Do not claim live FastAPI runtime proof until dependencies are installed and `/health` responds.

## Railway Migration Gate

Local proof is strong enough to plan Railway migration only after:

- local FastAPI service starts and `/health` responds;
- all required endpoints return expected gated packets;
- auth and allowed origin policy are defined;
- env values are in approved secret storage;
- OpenRouter is either disabled or fully budget-guarded;
- voice storage policy is explicit;
- AF Review passes;
- public safety scan and runtime guard pass;
- owner approves deployment.

Railway is not required for static dashboard review.

## Must Not Claim Unless Verified

Do not claim:

- provider-backed Jarvis;
- active OpenRouter runtime;
- live budget enforcement against real provider calls;
- production Railway backend;
- persistent voice pipeline;
- owner-device microphone/speaker proof;
- Telegram delivery;
- dashboard-driven Notion/GitHub/WikiLLM writeback;
- CrewAI as default runtime;
- full PRD/ICP test-cycle completion.

## Owner Decisions

These remain explicit owner decisions:

1. Approve or defer the full PRD/ICP test cycle.
2. Approve or defer FastAPI dependency install and runtime proof.
3. Approve or defer OpenRouter server-side activation and budget ledger.
4. Approve or defer Railway, Telegram, production/Figma sync, and dashboard-driven writeback.
