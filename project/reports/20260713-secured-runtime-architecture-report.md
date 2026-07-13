# ArchFlow Secured Agentic Runtime and Public Product Architecture

**Status:** public-safe architecture baseline | 2026-07-13 | evidence-led review

## Executive summary

ArchFlow is being shaped as a public GitHub repository and a full-solution product for building knowledge bases and bounded agentic workflows. The public repository is the explainable, safe-by-default layer: website, dashboard, architecture contracts, role cards, demo fixtures, reports, and static proof. A private sibling layer holds local runtime state, private corpus manifests, checkpoints, journals, and owner-approved operational controls. Private knowledge is never copied into the public corpus; promotion is one-way, sanitized, and review-gated.

The current design is strong enough for a public architecture release and a controlled local runtime trial. It is not yet evidence for a production hosted agent, autonomous writeback, paid customer ROI, or an always-on service on this host. Those claims remain gated until their proof conditions are met.

## Evidence vocabulary and authority

- **PROVEN:** a deterministic local test, parser, safety scan, or artifact supports the claim.
- **REVIEW:** architecture is documented and checked, but the production proof is incomplete.
- **PLANNED:** a bounded next step with an explicit gate.
- **BLOCKED:** a safety, evidence, or host-runtime condition prevents promotion.
- **SUPERSEDED:** an older claim is retained only as history.

The public repository is the public product and communication surface. The private sibling is the operational control plane. WikiLLM and reviewed Obsidian notes are durable semantic memory; Graphify is generated structure; Nexus is a live bridge only after schema and socket proof. Codex remains the local integrator and editor. LangGraph owns execution state; no agent or provider may silently become the state owner.

## Architecture map

```text
Owner authority and goal contract
        |
Context capsule (CAG) + bounded corpus routing
        |
Plan and task graph (budget, stop, approval gates)
        |
LangGraph state, checkpoints, resumes, fan-out/fan-in
        |
CrewAI role packs / bounded makers / verifier / reviewer
        |
LlamaIndex retrieval cascade -> optional TurboVec trial
        |
Verification, safety scan, provenance, rollback
        |
WikiLLM + Obsidian semantic memory | Graphify structural reference | Nexus live bridge
        |
Public dashboard / GitHub artifacts / gated provider or writeback action
        |
Metrics, retrospective, issue and decision records
```

## Layer responsibilities

| Layer | Responsibility | Current state |
|---|---|---|
| Authority | Owner intent, scope, approvals, secrets boundary | PROVEN contract |
| Goal engineering | Objective, verifier, budgets, kill switches | REVIEW, public contract |
| Context | CAG capsule, project routing, corpus manifest | PROVEN private templates |
| Planning | Task graph, role assignments, dependency order | PROVEN local graph tests |
| Orchestration | LangGraph state, checkpoints, resumable paths | PROVEN 14/14 local tests |
| Execution | CrewAI-style role packs inside bounded graph nodes | REVIEW; direct CrewAI is not default |
| Retrieval | LlamaIndex cascade with lexical rollback | PROVEN fixture; production corpus absent |
| Compression | TurboVec 0.8.0 isolated optional trial | REVIEW; default promotion BLOCKED |
| Verification | maker/checker, safety, provenance, acceptance gates | PROVEN for current fixtures |
| Memory | WikiLLM, Obsidian, Graphify, Nexus with separate roles | REVIEW; live Nexus is not asserted |
| External action | Providers, deploy, writeback, private channels | BLOCKED/gated until owner proof |
| Measurement | recall, MRR, latency, failures, cost, review outcomes | REVIEW; synthetic baseline only |

## Connected tools, libraries, roles, and skills

| Component | Role in the system | Boundary |
|---|---|---|
| Codex | local operator, editor, integrator, final reviewer | may edit only scoped files; preserves inherited work |
| LangGraph | state machine and checkpoint owner | model-disabled monitor is observation-only |
| CrewAI | named role vocabulary and bounded team patterns | direct autonomous runtime is not enabled |
| LlamaIndex/RAG | nodes, chunking, retrieval cascade, provenance | targeted corpora; no whole-device ingestion |
| TurboVec | optional dense retrieval/compression experiment | isolated venv, pinned 0.8.0, no default promotion |
| WikiLLM | cross-run durable project memory | reviewed summaries, not raw secret storage |
| Obsidian | human semantic layer and decision walls | selective vault routing |
| Graphify | generated code/document relationship graph | reference only, never final synthesis |
| Nexus | live vault/search/workspace bridge | tools/schema/socket proof required first |
| LangSmith | tracing/configuration option | not production-execution proof |
| Ollama | local model option | only when localhost runtime is healthy |
| Mistral/OpenRouter | optional provider paths | explicit key, spend, and approval gate |
| Cognee | future graph-memory candidate | deferred |
| Role/skill packs | discover, plan, make, check, review, publish, recover | bounded handoffs and stop conditions |
| Dashboard/Jarvis | public documentation, local workflow editor, status surface | no durable backend or provider claim |
| GitHub/Vercel/Figma | public source, static delivery, design baseline | deploy and sync are explicit user actions |

## Website review

The website communicates a three-block wedge: knowledge continuity, agentic workflow setup, and measurable operational proof. Its seven-layer tower (govern, connect, orchestrate, execute, verify, remember, measure) makes the architecture legible without exposing private runtime data. The service surface uses two lanes: a bounded proof/setup lane and a gated implementation lane. The ROI and knowledge-base readiness calculators are directional tools, not financial guarantees.

The public surface can be marketed as an architecture-led GitHub product: start from a safe corpus, define roles and gates, inspect the graph, run a bounded workflow, and promote only reviewed knowledge. Claims must remain tied to the evidence labels above.

## Dashboard and public repository review

The dashboard is documentation-first and browser-local. Its architecture, knowledge, roles, runs, and reference views explain the system and let a user compose a workflow without implying a durable backend. The Jarvis/API surface currently reports provider-disabled and writeback-disabled states. This is a correct safety boundary, not a missing marketing feature.

The public repository is independently operable and English-only. `scripts/public_safety_scan.py` is the authoritative secret/path scan. Public folders contain source-safe reports, contracts, generated reference, static dashboard data, and demo fixtures. The private sibling is not a public ingestion target. A remaining documentation reconciliation item is to update older TurboVec wording from “future/deferred” to “trial evidence exists; default remains blocked” after the active shared-file integration lane releases its claim.

## Private sibling and promotion flow

The private layer contains the secured operating contract, role registry, corpus manifests, promotion schema, LangGraph runtime, isolated retrieval trial, journals, checkpoints, and rollback snapshot. The pre-change instruction snapshot is retained in history for restoration. The promotion contract requires source classification, sanitization, provenance, reviewer approval, and a public-safe artifact before anything crosses the boundary.

## Current proof and gaps

| Area | Evidence | Verdict |
|---|---|---|
| LangGraph controller | 14/14 tests; restart, corruption degradation, retention, strict gates | PROVEN local |
| LlamaIndex/TurboVec trial | 9/9 tests; TurboVec 1.00 recall@3 and 0.8167 MRR on 10-query synthetic fixture | REVIEW; optional only |
| Public safety | public safety scan passed; dashboard JSON parses; site JS syntax passes | PROVEN static |
| Dashboard static smoke | sandbox returned `Operation not permitted` | GAP; rerun in permitted browser context |
| Launchd supervisor | plist/import/static checks pass; job loads but heartbeat remains stopped and launchd reports respawn scheduling | BLOCKED host activation |
| Providers/writeback/deploy | disabled or approval-gated | NOT CLAIMED |
| Nexus live tools | schema/socket proof not established in this run | NOT CLAIMED |
| Customer/paid ROI | no external buyer or production cohort evidence | NOT CLAIMED |

Residual issues are intentionally explicit: host-level launchd activation and log-retention proof, standalone monitor reconciliation, a larger approved retrieval corpus with fixed embeddings and scale tests, live Nexus verification, provider/auth/spend controls, production deployment proof, and primary-customer/paid-start validation.

## Public GitHub product and marketing plan

1. **Public foundation:** README, architecture diagram, role/skill cards, safe demo corpus, quickstart, safety policy, and evidence labels.
2. **Installable local path:** one command to inspect, run, stop, uninstall, and restore the observation-only runtime; no hidden credentials or autonomous writeback.
3. **Proof-led demo:** show a bounded goal, CAG capsule, task graph, retrieval provenance, checker result, and promoted summary.
4. **ICP packaging:** operations/knowledge teams that repeatedly lose context across tools, with an implementation lane for corpus mapping, role design, and verification gates.
5. **Paid wedge:** sell setup and evidence-backed workflow enablement first; treat ROI calculators as discovery aids until customer data validates them.
6. **Roadmap gates:** E1 public explainability, E2 install/readiness, E3 bounded runtime, E4 retrieval graduation, E5 live vault bridge, E6 provider/writeback approvals, E7 hosted controls, E8 productized package and paid proof.

Marketing language should say “safe-by-default blueprint and local proof path” today. It should not say “autonomous enterprise brain,” “continuous production monitoring,” or “guaranteed ROI” until those gates are independently evidenced.

## Immediate next actions

- Keep the monitor model-disabled and observation-only; resolve the host launchd GAP with a permitted user-session test and capture configured/running/stopped/removed evidence.
- Reconcile the shared public TurboVec wording after the active integration lane releases its claim.
- Rerun dashboard browser smoke outside the restricted sandbox.
- Expand retrieval evaluation to an approved 20-query corpus with fixed production embedding dimensions before any default decision.
- Verify Nexus tool schemas and live socket per vault before claiming live memory operations.
- Validate GitHub repository ownership, branch protection, and public release checklist before marketing or deploy.

## Not claimed

No private source text, credentials, tokens, account identifiers, local secret values, production provider calls, autonomous writeback, live Nexus actions, production deployment, Figma synchronization, customer revenue, or guaranteed ROI is claimed by this report.

## Public references

- `README.md`
- `project/README.md`
- `project/agentic-stack.md`
- `project/reports/2026-07-13-self-supporting-agentic-architecture-review.md`
- `project/reports/2026-07-13-icp-audience-product-surface.md`
- `project/dashboard/`
- `scripts/public_safety_scan.py`
- `project/live/communication/`

