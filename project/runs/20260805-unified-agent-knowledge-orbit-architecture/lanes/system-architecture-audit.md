# System Architecture Audit — One Governed Knowledge-Agent Workflow

Run: `20260805-unified-agent-knowledge-orbit-architecture`

Lane: system architecture engineer

Status: maker audit complete; independent review and integration pending

Execution boundary: provider-disabled planning; no dashboard, runtime, external-system, deployment, vault, or Git mutation

## Executive finding

**FACT:** The public repository already says that ArchFlow is not primarily a PRD generator. Its current strategic baseline is a maintained, source-grounded knowledge-continuity system in which PRDs, ICPs, research, content, outreach, and task packs are downstream artifacts. The secured architecture also defines one request-to-evidence-to-review-to-promotion control flow.

**FACT:** The older split remains visible in active dashboard code and historical reports as `Architecture 1` for PRD/ICP service output and `Architecture 2` for agent control. Later documentation renamed the user-facing stages `Knowledge Service` and `Agent Control` and requires the first report before the second handoff. This is a partial conceptual migration, not a completed architecture migration.

**INTERPRETATION:** `Architecture 1` and `Architecture 2` are no longer valid top-level product architectures. They are two views over one governed case: establish reviewed knowledge and requirements, then use that same case to support or validate bounded work. Keeping them as peer architectures duplicates state, encourages PRD-first routing, and obscures the shared evidence, authority, review, and promotion lifecycle.

**INTERPRETATION:** The deepest reusable module is a **Knowledge Case Controller** with one small interface and one authoritative state packet. Retrieval, requirements and market research, role planning, design, outreach preparation, action validation, review, and memory promotion sit behind that interface. Dashboard pages, private knowledge tools, and external-action tools are adapters at explicit seams, not alternative architectures.

**RECOMMENDATION:** Replace the top-level split with one workflow:

`request -> admission -> bounded context -> evidence reconciliation -> reviewed requirements/decisions -> role-safe support or proposed work -> action validation -> approval when required -> execution receipt -> verification -> knowledge-promotion review -> terminal handoff`

The PRD and market-research functions become one bounded `requirements_and_market_research` role inside this workflow. Its product is a reviewed requirements packet, not a separate architecture and not action authority.

**HYPOTHESIS:** This unified workflow is a better product foundation for employee onboarding because the same case can answer a newcomer’s question, show the current source and decision, propose a first task, validate the proposal against reviewed requirements, stop on ambiguity, and learn only from independently accepted outcomes.

**GAP:** The repository has not yet implemented one canonical case schema, one requirement/action validator, compatibility migration from the numbered labels, or end-to-end proof that a proposed employee action is checked against reviewed requirements and decisions before execution.

## Audit boundary and method

This audit used targeted repository reads only. It prioritized active architecture, workflow, role, knowledge, and run evidence related to PRD/ICP, onboarding, market and pain research, qualification and outreach, social/publication creative, design, review, knowledge promotion, and integration. Private architecture and manifest contracts were reviewed only to derive sanitized public conclusions; private text, paths, identifiers, and local configuration details are intentionally omitted.

The audit distinguishes:

- **FACT:** directly supported by the source register below.
- **INTERPRETATION:** architecture meaning inferred from multiple facts.
- **HYPOTHESIS:** a design proposition that still needs a fixture or user evidence.
- **GAP:** missing proof, unresolved conflict, or unimplemented contract.

## Source register

All paths are relative to the standalone public repository.

### Current authority and architecture

| Source | Authority used in this audit |
|---|---|
| `AGENTS.md` | Public operating and safety contract. |
| `project/operating-rules.md` | Current public-safe, role, reporting, approval, and communication rules. |
| `project/README.md` | Current project mission and local-surface truth boundary. |
| `project/strategic-plan-2026-07-13.md` | Canonical knowledge-architecture-first E1–E8 strategy. |
| `project/task-contract-index-2026-07-13.md` | Current task/evidence states, role ownership, and proof gates. |
| `project/architecture/e1-e8-role-state-matrix.md` | Deterministic admission profiles, state coverage, reviewer separation, and terminal evidence. |
| `project/architecture/run-profiles.yaml` | Approved provider-disabled run-profile policy. |
| `project/agentic-stack.md` | Current stack description plus residual two-screen architecture language. |
| `project/context/cag-core.yaml` | Stable context assembly contract. |
| `project/workflows/langgraph-controller.yaml` | Current controller state and node contract. |
| `project/workflows/crewai-crew.yaml` | Declarative role/task pack and runtime-level truth. |
| `project/workflows/llamaindex-rag.yaml` | Bounded retrieval, source-path, canonical/superseded, and lexical-fallback rules. |
| `project/workflows/knowledge-integration.yaml` | Knowledge-layer responsibilities and promotion order. |
| `project/workflows/market-research-engine.yaml` | Existing evidence-to-message-to-action-pause-to-learning route. |
| `project/agents/agent-roster.yaml` | Configured roles, legacy aliases, skill bindings, and authority limits. |
| `project/agents/marketing-role-pack.md` | Current ICP-to-payment role sequence and shared state fields. |
| `project/knowledge/audience/icp-knowledge-continuity.md` | Current audience/forcing-moment knowledge node. |
| `wiki/memory.md` | Durable current constraints and corrected assumptions. |
| `wiki/insights.md` | Reusable knowledge, retrieval, review, and forcing-moment conclusions. |
| `wiki/rules/public-wikillm-contract.md` | Public durable-memory lifecycle. |

### Superseded and transitional architecture evidence

| Source | Use in this audit |
|---|---|
| `project/project-plan.md` | Historical proof ledger; explicitly superseded for current planning. |
| `project/reports/2026-07-02-e1-2-testmeeting-dashboard-architecture.md` | Original `Architecture 1` / `Architecture 2` dashboard split and PRD-first proof. |
| `project/reports/2026-07-03-e1-7-railway-jarvis-final-report.md` | Guarded route proof and explicit productization gaps for both numbered lanes. |
| `project/reports/2026-07-10-prd-icp-delivery-product-architecture.md` | Transitional service-first PRD/ICP architecture and evidence boundaries. |
| `docs/dashboard-operating-manual.md` | Later `Knowledge Service -> Agent Control` sequencing and browser-local boundary. |
| `docs/api-contract.md` | Current report/handoff shapes and guarded legacy endpoint names. |
| `project/dashboard/app.js` | Active implementation residue: numbered architecture selector and labels remain. |

### Historical role and execution evidence

| Source | Execution evidence traced |
|---|---|
| `project/runs/E1.3/2026-06-30-kb-readback/kb-writeback-report.md` | AF Tools, Context, Manager, Knowledge, Review, Publisher, and visual-reporting role history. |
| `project/runs/E1.3/2026-06-30-kb-readback/kb-readback-report.md` | Durable lexical readback of mission, outputs, gates, roles, and gaps. |
| `project/runs/2026-07-03-kb-update-principle/agent-handout.md` | Retrieval-versus-memory distinction and promotion rule. |
| `project/runs/2026-07-03-prd-icp-dry-run/agent-handout.md` | PRD-to-ICP evidence method, source grades, account cards, and no-outreach boundary. |
| `project/runs/20260803-onboarding-positioning-market-research/task-contracts.md` | Package audit, market/economics research, company-universe, commercial planning, and maker/reviewer gap. |
| `project/runs/20260803-onboarding-positioning-market-research/evidence-review.md` | Claim ledger and release blockers for onboarding positioning. |
| `project/runs/20260803-seven-document-onboarding-package-refresh/task-contract.md` | Strategy maker, GTM maker, integrator, and independent document reviewer. |
| `project/runs/20260803-seven-document-onboarding-package-refresh/review/final-review.md` | Final evidence, claim, parity, visual, and agent-boundary review. |
| `project/runs/20260729-qualified-prospect-outreach-expansion/task-contract.md` | Qualification planner, independent reviewer, and exact-scope integrator. |
| `project/runs/20260730-pain-evidence-outreach-refresh/task-contract.md` | Research maker, copy maker, independent reviewer, and external-write integrator. |
| `project/runs/20260730-pain-evidence-outreach-refresh/independent-review.md` | Claim, stage, variant, send-boundary, and post-write readback proof. |
| `project/runs/20260729-brand-positioning-content-redesign/task-contracts.md` | Brand/ICP/content, visual/layout, copy, automation, Figma-maker, and independent-review roles. |
| `project/runs/20260729-brand-positioning-content-redesign/agent-handout.md` | Integrated positioning, design, rights, automation, QA, and review outcome. |
| `project/runs/20260729-final-social-publication-rebuild/task-contracts.md` | Content visual auditor, New Posts auditor, copy/platform auditor, Figma maker, and reviewer. |
| `project/runs/20260729-final-social-publication-rebuild/final-acceptance-verdict.md` | Reviewer-controlled repair and accepted publication package. |
| `project/runs/20260730-pain-led-social-design-rebuild/task-contracts.md` | Market/source, pain/copy, visual-system, maker/integrator, and independent-review lanes. |
| `project/runs/20260730-pain-led-social-design-rebuild/visual-system-audit.md` | Designer’s scene grammar, evidence/rights rules, and maker implementation order. |
| `project/runs/20260730-pain-led-social-design-rebuild/independent-review-final.md` | Final maker-separated visual acceptance. |
| `project/runs/20260804-publication-sequence-visual-refinement/task-contract.md` | Integrated content/Figma maker and read-only reviewer contract. |
| `project/runs/20260804-publication-sequence-visual-refinement/review/final-review.md` | Structural, copy, export, and focused visual review with bounded gap. |
| `project/runs/20260804-publication-01-shrm-redesign/task-contract.md` | Bounded designer task with source and rollback requirements. |
| `project/runs/20260804-publication-01-shrm-redesign/review/final-review.md` | Independent visual, source, claim, and layout acceptance. |

## Current versus superseded architecture map

| Architecture surface | Evidence state | What remains valid | What is superseded or must change |
|---|---|---|---|
| June 24 Block 1 chain: dialogue/context -> PRD -> tasks -> KB -> review | Historical foundation | Source boundary, structured context, task extraction, KB update, and review are reusable workflow stages. | PRD as the organizing product and market research as a later separate block are superseded by knowledge-architecture-first strategy. |
| `Architecture 1` — PRD/ICP service lane | Historical product framing; active implementation residue | Its source-to-reviewed-artifact mechanics and guarded legacy route can serve as compatibility adapters. | It must stop being a top-level architecture. PRD/ICP becomes one artifact option of the requirements-and-market-research role. |
| `Architecture 2` — Agent Orchestra/control lane | Historical product framing; active implementation residue | Role contracts, maker/reviewer separation, stop rules, and handoffs remain essential. | It must stop being a peer architecture. Role planning and execution control are stages within the same case that produced the evidence/requirements. |
| `Knowledge Service -> Agent Control` | Transitional current UI/documentation model | Correctly sequences reviewed context before role planning and preserves a shared browser-local report ID. | Still presents two named products and two packet types. They should become views/stages of one case record, not independent sources of state. |
| E1–E8 knowledge-architecture-first strategy | Current canonical strategy | Knowledge authority, goal/loop control, roles/tools, bounded retrieval, market-to-payment, surfaces, assurance, and productization are one strategic spine. | Needs a smaller operational state machine for day-to-day onboarding and action support; E1–E8 epics are governance categories, not runtime states. |
| Secured public/private architecture | Current operational architecture | One control flow, bounded retrieval, public/private seams, independent review, sanitized promotion, and deterministic fallbacks. | Needs a public reusable case schema and adapter contracts so the public system can be cloned without private dependencies. |
| Proposed Knowledge Case Controller | Proposed target | One case, one evidence/requirement spine, one validation contract, role-safe projections, and receipts. | Requires independent review, schemas, fixtures, migration, and compatibility tests before becoming canonical. |

### What the numbered split caused

**FACT:** The old PRD/ICP lane and agent-orchestra lane had different endpoint names, prompts, screen defaults, and labels, while later docs required the first lane’s report before the second lane could prepare a handoff.

**INTERPRETATION:** The system was already behaving like one workflow with two presentations, but the top-level naming made the seam too shallow. The first presentation owned “knowledge/product work” and the second “agent work,” even though both depended on the same source boundary, goal, reviewer, approval state, and durable handoff.

**RISK:** Separate architecture selection lets a request enter “agent control” without an authoritative requirement set, or enter “PRD service” and stop before action authority, validation, and outcome readback are defined.

## Historical execution trace

### PRD, ICP, and market/pain analysis

**FACT:** Early PRD proof used a linear route: source inventory, context digest, PRD, task/responsibility matrix, knowledge update, review, and readback. Later PRD-to-ICP work added public-source boundaries, source grades, account evidence cards, role currentness, and a two-independent-signal rule.

**FACT:** The onboarding market run split package audit, market/economics research, company-universe screening, and commercial plans, but its maker also performed integration and explicitly recorded that independent review was missing. A later seven-document refresh restored maker separation: strategy/evidence maker, GTM/validation maker, integrator, and independent reviewer.

**INTERPRETATION:** Requirements synthesis and market evidence are naturally one bounded role because they share claim lineage, contradictions, assumptions, target scope, acceptance criteria, and decision questions. They should not be separate top-level architectures. They may still use internal read-only branches for source collection, economics, cohort evidence, and requirement extraction.

### Qualification and outreach preparation

**FACT:** Qualification runs did not treat a company signal as pain proof. They reconciled eligible records, current stage, assignment, current role, and existing page state before drafting. Outreach preparation separated research maker, copy maker or action planner, independent reviewers, and the integrating writer. Sending, scheduling, property changes, stage changes, and tracking remained forbidden unless separately authorized.

**FACT:** The strongest message contract was `pain -> bounded mechanism -> low-pressure question`, with variants tied to decision/handoff reliability or role-specific assistants over approved knowledge. An independent partnership review and humanization review occurred before exact-scope writeback; a post-write readback verified the target state.

**INTERPRETATION:** Qualification is not a special sales architecture. It is the general action-validation contract applied to an external communication proposal: target identity, source support, stage/currentness, message version, permission, owner approval, and readback.

### Publication creative and design

**FACT:** Publication work repeatedly used specialist read-only lanes for market/source evidence, positioning/copy, visual-system audit, rights/source control, and automation architecture; one Figma maker/integrator then changed the shared design surface; a separate reviewer inspected frozen output. Review findings triggered bounded maker repair and re-review.

**FACT:** Accepted visual work required an explicit content job, evidence boundary, rights decision, source/currentness state, typography and layout constraints, phone-scale checks, recoverability, and zero publication authority. Later refinements preserved previous groups for rollback and recorded bounded gaps when the reviewer did not reopen the full export breadth.

**INTERPRETATION:** Designer is a first-class workflow role, not a rendering tool under copy or integration. The designer owns a testable visual specification and editable design artifact; it does not own claim approval, publication authority, or final acceptance.

### Reviewer, librarian, and integrator

**FACT:** The reviewer role is strongest when it is read-only, checks a frozen maker artifact, issues `APPROVE`, `REVISE`, or `BLOCK`, and names exact repair evidence. Reviewers did not silently repair maker output.

**FACT:** The knowledge role converted accepted outputs into KB candidates, public-safe history, source registries, memory candidates, and readback. Retrieval itself was not durable memory.

**FACT:** The integrator owned file claims, merge order, shared-surface mutation, exact-scope writeback, reconciliation, final validation, run evidence, and owner handoff. The integrator did not gain self-approval or unrestricted external authority.

**INTERPRETATION:** These three roles form the irreducible governance triangle:

1. maker produces a bounded candidate;
2. independent reviewer controls acceptance;
3. librarian promotes only accepted reusable knowledge;

The integrator coordinates the triangle but cannot collapse it into one approval authority.

## Normalized role catalog

Runtime names, model names, historic nicknames, and lane IDs are bindings, not authority. A role is selected because a case needs its output and gate.

| Normalized role | Historical/configured labels normalized | Evidence state | Owns | Must not own |
|---|---|---|---|---|
| `admission_controller` | Hermes/watchdog, deterministic admission controller, execution classifier | Deterministic admission executed; autonomous watchdog planned | Risk/profile classification, source class, required roles, side-effect gates, initial state | Project edits, provider activation, self-approval, permission expansion |
| `goal_and_architecture_operator` | Goal Architect, Architecture Operator, system architecture engineer | Executed in planning/review runs | Objective, done conditions, state design, role/skill/retrieval/gate contract | High-risk self-verification or external action |
| `source_and_context_operator` | AF Tools, AF Context, retrieval operator, source analyst | Executed | Allowlist, source inventory, CAG, bounded retrieval, evidence capsule, lexical fallback | Durable promotion, unbounded ingestion, unsupported synthesis |
| `requirements_and_market_research` | AF Manager, AF Discovery, AF PRD Architect, AF Research, market analyst, strategy/evidence maker, ICP analyst | Executed as several separate roles; target normalization proposed | Reviewed requirement candidates, problem/market evidence, assumptions, contradictions, non-goals, acceptance criteria, requirement-to-source lineage | Product authority, demand claims, outreach/send, requirement approval, execution |
| `task_and_handoff_planner` | AF Task Translator, task architect, PM/task reviewer | Executed | Dependency graph, bounded task packets, expected artifacts, checks, owner questions, stop conditions | Shared-file mutation unless assigned, status inflation, external action |
| `positioning_and_copy_maker` | AF Copy, pain-to-positioning copy analyst, B2B copywriter, social strategist, humanization reviewer when maker-assigned | Executed | Evidence-linked positioning, message/caption candidates, CTA, claim table, platform adaptation | Invented proof, claim approval, sending/publishing |
| `qualification_and_channel_planner` | ICP evidence agent, external-action planner, ABM Channel Agent, sourcing/GTM maker | Executed | Current target/stage/role verification, channel packet, sequence candidate, send checklist | Autonomous send, bulk enrichment, pain assertion from signals, stage inflation |
| `designer` | GloomyLord visual sidecar, senior editorial designer, visual-system analyst, layout auditor, Figma redesign maker, experience engineer | Executed | Visual brief, scene/interface grammar, editable artifact, design-system fidelity, accessibility/layout evidence, rollback-safe maker output | Claim acceptance, rights approval without evidence, publication, self-review |
| `implementation_maker` | Executor, Luna/actor, Codex maker, document maker, Figma maker | Executed | One bounded implementation slice, claimed files, focused checks, repair | Scope expansion, final review, unapproved side effects |
| `verifier` | Technical reviewer, document/package validator, content visual auditor, QA specialist | Executed | Deterministic and observational checks, regression findings, parity/readback evidence | Silent acceptance beyond assigned criteria, maker edits unless a repair is separately assigned |
| `independent_reviewer` | AF Review, safety reviewer, claims/safety reviewer, evidence reviewer, partnership reviewer, design reviewer, release reviewer | Executed repeatedly | `APPROVE/REVISE/BLOCK`, claim calibration, privacy/permission/currentness/reversibility review, exact repair requests | Repairing the candidate, approving own high-risk output, external action |
| `knowledge_librarian` | AF Knowledge, knowledge-base maintainer, memory curator, promotion reviewer | Executed | Duplicate search, promotion candidate, source/decision/requirement lineage, supersession, freshness, readback, durable delta | Raw trace promotion, secret storage, unsupported claims, bypassing reviewer |
| `integrator` | Codex/lead integrator, Terra Integrator, Figma/document/outreach integrator | Executed repeatedly | Lane registration, conflict resolution, deterministic fan-in, shared-surface mutation, final checks, receipts, handoff | Hiding blockers, self-approval, permission inference |
| `external_action_operator` | External-action role, exact-scope writer, owner-authorized Figma/Notion operator | Executed in explicitly authorized bounded runs | One approved target/action, preflight, action receipt, readback | Reusing approval, chaining actions, credential logging, action beyond exact target |
| `release_operator` | AF Publisher, public release operator | Executed in earlier release runs; gated in audited runs | Git/release preparation, release evidence, publication review packet | Push/deploy/publication without exact approval, claim promotion |
| `growth_and_outcome_analyst` | AF Growth Evidence, funnel/ROI analyst | Configured; parts executed in market/economics analysis | Event ledger, denominators, modeled-versus-observed outcome, pursue/pivot/stop recommendation | Treating attention as demand, modeled ROI as observed, invented events |
| `observability_and_efficiency_observer` | Model-efficiency observer, automation reliability analyst | Executed as audits/configuration; provider performance proof incomplete | Run/model/tool usage evidence, runtime drift, budget and reproducibility gaps | Provider activation, invented cost/token claims, completion authority |
| `surface_projection_operator` | Dashboard workflow owner, dashboard operator, Agent Orchestra reviewer | Executed for static/browser-local surfaces | Read-only projections, local review packets, export/handoff UX, truthful state labels | Source-of-truth ownership, file creation, provider calls, writeback |
| `product_packaging_engineer` | AF Product Packaging Engineer | Planned behind productization gates | Clean-clone package, least-privilege adapters, install/upgrade/uninstall/rollback proof | Productization from desk research alone, write-by-default tools, self-approved release |

### Role-selection rules

1. Every case has exactly one accountable integrator.
2. Every material candidate has a maker; high-risk candidates have a different independent reviewer.
3. `requirements_and_market_research` is invoked when the request changes scope, requirements, market assumptions, audience, acceptance criteria, or decision rationale. It is not mandatory for a purely mechanical task whose approved requirement already exists and is fresh.
4. `designer` is invoked when visual hierarchy, interface behavior, brand expression, document layout, or creative artifact quality is part of acceptance.
5. `qualification_and_channel_planner` prepares external communication but never sends.
6. `external_action_operator` exists only after a target-specific approval interrupt.
7. `knowledge_librarian` runs after acceptance, not after every generated artifact.
8. A runtime may hold more than one low-risk maker role in a small case, but reviewer and external-approval authority remain separate.

## Target module and seams

### Knowledge Case Controller

The target should be a deep module: callers learn one interface while the implementation contains state transitions, role selection, evidence/requirement lineage, review, approval, receipt, and promotion logic.

Proposed interface, expressed behaviorally rather than as a programming-language signature:

| Operation | Required input | Returned result | Side-effect rule |
|---|---|---|---|
| `open_case` | goal, actor role, source boundary, desired outcome, constraints, stop conditions | admitted or blocked case with stable ID and next state | Planning-only; no retrieval or writes implied |
| `advance_case` | case ID, candidate artifact or evidence delta, actor role | next state, required role, missing evidence, allowed actions | Deterministic state update only in an approved runtime |
| `evaluate_proposal` | case ID, proposed action/diff, requirement and decision references | eligibility verdict, blocking reasons, required reviewer/approval/checks | No execution |
| `record_result` | case ID, execution receipt, verification evidence | verified, repair, failed, or blocked result | Receipt is evidence, not durable knowledge |
| `propose_promotion` | case ID, accepted reusable delta | public, private, role-projection, supersession, or no-promotion candidate | Promotion waits for independent boundary review and readback |

Internal adapters may vary without changing this interface:

- source adapters for public files and approved private manifests;
- retrieval adapters for lexical and later benchmarked alternatives;
- role-worker adapters for local deterministic operators or approved model-backed workers;
- action adapters for files, design tools, task boards, communication, deployment, or other systems;
- memory adapters for public durable knowledge and private human-readable knowledge;
- projection adapters for dashboard, CLI, reports, or private knowledge interfaces.

The interface is the test surface. A clean-clone public fixture should exercise the whole state contract with in-memory or local adapters before any private or external adapter is considered proven.

## Canonical case state packet

Every role reads a projection of the same case. No role receives more source content or authority than its contract allows.

| Field group | Required fields |
|---|---|
| Identity | `case_id`, `schema_version`, `created_at`, `updated_at`, `case_type`, `workflow_state`, `evidence_state` |
| Goal | `goal`, `decision_supported`, `requested_outcome`, `done_conditions`, `non_goals`, `stop_conditions` |
| Actor and authority | `requester_role`, `accountable_owner_role`, `maker_role`, `reviewer_role`, `allowed_actions`, `forbidden_actions`, `approval_class` |
| Source boundary | `allowed_source_classes`, `excluded_source_classes`, `manifest_refs`, `retrieval_mode`, `source_freshness_policy`, `source_boundary_status` |
| Evidence | `evidence_refs`, `claim_ids`, `claim_states`, `contradictions`, `gaps`, `canonical_or_superseded_state` |
| Requirements | `requirement_ids`, `requirement_versions`, `requirement_states`, `decision_refs`, `acceptance_checks`, `unresolved_questions` |
| Work | `task_contract_refs`, `dependencies`, `claimed_outputs`, `attempt_count`, `repair_count`, `budget_state` |
| Proposal | `proposal_id`, `proposed_change`, `requirement_coverage`, `predicted_effect`, `side_effects`, `reversibility`, `rollback`, `permission_scope` |
| Review and approval | `review_phase`, `review_verdict`, `findings`, `approval_state`, `approval_receipt`, `approval_expiry` |
| Result | `execution_receipt`, `verification_refs`, `readback_state`, `actual_outcome`, `remaining_gaps` |
| Knowledge | `promotion_candidate_ids`, `promotion_domain`, `supersedes`, `freshness_owner`, `next_review_at`, `promotion_status` |

## Unified state machine

The state machine is intentionally smaller than the E1–E8 strategy. Epics classify governance and product maturity; case states control one request.

| State | Required evidence | Owner | Allowed transition | Fail-closed condition |
|---|---|---|---|---|
| `request_received` | Goal and requested outcome | admission controller | `admission_checked` | Goal or actor authority is missing |
| `admission_checked` | Profile, risk, side-effect class, role minimum, stop rules | admission controller | `context_bound` or `blocked` | Provider/external/destructive scope lacks approval or profile |
| `context_bound` | CAG references, source allowlist/exclusions, canonical pointers | source/context operator | `evidence_gathering` or `blocked` | Public/private boundary or authority conflict |
| `evidence_gathering` | Source-path results and freshness metadata | source/context operator; parallel read-only branches allowed | `evidence_reconciled` | Missing provenance, unbounded corpus, or prohibited source |
| `evidence_reconciled` | FACT/INTERPRETATION/HYPOTHESIS/GAP, contradictions, canonical/superseded status | integrator plus verifier | `requirements_review` or `work_planning` | Unresolved contradiction controls the requested decision |
| `requirements_review` | Requirement candidates, market/problem evidence, non-goals, tests, owners | requirements and market research maker | `requirements_approved`, `repair`, or `blocked` | Requirement lacks evidence state, owner, acceptance, or independent review |
| `requirements_approved` | Reviewer verdict and approved requirement/decision versions | independent reviewer and accountable owner where needed | `support_ready` or `work_planning` | Reviewer is maker or decision is stale |
| `support_ready` | Role-safe source projection and answer policy | knowledge librarian / support adapter | `answered`, `work_planning`, or `blocked` | Answer would hide conflict, exceed role, or invent company truth |
| `work_planning` | Task graph, roles, claimed outputs, checks, repair/stop rules | task planner and integrator | `candidate_in_progress` | Overlapping write claims or missing reviewer |
| `candidate_in_progress` | Bounded maker artifact and focused checks | assigned maker/designer/copy/research role | `candidate_review` or `repair` | Scope expansion, budget/attempt cap, or forbidden action |
| `candidate_review` | Frozen candidate plus verification evidence | independent reviewer | `proposal_ready`, `repair`, or `blocked` | Missing evidence, self-review, unsupported claim, safety defect |
| `proposal_ready` | Proposed action/diff linked to approved requirements and decisions | integrator | `proposal_validated` | Missing requirement coverage, target, rollback, or permission scope |
| `proposal_validated` | Validator verdict, reviewer state, exact checks | verifier/reviewer | `approval_wait`, `execution_ready`, `repair`, or `blocked` | Role, requirement, source, permission, or safety rule fails |
| `approval_wait` | Target-specific approval request | owner | `execution_ready` or `stopped` | Approval missing, expired, ambiguous, or for a different action |
| `execution_ready` | Exact target, action, adapter, rollback, preflight | external action operator or local executor | `executed` or `blocked` | Target drift, precondition failure, or unavailable adapter |
| `executed` | Action receipt with exact observed target/result | executor | `result_verification` | Receipt missing; do not infer success |
| `result_verification` | Deterministic checks and post-action readback | verifier | `accepted_result`, `repair`, `failed`, or `blocked` | Result differs from approved proposal or cannot be read back |
| `accepted_result` | Independent acceptance and remaining gaps | reviewer/integrator | `promotion_review` or `closed_no_promotion` | Acceptance overstates scope or evidence |
| `promotion_review` | Reusable delta, domain, provenance, supersession, freshness, boundary checks | knowledge librarian plus independent reviewer | `promoted`, `closed_no_promotion`, or `blocked` | Raw trace/private leakage/unsupported conclusion/no future value |
| `promoted` | Durable write receipt and readback | librarian/verifier | `closed` | Readback fails or conflicting durable state exists |
| `repair` | Exact finding, assigned maker, attempt count | integrator | returns to the producing state | Three attempts or same failure twice |
| `blocked` / `failed` / `stopped` / `closed` | Accurate terminal receipt and next safe action | integrator | terminal | No silent upgrade to Done |

### Supported case routes

The machine is one workflow, but not every request visits every state.

- **Onboarding question:** admission -> context -> evidence -> support-ready -> answered -> optional promotion review.
- **First-task proposal:** admission -> context -> evidence -> approved requirements -> planning -> candidate -> review -> proposal validation -> local execution or approval wait -> verification -> promotion review.
- **PRD/market request:** admission -> context -> evidence -> requirements review -> approved requirements -> handoff or work planning. The PRD is an output view of the requirement set.
- **Outreach proposal:** admission -> context -> evidence/qualification -> copy candidate -> independent review -> action validation -> owner approval -> exact send/write adapter -> readback -> outcome evidence. Preparation may terminate safely before action.
- **Publication creative:** admission -> evidence/claim packet -> copy/design makers -> frozen review -> owner publication approval -> publication adapter -> readback. Design completion alone is not publication.
- **Knowledge correction:** admission -> context -> contradiction -> reviewed correction/supersession -> promotion review -> readback.

## Requirements-and-market-research role contract

This role replaces the top-level PRD/ICP architecture and consolidates the evidence-bearing parts of AF Manager, AF Discovery, AF PRD Architect, AF Research, market analyst, ICP analyst, and strategy/evidence maker.

### Purpose

Turn an approved product, onboarding, operational, or market question into a reviewable requirement set that preserves the difference between observed evidence, interpretation, hypothesis, contradiction, and gap.

### Inputs

- admitted case goal and decision supported;
- source boundary and freshness rules;
- existing canonical requirements and decisions;
- approved public evidence and sanitized private evidence capsule where authorized;
- target users/roles and forcing-moment hypothesis;
- requested output shape such as decision brief, PRD view, ICP view, onboarding task, experiment, or validation plan.

### Internal read-only branches

- requirement extraction and conflict detection;
- user/job/forcing-moment evidence;
- market and alternative evidence;
- economics and measurement assumptions;
- cohort/account evidence where relevant;
- negative cases and disconfirming evidence;
- acceptance, non-goal, and stop-condition drafting.

One role owner reconciles branches. Parallel branches may not write the canonical packet.

### Required output: requirements packet

| Field | Contract |
|---|---|
| `requirement_id` | Stable ID; never inferred from section order |
| `version` | Monotonic version or content hash |
| `statement` | One testable need, constraint, or decision rule |
| `requirement_type` | outcome, behavior, safety, permission, evidence, usability, quality, market, measurement, non-goal, or stop rule |
| `state` | proposed, reviewed, approved, rejected, superseded, blocked, or gap |
| `evidence_refs` | Source-path or approved private-manifest references; no unsupported claim |
| `claim_status` | fact, interpretation, hypothesis, or gap |
| `market_scope` | Cohort, buyer/user role, geography/time boundary, and limitations where applicable |
| `rationale` | Why the requirement exists and which decision it supports |
| `owner_role` | Accountable requirement owner |
| `reviewer_role` | Independent acceptance role |
| `acceptance_checks` | Observable pass/fail evidence |
| `non_goals` | Explicit exclusions |
| `conflicts` | Contradictory requirement/decision/evidence IDs retained, not erased |
| `freshness` | Evidence date, expiry/review trigger, and currentness state |
| `supersedes` | Prior requirement/decision IDs and reason |
| `action_constraints` | Roles, permissions, target classes, review, and approval gates |

### Optional projections

The same reviewed packet may render as:

- PRD;
- ICP/problem card;
- market evidence report;
- onboarding map;
- backlog and Definition of Done;
- account-screening method;
- pilot/experiment brief;
- decision memo;
- role-safe support context.

These are projections, not separate sources of truth. Editing a projection does not change an approved requirement unless the change returns through review.

### Gate and forbidden actions

The role may propose requirements but cannot approve them, execute work, contact targets, publish, activate providers, promote memory, or present market signals as demand. An independent reviewer checks source quality, contradiction handling, requirement testability, commercial/outcome claim status, and public/private safety.

## Requirement/action validation contract

Every proposed action is evaluated against the reviewed case before a tool is selected. Tool connectivity never establishes permission or business correctness.

### Action proposal schema

| Field | Required meaning |
|---|---|
| `proposal_id` | Stable candidate ID |
| `case_id` | Governing case |
| `actor_role` | Role requesting execution |
| `intent` | The business or user outcome, not only the tool operation |
| `target` | Exact file, record, design node, endpoint, communication, or other bounded target |
| `change_set` | Human-reviewable diff or precise action payload |
| `requirement_refs` | Approved requirement versions covered by the proposal |
| `decision_refs` | Current decisions and rationale governing the action |
| `evidence_refs` | Evidence used to choose the action |
| `coverage` | Requirement-by-requirement explanation: satisfied, unaffected, exception, or gap |
| `predicted_effect` | Expected observable result, explicitly a prediction |
| `permission_scope` | Allowed role, source/data class, target, operation, duration, and approval class |
| `side_effects` | Known writes, messages, state changes, spend, disclosure, persistence, or destructive risk |
| `reversibility` | Reversible, compensatable, or irreversible |
| `rollback` | Exact restore/compensation method when applicable |
| `verification_plan` | Preflight, postcondition, readback, reviewer, and evidence location |
| `open_gaps` | Unresolved information that may block or constrain execution |

### Deterministic validation rules

An action may become `execution_ready` only when all applicable rules pass:

1. The case is admitted and not terminal, stale, or over attempt/budget limits.
2. Every claimed effect maps to an approved, current requirement or an explicit incident/maintenance exception.
3. Referenced decisions are current; superseded decisions cannot authorize action.
4. Contradictions material to the action are resolved or the proposal is explicitly narrowed to avoid them.
5. The actor role has authority for the operation and exact target.
6. The proposed source/data use stays inside the case boundary.
7. The change set is reviewable and no hidden chained action is required.
8. Acceptance checks and a post-action readback exist.
9. Side effects, reversibility, rollback, and retention are explicit.
10. The maker is not the final reviewer for high-risk output.
11. External communication, private-data provider use, deployment, production promotion, credential storage, live memory writeback, and destructive action have an unexpired target-specific owner approval.
12. The executing adapter’s current readiness is proved separately from its configuration.

### Validator verdicts

| Verdict | Meaning | Next state |
|---|---|---|
| `eligible` | All in-scope rules pass and no owner interrupt is required | `execution_ready` |
| `needs_approval` | Proposal is otherwise valid but exact external/high-risk approval is missing | `approval_wait` |
| `needs_repair` | Candidate can be corrected within the bounded case | `repair` |
| `stale_requirement` | Governing evidence, decision, role, or requirement is no longer current | `requirements_review` |
| `conflict` | Current evidence or decisions disagree materially | `evidence_reconciled` or `blocked` |
| `out_of_authority` | Actor, adapter, source, or target is not permitted | `blocked` |
| `not_verifiable` | No objective postcondition/readback exists | `blocked` |
| `blocked` | Safety, privacy, permission, or repeated-failure condition prevents execution | terminal or owner escalation |

### Result contract

Execution success is not inferred from a command returning, a page loading, or a receipt file existing. The result records:

- exact proposal/version executed;
- exact observed target and state before/after;
- execution adapter and authority receipt;
- deterministic checks;
- readback result;
- divergence from the proposal;
- reviewer verdict;
- remaining gaps;
- reusable knowledge delta, if any.

## Employee onboarding and role-safe support

The target product route is one knowledge case per onboarding objective or meaningful task, not a generic employee clone.

### Support contract

1. Identify the employee’s approved role, current task, manager/reviewer, allowed corpus, and decision supported.
2. Retrieve current requirement, decision, source, rationale, owner, freshness, contradiction, and review-trigger fields.
3. Answer with source and authority visibility. Distinguish current truth, historical rationale, hypothesis, and gap.
4. If the employee asks “what should I do?”, create an action proposal rather than issuing an unvalidated instruction.
5. Validate the proposal against reviewed requirements, decisions, role permission, negative cases, and acceptance checks.
6. Escalate when the source is stale, a conflict exists, the role lacks authority, or the manager/reviewer must decide.
7. After work, record the result and reviewer acceptance. Promote only the accepted reusable delta.

### Required behaviors

- cite and explain rather than imitate a departed employee;
- expose why a decision is current and who owns it;
- show what changed and what remains unresolved;
- suggest the smallest useful next step inside the employee’s role;
- make acceptance and review explicit;
- abstain on unsupported company truth;
- never monitor employees, invent approval, or inherit broader permissions from the source author;
- never convert one person’s successful task into company policy without promotion review.

### Validation fixture set

The public implementation should ship with sanitized cases for:

1. new PM asks why a feature constraint exists;
2. engineer proposes a change that conflicts with a current product requirement;
3. internal mover sees two contradictory decision records;
4. reviewer rejects an otherwise plausible action because the requirement is stale;
5. manager approves an exact bounded action and post-action readback passes;
6. accepted task outcome proposes a knowledge delta but promotion is rejected as too case-specific;
7. approved correction supersedes an old decision while retaining the historical rationale;
8. private source supports a public-safe conclusion but raw private content is blocked from promotion.

## Knowledge promotion rules

### Knowledge classes

| Class | Examples | Default lifecycle |
|---|---|---|
| Ephemeral evidence | Retrieval results, intermediate drafts, model output, screenshots, traces, temporary calculations | Remains in bounded run evidence; not durable truth |
| Accepted case result | Verified artifact, action receipt, reviewer verdict, readback | Durable run evidence; not automatically reusable knowledge |
| Public durable knowledge | Public-safe requirement, decision, rule, insight, role contract, reusable method | Independent boundary review -> public promotion -> readback |
| Private durable knowledge | Confidential decision/context retained under approved local policy | Private promotion path only; no public dependency |
| Role projection | Minimal task/role-specific view of accepted knowledge | Derived and rebuildable; never canonical |
| Generated structure | Search index, graph, embeddings, dashboard data | Rebuildable reference; never canonical |

### Promotion test

A candidate may be promoted only when:

1. it changes how a future authorized role should understand or act;
2. its source, claim, requirement, decision, and case lineage are retained;
3. FACT, INTERPRETATION, HYPOTHESIS, and GAP remain distinguishable;
4. accountable owner, independent reviewer, freshness, review trigger, contradictions, and supersession are explicit;
5. raw traces, secrets, credentials, private identifiers, private URLs, raw private passages, local paths, screenshots, and deployment metadata are absent from public candidates;
6. the candidate does not overstate execution, demand, runtime, ROI, or external availability;
7. the destination is searched first to avoid duplicate or competing canonical records;
8. public/private boundary checks and the authoritative public-safety check pass after the final public edit;
9. readback proves a future case resolves the current record and can still find the superseded rationale;
10. failed readback reopens promotion review rather than silently leaving two truths.

### Supersession and correction

- Correct durable knowledge through a new reviewed version linked by `supersedes`; do not erase contrary history merely to simplify retrieval.
- A current pointer controls default retrieval; superseded records remain available for rationale and audit.
- Contradiction is preserved as evidence until an owner/reviewer decision resolves it.
- Freshness can downgrade `approved` to `review_required`; it cannot silently rewrite the requirement.
- Deletion or retention expiry is a separate policy action and is never implied by supersession.

## Public/private seams

### Public system

The public repository must remain a complete, clean-clone reference implementation. It owns:

- public schemas and sanitized fixtures;
- the Knowledge Case Controller contract;
- role and workflow documentation;
- public source adapters and lexical fallback;
- deterministic validators and in-memory/local test adapters;
- public-safe diagrams and dashboard projections;
- run, review, and promotion evidence safe for publication.

It must not require a private vault, private corpus, private runtime, private identifier, connector credential, or owner-specific path to build, test, or explain itself.

### Private system

The private domain may provide manifest-approved evidence, local runtime state, confidential decisions, and private memory adapters. Its facts enter a public case only as an independently reviewed sanitized conclusion. Public artifacts receive a non-sensitive evidence reference or claim state, not raw content or implementation detail.

### Seam rules

| Seam | Public interface | Private/external adapter rule | Fail-closed behavior |
|---|---|---|---|
| Source | Manifest reference, source class, freshness, allowed operation | Private adapter resolves only owner-approved relative entries | Reject unknown/broad source or missing approval |
| Retrieval | Query, filters, source refs, claim state | Private index remains local and source-bounded | Lexical/public fallback or explicit GAP; never widen corpus |
| Role context | Minimal case projection | Private role/employee context is least-privilege | Omit unavailable fields; do not infer identity/authority |
| Action | Exact proposal, target class, permission, approval, rollback | Adapter performs one approved operation | No approval reuse, chaining, or hidden write |
| Memory | Reviewed promotion candidate | Private and public destinations remain separate | No cross-domain write when boundary review fails |
| Human knowledge interface | Read/search/update contract with schema discovery | Local knowledge tool must prove live readiness separately | Read-only/file fallback; no guessed tool or claimed write |
| Dashboard | Read-only case projection and candidate packet | No direct access to private corpus or action credentials | Display `not configured`, `blocked`, or `review required` truthfully |

**INTERPRETATION:** These are real seams because the system needs at least a public/local test adapter and a private or external adapter. They should be injected behind the controller interface. Internal role steps should not become public interfaces merely because tests or one runtime need them.

## Dashboard-plan implications only

No dashboard implementation is authorized by this lane. The future plan should:

1. Replace the top-level `Architecture 1` / `Architecture 2` selector with one `Knowledge Case` entry point.
2. Keep `Knowledge Service` and `Agent Control` only as optional stage/view labels during migration, not independent products or stores.
3. Use one case ID and one state packet across intake, evidence, requirements, roles, proposals, review, approval, execution receipt, verification, and promotion.
4. Add a requirement/decision view showing current version, source, rationale, owner, reviewer, freshness, contradictions, supersession, and acceptance checks.
5. Add a proposal-validation view showing requirement coverage, exact change set, permission, side effects, rollback, checks, verdict, and owner interrupt.
6. Add a role-safe onboarding view that reveals only the employee’s allowed sources/actions and clearly distinguishes answer, proposal, approval, and executed result.
7. Show public/private source class and evidence state without displaying private paths, identifiers, or raw snippets.
8. Keep the static/public surface report-only: suggested files remain `created: false`; actions remain `not_executed`; memory remains `not_promoted` until a separate approved operator receipt exists.
9. Keep compatibility import for legacy PRD/ICP reports and agent-orchestra handoffs, mapping both into one case while preserving their original evidence state.
10. Remove numbered labels only after schema migration, documentation updates, browser fixtures, clean-clone checks, and independent review pass.

Suggested future navigation:

`Cases | Evidence | Requirements & Decisions | Roles & Work | Proposed Actions | Reviews & Approvals | Receipts | Knowledge`

## Migration plan

### Phase 0 — freeze truth and inventory

- Mark the numbered architecture framing as `legacy_compatibility` in new documentation while preserving historical run evidence.
- Inventory every active selector, endpoint, prompt, report field, dashboard-data record, role alias, and documentation reference that depends on `Architecture 1`, `Architecture 2`, PRD/ICP Flow, Agent Orchestra, Knowledge Service, or Agent Control.
- Record which items are source contracts versus generated data or historical text. Historical artifacts are not rewritten.

**Exit gate:** reviewed inventory and no ambiguous canonical pointer.

### Phase 1 — public schemas and fixtures

- Define versioned case, evidence, requirement, decision, proposal, review, approval, execution-receipt, result, and promotion schemas.
- Define the normalized role catalog as contract data, with legacy alias mapping.
- Create sanitized onboarding, PRD/market, outreach, publication, contradiction, and supersession fixtures.

**Exit gate:** deterministic schema validation, negative fixtures, and independent architecture/privacy review.

### Phase 2 — controller and validator

- Implement the Knowledge Case Controller with local/in-memory adapters first.
- Implement requirement/action validation as a pure result-returning module; it must not execute actions.
- Test through the controller interface, including repair caps, self-review rejection, stale requirements, approval expiry, receipt/readback failure, and promotion rejection.

**Exit gate:** provider-disabled end-to-end fixtures reach accurate accepted or blocked states with no external writes.

### Phase 3 — role and knowledge adapters

- Bind public retrieval, role workers, designer, reviewer, librarian, and integrator projections to the case schema.
- Add explicit public and private memory adapters without making the public build depend on the private adapter.
- Add the private human-knowledge adapter only after live schema/readiness proof; default to read-only and fail closed.

**Exit gate:** public clean clone passes with test adapters; private integration passes separate boundary/readback review.

### Phase 4 — compatibility and dashboard plan execution

- Map legacy PRD/ICP packets to requirement projections.
- Map legacy agent-orchestra packets to role/task/proposal projections.
- Migrate the dashboard to one case state without changing historical run records.
- Keep old endpoint/packet adapters temporarily, returning deprecation metadata and the new case ID.

**Exit gate:** old and new fixture parity for supported behavior, truthful no-execution labels, accessibility/browser review, and independent reviewer PASS.

### Phase 5 — operational pilots

- Run internal onboarding-question and first-task cases.
- Run one mechanical local action proposal and one exact-scope approved external-action simulation before any real external action.
- Measure retrieval accuracy, contradiction detection, requirement coverage, reviewer defects, repair count, readback, and promotion quality.

**Exit gate:** no critical safety/provenance regression; results are measured, not inferred.

### Phase 6 — retire top-level tracks

- Remove numbered selector and canonical documentation only after compatibility evidence and owner acceptance.
- Retain legacy import adapters for a declared period; remove them through a separately reviewed breaking-change decision.
- Promote the unified workflow only after the public safety, clean-clone, architecture, evidence, design, and privacy reviews pass.

## Risks and controls

| Risk | Why it matters | Control | Current state |
|---|---|---|---|
| Big-bang rename breaks historical evidence or active UI | Numbered labels remain in code, generated data, reports, and legacy endpoints | Inventory, compatibility adapters, do not rewrite history | GAP — inventory not yet complete |
| Unified case becomes a shallow “god object” | One schema could expose every internal detail to every caller | Small controller interface, role projections, internal seams, test through interface | Proposed |
| Requirements role becomes an unbounded super-agent | PRD, market, discovery, economics, and ICP can expand indefinitely | Bounded question, allowlisted sources, internal read-only branches, one reconciler, stop rules, reviewer | Proposed; prior evidence supports shape |
| Market evidence silently becomes requirement truth | Hiring/social signals are not pain or demand proof | Claim states, two-signal rule, direct-evidence requirement, reviewer, freshness | Partly proven in research/outreach runs |
| Action validator becomes ceremonial | A packet could pass without exact requirement coverage or readback | Deterministic rules, negative fixtures, pure verdict module, exact proposal version and result receipt | GAP — not implemented |
| Role alias confusion expands authority | Historical names mix runtime identity, model tier, and role | Canonical role IDs, aliases as metadata, authority only from case contract | Current configs partly support this |
| Designer is treated as a tool under the integrator | Visual requirements and evidence get checked too late | First-class designer contract, frozen artifact, independent design review | Proven pattern in publication runs |
| Reviewer bottleneck or self-review | High-quality runs needed multiple focused reviews and repairs | Risk-based reviewer selection, read-only verdict, exact findings, repair caps | Proven pattern; capacity unmeasured |
| Promotion duplicates or overwrites truth | Retrieval can surface old and new records | Search-before-write, current pointer, supersession, contradiction retention, readback | Contract exists; unified schema GAP |
| Private leakage through citations or dashboard | Public artifacts could reveal private path or context | Source-class projection, sanitized claims, public safety scan, separate adapters | Current policy; needs fixtures |
| Adapter readiness confused with configured state | A connector or endpoint can exist without live action proof | Separate configured/tested/running/readback states; fail closed | Current policy; recurrent historical issue |
| Approval reuse or action chaining | One approval could mutate more than reviewed | Exact action/target/payload/expiry, one receipt, no chaining | Current contract; unified validator GAP |
| Static dashboard overclaims execution | Browser-local animation or packets may look live | `not_executed`, `created:false`, receipt-required states, read-only projection | Current docs support this; numbered residue remains |
| Case state diverges across public/private memory | Two durable truths defeat onboarding reliability | One public/private promotion seam, domain-specific canonical pointer, cross-domain receipt without raw-copy dependency | Proposed; integration proof pending |
| Clean-clone system depends on owner environment | Reuse would fail outside the private setup | Public fixtures and test adapters, no private paths/IDs/config dependency | Acceptance criterion; not yet proven |

## Final architecture decisions proposed for integration

1. **Remove `Architecture 1` and `Architecture 2` as top-level conceptual tracks.** Preserve them only as temporary compatibility aliases and historical labels.
2. **Adopt one Knowledge Case Controller and one canonical case packet.** All roles consume least-privilege projections of that packet.
3. **Make PRD plus market research one bounded `requirements_and_market_research` role.** PRD, ICP, evidence report, and onboarding map are projections of reviewed requirements.
4. **Make action validation a mandatory pure gate before tool selection or execution.** Connectivity is not authority; a proposal must map to current requirements and decisions.
5. **Keep designer, reviewer, librarian, and integrator as separate first-class roles.** Designer owns visual implementation, reviewer owns acceptance, librarian owns promotion, integrator owns reconciliation.
6. **Use one state machine for onboarding questions, first-task support, PRD/market work, outreach, publication creative, local work, and external actions.** Routes skip irrelevant states but do not bypass evidence, authority, review, or receipts.
7. **Keep public and private systems independently operable at a strict seam.** The public implementation uses schemas, sanitized fixtures, and test adapters; private adapters never become public build dependencies.
8. **Treat dashboard work as a projection migration only.** No dashboard state may become canonical or imply execution without receipts.

## Remaining gaps for the integrator and reviewer

- **GAP:** Exact active-reference inventory for every numbered architecture string, endpoint, generated data record, and documentation link is not yet complete.
- **GAP:** Canonical JSON/YAML schemas for case, requirement, decision, proposal, verdict, receipt, and promotion do not yet exist as one versioned set.
- **GAP:** The proposed role normalization has not been reconciled against every repository role alias or tested for clean-clone discoverability.
- **GAP:** No provider-disabled end-to-end fixture yet demonstrates newcomer question -> reviewed requirement -> proposed first task -> validation -> verification -> promotion decision.
- **GAP:** No unified validator currently rejects stale, superseded, out-of-authority, unreviewable, or unapproved proposals through deterministic tests.
- **GAP:** Private human-knowledge integration and its public-safe adapter contract require separate implementation evidence from the integration lane.
- **GAP:** Dashboard migration, endpoint compatibility period, and removal timing require an owner-approved implementation task; this lane provides implications only.
- **GAP:** Independent architecture, evidence, privacy, and design review has not yet evaluated this proposal.

## Lane handoff

The integrator should treat this report as a maker proposal, not accepted architecture. Reconcile it with the private integration lane and public repository benchmark lane, then produce versioned public schemas, diagrams, and clean-clone documentation. The independent reviewer should specifically challenge the state-machine skip rules, role consolidation, private/public evidence references, proposal validator, supersession behavior, compatibility migration, and the claim that the public clone remains useful without private adapters.
