# Vercel Production Cure Report

Date: 2026-07-03
Status: complete for production-current guarded review flow; blocked for live provider execution
Scope: Vercel production alias, Railway Jarvis API, guarded OpenRouter routes, dashboard freshness, and Epic 1 cloud closeout

## Executive Verdict

The public dashboard cure succeeded for the review-flow scope. The exact public URL now points to the current Vercel production deployment, loads the dashboard, serves regenerated July 3 dashboard data, and exposes the Vercel same-origin Jarvis API.

Railway is also healthy for the Jarvis API. The service uses the Python/Nixpacks deployment path, passes health checks, stays awake, and serves the Architecture 1 PRD/ICP, Architecture 2 agent-orchestra, role config, role-update candidate, chat, and voice-text routes.

OpenRouter execution is wired but not activated. Both Vercel and Railway report `MODEL_PROVIDER=openrouter`, but provider calls remain `0` because copying the local OpenRouter key into external SaaS runtime env storage was blocked by approval review. That is the correct safety outcome until explicit credential-storage approval is given.

## What Changed

| Area | Result |
|---|---|
| Vercel production alias | Public dashboard URL now points to the current production deployment |
| Dashboard freshness | Production `data.json` is current for this cure run |
| Vercel API | `/api/health`, Architecture 1, Architecture 2, voice-text, and role config routes work |
| Railway API | Final deployment succeeded with Nixpacks, healthcheck path, restart policy, and one running instance |
| OpenRouter path | Guarded server-side path implemented for Vercel and Railway |
| Provider calls | `0`; approved-route tests stopped at `openrouter_api_key_missing` |
| Writeback | `0`; no Notion/GitHub/WikiLLM writeback from dashboard/API |
| Legacy Vercel projects | No deletion performed; no project was proven unused enough for safe deletion |

## Endpoint Matrix

| Surface | Check | Result | Interpretation |
|---|---|---|---|
| Public dashboard | `GET /project/dashboard/` | Passed | Current review surface is reachable |
| Public dashboard data | `GET /project/dashboard/data.json` | Passed | Regenerated during the final deployment sync and served with no-store caching |
| Vercel API | `GET /api/health` | Passed | `MODEL_PROVIDER=openrouter`, provider calls `0`, writeback `0` |
| Vercel Architecture 1 | `POST /api/lanes/prd-icp` with provider approval flags | Passed as review packet | Route is wired; provider execution blocked at missing approved server-side key |
| Vercel Architecture 2 | `POST /api/lanes/agent-orchestra` with provider approval flags | Passed as review packet | Agent-control route is wired; provider execution blocked at missing approved server-side key |
| Vercel voice-text | `POST /api/voice/chat` | Passed as review packet | Text transcript path only; no raw audio storage |
| Vercel roles | `GET /api/config/roles` | Passed | Role config is available |
| Railway health | `GET /health` | Passed | `MODEL_PROVIDER=openrouter`, provider calls `0`, writeback `0` |
| Railway CORS | Preflight from public dashboard origin | Passed | Dashboard origin can call hosted API |
| Railway Architecture 1 | `POST /api/lanes/prd-icp` with provider approval flags | Passed as review packet | Route is wired; provider execution blocked at missing approved server-side key |
| Railway Architecture 2 | `POST /api/lanes/agent-orchestra` with provider approval flags | Passed as review packet | Agent-control route is wired; provider execution blocked at missing approved server-side key |
| Railway voice-text | `POST /api/voice/chat` with provider approval flags | Passed as review packet | Voice-text route now reads provider approval fields; raw audio remains off |
| Railway role update | `POST /api/config/roles/update` | Passed as candidate packet | Configuration updates are review candidates, not durable writes |

## Issue Found And Fixed

FACT:

- The first Railway replacement deploy used the wrong archive root and was detected as a static/Caddy app.
- That deployment crashed because `uvicorn` was unavailable.
- The previous healthy Railway instance continued serving while the replacement failed.
- Redeploying with the service directory as the archive root made Railway detect the Python/Nixpacks service correctly.
- A follow-up Vercel publish wrapper run targeted the older parent Vercel project because it executes from the parent ArchFlow folder.
- The canonical public URL was corrected by deploying directly from the `public` repo root and assigning the public alias to that deployment.
- Health metadata was corrected from older provider-disabled wording to `guarded_openrouter_review_packet`.

INTERPRETATION:

The reliable Railway deploy command for this service must force the service directory as the deployment root. Otherwise Railway may infer the public repository as a static app and ignore the Python requirements.

The reliable Vercel deploy command for this public dashboard must run from the public repo root when the target is `archflowautomate.vercel.app`. Parent-folder deploy wrappers can be useful for their own linked project, but they are not proof that the canonical public dashboard was updated.

NEXT:

Use the path-root Railway deploy pattern for future `services/jarvis-api` deploys. Use direct public-root Vercel deploy plus alias verification for the canonical dashboard URL.

## Vercel Legacy Cleanup Decision

No Vercel projects were deleted. The current team shows more than one project, but there was not enough evidence to prove which historical projects are unused and safe to remove. The safe cure was to update the public alias to the current `public` production deployment.

Deletion should only happen after an explicit inventory that checks project name, latest production URL, linked domains, Git source, recent deployment activity, and owner confirmation.

## Remaining Gates

| Gate | Status | Required next |
|---|---|---|
| OpenRouter live execution | Blocked | explicit approval to store the key in Vercel/Railway env, then one low-cost ledgered test |
| Durable writeback | Blocked | auth, approval workflow, audit log, rollback |
| Client workspaces | Not built | auth, persistence, data isolation |
| Raw voice/STT/TTS | Not productized | retention policy, provider decision, storage boundary |
| Full LangGraph cloud state machine | Not proven | hosted state transitions, persistence or explicit stateless contract |
| Default CrewAI runtime | Not promoted | controlled artifact-producing run and reviewer verdict |

## Epic 1 Status

Epic 1 is complete for the production-current guarded cloud review-flow scope. It remains Review for full product runtime and should not be sold as a self-serve SaaS until provider execution, auth, persistence, writeback, and buyer proof are separately implemented and verified.
