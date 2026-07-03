# Cloud And KB Retrospective

Date: 2026-07-03
Status: Review
Scope: Jarvis cloud reliability, Vercel freshness, E1.6 collaborator KB, daily founder-note addendum, Graphify/Obsidian knowledge-system retrospective

## Executive Verdict

The Jarvis cloud path is working for the current provider-disabled review-packet baseline. Railway is running and the hosted API passed all checks used in this continuation.

It is not perfect yet. Vercel production is reachable and browser-clean, but it serves an older dashboard data bundle than the current E1.7 review preview. Therefore the correct status is:

```text
Railway Jarvis review packets: working
Vercel production availability: working
Vercel production freshness: stale
Vercel current preview: ready and fresh
Full product runtime: gated
```

## Scorecard

| Area | Score | Visual | Result |
|---|---:|---|---|
| Railway API availability | 5/5 | ##### | service running, health passed |
| Provider safety | 5/5 | ##### | provider calls stayed `0` |
| Writeback safety | 5/5 | ##### | external writeback stayed `0` |
| Endpoint coverage | 5/5 | ##### | health, CORS, chat, PRD/ICP, orchestra, roles, voice text, approval gate checked |
| Dashboard browser QA | 5/5 | ##### | production and current preview UI load, expected controls present, no browser errors found |
| Vercel update freshness | 3/5 | ###.. | current preview fresh after push; production still stale |
| Full SaaS product runtime | 2/5 | ##... | auth, persistence, provider ledger, writeback, voice storage, client workspaces remain gated |

## Cloud Function Proof

| Function | Result | Meaning |
|---|---|---|
| Railway service state | Passed | hosted backend is running; private IDs are not stored in public files |
| `GET /health` | Passed | model provider `none`, provider calls `0`, writeback `0` |
| CORS preflight from Vercel production origin | Passed | production dashboard origin can call the hosted API |
| `POST /api/chat` | Passed | returns review packet only |
| `GET /api/config/roles` | Passed | role config is available |
| `POST /api/config/roles/update` | Passed as candidate packet | update is not durable until Codex/source review |
| `POST /api/lanes/prd-icp` | Passed | Architecture 1 service-output route works |
| `POST /api/lanes/agent-orchestra` | Passed | Architecture 2 control/orchestration route works |
| `POST /api/voice/chat` | Passed | text transcript packet only; no raw audio storage |
| `POST /api/test-runs/meeting-prd` without approval | Passed gate | returns approval-required, as intended |

## Vercel And Browser QA

FACT:

- Production dashboard route returned HTTP 200.
- Review preview dashboard route returned HTTP 200.
- After the main push, a non-production Vercel preview was created and reached `Ready`.
- Production browser snapshot showed the dashboard, Jarvis, PRD/ICP, Agent Orchestra, Config, Project Plan, WikiLLM, Graphify, LangGraph, LlamaIndex, CrewAI, LangSmith, Env, and Gates surfaces.
- Current preview browser snapshot showed the Jarvis command center, PRD/ICP, agent-orchestra, Config, project plan, WikiLLM, Graphify, LangGraph, LlamaIndex, CrewAI, LangSmith, Env, and Gates controls.
- Production Config screen exposed editable chain fields, `Save locally`, and `Export config packet`.
- `Save locally` was clicked successfully in the production browser session.
- Browser console and page-error probes returned no errors.
- Production dashboard data was generated on July 2.
- Review preview dashboard data was generated on July 3 after the E1.7 artifacts.
- Current preview dashboard data was generated on July 3 after the final cloud/KB retrospective update.
- Current preview URL and private deployment metadata are not stored in the public repo.

INTERPRETATION:

The user-facing production dashboard shell is healthy, but the production data bundle is stale. A current non-production preview exists for review. The main reliability defect is still production freshness, because production did not automatically reflect the latest pushed state during this continuation.

GAP:

- No production promotion was performed in this continuation because production promotion remains gated.
- Production should either be promoted explicitly from the current preview or have its Git-to-Vercel freshness repaired before it is treated as the always-current review surface.

## E1.6 Collaborator KB Update

The collaborator KB was structurally complete before this continuation, but it was not substantively populated. The new collaborator note turns the Daily Founder Notes packet into a role-specific working brief.

The collaborator lane now has:

- the reset-through-E1.7 story in public-safe language;
- the core proof chain;
- the ICP/product wedge correction;
- the cloud-runtime boundary;
- Epic 2 collaborator questions;
- explicit overclaiming risks.

This improves E1.6 from "folder exists" to "folder contains usable collaborator context."

## Primary-Operator Daily Founder Notes Addendum

The primary-operator note records the corrected July 3 interpretation:

- earlier daily founder notes were accurate for the pre-E1.7 state;
- the later E1.7 run moved Railway from gated to provider-disabled hosted baseline verified;
- Vercel production freshness remains the new problem;
- full product runtime remains gated.

This prevents future agents from reading the earlier current-state report and missing the later cloud proof.

## KB Retrospective

FACT:

- WikiLLM remains the durable memory layer.
- LlamaIndex remains bounded retrieval, not memory.
- Graphify remains generated structure, not final synthesis.
- Obsidian/Nexus remain human-readable semantic and live-vault layers after review.
- Daily founder notes are useful narrative memory, but they must be corrected by later proof when the same day has multiple major runs.

INTERPRETATION:

The current knowledge system is stronger when every layer has one job:

| Layer | Job | Current quality |
|---|---|---|
| WikiLLM | durable facts, runs, insights, memory | strong |
| Run handouts | continuation state and proof | strong |
| Reports/PDFs | human executive explanation | strong |
| Dashboard data | current public evidence index | useful but deploy freshness-dependent |
| Graphify | structural graph/reference | refreshed after new files; 4,913 nodes, 5,086 links, 461 communities |
| Obsidian/Nexus | semantic human control room | useful after public-safe sync, not a raw dump |
| Notion | task/PM/private review layer | append-only updates work; statuses must avoid overclaiming |

## Critique

The system is now better than a static dashboard, because Railway can serve review packets without the local machine. But it is still not a finished cloud product.

The biggest weakness is state freshness. A backend can be healthy while the public dashboard still shows stale generated data. A preview can be current while production remains stale. This creates a subtle overclaiming risk: "production loads" is not the same as "production reflects the latest verified project state."

The second weakness is durability. Role updates, dashboard config, and Jarvis packets are candidates until Codex reviews and writes files. That is safe, but it is not yet a true web app with durable state.

## Acceptance Position

E1.7 should remain:

```text
Review for provider-disabled hosted runtime
Not Done for full always-on product runtime
```

E1.6 should move from structural Review to stronger Review because the collaborator lane now has a substantive daily-note-derived brief.

## Next Gates

- Promote production only with explicit approval.
- Add an always-current deploy/freshness proof if production should be the primary review surface.
- Add auth, persistence, provider budget ledger, durable writeback approvals, audit logs, and client workspace isolation before SaaS claims.
- Run Epic 2 only from source-grade evidence cards and owner answers.
