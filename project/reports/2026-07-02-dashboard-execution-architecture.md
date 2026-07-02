# Dashboard Execution Architecture

Date: 2026-07-02
Status: Prompt 1.2 complete; Level 3 proof integrated, not default runtime
Lead integrator: Jesus/Codex

## Executive Decision

Prompt 1.2 defines the operational execution layer for the Jarvis dashboard without building the UI, deploying Railway, activating providers, or claiming autonomous CrewAI runtime.

The dashboard should become the control surface for ArchFlow's Product Discovery-to-Production PRD Pack. It should make LangGraph, OpenRouter, and CrewAI understandable from the dashboard model through two screens:

- `(1) PRD/ICP Flow`: client/product flow for turning approved product-team material into a reviewed PRD/ICP artifact bundle.
- `(2) Agent Orchestra`: operator flow for assigning roles, supervising bounded agent work, collecting artifacts, running review gates, and producing handoffs.

Implementation should build toward Level 2: LangGraph-wrapped role execution with server-side model routing only after explicit approval and proof. Level 3 direct CrewAI runtime now has a deterministic local proof package, but it remains `proof_passed_not_default_runtime`.

## Evidence Reviewed

- `project/reports/2026-07-02-jarvis-dashboard-icp-task-consolidation.md`
- `project/runs/2026-07-02-jarvis-dashboard-icp-task-consolidation/agent-handout.md`
- `project/dashboard/README.md`
- `project/runs/2026-07-01-dashboard-two-layer-schema/agent-handout.md`
- `project/agentic-stack.md`
- `project/agents/agent-roster.yaml`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/config/model-routing.yaml`
- `project/runs/2026-07-02-crewai-level-3-proof/runtime-proof.json`
- `project/runs/2026-07-02-crewai-level-3-proof/model-call-ledger.jsonl`
- `project/runs/2026-07-02-crewai-level-3-proof/budget-guard.json`
- `project/runs/yushchenko-model-efficiency/2026-07-02-1112-model-efficiency-report.md`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`

Six bounded read-only reviewer lanes contributed findings for Screen 1, Screen 2, LangGraph route design, CrewAI role/task mapping, OpenRouter/backend boundary, and Prompt 2 readiness.

## Execution Levels

| Level | Meaning | Current status |
|---|---|---|
| Level 1: Configured roles | Roles, tasks, dashboard fields, review gates, and expected outputs exist as YAML/config/docs. No LLM execution is claimed. | Active. |
| Level 2: LangGraph-wrapped role execution | LangGraph owns route selection, state, gates, artifact capture, and role-worker calls. Workers may use OpenRouter only through an approved server-side route with ledger and budget gates. | Target architecture. |
| Level 3: CrewAI runtime execution | CrewAI directly runs role/task flows, directly or through LangGraph. | Proof passed for deterministic local fixture; not default/provider runtime. |

The dashboard may display and edit safe config candidates for Level 1 and Level 2, but source files remain the source of truth until a backend endpoint is approved.

## Screen (1): PRD/ICP Flow

Purpose: client/product flow for the PRD Pack.

Roles:

- AF Context: source boundary, context digest, FACT/INTERPRETATION/HYPOTHESIS/GAP.
- AF Research: ICP, competitor, customer pain, and evidence-card summaries from approved sources only.
- AF Manager: PRD structure, milestones, task matrix, acceptance criteria.
- AF Copy: readable PRD/service language from structured product logic.
- AF Review: public-safety, claim support, completeness, and runtime-boundary review.
- Jesus/Codex: local operator and final approval boundary.

LangGraph route:

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

Stop logic:

- Block if raw private material, credentials, unsanitized upload bodies, or external-write requests enter the packet.
- Revise if gaps or unsupported claims remain.
- Approve only when public boundary, source labels, claim support, and writeback-disabled status are explicit.

## Screen (2): Agent Orchestra

Purpose: operator/execution flow for specialist roles and multi-agent work.

Roles:

| Role | Responsibility |
|---|---|
| Jesus | Lead integrator, final architecture decision, Prompt 2 readiness, handout. |
| LOL | Dashboard workflow and block-schema control surface. |
| Ronaldinho | Technical review of LangGraph, OpenRouter, CrewAI, backend, and Railway boundaries. |
| Messi | PM/task status, review gates, handoff, and task-board update package. |
| Ronaldo | Product/ICP fit for the B2B SaaS PRD/ICP service offer. |
| Yushchenko | Model routing, budget, token/cost logging, and efficiency gaps. |
| Actor | Bounded subagent for one scoped slice. |
| AF Tools | Runtime/source/tool readiness. |
| AF Knowledge | WikiLLM/public memory packets. |
| AF Publisher | Git/deploy/release packet preparation after approval. |
| AF Review | Final public-safety and claim review. |

LangGraph route:

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

Status model:

- `draft`
- `ready`
- `running`
- `blocked`
- `review`
- `revise`
- `approved`
- `done`
- `gated`

Blocker model:

- `missing_input`
- `unsafe_source`
- `unsupported_claim`
- `runtime_not_approved`
- `proof_missing`
- `owner_approval_required`
- `file_claim_conflict`

## Configuration Model

The future dashboard can expose these fields as reviewable config candidates:

- active lane
- selected role
- role objective
- allowed tools
- source boundaries
- model route
- review gate
- output artifact type
- handoff target
- status
- safety mode

Allowed safety modes:

- `local-only`
- `server-side-model`
- `external-write-gated`

Browser-local edits must export a packet for Codex/operator review. The browser must not write source YAML or Markdown directly.

## LangGraph Role

LangGraph is the controller:

- owns route selection;
- owns execution state;
- owns review gates and stop conditions;
- calls role workers only through controlled nodes;
- selects mock/Codex/manual packet mode today;
- can call OpenRouter server-side only after backend/local-bridge, secret, ledger, budget, and approval gates pass;
- stops before external side effects.

## CrewAI Role

CrewAI is the role/task layer:

- Level 1 is active as configured roles and tasks.
- Level 2 uses CrewAI role/task mapping as configuration for LangGraph-wrapped workers.
- Level 3 direct CrewAI runtime has proof status `proof_passed_not_default_runtime`.

Level 3 was blocked because direct CrewAI task execution had not produced a reviewed public-safe artifact. That proof gap is now closed for a tiny deterministic local fixture only. CrewAI is not the default runtime, and provider-backed CrewAI is still gated.

Proof package:

- fixture: `project/runs/2026-07-02-crewai-level-3-proof/input-fixture.md`;
- direct output: `project/runs/2026-07-02-crewai-level-3-proof/crew-output.md`;
- model-call ledger: `project/runs/2026-07-02-crewai-level-3-proof/model-call-ledger.jsonl`;
- budget guard: `project/runs/2026-07-02-crewai-level-3-proof/budget-guard.json`;
- AF Review: `project/runs/2026-07-02-crewai-level-3-proof/review-report.md`;
- runtime proof: `project/runs/2026-07-02-crewai-level-3-proof/runtime-proof.json`;
- dashboard state: `project/runs/2026-07-02-crewai-level-3-proof/dashboard-state.md`.

Proof result:

- Direct CrewAI fixture run: pass.
- Provider calls: zero.
- External writeback: zero.
- Actual spend: 0.00 USD.
- OpenRouter daily cap represented: 5.00 USD.
- Per-run cap represented: 1.99 USD, which keeps runs under 2.00 USD.
- Promoted status: `proof_passed_not_default_runtime`.

Remaining gates before default/provider runtime:

1. Explicit owner approval for provider-backed or default CrewAI runtime.
2. Backend/local bridge with server-side secrets outside the public repo.
3. Fresh provider model list and pricing check.
4. Provider-backed ledger write proof with actual provider cost fields.
5. Live budget guard against real provider pricing.
6. Expanded AF Review for non-fixture outputs.

## OpenRouter Role

OpenRouter is the future server-side model provider:

- no browser keys;
- no static-dashboard provider calls;
- sanitized packets only;
- selected through model-routing config;
- logged with provider, model, role, source IDs, prompt version, token/cost fields, budget fields, status, and reviewer gate;
- disabled if API key, backend, ledger, budget, or approval is missing.

Current budget policy:

- Daily OpenRouter cap: 5.00 USD.
- Per-run OpenRouter cap: always under 2.00 USD; config uses 1.99 USD as the hard stop threshold.
- If a run would exceed either cap, stop and request owner approval before continuing.

The model-call ledger is an activation blocker. Token and cost numbers must be reported as missing until a ledger records them.

Minimum ledger fields:

- `timestamp_utc`
- `run_id`
- `epic_or_task`
- `provider`
- `model_id`
- `model_role`
- `prompt_version`
- `source_ids_used`
- `input_artifact`
- `output_artifact`
- `context_window_tokens`
- `prompt_tokens`
- `output_tokens`
- `actual_or_estimated_cost`
- `cost_currency`
- `pricing_source`
- `budget_cap`
- `budget_remaining`
- `decision`
- `reviewer_model_id`
- `human_gate_required`
- `runtime_source`
- `status`
- `error_type`

## Prompt 2 Readiness

Prompt 2 is ready only after this report, the run handout, and the live-log completion entry exist.

Allowed Prompt 2 scope:

- static/browser-local dashboard MVP;
- render Level 1 and Level 2 contracts;
- show Screen 1 and Screen 2 state/control blocks;
- show runtime labels: static snapshot, browser-local, provider disabled, backend absent, writeback gated;
- export local review packets;
- regenerate dashboard data;
- run static validation and smoke checks.

Blocked in Prompt 2 unless separately approved:

- OpenRouter/provider activation;
- Railway/backend or local bridge implementation;
- default or provider-backed CrewAI runtime execution;
- live Nexus/Notion/GitHub/WikiLLM writeback;
- Telegram delivery;
- owner-device voice proof or raw voice persistence;
- production promotion or Figma sync;
- validated demand, ROI, or customer-outcome claims.

## Config Changes Made

- `project/agentic-stack.md`: added the Prompt 1.2 dashboard execution contract.
- `project/agents/agent-roster.yaml`: added operator-only dashboard execution role mapping, status model, blocker model, and runtime labels.
- `project/workflows/langgraph-controller.yaml`: added `screen_contracts` for PRD/ICP Flow and Agent Orchestra plus Level 3 proof state and disabled boundaries.
- `project/workflows/crewai-crew.yaml`: added execution levels, dashboard/operator reviewer roles, Level 1/Level 2 task policy, and Level 3 proof status.
- `project/config/model-routing.yaml`: added disabled-state behavior, ledger schema, server-side activation gates, and Level 3 proof metadata.
- `project/dashboard/app.js`: represented the Level 3 proof branch on Screen 1 and Screen 2.
- `project/scripts/generate-dashboard-data.py`: added Level 3 proof status, ledger, and cost fields.

## FACT

- Prompt 1 consolidation is complete and permits only static/browser-local Prompt 2 implementation.
- Static/browser-local dashboard proof exists from prior runs.
- No active OpenRouter runtime evidence was found in current local public-safe evidence.
- No canonical provider-backed model-call ledger exists.
- CrewAI config/import proof exists.
- Direct CrewAI deterministic local fixture proof passed and wrote a proof ledger.

## INTERPRETATION

- The right next build is a static/dashboard rendering of the execution contract, not backend/provider activation.
- LangGraph should remain the controller, with CrewAI as role/task configuration plus a proof-passed Level 3 readiness branch.
- OpenRouter should be treated as a disabled server-side route until logging and approval gates are real.

## HYPOTHESIS

- A dashboard that makes the two screens, role packets, review gates, and runtime labels clear will reduce implementation drift in Prompt 2 and make provider/runtime activation easier to approve later.

## GAP

- No backend/local bridge.
- No provider runtime.
- No provider-backed model-call ledger.
- No default or provider-backed CrewAI execution proof.
- No live writeback.
- No production promotion approval.
- No owner-device voice proof.

## Final Readiness Decision

Prompt 2 may proceed after the completion entry for this run. It must implement only the static/browser-local dashboard MVP against this contract and must preserve all runtime gates.
