# Taras Alternative — Employee Mission Desk

Status: maker proposal for integrator comparison; not an implementation or accepted architecture

Optimization target: a new employee's first 30 minutes, first useful task, daily work, escalation, and learning feedback

Primary question: **What is the next safe, useful thing I can do, why does it matter, and who will review it?**

## Recommendation in one sentence

Make the dashboard open on one role-safe mission, with Taras as the source-visible guide, and move architecture, framework, model, retrieval, and role configuration behind a proof drawer and a separately gated administration surface.

## Evidence posture

**FACT:** The committed dashboard audited for this lane is at `6c4150c`. Its source is a browser-local documentation console with a developer-facing default, 9 primary navigation destinations, 12 detailed-tool destinations, a separate Jarvis link, two legacy workflow modes, editable role configuration, and local review-packet export. The UI explicitly says that its animation and packets do not launch agents, write files, call a provider, or perform durable writeback.

**FACT:** The current dashboard has useful accessibility and responsive foundations: a skip link and live content region in `project/dashboard/index.html`; keyboard activation, dialog focus trapping, Escape handling, and focus restoration in `project/dashboard/app.js`; reduced-motion handling and mobile/tablet layout rules in `project/dashboard/styles.css`.

**FACT:** The generated dashboard role projection is derived from `project/agents/agent-roster.yaml` through `project/scripts/generate-dashboard-data.py` and written to `project/database/role-catalog.json` and `project/dashboard/data.json`. The newer canonical authority catalog is `project/system/contracts/role-catalog.json`. The two catalogs currently use different IDs and labels.

**FACT:** The existing `graphify-out/GRAPH_REPORT.md` was built from commit `324955b5`, so it is stale relative to the audited commit. Current dashboard findings in this lane therefore come from direct source reads and targeted repository search, not from treating the old graph as current proof.

**INTERPRETATION:** The current console is strong for an architect or operator who already understands ArchFlow, but it asks a newcomer to learn the system before doing useful work. The two workflow modes, technical vocabulary, route volume, role-editing controls, and developer manual make architecture the foreground and the employee's mission the background.

**HYPOTHESIS:** A mission-first projection can reduce onboarding time and unsafe guessing without weakening the case, evidence, validation, review, receipt, or promotion contracts. The outcome targets below remain hypotheses until a bounded employee pilot measures them.

**GAP:** No public evidence demonstrates a real new employee completing this flow, no canonical employee event ledger exists, the committed dashboard has no unified mission object, and browser-local state is not durable cross-device continuity.

## Committed dashboard audit

| Area | Repo evidence | Finding | Preserve or change |
|---|---|---|---|
| Entry point | `project/dashboard/index.html`; `project/dashboard/app.js` (`activeTab`, `renderManual`) | The title is “Architecture Documentation” and the default view is a developer-facing operating manual. | Change the default to **Today** and the first-run state to **Meet Taras**. Keep the manual under Help/System. |
| Navigation | `project/dashboard/app.js` (`primaryTabs`, `secondaryTabs`, `renderNav`) | Nine primary and twelve detailed dashboard destinations expose system taxonomy before the employee has a task. | Reduce employee navigation to Today, Missions, Learn, and Help. Keep technical routes in a separate administration surface. |
| System model | `project/dashboard/app.js` (`architectureMode`, `defaultServiceBlockSchema`, `defaultControlBlockSchema`, `renderOperations`) | Knowledge Service and Agent Control behave as sequential stages but remain presented as two products/modes. | Replace them with views of one `case_id` and one state spine. Legacy packet imports remain compatibility adapters. |
| Truthfulness | `project/dashboard/app.js` (`executionStages`, `startExecutionPreview`, `downloadSessionReviewBundle`) | Local animation, packet preparation, and no-execution boundaries are unusually explicit. | Preserve the boundary verbatim in plain language; never show “working” unless a verified runtime receipt exists. |
| Work object | `project/dashboard/app.js` (`taskStages`, `renderRoleConfigPanels`, schema node inspector) | The console configures workflows and roles, but does not give an employee one compact mission with outcome, authority, evidence, done condition, reviewer, and escalation together. | Introduce a canonical Mission Card as the everyday projection of a knowledge case. |
| Role truth | `project/scripts/generate-dashboard-data.py`; `project/database/role-catalog.json`; `project/system/contracts/role-catalog.json` | Dashboard role data comes from the older roster, while the unified system has a different canonical role catalog. | Generate employee projections from the canonical system role catalog and carry legacy aliases as metadata only. |
| Continuity | `project/dashboard/app.js` (`storageKeys`, `sharedSession`, local packet export) | Work survives only in this browser unless exported; local state is accurately labeled. | Add explicit Save/Export/Import and “stored on this device” status. Do not imply durable team state without a verified adapter and readback. |
| Accessibility | `project/dashboard/index.html`; `project/dashboard/app.js` (`bindNodeControlPanel`); `project/dashboard/styles.css` (`prefers-reduced-motion`) | Skip navigation, keyboard activation, modal focus behavior, and reduced motion exist. | Reuse these patterns for mission and reviewer surfaces, then add 320 px reflow, touch-target, contrast, error-summary, and screen-reader acceptance checks. |
| Responsive behavior | `project/dashboard/styles.css` (`@media` rules at 1050/760/640 px) | The UI reflows and offers a stage list on smaller screens, but the many routes still become a horizontally scrolling control strip. | Use four-item bottom navigation on phones and keep the current mission action visible without horizontal navigation. |

## Public-repository execution evidence traced

The proposed employee flow is not invented from a generic task manager. Each mission type below maps to public ArchFlow evidence.

| Capability | Evidence | Reusable behavior in the Mission Desk |
|---|---|---|
| Onboarding | `docs/onboarding-knowledge-agent.md`; `project/system/fixtures/onboarding-case.json` | Bind role, manager/reviewer, corpus, and authority; show current requirement, rationale, source, freshness, contradictions, allowed actions, first task, readback, and escalation. |
| Requirements and market research | `docs/executed-role-and-knowledge-trace.md`; `project/workflows/market-research-engine.yaml`; `project/system/contracts/role-catalog.json` | Keep evidence, interpretation, hypothesis, contradiction, non-goal, acceptance, owner, reviewer, and freshness in one reviewed requirements packet; do not turn a signal into demand. |
| Pain analysis | `project/workflows/market-research-engine.yaml` (`pain_scoring`, evidence rules); `project/content/architecture/content-operation-model.md` | Tie pain to a role, forcing moment, source strength, current alternative, consequence, and disconfirming evidence; show GAP when pain is inferred. |
| Outreach qualification | `project/agents/marketing-role-pack.md`; `project/content/templates/qualification-checklist-template.md`; `docs/executed-role-and-knowledge-trace.md` | Verify target, current role, stage, forcing moment, channel, two-signal minimum, permission, stop conditions, and send checklist before any message proposal. |
| Outreach copy | `project/agents/marketing-role-pack.md`; `docs/executed-role-and-knowledge-trace.md` | Use `pain -> bounded mechanism -> low-pressure question`, keep a claim table, and separate drafting from sending and approval. |
| Publication creative | `project/content/operations/content-bot-role-contracts.md`; `project/content/architecture/content-operation-model.md`; `docs/executed-role-and-knowledge-trace.md` | Separate evidence, copy, visual direction, rights/source checks, accessibility, frozen review, owner publication approval, and external publication. |
| Designer | `project/system/contracts/role-catalog.json`; `docs/executed-role-and-knowledge-trace.md` | Make the designer a first-class maker of an editable, rollback-safe artifact with layout/accessibility evidence; never inherit claim approval, publication, or self-review. |
| Implementation | `project/system/contracts/role-catalog.json`; `docs/unified-operating-architecture.md` | Give one maker exact claimed targets, approved requirements, checks, side-effect limits, rollback, and a different verifier/reviewer. |
| Reporting and outcomes | `docs/reporting-daily-weekly-template.md`; `project/content/templates/after-execution-report-template.md`; `project/system/contracts/role-catalog.json` | Generate reports from receipts and explicit FACT/INTERPRETATION/HYPOTHESIS/GAP; distinguish observed outcomes from modeled scenarios and expose denominators and missing events. |
| Review | `project/content/templates/review-gate-template.md`; `project/outputs/templates/review-report.md`; `project/system/fixtures/action-proposal-reviewer-spoof.json` | Use a frozen candidate and a different reviewer; allow APPROVE, REVISE, or BLOCK; never let the maker repair under the reviewer identity or continue through a failed gate. |
| Knowledge promotion | `project/workflows/knowledge-integration.yaml`; `project/outputs/templates/knowledge-base-update.md`; `docs/unified-operating-architecture.md` | Promote only an accepted reusable delta with source, decision, owner, freshness, contradiction, supersession, receipt, and readback; retrieval and successful execution are not memory. |

## The radically different interface

The employee surface has five actions:

1. **Continue mission** — open the next valid step of one case.
2. **Ask Taras** — get a source-visible answer or an explicit gap.
3. **Request review** — freeze the current candidate and route it to the named reviewer.
4. **Resolve interrupt** — repair, ask the owner, wait, or stop; never “continue anyway.”
5. **Finish and reflect** — attach verification/readback, record the outcome, and suggest a reusable learning.

Everything else is hidden behind those actions:

- LangGraph controls state and interrupts but is not shown as a daily destination.
- CrewAI role/task contracts select the crew but do not become editable employee personas.
- LlamaIndex with lexical fallback retrieves bounded prose evidence; exact sources remain openable.
- Orbit/Graphify contributes structural impact evidence, not business truth.
- TurboVec may supply an optional candidate result only when its benchmark and fallback gates pass.
- WikiLLM/Obsidian receives reviewed promotion candidates, not raw employee activity.
- Jarvis becomes Taras's embedded question box inside the mission, not a separate competing brain.

This is intentionally unlike a context-spine console or configurable crew studio: context appears when needed, configuration is not in the common path, and the employee starts from a useful outcome rather than a system diagram.

## First 30 minutes

For a large assignment, success at minute 30 means a validated first contribution or a correctly escalated blocker, not artificial task completion.

| Time | Employee experience | System and reviewer behavior | Evidence event |
|---|---|---|---|
| 0–2 min | **Welcome.** “I’m Taras. I’ll help you make one safe useful contribution.” The page states what is stored locally, what is not executed, and how to stop. | Bohdan checks the admitted profile; no retrieval or action occurs before role and source boundaries exist. | `onboarding_started`; `boundary_acknowledged` |
| 2–5 min | **Bind my role.** Confirm role, accountable manager, reviewer, permitted source classes, allowed actions, and forbidden actions. | Taras shows the smallest role projection. Missing manager, reviewer, or authority becomes an interrupt, not a guessed default. | `role_bound` or `onboarding_blocked` |
| 5–10 min | **Why this work.** Read a one-screen briefing: outcome, rationale, current requirement, owner, source/freshness, contradiction, and stop condition. Open at least one exact source. | Solomiia supplies bounded evidence; Taras labels FACT/INTERPRETATION/HYPOTHESIS/GAP. Stale or conflicting knowledge routes to review. | `mission_brief_opened`; `source_opened`; `comprehension_checked` |
| 10–15 min | **Accept the first mission.** See one small task, exact target, allowed action, done condition, reviewer, expected time, and escalation path. Choose Start, Ask, or Escalate. | Danylo prepares the mission; Iryna validates requirement coverage and permission before Start becomes available. | `first_mission_ready`; `mission_started` or `interrupt_opened` |
| 15–22 min | **Work with guidance.** The task stays central. Evidence and team are drawers; Taras answers source-visibly. Draft autosaves locally with an explicit device-only label. | Only the assigned maker role may own the candidate. Scope expansion re-enters admission instead of silently changing the mission. | `candidate_saved`; `question_answered` or `gap_declared` |
| 22–27 min | **Request review.** Preview exactly what will be reviewed, checks run, open gaps, and the reviewer. Submission freezes a version. | Mykola attaches deterministic evidence; Halyna returns APPROVE, REVISE, or BLOCK. External effects also require Iryna's action verdict and target-specific owner approval. | `review_requested`; `review_verdict_recorded` |
| 27–30 min | **Finish or recover.** If accepted, record readback and answer three learning prompts. If blocked, leave with an owner, reason, and next safe action. | Larysa receives only a promotion candidate after acceptance; Zoriana records aggregate outcome evidence. Nothing is promoted automatically. | `mission_accepted`, `accurate_escalation`, `feedback_submitted`, `promotion_decided` |

## Common-case information architecture

Employee navigation is intentionally small:

- **Today** — one current mission, waiting reviews, and the next safe action.
- **Missions** — active, waiting, completed, and stopped cases; not a raw run-log browser.
- **Learn** — reviewed role guidance, accepted lessons, corrections, and personal onboarding progress; no raw trace store.
- **Help** — Ask Taras, escalation contacts by role, safety boundary, and the operating manual.

“Who is helping?”, “Why?”, “Sources”, “Proof”, and “System details” are drawers inside a mission. Administration, role configuration, workflow editing, retrieval tuning, providers, and runtime status live under a separately gated **Manage system** route that is absent from employee navigation.

### Desktop mission view

```text
┌ Today ─ Missions ─ Learn ─ Help ┐        stored on this device · no live action
│ Good morning. One mission is ready.                                  [Ask Taras]
├─────────────────────────────────────────────────────────────────────────────────┤
│ CURRENT MISSION                                                                   │
│ Clarify the acceptance check for REQ-...                  READY · due today       │
│ Why: prevent an unreviewable implementation handoff                              │
│ Next: open the requirement, edit the exact target, request Halyna's review        │
│ [Continue mission] [Open source] [Escalate]                                      │
├──────────────────────────────────────┬──────────────────────────────────────────┤
│ Done when                            │ Who is helping                            │
│ □ exact target changed               │ Taras · guide        Halyna · reviewer    │
│ □ focused check passes               │ Dmytro · maker       Mykola · verifier     │
│ □ reviewer accepts frozen version    │ [Why these roles?]                        │
├──────────────────────────────────────┴──────────────────────────────────────────┤
│ Waiting on you: 0    Waiting on review: 1    Learned this week: 2                │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Screen contracts

| Screen | Job | Primary content | Primary action | Not shown by default |
|---|---|---|---|---|
| Meet Taras | Reach role-safe orientation quickly | boundary, role, manager/reviewer, source classes, first mission | Confirm role and continue | framework names, model routes, raw catalog |
| Today | Decide what to do now | one current mission, waiting items, urgent interrupt, reviewed learning | Continue mission | architecture status cards, configuration tables |
| Mission Room | Complete one bounded task correctly | outcome, why, next step, work area, done checks, reviewer, source health | Request review | full knowledge corpus, unrelated roles, provider controls |
| Ask Taras | Resolve uncertainty with visible evidence | concise answer, claim state, source, freshness, contradiction, next safe action | Use answer / open source / escalate | unsupported synthesis or unbounded chat memory |
| Review Interrupt | Make a blocked decision explicit | frozen version, reason, affected requirement, evidence, exact decision owner, repair attempts | Repair / ask owner / wait / stop | bypass, self-approval, hidden auto-retry |
| Learn | Close the feedback loop | accepted outcomes, reviewed corrections, reusable lessons, upcoming freshness checks | Suggest learning | raw prompts, raw transcript, automatic memory write |
| Mission History | Resume or explain prior work | state, artifact version, receipt, verdict, remaining gap, next owner | Resume / open receipt | false Done state or command-only success |

## Mission Card contract

The card is the everyday projection of one versioned knowledge case. The first ten fields are always visible; proof and control fields expand without leaving the mission.

### Always visible

1. `mission_title` and `case_id`
2. `outcome` — the observable result, in employee language
3. `why_now` — rationale and decision supported
4. `state` — plain label plus canonical state on demand
5. `next_safe_action`
6. `done_checks` — no more than five primary checks
7. `accountable_owner` and `assigned_maker`
8. `reviewer` and expected review service level
9. `evidence_health` — current, aging, stale, conflicting, or gap; never color-only
10. `stop_or_escalate_when`

### Proof and control drawer

- `requirement_refs`, versions, state, owner, rationale, and acceptance checks
- `decision_refs`, contradictions, non-goals, and declared gaps
- `source_refs`, source class, freshness, review-by date, and exact-source affordance
- `allowed_actions`, `forbidden_actions`, role authority, and source boundary
- `exact_target`, `proposed_change`, human-readable diff or artifact version
- `dependencies`, blocked-by, priority, due condition, and handoff target
- `risk`, `approval_class`, named approver, approval scope, and expiry
- `side_effects`, reversibility, rollback, preflight, and postcondition
- `verification_plan`, deterministic check results, receipt, and readback
- `review_verdict`, findings, assigned repair owner, attempt count, and stop threshold
- `learning_prompt`, promotion candidate, supersedes, freshness owner, and next review date
- `storage_state` — browser only, exported, verified adapter, or durable readback proven

No mission may display **Done** from progress animation, a generated draft, a command exit, a review request, or configuration alone.

## One card, adaptive mission templates

These are presets over the same fields and states, not separate architectures.

| Mission template | Lead visible crew | Additional required fields | Mandatory interrupt |
|---|---|---|---|
| Orientation / first task | Taras, Solomiia, Danylo, Iryna | role projection, manager/reviewer, current requirement, exact first action, readback | missing role/authority, stale requirement, contradictory owner instruction |
| Requirements / market | Oksana, Solomiia, Halyna | bounded question, market scope, source grades, disconfirming evidence, non-goals, acceptance, claim state | signal presented as demand, no owner, no independent source path |
| Pain analysis | Oksana, Zoriana, Halyna | actor, forcing moment, current alternative, consequence, evidence grade, counterevidence | inferred pain shown as fact, missing denominator or time boundary |
| Qualification | Andrii, Oksana, Iryna | target currentness, role/stage, two independent signals, anti-ICP, channel, consent/access | stale identity, one-signal shortcut, private/bulk enrichment, unapproved contact |
| Outreach copy | Olena, Andrii, Halyna | approved pain evidence, bounded mechanism, low-pressure question, claim table, message version | unsupported proof, message/target drift, any send request without exact approval |
| Publication creative | Olena, Kateryna, Mykola, Halyna | content job, evidence/rights, format, accessible alternative, platform readiness, recoverable source | rights/source gap, unsupported claim, inaccessible artifact, publication without owner approval |
| Design | Kateryna, Mykola, Halyna | visual/interface grammar, editable artifact, responsive states, accessibility evidence, rollback | designer self-review, missing phone-scale proof, claim or rights approval inferred |
| Implementation | Dmytro, Danylo, Mykola, Halyna | claimed targets, exact requirement, patch/artifact, checks, side effects, rollback | target/scope expansion, missing reviewer, failed repeated check, external effect |
| Reporting | Zoriana, Ostap, Halyna | event definitions, denominators, observed/modelled split, missing events, report period | modeled result shown as observed, cherry-picked cohort, invented event |
| Knowledge correction/promotion | Larysa, Solomiia, Mykola, Halyna | accepted delta, duplicate search, lineage, contradiction, supersession, freshness, readback | raw trace/private content, no future value, unsupported conclusion, failed readback |

## Employee-facing crew bindings

Call names are fictional Ukrainian names written in English letters. They improve conversation only; the stable ID and current case contract grant authority. Skill entries below are bounded method/package cues, not permission and not a claim that every package is active in every runtime.

| Call name · stable ID | Responsibility | Inputs → outputs | Bounded skills/methods | Permission boundary and reviewer route |
|---|---|---|---|---|
| Yaromyr · `goal_and_architecture_operator` | Define the outcome, done conditions, and case/gate shape. | owner request and constraints → goal contract | goal engineering, acceptance criteria, architecture mapping | No execution or high-risk self-verification; Halyna reviews material architecture. |
| Bohdan · `admission_controller` | Classify risk, profile, minimum roles, and stop rules. | request and actor → admission verdict | risk classification, run-profile selection, stop-rule enforcement | No project edit, provider activation, or self-approval; Maksym receives the verdict and Halyna audits exceptions. |
| Solomiia · `source_and_context_operator` | Build the smallest allowed evidence packet. | allowlist and question → source-visible context capsule | source-boundary control, LlamaIndex/lexical retrieval, exact-source read, structural evidence lookup | No broad ingestion, synthesis without evidence, or promotion; Mykola checks provenance and Halyna reviews boundary risk. |
| Oksana · `requirements_and_market_research` | Turn product, market, pain, or onboarding questions into reviewable requirements. | case question and evidence → requirement/market packet | company research, deep research, decision mapping, contradiction analysis | No requirement approval, demand inference, outreach, execution, or promotion; Halyna reviews. |
| Taras · `onboarding_guide` | Explain current knowledge and propose the smallest safe next task. | role projection and current case → source-visible answer or first-task proposal | guided onboarding, plain-language synthesis, escalation design, comprehension check | No invented truth, monitoring, permission inheritance, or unvalidated instruction; Iryna validates action proposals. |
| Danylo · `task_and_handoff_planner` | Shape dependencies, claims, checks, and handoff. | approved requirements → bounded mission packet | task breakdown, acceptance criteria, dependency mapping, handout writing | No unassigned shared edit, status inflation, or external action; Maksym integrates and Halyna reviews material plans. |
| Olena · `positioning_and_copy_maker` | Draft evidence-linked positioning, messages, and captions. | approved pain/claim packet → versioned copy candidate and claim table | content strategy, source-grounded copywriting, copy editing, platform adaptation | No invented proof, claim approval, sending, or publishing; Halyna reviews. |
| Andrii · `qualification_and_channel_planner` | Verify target/currentness and prepare the narrowest channel packet. | evidence card and channel rules → qualification verdict and send checklist | company research, acquisition-channel planning, customer journey, CRM hygiene | No autonomous send, bulk enrichment, pain inference, or stage inflation; Iryna validates action and Halyna reviews. |
| Kateryna · `designer` | Produce accessible, editable, rollback-safe visual/interface work. | approved brief and evidence → editable artifact and visual proof | interface design, brand system, responsive/a11y QA, visual source/rights check | No claim acceptance, unsupported rights approval, publication, or self-review; Mykola verifies and Halyna reviews. |
| Dmytro · `implementation_maker` | Implement one claimed local change. | approved mission and exact target → bounded change and focused checks | codebase design, implementation, debugging, task-specific testing | No scope expansion, final review, or unapproved side effect; Mykola verifies and Halyna reviews. |
| Iryna · `action_validator` | Check requirement coverage, role permission, side effects, and rollback. | proposed effect and current requirements → eligible, repair, approval-needed, or blocked verdict | deterministic requirement/action validation, permission and rollback checks | Cannot execute, infer approval, or rewrite the requirement; Halyna reviews the frozen candidate and owner handles exact approval. |
| Mykola · `verifier` | Produce deterministic and readback evidence. | frozen candidate and checks → verification packet or regression finding | schema/test validation, accessibility smoke, diff/readback inspection | No silent maker repair or evidence-free completion; Halyna owns acceptance. |
| Halyna · `independent_reviewer` | Issue APPROVE, REVISE, or BLOCK against a frozen version. | candidate, evidence, and rubric → verdict and exact findings | independent evidence, privacy, claim, currentness, and safety review | Cannot repair the candidate, self-approve, or act externally; repairs return to the maker and owner-only decisions escalate. |
| Larysa · `knowledge_librarian` | Decide whether an accepted delta is reusable and promotion-ready. | accepted result and lineage → promote, supersede, defer, or no-promotion candidate | duplicate search, memory filtering, lineage, supersession, freshness management | No raw trace/secret/unsupported promotion or review bypass; Halyna reviews boundary/meaning and Mykola verifies readback. |
| Maksym · `integrator` | Coordinate crew, conflicts, merge order, receipts, and handoff. | lane artifacts and verdicts → reconciled case result | evidence reconciliation, conflict resolution, integration, task handout | No hidden blocker, self-approval, or permission inference; Halyna is independent reviewer. |
| Pavlo · `external_action_operator` | Perform one exact owner-approved external action. | unexpired approval and preflight → action receipt and readback | exact-target execution, preflight, rollback, readback | No approval reuse, chaining, target expansion, or credential logging; Mykola verifies and Halyna reviews. |
| Nazar · `release_operator` | Prepare and, only when authorized, perform a release action. | accepted artifacts and release approval → release packet/receipt | release checks, public-safety scan, Git/release handoff | No deploy/publication/push without exact approval and no claim promotion; Halyna and owner gate. |
| Zoriana · `growth_and_outcome_analyst` | Measure outcomes and recommend pursue, pivot, or stop. | reviewed event ledger → observed/modelled outcome report | data analytics, experiment design, backtesting, denominator audit | No attention-as-demand, modeled-as-observed, invented event, or causal overclaim; Halyna reviews. |
| Ostap · `observability_and_efficiency_observer` | Report drift, usage evidence, and reproducibility gaps. | sanitized traces and ledgers → observation report | observability, cost/usage evidence, reproducibility review | No provider activation, invented usage, or completion authority; Maksym triages and Halyna reviews claims. |
| Marta · `surface_projection_operator` | Project case state truthfully into employee screens and exports. | least-privilege case projection → UI state or review packet | interaction design, accessible projection, export/handoff UX | No source-of-truth ownership, provider call, writeback, or execution; Mykola verifies and Halyna reviews. |
| Roman · `product_packaging_engineer` | Plan a clean-clone package after productization gates pass. | validated operational evidence → install/upgrade/uninstall/rollback package | backend/API architecture, packaging, security governance, deployment observability | Lifecycle remains planned; no productization from desk research or write-by-default tools; Halyna and owner gate. |

## One state spine, plain employee labels

The UI may skip irrelevant states, but every screen projects the same case and never creates a second workflow truth.

| Employee label | Canonical state(s) | Employee action | Required transition evidence |
|---|---|---|---|
| Getting ready | `request_received`, `admission_checked` | confirm role and boundary | actor, objective, profile, risk, stop rules |
| Finding context | `context_bound`, `evidence_gathering`, `evidence_reconciled` | read brief, open source, ask Taras | allowlist, provenance, freshness, FACT/INTERPRETATION/HYPOTHESIS/GAP, contradiction state |
| Ready to start | `requirements_review`, `requirements_approved`, `support_ready`, `work_planning` | accept mission or escalate | current requirement, owner/reviewer, acceptance, role permission, exact target, checks |
| Working | `candidate_in_progress` | create the bounded candidate | claimed target, version, local autosave state, focused checks, no scope drift |
| In review | `candidate_review` | wait, answer question, or receive repair | frozen candidate, different reviewer, evidence packet, explicit verdict |
| Validating action | `proposal_ready`, `proposal_validated` | inspect exact effect | requirement coverage, permission, side effects, rollback, validator verdict |
| Approval needed | `approval_wait` | ask named owner, wait, or stop | exact target/action/payload, approver, expiry, no approval reuse |
| Applying and checking | `execution_ready`, `executed`, `result_verification` | observe receipt or respond to failure | preflight, action receipt, deterministic checks, readback |
| Accepted | `accepted_result` | finish and reflect | independent acceptance, actual outcome, remaining gaps |
| Learning review | `promotion_review`, `promoted`, `closed_no_promotion`, `closed` | suggest learning or close with no promotion | reusable delta, duplicate search, lineage, boundary review, freshness, durable readback |
| Needs repair | `repair` | follow exact finding or escalate | assigned maker, finding, attempt count, changed evidence; maximum three attempts and same failure twice stops |
| Stopped | `blocked`, `failed`, `stopped` | open reason and next safe action | terminal receipt, owner, blocker, recovery condition; no silent upgrade to Done |

## Reviewer interrupts

An interrupt is a blocking full-width sheet on desktop and a full-screen dialog on mobile. Focus moves to its heading, remains trapped while a decision is required, and returns to the triggering control after resolution. Status is announced through a polite live region; destructive or external approval uses an assertive confirmation summary. Escape may close an informational drawer, but never dismiss a mandatory approval or safety interrupt as accepted.

| Trigger | What the sheet must show | Allowed employee choices | Route |
|---|---|---|---|
| Stale or superseded requirement | current and old versions, owner, review date, affected task, source links | ask owner, switch to current version, stop | Oksana + Halyna; Iryna revalidates |
| Contradictory evidence | both claims, source/freshness, decision affected, unresolved GAP | request reconciliation, narrow mission, stop | Solomiia/Oksana → Halyna |
| Missing role authority | requested action, role boundary, required authority, forbidden action | ask accountable owner, propose lower-risk task, stop | Bohdan/Iryna |
| Scope or target changed | original versus proposed target, side effects, new risk/profile | submit a new scope, restore original, stop | Bohdan re-admission → Danylo |
| Reviewer requests repair | exact finding, rubric, frozen version, repair owner, attempt count | repair, ask clarification, stop | returns to the original maker; reviewer identity remains separate |
| External send/publication/deploy/write | exact target, payload summary, side effects, rollback, preflight, approval expiry | request owner approval, wait, cancel | Iryna → owner → Pavlo/Nazar |
| Verification or readback failed | expected versus observed result, checks, rollback state, data uncertainty | rollback, repair, mark failed, escalate | Mykola → maker/Maksym → Halyna |
| Knowledge promotion uncertain | candidate delta, duplicate/conflict, domain, private/public boundary, freshness owner | revise candidate, no promotion, escalate | Larysa → Halyna → Mykola readback |

There is no “ignore,” “force pass,” “approve my own work,” or generic “retry” action.

## Daily work and learning feedback

### Start of day

Today shows, in order:

1. one **Continue** mission;
2. one urgent interrupt, if any;
3. reviews waiting on others;
4. freshness changes that invalidate an active mission;
5. one reviewed learning relevant to the employee's role.

The system must not rank employees, infer productivity from dwell time, or expose private coworker activity. It may show case ownership, reviewer wait state, and published team guidance required for the task.

### End of mission

Taras asks only three questions:

- What did the result prove or disprove?
- What was missing, stale, or confusing?
- Would this help the next person in the same role?

The answers become a **learning candidate**, not memory. Larysa searches for duplicates/conflicts, classifies public/private/role scope, assigns freshness and supersession, requests independent review, and verifies readback. A one-off preference, raw draft, raw chat, or success command closes with `no_promotion`.

### Reporting

Zoriana builds daily/weekly summaries from state transitions, receipts, review verdicts, readback, and declared gaps. Ostap may report system latency or reproducibility separately. Reports must distinguish observed events from targets and modeled scenarios; no employee surveillance metrics, keystroke capture, raw prompt retention, or individual performance score is allowed.

## Measurable onboarding outcomes

These are **HYPOTHESIS targets**, not current results. Pilot with a synthetic public fixture first, then with separately approved internal users.

| Outcome | Definition | Initial target | Privacy-safe event evidence |
|---|---|---|---|
| Role-safe start | Role, manager/reviewer, source classes, and forbidden actions confirmed without a guessed field. | 90% within 5 minutes | timestamps for `onboarding_started` → `role_bound`; no personal text |
| Mission comprehension | Employee correctly identifies outcome, owner, done condition, and stop/escalation trigger. | 80% answer all four before Start | four boolean comprehension checks, not answer text |
| Source visibility | Employee opens at least one governing source and sees freshness/claim state. | 90% before first review request | `source_opened` with source class and opaque reference |
| Time to first valid proposal | From role binding to Iryna returning eligible or approval-needed for the first micro-task. | median ≤20 minutes | case-state timestamps and validator verdict |
| Thirty-minute useful outcome | Accepted micro-contribution or accurate escalation with owner, reason, and next safe action. | ≥80% of pilot sessions | `mission_accepted` or `accurate_escalation`; no productivity score |
| Unsafe bypass | Execution, send, publication, deployment, or promotion without current requirement/reviewer/approval. | 0 events | validator, approval, action, and promotion receipts |
| Repair clarity | Revisions resolved without repeated ambiguous findings. | median ≤1 repair; same failure twice escalates | finding code and attempt count, not raw feedback text |
| Knowledge quality | Accepted learning candidates with lineage, freshness owner, review, and successful readback. | 100% of promoted items | promotion and readback receipts |
| Accessibility completion parity | Keyboard-only and screen-reader pilot users can complete the same synthetic mission without a mouse-only step. | 100% critical-path completion; zero critical blocker | task-level accessibility test outcomes |

Targets should be revised from observed denominators, never promoted as performance or ROI proof from one run.

## Failure and recovery

| Failure | Employee-visible truth | Recovery | Terminal rule |
|---|---|---|---|
| No approved current requirement | “This mission is not ready; its governing requirement is missing or stale.” | route to Oksana/owner; offer a read-only context task | no implementation start |
| Source missing or retrieval fails | show GAP, attempted source class, and last known freshness; never fabricate an answer | exact-source retry, lexical fallback, narrower query, or owner escalation | block the affected claim if provenance remains absent |
| TurboVec candidate unavailable or fails gate | “Semantic candidate unavailable; using lexical/exact source route.” | fall back through LlamaIndex lexical and exact-source read | no loss of case or authority; no default promotion claim |
| Browser storage cleared/corrupt | “Local draft unavailable; no durable save was proven.” | import last reviewed public-safe case packet or restart from authoritative source | never reconstruct private/raw content from memory |
| Network/provider unavailable | show offline/provider-disabled state and which actions remain local | continue read-only/offline work, save/export packet, or wait | no fake live status or automatic provider switch |
| Role/reviewer conflict | identify the overlapping identity and affected gate | assign a different reviewer and freeze the candidate again | self-review remains blocked |
| Failed check | show expected/actual, exact check, repair owner, and remaining attempts | bounded repair with new evidence; rollback if effect already occurred | same failure twice or three attempts stops/escalates |
| Approval expired or target changed | show mismatch and expire the button | request a new exact approval after revalidation | approval cannot be reused or broadened |
| Action receipt missing | show `outcome_unknown`, never Done | read back exact target, rollback if safe, or mark failed | no success inference from command return alone |
| Promotion readback fails | keep accepted result but mark knowledge `not_promoted` | repair destination or close with no promotion | operational success does not imply durable memory success |

## Accessibility requirements

Target WCAG 2.2 AA for the employee critical path; claim conformance only after automated and manual evidence.

- Every mission action, drawer, source, checklist, interrupt, and review control must be keyboard operable in a logical order.
- Keep the existing skip-link, focus-visible, dialog trap, focus restoration, and reduced-motion patterns.
- Use semantic landmarks, one page heading, ordered steps, real buttons/links, associated labels, fieldset/legend for grouped decisions, and an error summary linked to invalid fields.
- State, evidence health, urgency, and verdict must use text/icon plus color. Minimum contrast: 4.5:1 normal text, 3:1 large text and meaningful UI boundaries.
- Minimum target size is 44 by 44 CSS px on touch screens, with spacing that avoids adjacent accidental activation.
- Review state changes use concise live-region announcements. Do not auto-advance a stage after an interrupt, steal focus for background refresh, or rely on animation to show progress.
- Source links describe source, state, and freshness. Abbreviations and Ukrainian call names have stable role IDs available to assistive technology.
- At 200% and 400% zoom, the critical path must reflow without loss, overlap, clipped controls, or two-dimensional scrolling.
- Tables in proof/admin views become labeled cards on narrow screens; the employee mission itself never requires a wide table or canvas.
- Support browser text resizing, forced colors, reduced motion, high contrast, screen-reader landmarks, switch input, and keyboard-only completion.
- Errors preserve entered values, name the problem in plain language, state whether work is saved, and expose the safe recovery action.

## Responsive requirements

| Width | Layout | Critical behavior |
|---|---|---|
| Phone: 320–640 px | one column; four-item bottom navigation; sticky Continue/Request review action; full-screen evidence/reviewer sheets | current outcome, state, and next action visible before secondary detail; no horizontal navigation or canvas required |
| Tablet: 641–1024 px | one main column plus optional right drawer; bottom or compact top navigation | mission and done checks stay together; team/evidence drawer does not push action below an unbounded scroll |
| Desktop: ≥1025 px | mission center with compact right rail for done checks and active crew; evidence drawer overlays or occupies a bounded third column | no more than one primary CTA; proof/configuration remains progressive disclosure |
| Wide desktop | cap reading width; do not stretch source prose; allow side-by-side candidate and review evidence only when requested | preserve scan order and focus order independent of visual placement |

Orientation, mission start, review request, interrupt resolution, acceptance, and feedback must be exercised at phone, tablet, and desktop sizes. Device rotation and interrupted/resumed local drafts require explicit tests.

## Implementation implications for the integrator

1. Make `Today` the employee default and keep the current manual and tools under Help/Manage system.
2. Generate dashboard roles from `project/system/contracts/role-catalog.json`; retain `project/agents/agent-roster.yaml` identifiers only through declared aliases/compatibility metadata.
3. Introduce one versioned mission/case projection. Legacy PRD/ICP and agent-orchestra packets import into that case and return deprecation metadata plus the new `case_id`.
4. Replace the architecture selector in the common path with mission templates. A template may change required fields and roles but never create a separate state store.
5. Reuse the current no-execution language, local export, keyboard dialog, focus restoration, and reduced-motion code patterns.
6. Make Taras a view over approved case evidence, not an unconstrained chat persona. Every answer returns claim state, source/freshness, and next safe action or GAP.
7. Add canonical fixtures for onboarding, research/pain, outreach, publication/design, implementation, reporting, review spoof, stale knowledge, failed readback, and promotion rejection.
8. Validate import/export schema, role/reviewer separation, stale/superseded requirements, scope drift, approval expiry/reuse, receipt absence, repair caps, and no-promotion closure deterministically.
9. Keep technical settings out of the employee bundle. Configuration export/import remains public-safe and review-only; secrets never enter browser packets.
10. Do not remove historical routes or records in the same step. Hide legacy navigation from employees only after fixture parity, migration, rollback, accessibility review, and independent approval pass.

## Trade-offs

The Mission Desk is deliberately specialized. It makes the common case easy and the architecture less discoverable from the default screen. Administrators therefore need a separate, clearly labeled system view. Progressive disclosure also creates projection work: every technical state needs a plain-language label without losing exact proof.

The gain is depth. Five employee actions hide retrieval, orchestration, role selection, action validation, independent review, receipts, and knowledge promotion while keeping each inspectable on demand. The interface becomes harder to misuse because there is no generic Run Agent, Continue Anyway, Publish, or Promote button.

## Final FACT / INTERPRETATION / HYPOTHESIS / GAP

**FACT:** Public repository evidence supports one governed case flow across onboarding, research, pain analysis, qualification, copy, publication creative, design, implementation, reporting, review, and promotion. It also supports strict maker/reviewer separation and truthful local-only dashboard states.

**INTERPRETATION:** The best employee projection is not a smaller architecture console. It is a mission desk that reveals only the evidence, crew, and controls needed for the current task while preserving the same underlying case and receipts.

**HYPOTHESIS:** A guided 30-minute mission can make a new employee useful sooner, reduce ungrounded questions, and produce better escalation and learning signals. The proposed thresholds require a synthetic-fixture usability pilot and then approved internal measurement.

**GAP:** No employee pilot, durable authenticated state, live case feed, unified dashboard role source, or accessibility conformance evidence exists yet. The old Graphify snapshot is stale, and the current browser-local UI cannot prove multi-user continuity.

## Repo-relative evidence index

- Dashboard implementation: `project/dashboard/index.html`, `project/dashboard/app.js`, `project/dashboard/styles.css`, `project/dashboard/README.md`
- Dashboard generation and current generated roles: `project/scripts/generate-dashboard-data.py`, `project/database/role-catalog.json`, `project/dashboard/data.json`
- Unified role and case authority: `project/system/contracts/role-catalog.json`, `project/system/fixtures/onboarding-case.json`, `docs/unified-operating-architecture.md`
- Employee onboarding and executed role trace: `docs/onboarding-knowledge-agent.md`, `docs/executed-role-and-knowledge-trace.md`
- Research, pain, qualification, and copy: `project/workflows/market-research-engine.yaml`, `project/agents/marketing-role-pack.md`, `project/content/templates/qualification-checklist-template.md`
- Publication and design: `project/content/operations/content-bot-role-contracts.md`, `project/content/architecture/content-operation-model.md`
- Reporting, review, and promotion: `docs/reporting-daily-weekly-template.md`, `project/content/templates/after-execution-report-template.md`, `project/content/templates/review-gate-template.md`, `project/workflows/knowledge-integration.yaml`, `project/outputs/templates/knowledge-base-update.md`
- Structural-reference freshness: `graphify-out/GRAPH_REPORT.md`

## Recommendation

Select the Employee Mission Desk as the default employee experience, while retaining the context spine as an on-demand proof drawer and the configurable crew studio as a separately gated administrator surface. Implement the unified case and canonical role projection first; then test the complete 30-minute flow at phone, tablet, and desktop widths with a provider-disabled onboarding fixture and an independent reviewer before replacing legacy navigation.
