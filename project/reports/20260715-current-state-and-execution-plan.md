# ArchFlow Current State and Execution Plan

Date: 2026-07-15

Status: active implementation and verification plan

## One-sentence position

ArchFlow currently provides a public-safe Knowledge Reliability Setup and Agent Control console that prepares reviewable, source-grounded work packets locally; its provider, durable-runtime, external-writeback, and multi-user product layers remain gated.

## Current state

| Area | Current state | Evidence | Confidence |
|---|---|---|---|
| Public product surface | Website, dashboard, Jarvis report/download console, Operating Manual, generated public catalog | Current public source, ten-route dashboard smoke, and Jarvis static contract | High within static/browser scope |
| Knowledge Service | Browser-local source-to-report preparation with explicit evidence labels | Dashboard manual, current architecture report, review-packet contract | High within public-safe scope |
| Agent Control | Browser-local role/skill/task/handoff preparation with parallel-branch boundaries | Manual route, role catalog, task contracts, communication protocol | High for contract representation; not live execution |
| Workflow architecture | LangGraph-style routing, bounded CrewAI role contracts, LlamaIndex retrieval contract, Graphify reference, WikiLLM durable-memory boundary | Workflow validation and public architecture docs | Review/proven by bounded fixtures, not continuous runtime |
| API and safety | Guarded Jarvis contract, owner/acknowledgement/allowlist/replay gates, provider calls/writeback zero | API and serverless smoke outputs | High for tested contract |
| Browser QA | Ten current dashboard routes and the Jarvis report/download contract render after manual-route repair | `dashboard_static_smoke=ok routes=10 jarvis_static=ok provider_calls=0 writeback=0` | High for the tested environment |
| Model efficiency | Local deterministic fixture has token/cost fields; provider efficiency is unmeasured | Yushchenko reports and model-efficiency issue register | Explicit GAP |
| Production/backend | Static public hosting path exists; always-on backend, live provider execution, and durable database are not current proof | Production and runtime reports | Gated |
| External systems | Notion/Nexus/GitHub/Telegram/Figma actions require target-specific proof and approval | External-action gates and task contracts | Gated |

## What is actually efficient now

The efficient unit is a bounded public-safe review cycle:

1. Read the current source-of-truth files.
2. Create one task contract with owner, reviewer, files, evidence, stop rule, and gate.
3. Use the dashboard/manual to prepare a local report or handoff.
4. Run the smallest relevant deterministic checks.
5. Let an independent reviewer inspect the result.
6. Integrate, update the current report, and only then consider commit/push/deploy/writeback as separate actions.

This reduces repeated broad scans, prevents parallel-file conflicts, and keeps provider spend at zero. It is not a measured claim about live model throughput or token cost.

## Staged execution plan

| Stage | Objective | Output | Required verification | Gate / stop rule |
|---|---|---|---|---|
| 0. Current-state lock | Keep one current architecture, dashboard manual, and test report aligned. | Updated reports and run handout. | Safety, syntax, data parse, workflow, API guard, runtime guard, browser smoke, diff check. | Stop if a report claims more than its evidence. |
| 1. Public console hardening | Keep `#manual`, `#operations`, `#schema`, Jarvis, and generated data internally consistent. | UI/docs patch and regenerated data. | Ten-route smoke, no provider calls, no writeback, mobile/desktop review. | Stop on private-data, auth, or live-runtime requirement. |
| 2. Sanitized event fixture | Make future live-status claims evidence-shaped without activating a runtime. | Runtime-event schema fixture and read-only display contract. | Schema parse, stale-event rejection, source/evidence reference check. | Do not call a browser animation “live” without a fresh event. |
| 3. Canonical efficiency ledger | Separate local deterministic proof from future provider-backed usage. | Public-safe model-call ledger schema and fixture. | Required token, cost, model, latency, source, reviewer, and budget fields; privacy scan. | No provider activation until ledger, budget, owner auth, and readback exist. |
| 4. Bounded retrieval benchmark | Measure retrieval quality and provenance on an approved corpus. | Benchmark packet with baseline, candidate, queries, citations, and rollback. | 20-query benchmark, lexical fallback, provenance, private-boundary rejection. | Keep vector/TurboVec/Cognee non-canonical until paired evidence passes. |
| 5. Installability and database decision | Decide whether the public setup becomes a distributable package or remains a service/setup method. | License decision, installability checklist, evidence-ledger design. | Dependency, permission, migration, backup/restore, auth, tenancy, and security review. | Do not claim SaaS/multi-user readiness without proof. |
| 6. Owner-approved external lane | Only if specifically requested: provider, deployment, Notion/Nexus/GitHub, Telegram, Figma, or production promotion. | Target-specific action packet, receipt, readback, rollback record. | Exact target/schema, approval, idempotency, safety, post-action verification. | One approval authorizes one bounded action only. |

## Parallel-chat execution contract

Use one integrator plus independent sidecars:

- Architecture reviewer: checks layer responsibilities, proof state, and future-gate logic.
- Dashboard/UX reviewer: checks routes, interaction, accessibility, and browser-local truth.
- Technical/runtime reviewer: checks API, workflow, provider, environment, and hosting boundaries.
- Safety reviewer: checks public/private separation, secrets, provenance, and unsupported claims.
- Integrator: owns file claims, merge order, final tests, report updates, and handoff.

Each sidecar must read the live communication files, claim disjoint files, avoid external actions, and return exact evidence. If two chats need the same file, pause and coordinate before editing. The full procedure is in [`docs/dashboard-operating-manual.md`](../../docs/dashboard-operating-manual.md).

## Decision gates before calling the work complete

- Current report and dashboard manual link to the same test-results report.
- `#manual` and all current routes render.
- Static and API checks pass in the documented project environment.
- Provider calls and writeback remain zero in public smoke tests.
- No claim of provider efficiency is made without a provider-backed ledger.
- Remaining gaps are recorded rather than hidden in “Done” language.
