# Agent Handout: Vercel Dashboard And Jarvis Connection

Date: 2026-07-03
Status: complete for Vercel provider-disabled dashboard/Jarvis connection
Lane: E1.7 hosted dashboard/Jarvis connection

## Goal

Make the hosted Vercel dashboard connect to a working provider-disabled Jarvis API surface while keeping local Jarvis working on `127.0.0.1:8787`.

## Current Implementation

FACT:
- The static dashboard remains served by Vercel through `/dashboard`.
- A Vercel serverless Jarvis contract now exists under `api/`.
- `/health` rewrites to `/api/health` on Vercel.
- The Vercel-hosted API was reduced to the core dashboard connection surface after the first deploy hit the hosting-plan serverless function limit.
- The hosted API returns review packets only.
- Provider calls, durable writeback, raw audio storage, Telegram automation, and production publication remain disabled.
- Local FastAPI Jarvis was restarted on port `8787` with OpenRouter selected in status and provider calls still disabled behind budget/approval guards.
- Production Vercel deployment is ready at `https://public-meacasjjm-mcharniuk1-4994s-projects.vercel.app`.
- Production alias is `https://public-ruddy-nine-40.vercel.app`.
- Hosted `/health` returns `status=ok`, `hosting=vercel_serverless`, `model_provider=openrouter`, `provider_calls=0`, and `writeback=disabled`.
- Hosted `/api/lanes/prd-icp` returns `review_packet_created`.
- Hosted `/dashboard` returns 200.
- Hosted `/project/dashboard/data.json` returns 200 with `Cache-Control: no-store`.
- Notion E1 parent, E1.3.9, and E1.7 were updated through the connector.
- Telegram delivery succeeded through the approved sender path.

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

1. Compile Vercel Python API routes. Passed.
2. Parse `vercel.json`. Passed.
3. Regenerate and parse dashboard data. Passed.
4. Verify local FastAPI `/health` and PRD/ICP lane. Passed.
5. Run dashboard static and screenshot smoke. Passed.
6. Deploy to Vercel. Passed after reducing hosted API to fit the serverless function limit.
7. Verify hosted `/health`, `/api/lanes/prd-icp`, and `/dashboard`. Passed.
8. Update Notion and Telegram. Passed.

## Deployment Notes

The first production deploy failed because the initial Vercel API surface exceeded the current serverless function limit. The hosted API was reduced to the core dashboard connection endpoints: `/health`, `/api/chat`, `/api/config/roles`, `/api/lanes/prd-icp`, `/api/lanes/agent-orchestra`, and `/api/voice/chat`.

The local FastAPI service still keeps the broader development endpoint set for future Railway migration.

## Final State

The dashboard and Jarvis are connected to Vercel for provider-disabled review packets. Local Jarvis also works again on port `8787`. OpenRouter is selected in status, but provider calls remain disabled by approval and budget guards.
