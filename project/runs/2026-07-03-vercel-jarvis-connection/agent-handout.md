# Agent Handout: Vercel Dashboard And Jarvis Connection

Date: 2026-07-03
Status: in progress
Lane: E1.7 hosted dashboard/Jarvis connection

## Goal

Make the hosted Vercel dashboard connect to a working provider-disabled Jarvis API surface while keeping local Jarvis working on `127.0.0.1:8787`.

## Current Implementation

FACT:
- The static dashboard remains served by Vercel through `/dashboard`.
- A Vercel serverless Jarvis contract now exists under `api/`.
- `/health` rewrites to `/api/health` on Vercel.
- The hosted API returns review packets only.
- Provider calls, durable writeback, raw audio storage, Telegram automation, and production publication remain disabled.
- Local FastAPI Jarvis was restarted on port `8787` with OpenRouter selected in status and provider calls still disabled behind budget/approval guards.

INTERPRETATION:
- Vercel can now make the dashboard show `Jarvis API connected` without needing the local machine.
- This is not a full always-on agent runtime. It is a hosted review/control contract.

GAP:
- Railway or another long-running backend is still needed for workers, queues, stronger auth, long provider tasks, and durable writeback.
- Provider-backed Jarvis execution remains a separate approval-gated lane.

## Files In Scope

- `api/`
- `vercel.json`
- `project/dashboard/app.js`
- `project/scripts/generate-dashboard-data.py`
- `project/dashboard/data.json`
- `docs/dashboard-operating-manual.md`
- `project/runs/2026-07-03-vercel-jarvis-connection/`
- `wiki/log.md`
- `project/live/communication/agent-communication-log.md`

## Verification Plan

1. Compile Vercel Python API routes.
2. Parse `vercel.json`.
3. Regenerate and parse dashboard data.
4. Verify local FastAPI `/health` and PRD/ICP lane.
5. Run dashboard static and screenshot smoke.
6. Deploy to Vercel.
7. Verify hosted `/health`, `/api/lanes/prd-icp`, and `/dashboard`.
8. Update Notion and Telegram.

