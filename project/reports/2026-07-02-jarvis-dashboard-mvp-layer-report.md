# Jarvis Dashboard MVP Layer Report

Date: 2026-07-02
Status: implementation complete for static/dashboard and provider-disabled API-contract scope

## 1. Public Website Layer

No buyer-facing website content was changed. The public website remains separate from the operator dashboard and should not claim live Jarvis, provider, Railway, or autonomous execution.

## 2. Dashboard UI Layer

`project/dashboard/app.js` and `project/dashboard/styles.css` now expose a stronger operator surface:

- fixed bottom global composer with safe-area padding;
- Jarvis voice controls for mic, stop, cancel, timer, transcript preview, send transcript, playback, stop playback, and auto-speak;
- block-schema zoom controls;
- visible API/env/budget status;
- generated data refreshed through `project/scripts/generate-dashboard-data.py`.

## 3. Screen (1) PRD/ICP Flow

Screen 1 now includes a direct PRD/ICP request surface. It attempts the local backend lane when available and falls back to a browser-local review packet when the backend is unavailable.

Visible output blocks:

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

The output contract includes suggested Jira/GitLab backlog and missing-info questions.

## 4. Screen (2) Agent Orchestra

Screen 2 now shows:

- task stages from Intake through Final Decision;
- editable browser-local role configuration cards;
- role fields for objective, responsibility, tools, model route, budget mode, output artifact, review gate, status, and handoff target;
- exportable role review packets.

Required named roles are represented: Jesus, LOL, Ronaldinho, Messi, Ronaldo, Yushchenko, Theory subagent, Security subagent, Actor, AF Tools, AF Knowledge, AF Publisher, AF Review, and CrewAI role workers.

## 5. Backend/API Layer

`services/jarvis-api/` was added as a provider-disabled FastAPI service contract.

Implemented endpoints:

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

The current local runtime does not have FastAPI installed, so import/runtime smoke is dependency-gated. Syntax compilation passed.

## 6. LangGraph Routing Layer

LangGraph remains the controller for routes, state, approval gates, and review stops. The dashboard renders the Prompt 1.2 two-lane contract and does not claim live LangGraph worker execution from the browser.

## 7. OpenRouter Model/Budget Layer

OpenRouter remains disabled. The budget contract is preserved:

- daily cap: `5.00` USD;
- run hard stop: `1.99` USD;
- over-cap behavior: stop and request owner approval.

The API contract stops provider routes unless approval, server-side secrets, and budget environment are present. Browser provider keys remain forbidden.

## 8. CrewAI Role/Direct-Proof Layer

CrewAI Level 3 remains `proof_passed_not_default_runtime`. The dashboard and API show that proof as deterministic local evidence only. It is not default runtime, provider runtime, production runtime, or writeback proof.

## 9. Voice/STT/TTS Layer

Voice is browser-local UI only:

- browser speech recognition can fill an editable transcript preview;
- manual transcript fallback is preserved;
- browser speech synthesis can play replies;
- auto-speak is explicit and local;
- raw audio and raw transcript persistence remain off by default.

## 10. Retrieval/Memory Layer

WikiLLM remains the durable public memory layer. The dashboard can create local packets, but it does not write WikiLLM, Obsidian, Notion, GitHub, or Telegram without an approved operator/backend path.

## 11. Notion/GitHub/WikiLLM Reporting Layer

Docs and run artifacts were added for PRD/ICP output, daily/weekly reporting, test runbook, role configuration, and CrewAI/LangGraph operations. Append-only Notion evidence notes were added to the matching E1/E1.2/E1.3.9/security/reporting rows. Live Notion writeback is not active from the dashboard.

## 12. Env/Secret Layer

`docs/tgapi.md` was removed after a Telegram-token-shaped value was detected. New tracked env examples contain placeholders only:

- `.env.example`
- `services/jarvis-api/.env.example`

Real values remain in ignored env files or provider secret stores.

## 13. Deployment/Railway Readiness Layer

Railway deployment was not started. The API service is a local/backend contract that can become a Railway service only after account, spend, auth, secret storage, allowed origins, and write policy are approved.

## 14. What Works Now

- Static dashboard UI renders stronger PRD/ICP and Agent Orchestra surfaces.
- Browser-local packets preserve requests when backend is unavailable.
- Voice controls are visible and review-oriented.
- Role config panels can be edited locally and exported.
- API files and endpoint contracts exist.
- Templates and runbook docs exist.
- Dashboard data generation knows about the API and template status.
- Public safety, workflow validation, runtime guard, CrewAI config check, dashboard JSON parse, node syntax check, dashboard static smoke, and diff whitespace checks pass.

## 15. What Is Mocked/Deferred

- Live FastAPI runtime import is deferred until FastAPI dependencies are installed.
- Backend persistence, queues, auth, SSE/websocket, and Railway deployment are deferred.
- Default provider-backed OpenRouter operation remains deferred, except for the completed 2026-07-03 sanitized E1.2.8 comparison.
- Live dashboard-driven Notion/GitHub/WikiLLM/Telegram writeback is deferred.
- The private-fixture E1.2.8 PRD/PDF test cycle is no longer deferred; it completed locally and has a review-gated OpenRouter comparison.

## 16. What Is Gated By Owner Approval

- Running the full PRD/ICP test cycle.
- OpenRouter activation.
- Provider-backed CrewAI.
- Default CrewAI runtime promotion.
- Railway deployment.
- Production Telegram automation.
- Dashboard-driven Notion live writeback.
- Production promotion and Figma sync.
