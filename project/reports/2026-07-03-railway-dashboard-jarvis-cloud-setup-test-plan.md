# Railway Dashboard And Jarvis Full-Cloud Setup Test Plan

Date: 2026-07-03
Status: setup/test plan complete, deployment not executed in this run
Scope: E1.7 hosted dashboard, Jarvis API, and agentic control surface

## Executive Answer

Railway is the right next backend host only for runtime features that Vercel static/serverless review packets cannot honestly provide: long-running workers, queues, provider calls, SSE/websocket events, durable uploads, persistent run state, auth, and controlled writeback.

Current proven state is Vercel-connected and provider-disabled. Railway has service scaffolding and prior MCP/project initialization evidence, but no deployment or `/health` proof. E1.7 should finish when Railway runs a provider-disabled Jarvis API with health, CORS/auth, budget guard, and dashboard routing verified without local Codex/Jarvis.

## Live Railway Check On 2026-07-03

FACT: The official Railway MCP is reachable and authenticated in this Codex session. Public report wording intentionally excludes account-identifying details.

GAP: The current local workspace is not linked to a Railway project. Environment status, deployment list, and service config queries fail because no `project_id` is available in this session. No Railway deployment or hosted `/health` test was executed in this run.

## Current Cloud Readiness

| Layer | Current proof | Status |
|---|---|---|
| Static dashboard | Vercel-hosted dashboard/provider-disabled API contract recorded in prior handout | Working for review packets |
| Local Jarvis API | FastAPI contract under `services/jarvis-api/` | Code scaffold exists |
| Railway | Prior run created project/service and variables; deployment blocked by approval | Not deployed |
| Provider calls | `MODEL_PROVIDER=none` default; provider routes disabled | Gated |
| Writeback | Git/Notion/WikiLLM/Telegram dashboard writeback disabled | Gated |
| Voice | Browser-local controls and text path only | Gated for raw audio/storage |

## Target E1.7 Definition

E1.7 means: hosted dashboard, Jarvis API, and agentic system can run the provider-disabled review-packet contract without relying on the local machine.

It does not mean provider-backed automation, autonomous Notion/GitHub/WikiLLM writeback, raw voice storage, or paid customer runtime.

## Deployment Architecture

```text
Vercel static dashboard
  -> configured backend URL
  -> Railway jarvis-api service
  -> provider-disabled review packet endpoints
  -> logs/status packets
  -> Codex/owner review before any writeback
```

## Railway Setup Plan

| Step | Action | Check | Gate |
|---|---|---|---|
| R1 | Confirm Railway project/service from prior setup or link/create project | `railway status` or Railway MCP project/service list | Owner approval for cloud work |
| R2 | Deploy only `services/jarvis-api` | Railway deploy logs show build/start | Approval for code upload |
| R3 | Set env variables from placeholders | `MODEL_PROVIDER=none`, allowed origin, budget defaults | No secrets in repo |
| R4 | Verify health | `GET /health` returns ok, provider calls 0, writeback disabled | Required before dashboard routing |
| R5 | Verify CORS/auth boundary | Allowed origin works; disallowed origin blocked where applicable | Required before public URL use |
| R6 | Exercise endpoints | chat, roles, PRD/ICP, agent-orchestra, voice text route return review packets | Provider disabled |
| R7 | Point dashboard to Railway test backend | dashboard state shows connected and no provider calls | No production promotion |
| R8 | Record run | run note, PDF, dashboard data, wiki log, validation | Public safety scan |

## Endpoint Test Matrix

| Endpoint | Expected result | Failure meaning |
|---|---|---|
| `/health` | service ok, model provider none or gated, provider calls 0 | service not ready |
| `/api/chat` | review packet, no provider output | provider gate broken if it calls model |
| `/api/config/roles` | role config payload | dashboard cannot configure orchestra |
| `/api/lanes/prd-icp` | PRD/ICP review packet | Architecture 1 cloud route broken |
| `/api/lanes/agent-orchestra` | agent-orchestra review packet | Architecture 2 cloud route broken |
| `/api/voice/chat` | text review packet only | voice storage/provider risk if raw audio stored |

## Provider Activation Gate

Provider activation is a later lane. Required before any model call:

- server-side secrets only;
- current model list and pricing checked;
- ledger writes for model, input class, output class, token estimate, spend estimate;
- daily cap and run hard stop active;
- sanitized input class approved;
- AF Review and owner approval recorded;
- no raw private transcript, credentials, private URLs, local paths, or account IDs sent.

## What Full Cloud Setup Provides

For ArchFlow:

- a durable operator dashboard when local Codex/Jarvis is off;
- a cloud review-packet API for PRD/ICP and Agent Orchestra lanes;
- a future bridge for provider-backed tasks after budget/safety gates;
- a cleaner demo of the operating system behind the PRD Pack.

For clients:

- a visible method for turning source material into reviewed artifacts;
- stronger confidence that outputs are gated, traceable, and not raw AI chat;
- a future path toward secure client portals and artifact delivery.

## Critique

The current setup is useful but fragile if described as a finished product. It is an operator control system plus service-delivery proof, not yet a customer-ready cloud app. Railway should be used to prove backend reliability and policy enforcement first. Productization should wait until E2/E6/E7 prove buyer demand.

## Acceptance Criteria

- Railway deployment uses only `services/jarvis-api`.
- `/health` passes from the Railway domain.
- Provider calls remain zero.
- Writeback remains disabled.
- Dashboard connects to Railway backend in a test environment.
- Public safety scan, runtime guard, dashboard JSON parse, and diff check pass.
- Run handout and Notion/GitHub/Telegram packets are created.
