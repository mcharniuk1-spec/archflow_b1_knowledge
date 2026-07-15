# ArchFlow Public Product Operations Architecture Report

Date: 2026-07-15

Status: active current public architecture baseline

Scope: public website, dashboard, Jarvis, generated public data, role/skill presentation, documentation, local review packets, and the evidence/approval boundaries around future runtime work.

## Executive conclusion

FACT: The current ArchFlow public product is a documentation-first Knowledge Reliability Setup plus an Agent Control surface. It is implemented as a public-safe, browser-local console with generated JSON, local draft state, review-packet exports, guarded provider-disabled API contracts, and explicit handoff gates.

FACT: The current dashboard and Jarvis surface now includes an Operating Manual route, Knowledge Service and Agent Control explanations, browser-local Administrator/Guest preview labels, shared local report context, local Markdown/JSON report downloads, role/skill catalog references, and current report/test links.

FACT: The current verified setup passes public safety, JavaScript syntax, generated-data parsing, local workflow validation, guarded Jarvis API contract checks, serverless owner-guard checks, runtime guard checks, and a ten-route rendered dashboard smoke with `provider_calls=0` and `writeback=0`. Exact commands and environment limitations are recorded in [`20260715-architecture-test-results.md`](20260715-architecture-test-results.md).

INTERPRETATION: This is an efficient bounded preparation, review, and handoff system. It is not yet an always-on autonomous agent runtime, a multi-user application, a live database, or a provider-backed production system.

GAP: No canonical provider-backed model-call ledger exists. The local deterministic CrewAI proof ledger demonstrates local mechanics and zero-cost test execution; it does not prove OpenRouter or other provider efficiency.

## Current architecture

| Layer | Current responsibility | Current proof | Next graduation gate |
|---|---|---|---|
| Authority and goal | Bind objective, owner, scope, stop rule, and approval boundary. | Public task contracts and operating rules. | Operator accepts a task-specific contract. |
| Context and knowledge | Assemble the smallest source-grounded context capsule and preserve provenance. | Public WikiLLM/Graphify/LlamaIndex contracts and bounded corpus descriptions. | Bounded-corpus benchmark with current evidence. |
| Plan and orchestration | Represent typed routes, checkpoints, parallel branches, merge, and stop conditions. | LangGraph workflow contract and deterministic smoke fixtures. | Sanitized runtime-event feed for live status. |
| Execution and roles | Assign role, skills, tools, output schema, reviewer, and forbidden actions. | 21 public role contracts and 12 reviewed public skill packages. | Approved executor under a claimed file scope. |
| Loop and verification | Separate maker from reviewer and cap retries/repairs. | Review contracts, runtime guard, API owner-guard tests. | Representative independent fixtures and recovery evidence. |
| Memory and external gate | Promote reviewed conclusions and hold external actions behind approval. | WikiLLM/run/decision contracts and browser-local review bundles. | Current target, schema, idempotency, rollback, approval, and readback proof. |
| Measurement and optimization | Compare quality, reliability, retrieval, latency, tokens, cost, and human effort. | Measurement policy and local deterministic ledger examples. | Canonical public-safe event/model-call ledger and paired benchmark. |

## Product surfaces and current flow

### Knowledge Service

Use this lane when bounded public-safe context must become a PRD, ICP brief, decision, evidence map, backlog, context capsule, or knowledge-update candidate.

1. State the goal, source boundary, allowed evidence, exclusions, intended output, constraints, reviewer, and stop rule.
2. Prepare a browser-local review report with `FACT`, `INTERPRETATION`, `HYPOTHESIS`, and `GAP` sections.
3. Download the report for Codex/operator review.
4. Do not treat the download as a repository patch, Git commit, provider request, database write, or memory promotion.

### Agent Control

Use this lane after the desired work needs role assignment, skills/tools, source allowlists, LangGraph-style routing, parallel branches, independent review, approval nodes, and a durable handoff.

1. Reference a reviewed Knowledge Service report.
2. Define the role, skill/source/tool boundary, expected artifacts, reviewer, file claim, approval gate, repair cap, and stop condition.
3. Give each parallel chat an exclusive scope; do not assign two chats the same write target.
4. Merge branch evidence through the integrator before any repository or external action.

### Dashboard and Jarvis

- Canonical dashboard: `/project/dashboard/`; `/dashboard` redirects to it.
- Default view: `#manual`, the current developer-facing operating guide.
- Main views: `#overview`, `#architecture`, `#knowledge`, `#agents`, `#operations`, `#data`, `#runs`, `#reference`, and `#manual`.
- Detailed tools: `#service`, `#schema`, `#config`, `#wikillm`, `#graphify`, `#langgraph`, `#llamaindex`, `#crewai`, `#langsmith`, `#env`, and `#gates`.
- `/jarvis` is a guarded text review console. It prepares a local Knowledge Service report first, then an Agent Control handoff and downloads; provider execution, raw voice storage, and durable writeback remain disabled by default.
- Administrator/Guest are browser-local preview labels. They are not authentication, authorization, tenancy, or durable per-user memory.

The detailed procedure is [`docs/dashboard-operating-manual.md`](../../docs/dashboard-operating-manual.md), and the dashboard route is described in [`project/dashboard/README.md`](../dashboard/README.md).

## Parallel-chat operating model

FACT: Separate chats can work safely only as bounded sidecar lanes under one integrator.

Before work, every chat reads the live communication README, current notice, latest log, and task contract; states one role, one output, one file scope, one reviewer, one stop condition, and one next action; then appends a public-safe `starting` update.

During work, the chat stays inside its claimed scope, announces scope changes before editing, records exact checks, and stops on file overlap, private-data requirements, provider activation, deployment, or external-write requirements.

At handoff, it returns changed files, checks, `FACT / INTERPRETATION / HYPOTHESIS / GAP`, blockers, and an `approve`, `revise`, or `block` recommendation. The integrator compares claims against the current files, preserves contradictions as gaps, reruns checks, updates the run handout/current report, and appends a closing communication entry.

The coordination contract is [`project/live/communication/README.md`](../live/communication/README.md). The current manual task contract is [`project/runs/20260715-dashboard-operating-manual/task-contract.md`](../runs/20260715-dashboard-operating-manual/task-contract.md).

## Setup efficiency: what is proved

The setup is efficient within the bounded public/static scope because one local validation pass covers data shape, workflow shape, API safety, owner gates, runtime guardrails, public safety, and rendered route behavior without activating a provider.

Proved in the current run:

- public data parses and remains generated rather than pretending to be a live database;
- workflow validation covers LangGraph, LlamaIndex, CrewAI, knowledge integration, market research, and model-routing contracts;
- the guarded Jarvis API checks 18 endpoint cases plus five owner/approval/replay/CORS cases;
- the serverless owner guard proves owner, acknowledgement, allowlist, durable-control, and replay gates;
- the runtime guard verifies configured workflow fixtures without provider activation;
- the current ten dashboard routes plus the Jarvis report/download static contract render with zero provider calls and zero writeback;
- the public-safety scan and JavaScript syntax checks pass.

Not proved:

- provider token/cost efficiency or model-quality efficiency;
- continuous uptime, hosted freshness, real subagent launch, live Nexus/Notion/GitHub writeback, or durable multi-user memory;
- a production database or live event feed;
- buyer demand, paid intent, ROI, or customer outcomes.

## Current production truth

| Capability | State | Evidence interpretation |
|---|---|---|
| Public website and dashboard source | Implemented and Git-tracked | Local/public source and browser/static proof exist. |
| Dashboard data | Generated public JSON | Refresh after source/report changes; not a live database. |
| Jarvis review-packet contract | Guarded and provider-disabled | API contract checks pass; provider execution remains blocked by design. |
| Local FastAPI contract | Locally testable in project virtual environment | Contract smoke passes; always-on hosting is not inferred. |
| Railway | Future backend lane | Requires separate service, auth/CORS, logs, budget, health, rollback, and approval proof. |
| Notion/Nexus/GitHub writeback | Not enabled from the public browser | Requires exact target/schema/idempotency/rollback/readback and owner approval. |
| Parallel-agent execution | Contracted, not always running | Chats must be explicitly assigned and independently reviewed. |
| Provider runtime | Disabled | No current provider-backed token/cost ledger exists. |

## Current gaps and next gates

1. Maintain the current manual route and ten-route smoke contract as the dashboard changes.
2. Add a sanitized runtime-event fixture before showing any live stage or “running” state.
3. Add a canonical provider/model-call ledger before making efficiency or cost claims.
4. Keep the public Data Lab bounded until an evidence-ledger design proves migrations, read-only queries, limits, audit, backup, restore, and private-source isolation.
5. Decide on a software license before claiming redistribution/installability.
6. Treat commit/push, deploy, provider activation, Notion/Nexus/GitHub writeback, and production promotion as separate owner-approved releases.

## Source-of-truth files

- [`project/reports/20260715-current-state-and-execution-plan.md`](20260715-current-state-and-execution-plan.md) — active implementation state and staged plan.
- [`project/reports/20260715-architecture-test-results.md`](20260715-architecture-test-results.md) — exact current checks and limitations.
- [`docs/dashboard-operating-manual.md`](../../docs/dashboard-operating-manual.md) — detailed operator and parallel-chat usage.
- [`project/dashboard/README.md`](../dashboard/README.md) — quickstart and command reference.
- [`project/strategic-plan-2026-07-13.md`](../strategic-plan-2026-07-13.md) — strategic E1-E8 spine; use the 2026-07-15 report for current implementation truth.
