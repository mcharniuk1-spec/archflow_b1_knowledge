# Agentic Stack

## Layer Decision

Use this structure:

```text
Authority and safety envelope
  -> Codex-authenticated operator prompt
  -> Hermes watchdog/controller prompt (planned, non-executing)
  -> Goal Engineering objective, verifier, budget, and kill switches
  -> CAG core plus bounded LlamaIndex retrieval
  -> LangGraph task graph, checkpoints, and human gates
  -> Terra integration or Luna bounded worker task
  -> Loop Engineering maker/checker repair contract
  -> deterministic verification and AF Review safety gate
  -> WikiLLM promotion decision and Graphify rebuild policy
  -> approved public output or action-specific external gate
```

The safety envelope applies across every layer. Platform approvals remain authoritative; a future destructive-command hook can add defense in depth but cannot expand authority or replace review.

## Tool Responsibilities

| Tool | Responsibility | Public Project Use |
|---|---|---|
| Codex | Current local operator binding for execution, editing, verification, and final integration. | Default interface for now; role contracts, not runtime identity, determine authority. |
| Hermes | Current label for the planned watchdog/controller/reviewer role. Classifies work, assembles context capsules, writes task contracts, reviews evidence, and stops unsafe or complete work. | Planned controller overlay only. Any compatible watchdog remains non-executing: no edits, deployment, task-board mutation, provider call, or external write. |
| Goal Engineering | Persistent bounded objective, observable completion, independent verifier, lifecycle, budget, and kill switches. | Active design contract under `project/goals/`; G1 is the new default and G2 remains a fixture target. |
| CAG context capsules | Controlled Context Assembly Generation before subagent prompting. | Stable context packet under `project/context/`; not durable memory and not broad ingestion. |
| LangGraph | Path control, state, conditional routing, review gates. | Full Block 1 workflow controller. |
| Loop Engineering | State, attempt caps, budget, maker/checker split, stop conditions. | L1 report-only loop contract under `project/loops/`. |
| CrewAI | Named roles and task execution. | AF Tools, AF Context, AF Research, AF Manager, AF Knowledge, AF Copy, AF Review, AF Publisher. |
| LlamaIndex | Bounded hybrid retrieval and RAG. | Search only approved public-safe project and sanitized history with source-grounded semantic plus lexical retrieval, stable chunk metadata, and lexical fallback. |
| turbovec | Future local vector store under LlamaIndex. | Deferred until stable source IDs, chunk IDs, embeddings, metadata, source filters, and the 20-query benchmark pass. |
| WikiLLM | Canonical curated memory. | Source of truth for approved runs, decisions, memory, insights, and issues. |
| Cognee | Future operational recall and knowledge graph. | Deferred until E1.3 readback passes; never replaces WikiLLM. |
| Ollama | Local model serving. | Minor/background tasks only; active model is Qwythos and fallback is `gemma4:e4b`. |
| Mistral | Optional cloud quality pass. | Disabled until credentials, sanitized inputs, budget, model metadata logging, and AF Review approval exist. |
| LangSmith | Observability and trace review. | Configured for tracing only; waits for manual API key insertion. |
| Destructive command defense | Pre-execution command analysis plus platform approval and sandbox controls. | Platform approval/sandbox is active. Third-party `destructive_command_guard` is trial-only pending a completed scan, pinned release, hook-diff review, fixture tests, and rollback. |
| Obsidian methods | Index-first navigation, source preservation, provenance, reconciliation, and write propagation. | Selectively adopted through current vault rules. Unattended permission bypass and uncontrolled background vault writes are rejected. |
| Google and NVIDIA ecosystems | Reference build/evaluate/deploy/govern/observe patterns and task-specific verified skills. | Selective source and skill governance inputs only; no wholesale install or second orchestrator is active. |

## Role-Based Runtime Interpretation

Architecture roles are permission contracts, not exclusive product or model assignments. A compatible runtime may fulfil a role only when it satisfies the role's source boundary, evidence requirement, and forbidden-action list. Naming a runtime in a diagram or configuration therefore does not authorize it to execute the role.

| Architecture stage | Required role | Compatible runtime status | Evidence required before stage completion |
|---|---|---|---|
| Classify, assemble CAG, issue task contract, decide stop/repair | Watchdog | Planned Hermes contract or another non-executing controller that follows the same prohibition set. | Context capsule, bounded contract, and decision record. |
| Produce a bounded artifact | Executor | Codex is the active local executor; a later approved worker may be substituted only through a task contract. | Claimed file scope, artifact, and run trace. |
| Check correctness and completeness | Verifier | A compatible reviewer separate from the maker; Codex or an approved deterministic check may fulfil it. | Reproducible check output and unresolved-gap list. |
| Check source boundary, public safety, and claim support | Safety reviewer | AF Review contract or another independently assigned compatible reviewer. | Safety scan plus claim and source review. |
| Reconcile evidence and choose the next internal action | Integrator | Codex is the current final integration boundary. | Reviewed branch evidence, merge decision, and handout. |
| Call a provider, deploy, publish, or write externally | External-action role | No default runtime is authorized. A compatible runtime is eligible only after its action-specific approval gates pass. | Owner approval, target/schema proof, secret isolation, budget/rollback evidence, and post-action verification. |

This interpretation replaces any hard division that equates a role name with a permanently assigned runtime. It does not weaken the Hermes prohibition set: the planned watchdog remains non-executing, and the active local operator remains responsible for edits, validation, and final integration.

## Agent Hooks

| Hook | Use |
|---|---|
| AF Graph | Full controlled workflow. |
| AF RAG | Source-grounded retrieval over approved corpus. |
| AF Crew | Team-mode work split by role. |
| AF Research | E2 market evidence extraction, scoring, and ICP synthesis. |
| AF Copy | E3/E4/E6 positioning, content, and outreach drafts from approved evidence. |
| AF Review | Final public-safety and evidence gate. |

## Public Corpus Rules

Allowed by default:

- `project/`
- `history/`
- `skills/`
- `wiki/`

Not allowed by default:

- Raw private exports.
- Legacy root files.
- Private Notion pages.
- Local machine paths.
- Credentials.
- Private or scraped profile data.

## Hermes Watchdog And CAG/RAG Contract

Status: planned controller architecture, not runtime execution.

Hermes is the current label for the watchdog permission set, not proof of a hosted or always-online controller. If a compatible controller fulfils the watchdog role later, it must retain every prohibition below and must not self-approve high-risk work.

Hermes is allowed to:

- classify the execution type and risk;
- assemble CAG core from stable project rules, role registry, skill governance, current architecture, E1-E8 task state, and gated claims;
- request bounded RAG evidence from the approved corpus;
- build or review context capsules;
- generate task contracts for Codex or subagents;
- decide accept, repair, split, escalate, or stop.

Hermes is not allowed to:

- edit files;
- run commands;
- deploy;
- mutate Notion, Linear, GitHub, WikiLLM, Obsidian, Nexus, Telegram, Railway, Figma, or production systems;
- activate provider calls;
- approve its own high-risk output.

CAG is the stable context assembly layer. RAG is task-specific retrieval with required repo-relative source paths. WikiLLM remains durable reviewed memory only after promotion.

Current context files:

- `project/context/README.md`
- `project/context/cag-core.yaml`
- `project/context/context-capsule.schema.json`
- `project/context/retrieval/source-boundary-policy.yaml`
- `project/context/capsules/`

## LlamaIndex Retrieval Contract

LlamaIndex is the retrieval layer, not the durable knowledge store. WikiLLM remains the curated memory source of truth.

Current role:

- bounded approved-corpus retrieval over `project/`, `history/`, `skills/`, and `wiki/`;
- hybrid query mode when a local embedding adapter is available;
- deterministic lexical retrieval as the smoke path and fallback;
- stable `doc_id` and `chunk_id` metadata for every result;
- required `source_path`, `document_type`, and `updated_at` provenance fields;
- refusal of private-source matches by default.

Retrieval guarantees:

- no raw private ingestion by default;
- source-grounded output only;
- auditable result sources and scores;
- full vector defaulting remains blocked until the 20-query benchmark passes with no regression against lexical retrieval.

Retrieval feeds context capsules only after source-boundary checks. A retrieved snippet without a repo-relative source path is not acceptable evidence.

## Service Company Operating Model

Status: active strategy, proof-backed method, not validated demand.

ArchFlow is positioned first as a productized service:

1. Forcing-Moment Knowledge Diagnostic.
2. Product Knowledge Reliability Sprint.
3. Knowledge Continuity Operating Retainer only after paid-start and reliability evidence.

The service core is a verified forcing moment to source/owner/freshness map, reviewed knowledge spine, task-specific generated output pack, and governed handoff. PRD, ICP, backlog, and content remain possible downstream outputs. SaaS readiness, autonomous runtime, provider-backed execution, writeback, customer demand, paid clients, and ROI claims remain gated until current evidence exists.

## Loop And Parallelism Rules

- Default loop level is L1 report-only.
- Default goal level is G1; a loop may repair a task but may not redefine the goal or broaden its authority.
- `max_revision_loops` remains 2.
- Item-level retry cap is 3.
- Default parallel branch cap is 3 unless the goal contract explicitly lowers or raises it with evidence.
- A maker cannot approve its own high-risk output.
- Terra is the sole-writer/integrator role for high-impact synthesis. Luna roles are bounded read-only workers by default. These labels do not imply a particular model.
- Parallel work is allowed only for independent extraction, drafting, or critique tasks such as E2 website parsing, job-signal capture, review mining, and social-language mining.
- Synthesis, role verification, memory promotion, Notion updates, outreach, and payment verdicts remain sequential and reviewed.

## Architecture Factory Contract

Status: active design baseline; deterministic/provider-disabled pilot still required.

The architecture can generate bounded role architectures for knowledge systems, PRD/ICP, engineering, agent engineering, research, content/growth, sales/outreach, finance/operations, web/interactive media, and long-form publishing. The factory must emit a goal contract, dependency graph, role/skill pack, retrieval profile, state machine, loop budget, verification plan, safety boundary, memory-promotion policy, and benchmark. The reusable procedure lives in `skills/archflow-architecture-operator/`.

An architecture template is not production-ready because it exists. It graduates only after the same provider-disabled fixture and then, when authorized, provider-backed evaluation pass the declared quality, reliability, retrieval, context, cost, safety, and recovery thresholds.

## Model Routing

Current default:

- Codex is the operator/reviewer.
- Ollama/Qwythos is the bounded local minor/background model path.
- `gemma4:e4b` is fallback.
- Cloud model execution is disabled by default.

Future gated route:

- Mistral Small for sanitized batch normalization and draft variants.
- Mistral Medium for final strategy, PRD, ICP, proposal, or copy quality passes after facts are fixed.
- Mistral OCR only after a live model-name and privacy preflight.

## Dashboard Execution Contract - Prompt 1.2

Status: architecture contract only. No backend, provider runtime, direct CrewAI runtime, external writeback, deployment, or production promotion is activated by this section.

The dashboard control surface has two screens:

| Screen | Job | Current execution level |
|---|---|---|
| `(1) PRD/ICP Flow` | Client/product path for turning approved product-team material into a reviewed PRD/ICP artifact bundle. | Static/browser-local dashboard plus Codex-operated execution packets. |
| `(2) Agent Orchestra` | Operator path for assigning roles, supervising specialist work, collecting artifacts, review gates, blockers, and handoffs. | Static/browser-local dashboard plus Codex-operated role coordination. |

### Runtime Levels

| Level | Meaning | Current status |
|---|---|---|
| Level 1: Configured roles | YAML/config and documentation define roles, responsibilities, tasks, outputs, dashboard fields, and review gates. No LLM execution is claimed. | Active. |
| Level 2: LangGraph-wrapped role execution | LangGraph selects the lane, owns execution state, calls bounded role worker functions, records artifacts, and stops for AF Review/Jesus approval before any external side effect. Workers may use server-side OpenRouter only after explicit approval, backend/local-bridge proof, ledger proof, and budget gates. | Target architecture for the next implementation contract. |
| Level 3: CrewAI runtime execution | CrewAI directly executes role/task flows, either directly or through LangGraph, with local proof artifacts and safety checks. | Direct deterministic public-safe fixture proof passed; not default runtime and not provider-backed runtime. |

For now, build toward Level 2 while preserving Level 1 as the source of truth. Describe Level 3 only as proof passed, not as default active runtime.

### Reliability And Always-Online Status

| Surface | What the repository supports | What this does not prove |
|---|---|---|
| Static dashboard and browser-local packets | Public-safe UI and local packet workflow. | A continuously available service, provider execution, durable state, or external writeback. |
| Provider-disabled Jarvis API contract | Local and serverless review-packet routes with a health contract. | Current hosted freshness, authenticated production traffic, or a Railway deployment in this run. |
| Railway migration material | Service configuration and a readiness path for a future long-running API/worker lane. | An active Railway service, continuous monitoring, provider activation, or production readiness. |
| OpenRouter routing policy | Server-side-only activation requirements, budget/ledger gates, and observer review responsibilities. | A selected current model, available credits, a live key, or any provider call. |

Railway healthchecks are deployment-time readiness checks, not continuous monitoring. Any future always-online claim needs current, separately recorded service, health, observability, auth, persistence, and recovery evidence.

### Screen (1): PRD/ICP Flow

Roles:

- AF Context validates approved source boundaries and writes the context digest.
- AF Research prepares ICP, competitor, customer pain, and evidence-card outputs only from approved summaries.
- AF Manager creates the PRD structure, milestones, task matrix, and acceptance criteria.
- AF Copy converts structured product logic into readable PRD/service language.
- AF Review checks claims, gaps, public safety, completeness, and runtime-boundary wording.
- Codex/Jesus remains the final local operator and approval boundary.

Route:

1. `receive_direct_request`
2. `classify_request`
3. `load_project_context`
4. `select_model_or_mock`
5. `run_context_stage`
6. `run_research_stage`
7. `run_prd_stage`
8. `run_copy_stage`
9. `run_review_stage`
10. `return_response_to_dashboard`
11. `save_artifact_for_review`

Dashboard blocks:

- Input
- Context
- Research
- PRD Draft
- Acceptance Criteria
- Review
- Output Packet
- Questions
- Runtime Gates

### Screen (2): Agent Orchestra

Roles:

- Jesus: lead integrator and final architecture/execution owner.
- LOL: dashboard workflow and two-screen control-surface owner.
- Ronaldinho: technical boundary and implementation-risk reviewer.
- Messi: PM/task-state, Notion update package, review-gate, and handoff reviewer.
- Ronaldo: product/ICP reviewer for the PRD/ICP service offer.
- Yushchenko: model-efficiency observer for OpenRouter routing, budget, tokens, and logging gaps.
- Actor: bounded implementation or review worker for one clearly scoped slice.
- AF Tools, AF Knowledge, AF Publisher, and AF Review provide stable functional roles for runtime/source readiness, memory packets, release preparation, and final public-safety checks.

Route:

1. `receive_operator_task`
2. `classify_lane_and_scope`
3. `assign_roles`
4. `create_task_packet`
5. `run_role_workers`
6. `collect_artifacts`
7. `run_review_gate`
8. `merge_findings`
9. `produce_handoff`
10. `wait_for_integrator_decision`
11. `optionally_prepare_git_notion_deploy_actions`

Dashboard blocks:

- Task Intake
- Role Assignment
- Active Agents
- Work Artifacts
- QA Gate
- Docs/Reports
- Git/Deploy Sequence
- Notion/Memory Closeout
- Blockers
- Final Decision

### Configuration Surface

The dashboard may expose these editable fields as safe config candidates, but browser code must not write source files directly:

- active lane
- selected role
- role objective
- allowed tools
- source boundaries
- model route
- review gate
- output artifact type
- handoff target
- status: `draft`, `running`, `blocked`, `review`, `done`
- safety mode: `local-only`, `server-side-model`, `external-write-gated`

The source of truth remains repo YAML and Markdown until a backend endpoint is approved. Static dashboard edits should be exported as review packets for Codex/operator application.

### Stop Rules

AF Review/Jesus approval is required before any of these actions:

- Notion status Done
- Git push or production promotion
- Telegram delivery
- WikiLLM/Obsidian/Nexus durable writeback
- public claim promotion
- provider-backed Jarvis call
- Railway/backend deployment
- direct CrewAI runtime execution
- memory promotion from unreviewed output

Prompt 2 readiness is limited to static/browser-local dashboard MVP implementation that renders these contracts and gates honestly.

## Proof Run Baseline

The first completed proof runs used sanitized internal source summaries, not raw transcripts.

Current public-safe proof folders:

- `project/runs/2026-06-26-june24-next-steps-proof/`
- `project/runs/E1.2/2026-06-26-full-test/`

Baseline proof outputs:

- context digest
- PRD
- task and responsibility matrix
- KB update note
- review report
- agent handout

## Current Workflow Configs

- `workflows/langgraph-controller.yaml`
- `workflows/crewai-crew.yaml`
- `workflows/llamaindex-rag.yaml`
- `workflows/market-research-engine.yaml`
- `loops/LOOP.md`
- `langsmith-setup.md`
- `../wiki/index.md`

## Output Documents

Templates are present under `outputs/templates/`.
Completed proof runs now live under `project/runs/` and provide the current public-safe reference for future E1.3 work.
