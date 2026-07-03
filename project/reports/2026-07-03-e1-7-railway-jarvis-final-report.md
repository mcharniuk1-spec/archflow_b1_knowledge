# E1.7 Railway Jarvis Final Report

Date: 2026-07-03
Status: Review / provider-disabled hosted runtime verified
Scope: hosted Jarvis API, dashboard API routing, agent-orchestra review packets, final Epic 1 runtime gate

## Executive Result

E1.7 is complete for the provider-disabled hosted runtime baseline. The Railway `jarvis-api` service was deployed from the service root, reached running success state, received a Railway service domain, and passed hosted HTTPS checks for health, CORS, chat, PRD/ICP, agent-orchestra, role config, and voice-safe text routes.

This is not a full customer SaaS runtime yet. Provider calls, durable writeback, raw voice storage, authenticated client portals, and persistent client data remain gated.

## Proof Scorecard

| Capability | Score | Visual | Current result |
|---|---:|---|---|
| Hosted API availability | 5/5 | ##### | Railway service running and health route passed |
| Provider safety | 5/5 | ##### | `MODEL_PROVIDER=none`, provider calls `0` |
| Writeback safety | 5/5 | ##### | external writeback `0`; dashboard writeback still gated |
| Dashboard routing | 4/5 | ####. | API-base config and lane send controls implemented; latest site deploy remains a review-link step |
| Multi-agent control surface | 4/5 | ####. | Architecture 2 packet route passes; real autonomous execution remains gated |
| Voice runtime | 2/5 | ##... | text-only voice-safe packet passes; raw audio, STT, TTS, and storage are not productized |
| Product readiness | 2/5 | ##... | backend proof exists; auth, persistence, billing, and customer workspaces are missing |

## Architecture Proven

```text
dashboard browser
  -> local API-base setting
  -> hosted Railway Jarvis API
  -> provider-disabled review packet
  -> owner/Codex review before any durable write
```

## Endpoint Evidence

| Check | Result | Safe interpretation |
|---|---|---|
| Railway service status | Passed | latest deployment running successfully |
| Railway service domain | Passed | HTTPS domain generated and reachable |
| `GET /health` | Passed | runtime reports ok, provider none, zero model calls, zero writeback |
| CORS preflight | Passed | Vercel dashboard origin allowed for POST traffic |
| `POST /api/chat` | Passed | returns review packet without provider call |
| `GET /api/config/roles` | Passed | role configuration available for dashboard control |
| `POST /api/lanes/prd-icp` | Passed | Architecture 1 PRD/ICP packet works |
| `POST /api/lanes/agent-orchestra` | Passed | Architecture 2 control packet works |
| `POST /api/voice/chat` | Passed | text-only voice packet works; no raw audio persistence |
| Deploy logs | Passed | server started on assigned Railway port |
| Recent HTTP error logs | Passed | no hosted HTTP errors returned for validation probes |

## Dashboard And Configuration

The dashboard now supports a configurable Jarvis API base URL stored only in the browser. The operator can:

- save a hosted backend origin;
- check hosted `/health`;
- export the dashboard configuration packet with the selected API base;
- send service-mode packets to `/api/lanes/prd-icp`;
- send control-mode packets to `/api/lanes/agent-orchestra`.

This makes the dashboard configurable without committing runtime URLs or secrets into the public repository.

## Multi-Agent Architecture Status

| Layer | Current state | Productization gap |
|---|---|---|
| Architecture 1: service workflow | PRD/ICP packet route passes on Railway | needs source-card persistence and auth |
| Architecture 2: control workflow | agent-orchestra packet route passes on Railway | needs durable role state, approvals, and audit log |
| LangGraph controller | represented as the safe control contract | not yet a live cloud state machine |
| CrewAI roles | role config and proof lane represented | not default autonomous runtime |
| WikiLLM/Notion/GitHub | updated by Codex after review | dashboard-driven writeback remains disabled |

## Current Service Representation

For ArchFlow, this setup represents a controlled PRD Pack operating system:

- source material becomes reviewed artifacts;
- review packets separate service workflow from system-control workflow;
- the KB update principle controls what becomes memory;
- the hosted API can receive dashboard packets without provider spend;
- Codex remains the responsible operator for durable writes.

For clients, this can be described as a gated productized service method, not yet as a self-serve SaaS:

- inputs are handled through a source-bound process;
- outputs are PRD, backlog, decisions, questions, risks, and handoff artifacts;
- AI output is review-gated;
- sensitive data and raw transcripts are not stored in the public proof system.

## Critique

The main risk is overclaiming. The hosted runtime works, but it is intentionally narrow. It proves a safe backend bridge for review packets, not a complete cloud product. The next quality step is not more UI; it is auth, persistence, audit logging, provider budget ledgering, and a buyer-validated workflow from Epic 2.

## Remaining Gates

| Gate | Status | Required before Done |
|---|---|---|
| Provider-backed Jarvis | Gated | server-side secrets, budget ledger, sanitized input policy, owner approval |
| Durable writeback | Gated | authenticated action approvals, audit log, rollback policy |
| Raw voice/audio | Gated | raw audio policy, retention limits, STT/TTS provider decision |
| Client portal | Gated | auth, workspace isolation, data policy, billing path |
| Market proof | Gated | Epic 2/E6/E7 evidence and paid-intent test |

## Acceptance

E1.7 can move to Review for the provider-disabled hosted runtime. It should not move to Done for full cloud product runtime until the remaining gates are implemented and verified.
