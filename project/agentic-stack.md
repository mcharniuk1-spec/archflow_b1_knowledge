# Agentic Stack

## Layer Decision

Use this structure:

```text
Codex-authenticated operator prompt
  -> LangGraph path and state controller
  -> Loop Engineering run contract
  -> LlamaIndex bounded retrieval
  -> CrewAI named team tasks
  -> LangGraph review gate
  -> public-safe project outputs
```

## Tool Responsibilities

| Tool | Responsibility | Public Project Use |
|---|---|---|
| Codex | Operator runtime, editor, verifier, approval boundary. | Default interface for now. |
| LangGraph | Path control, state, conditional routing, review gates. | Full Block 1 workflow controller. |
| Loop Engineering | State, attempt caps, budget, maker/checker split, stop conditions. | L1 report-only loop contract under `project/loops/`. |
| CrewAI | Named roles and task execution. | AF Tools, AF Context, AF Research, AF Manager, AF Knowledge, AF Copy, AF Review, AF Publisher. |
| LlamaIndex | Bounded retrieval and RAG. | Search only approved public-safe project and sanitized history. |
| turbovec | Future local vector store under LlamaIndex. | Deferred until stable source IDs, embeddings, metadata, and benchmark exist. |
| WikiLLM | Canonical curated memory. | Source of truth for approved runs, decisions, memory, insights, and issues. |
| Cognee | Future operational recall and knowledge graph. | Deferred until E1.3 readback passes; never replaces WikiLLM. |
| Ollama | Local model serving. | Minor/background tasks only; active model is Qwythos and fallback is `gemma4:e4b`. |
| Mistral | Optional cloud quality pass. | Disabled until credentials, sanitized inputs, budget, model metadata logging, and AF Review approval exist. |
| LangSmith | Observability and trace review. | Configured for tracing only; waits for manual API key insertion. |

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

## Loop And Parallelism Rules

- Default loop level is L1 report-only.
- `max_revision_loops` remains 2.
- Item-level retry cap is 3.
- A maker cannot approve its own high-risk output.
- Parallel work is allowed only for independent extraction tasks such as E2 website parsing, job-signal capture, review mining, and social-language mining.
- Synthesis, role verification, memory promotion, Notion updates, outreach, and payment verdicts remain sequential and reviewed.

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
| Level 3: CrewAI runtime execution | CrewAI directly executes role/task flows, either directly or through LangGraph, with local proof artifacts and safety checks. | Deferred until direct CrewAI task execution is proven on a public-safe fixture. |

For now, build toward Level 2 while preserving Level 1 as the source of truth. Do not describe Level 3 as active.

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
