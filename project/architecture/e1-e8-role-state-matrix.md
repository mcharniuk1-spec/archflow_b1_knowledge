# E1–E8 Canonical Admission, Role, And State Matrix

Status: active, provider-disabled planning policy. `run-profiles.yaml` is the deterministic policy; this file is its public human-readable projection.

## One State Plane

Knowledge Case workflow states come only from `project/system/contracts/operating-model.json`. Admission mechanics use the separate `admission.*` namespace and project into a canonical workflow state; they are never alternate workflow states.

| Admission sequence state | Workflow projection | Meaning |
| --- | --- | --- |
| `admission.validated` | `admission_checked` | Request, provider-disabled mode, profile, and public boundary passed deterministic checks. |
| `admission.cag_bound` | `context_bound` | All six stable CAG references are present. |
| `admission.role_plan_composed` | `context_bound` | Canonical role IDs and Ukrainian call names were selected from the role catalog. |
| `admission.retrieval_plan_bound` | `context_bound` | Retrieval roots and source-path requirements were bounded; retrieval did not run. |
| `admission.approval_interrupt` | `approval_wait` | An exact owner decision is required before a side effect. |
| `admission.accepted_planning_only` | `context_bound` | The request may proceed to its declared profile entry state without provider, queue, or checkpoint mutation. |

The admission receipt records `admission_sequence`, `current_workflow_state`, and `planned_workflow_path` separately. A compatibility `sequence` field, when present, contains only namespaced admission states.

## Universal Admission Contract

| Requirement | Deterministic rule |
| --- | --- |
| Provider mode | `disabled`; any other value fails before planning. |
| CAG | Six exact references from `run-profiles.yaml` must exist, including the current operating model, role catalog, and this matrix. |
| Controller | Bohdan / `admission_controller`; owns profile and stop-rule composition, never project edits. |
| Roles | Stable machine IDs come from `role-catalog.json`; call names and titles are projections, not identities or permission. |
| Role task | Every active role materializes a schema-valid binding with inputs, one owned output, skill/tool ceilings, exact targets, checks, reviewer route, handoff, and stop conditions. |
| Retrieval | Repo-relative paths under `project/`, `history/`, `skills/`, or `wiki/`; LlamaIndex paths and exact reads are required where retrieval is used. |
| CrewAI | Declarative role/task projection only; provider execution, memory, planning, and autonomous delegation remain disabled. |
| LangGraph | Owns workflow state, reducers, interrupts, retries, and idempotency. It does not own evidence truth, permission, or approval. |
| Reviewer separation | Halyna / `independent_reviewer` reviews a frozen candidate and never repairs it. |
| Repairs | Stop after three attempts or when the same error repeats twice. |

## Epic Coverage

| Epic | Canonical entry | Terminal evidence | Retrieval | Stop rule | Approval gate |
| --- | --- | --- | --- | --- | --- |
| E1 | `context_bound` | Reviewed authority, provenance, and public/private boundary receipt | CAG or allowlisted lexical | Competing authority or boundary failure | Independent review |
| E2 | `requirements_review` | Provider-disabled goal-loop fixture or accurate blocked record | CAG | Unbounded loop or absent maker/checker split | Independent review |
| E3 | `work_planning` | Deterministic role, tool, recovery, and handoff evidence | Allowlisted lexical | Unapproved tool or default-autonomy claim | Independent review |
| E4 | `evidence_gathering` | Source-path, metadata-filter, exact-read, and lexical-fallback evidence | Allowlisted lexical | Missing provenance or unbounded corpus | Independent review |
| E5 | `evidence_gathering` | Reviewed evidence packet or explicit no-demand verdict | Allowlisted lexical | Private-channel access or unapproved outreach | Exact owner approval for action |
| E6 | `work_planning` | Reviewed public-safe surface or documentation receipt | CAG or allowlisted lexical | Deployment or production-promotion request | Exact owner approval for deploy/Figma |
| E7 | `evidence_gathering` | Paired fixture or benchmark receipt with independent verdict | Allowlisted lexical | Unsupported runtime/performance claim | Independent review |
| E8 | `proposal_ready` | Installability, safety, and buyer-gate receipt | Allowlisted lexical | Missing E5/E7 evidence or unapproved writeback | Exact owner approval for pilot/action |

## Adaptive Profile Packs

| Profile | Canonical path | Base role pack | Retrieval | Terminal evidence |
| --- | --- | --- | --- | --- |
| `documentation` | `work_planning → candidate_review → answered` | Marta / `surface_projection_operator`; Halyna / `independent_reviewer`; Maksym / `integrator` | CAG | Public-safe documentation and independent verdict |
| `research` | `evidence_gathering → candidate_review → answered` | Oksana / `requirements_and_market_research`; Solomiia / `source_and_context_operator`; Larysa / `knowledge_librarian`; Halyna; Maksym | Allowlisted LlamaIndex lexical baseline | Source register, calibrated claims, and independent evidence review |
| `architecture` | `work_planning → candidate_review → answered` | Yaromyr / `goal_and_architecture_operator`; Bohdan; Halyna; Maksym | CAG | Canonical state, role, retrieval, and gate record |
| `runtime` | `evidence_gathering → result_verification → answered` | Dmytro / `implementation_maker`; Mykola / `verifier`; Halyna; Maksym | CAG | Provider-disabled fixture or accurate blocked state |
| `runtime` monitor | Observation only | Ostap / `observability_and_efficiency_observer`; Halyna | CAG | Runtime observation report; no completion authority |
| `retrieval` | `evidence_gathering → result_verification → answered` | Solomiia; Mykola; Halyna; Maksym | Allowlisted LlamaIndex baseline | Source-path, exact-read, fallback, and candidate-gate receipt |
| `content` | `work_planning → candidate_review → answered` | Olena / `positioning_and_copy_maker`; Kateryna / `designer`; Halyna; Maksym | Allowlisted LlamaIndex baseline | Evidence-linked draft and independent review; no publication |
| `review` | `proposal_ready → candidate_review → answered` | Halyna; Maksym | Allowlisted lexical | Approve, revise, or block with exact gaps |
| `external_action` | `proposal_ready → proposal_validated → approval_wait` | Pavlo / `external_action_operator`; Nazar / `release_operator`; Iryna / `action_validator`; Mykola; Halyna; Maksym | Allowlisted lexical | Target-specific proposal and approval interrupt; no admission-time action |

The controller role is always Bohdan / `admission_controller`. Generic labels such as “architecture engineer” may describe a capability, but never identify a role or workflow state.

## Runtime Boundary

Admission is planning-only. It does not retrieve, call a model, start CrewAI, checkpoint LangGraph, mutate a queue, access a private vault, publish, send, deploy, or push. Those capabilities require their own canonical role binding, evidence, and approval gate.
