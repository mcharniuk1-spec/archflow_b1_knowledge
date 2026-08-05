# Final Independent Release Review — Responsive Knowledge Crew and Crew Desk

Run: `20260805-responsive-knowledge-crew-dashboard`
Review date: 2026-08-05
Reviewer: Halyna / `independent_reviewer`
Lane: review only
Verdict: **REVISE**

The repaired candidate is materially stronger and passes its provider-disabled core, six dashboard routes, responsive and accessibility matrix, landing-page layer projection, four visual readbacks, public-safety scan, artifact parsing, link check, and diff hygiene. It is not ready to stage because the active admission policy still carries a second role/state architecture, one current LlamaIndex contract still publishes unsupported TurboVec measurements, the role contracts do not yet contain every accepted responsibility field, and configuration/scope packets retain two bounded reliability defects.

This reviewer did not repair, format, stage, commit, push, deploy, activate a provider, ingest a private source, or write externally. This file is Halyna's only repository write.

## Release-blocking findings

### P1 — The active admission policy is not projected from the canonical Knowledge Case roles and states

`project/architecture/run-profiles.yaml:21-32` defines ten active generic role IDs such as `architecture_engineer`, `documentation_maker`, `evidence_reviewer`, `retrieval_engineer`, and `codex_integrator`. Its active profile packs use those IDs at `project/architecture/run-profiles.yaml:45-52`. They do not resolve through the canonical 21-role catalog, which uses Ukrainian call names and stable IDs such as Yaromyr / `goal_and_architecture_operator`, Solomiia / `source_and_context_operator`, Halyna / `independent_reviewer`, and Maksym / `integrator`.

The same active admission projection introduces another state vocabulary at `project/architecture/run-profiles.yaml:35-52` and `project/architecture/e1-e8-role-state-matrix.md:14,21-41`, including `admission_validated`, `cag_bound`, `architecture_admission`, and profile-specific review gates. Those values are not in `project/system/contracts/operating-model.json`. The public case schema cannot fail closed on this drift because `project/system/schemas/knowledge-case.schema.json:11` accepts any string as `workflow_state`. The mandatory CAG reference is also an unfinished older contract—`project/runs/20260729-architecture-enforcement/task-contract.md:3,20-27`—whose role lanes remain generic and unmapped.

Consequence: the repository presents one canonical employee crew in its README/dashboard while its active mandatory admission plane selects a different role catalog and state language. This fails the one-system invariant and acceptance criteria 1, 2, 3, and 10.

Required repair:

1. Make every active run-profile role reference a canonical role ID and expose its Ukrainian call name; if a profile label is useful, keep it as a capability label, not another agent identity.
2. Express admission as L1 transitions/receipts within the canonical state registry, or publish an explicit namespaced projection with a deterministic mapping to canonical states. No second unqualified `workflow_state` vocabulary may remain.
3. Supersede or complete the July `in progress` contract and point the required CAG set to one current architecture contract.
4. Constrain `workflow_state` to the canonical registry or add a validator that proves schema/model equality.
5. Extend deterministic validation to reject unknown run-profile roles, call-name drift, and unknown profile states.

### P1 — The LlamaIndex workflow still publishes unsupported TurboVec evidence

The repaired canonical JSON and strategic document correctly limit the public receipt to ten queries, 9/9 checks, candidate recall@3 1.00, MRR 0.8167, and an unpublished lexical baseline. However, `project/workflows/llamaindex-rag.yaml:103-108` still asserts `documents: 12` and `lexical_recall_at_3: 0.6`.

Consequence: two current runtime contracts disagree about the same evidence. `project/system/validate_system.py:165-178` validates only the canonical JSON, while the workflow validator checks YAML shape but not equality with that JSON, so both validators can pass this contradiction. This fails acceptance criteria 3, 4, and 10.

Required repair: replace the YAML evidence block with the calibrated public-receipt fields, cite the receipt path, and add a cross-contract assertion that the workflow projection cannot introduce unmatched metric or fixture claims.

### P1 — The accepted role contract is not complete enough to prove inputs, skills, and reviewer routes per role

The catalog correctly provides 21 unique call names, stable IDs, owned responsibilities, and forbidden actions. Most entries in `project/system/contracts/role-catalog.json:17-168`, however, do not declare role inputs, output contract, allowed skill references, reviewer route, or handoff. Only Oksana has an explicit `reviewer` at `project/system/contracts/role-catalog.json:40-46`. The CrewAI task template at `project/workflows/crewai-crew.yaml:162-175` requires sources, requirements, tools, reviewer, and handoff, but omits allowed skills and is not materialized per selected role. The Team projection at `project/dashboard/app.js:419-420` displays only purpose, ownership, and prohibitions.

Consequence: the narrative says each role receives inputs, outputs, tools/skills, reviewer, and handoff, but the machine and dashboard surfaces cannot reproduce that accepted contract. Workflow-pack inputs and outputs are shared pack fields, not responsibility-specific bindings. This fails acceptance criterion 2 and weakens the employee-onboarding goal.

Required repair: add a schema-validated adaptive role-task projection that binds, for every selected role, its inputs, owned output, allowed skill/tool references, permission boundary, reviewer route, and handoff. It may remain case-specific rather than hard-coded, but the public contracts, validator, and Team/Work projection must expose and prove it. Include `allowed_skills` in the CrewAI-compatible task contract.

### P2 — Configuration import coerces an invalid TurboVec type into an enabled proposal

`project/dashboard/app.js:603` uses `Boolean(next.turbovec_candidate)`. A JSON value of the string `"false"` therefore imports as boolean `true`; the independent negative browser check returned `string_false_imported_as=true`. The packet remains browser-local and cannot execute, so this is not a provider or external-action defect, but it is an incorrect validated configuration result.

Required repair: require the field to be a JSON boolean and reject other types. Add negative import fixtures for string/number/object values and preserve the existing size, unknown-field, numeric-range, checkpointer, and bridge-origin checks.

### P2 — The active run packet does not exactly describe its role and intended Git scope

The context capsule identifies `created_by` and the integrator role as `Codex integrator` at `project/runs/20260805-responsive-knowledge-crew-dashboard/context-capsule.json:5,75`, while the canonical call name is Maksym / `integrator`. Its exact `allowed_files` list at `context-capsule.json:44-60` includes `wiki/runs/` and `wiki/log.md` but omits the modified durable files `wiki/memory.md:329` and `wiki/insights.md:219,227`.

Consequence: the changes may be substantively appropriate under the post-run memory policy, but the frozen admission/scope packet does not authorize or name them. Acceptance criteria 2 and 11 require the packet, intended staging set, and canonical role trace to agree.

Required repair: name Maksym / `integrator`, add the two exact WikiLLM files to the admitted scope with the reason they pass the strict memory/insight filters, or exclude their diffs. Then regenerate/read back the public-safe run packet before staging.

## Iryna repair table

| Iryna finding | Repair state | Halyna evidence |
|---|---|---|
| Final review assigned to Iryna instead of Halyna | **REPAIRED** | `task-contract.md:36`, `agent-handout.md:25-27`, and `execution-report.md:40-42` now keep Iryna as action/contract validator and Halyna as independent reviewer. |
| Optional LangGraph smoke used noncanonical states and role | **REPAIRED FOR THAT SCRIPT** | `project/scripts/langgraph-smoke-run.py` now loads the canonical model, catalog, and fixture; checks registered roles/states; covers eligible, blocked, repair, approval wait, review, readback, and zero action. The separate active admission-policy drift is a new system-level finding above. |
| Canonical dashboard contract had nine routes while product had six | **REPAIRED** | `knowledge-crew-config.json` and `validate_system.py:210-212` now require `today`, `work`, `knowledge`, `team`, `review`, and `setup`; all six render. |
| TurboVec exact numbers lacked a matching public receipt | **NOT FULLY REPAIRED** | Canonical JSON, dashboard data, docs, and run notes are calibrated, but `project/workflows/llamaindex-rag.yaml:103-108` retains the unmatched 12-document and lexical-0.6 values. |
| README linked a missing license | **REPAIRED** | The broken link is gone; `README.md:195` explicitly states that no software license grant exists yet. |
| Old two-screen Jarvis manual looked current | **REPAIRED** | `docs/dashboard-local-jarvis-stack-manual.md:1-5` is clearly historical/superseded and links to the current manual. |
| Landing tower used generic layer vocabulary | **REPAIRED** | `site.js` projects the exact L1-L7 names; 28 layer/viewport checks passed. |
| Candidate failed diff hygiene | **REPAIRED** | `git diff --check` passes with no trailing whitespace. |

## Acceptance table

| # | Acceptance criterion | Verdict | Evidence |
|---:|---|---|---|
| 1 | One case/state spine | **REVISE** | Product contracts use one Knowledge Case, but the active admission policy retains a second unqualified role/state plane. |
| 2 | Named role responsibility contracts | **REVISE** | Twenty-one unique Ukrainian call names and ownership/prohibitions pass; active profiles use generic IDs and the adaptive role-task packet lacks explicit skill/input/reviewer bindings. |
| 3 | Non-overlapping framework jobs and truthful states | **REVISE** | Framework boundaries are strategically clear; active admission and LlamaIndex/TurboVec workflow projections drift from canonical contracts. |
| 4 | Bounded perception and calibrated TurboVec | **REVISE** | The 12,000-token capsule, exact reads, filters, lexical fallback, and promotion gate are sound; one YAML projection retains unsupported evidence. |
| 5 | Adaptive research and specialist methods | **PASS** | Ten packs preserve onboarding, requirements/market/pain/PRD, tasking, outreach, content, design, implementation, reporting, knowledge, and release. |
| 6 | Skill cleaning and update lifecycle | **PASS** | Discover-to-remove lifecycle, static/semantic distinction, Skill Spectre evidence, and Video Spectre pattern are explicit and calibrated. |
| 7 | Four precise source-controlled diagrams | **PASS** | Four SVG/PNG pairs parse, remain editable, are linked from README, and visibly explain architecture, perception, outputs/receipts, and onboarding/teamwork. |
| 8 | Responsive non-technical dashboard | **PASS** | Six routes pass at 320, 390, 768, and 1440 pixels with no page overflow, duplicate IDs, unlabeled controls, hidden truth state, or route errors. Forms wrap and remain keyboard-visible. |
| 9 | Public-safe configuration import/export | **REVISE** | Local-only boundary and remote-origin rejection pass; invalid TurboVec string values are coerced instead of rejected. A real authenticated bridge remains intentionally absent. |
| 10 | Deterministic, browser, safety, and independent evidence | **REVISE** | Core/browser/safety evidence passes, but cross-contract validators miss the active role/state and TurboVec drift. Optional framework runtime remains an explicit GAP. |
| 11 | Exact Git release readiness | **REVISE** | Candidate is intentionally unstaged/uncommitted/unpushed, and the context capsule does not yet match the full intended WikiLLM staging scope. |

## Checks run

- `python3 -B project/system/validate_system.py` — PASS; one eligible proposal, four blocked/rejected adversarial proposals, all `executed: false`.
- `python3 -B project/scripts/dashboard-static-smoke.py --skip-browser` — PASS.
- Full six-route headless dashboard smoke — PASS for Today, Work, Knowledge, Team, Review, and Set up.
- Independent Playwright dashboard matrix — PASS, 24 route/viewport combinations at 320, 390, 768, and 1440 pixels; no overflow, duplicate IDs, unlabeled controls, nav escape, page errors, or missing truth labels.
- Independent landing-layer matrix — PASS, 28 layer/viewport combinations with exact L1-L7 copy and containment.
- Valid loopback configuration import and arbitrary remote bridge rejection — PASS.
- Negative TurboVec type import (`"false"`) — FAIL; imported as `true`.
- `node --check project/dashboard/app.js` and `node --check site.js` — PASS.
- `python3 -B scripts/public_safety_scan.py` — PASS.
- `python3 -B project/scripts/pre-push-runtime-guard.py` — PASS for mandatory public core; optional framework runtime not requested.
- Project-local Pydantic workflow validation — PASS for the current YAML files as structural documents.
- Independent JSON parse, YAML parse, seven SVG/XML parses, and four PNG dimension/integrity checks — PASS.
- Visual readback of all four new diagrams plus mobile dashboard and 320/1440 landing screenshots — PASS for legibility, hierarchy, direction, and containment.
- Changed-Markdown relative-link check — PASS.
- `git diff --check` — PASS.
- Canonical CrewAI agent IDs versus role catalog — PASS, 21/21.
- Active admission profile IDs versus role catalog — FAIL; generic role plane remains.
- Workflow YAML evidence versus canonical TurboVec receipt — FAIL on 12-document and lexical-0.6 residue.
- Git staging, staged-snapshot checks, commit, push, and remote-hash readback — not performed by this reviewer.

## Calibrated gaps

- The inherited optional LangGraph/LlamaIndex/CrewAI environment is not runtime proof. Prior bounded imports stalled in the LangSmith/LlamaIndex dependency chain; this review did not wait on or relabel that known GAP.
- TurboVec remains `optional_trial_not_default`. The representative 20-query paired promotion gate, lexical comparison, citation/filter/persistence proof, and independent promotion verdict have not passed.
- Live private Obsidian/Orbit state, Graphify freshness, private retrieval, SQLite/PostgreSQL recovery, shared identity, provider execution, deployment, and external writeback are not proved by this public clone.
- The dashboard proposes a local bridge but does not call or authenticate one; that is an intentional public boundary.
- Employee comprehension and operational improvement remain hypotheses until a representative onboarding pilot.
- No software license grant exists. The README now states this accurately; the owner must choose any future license.
- Git release and remote readback remain pending and must occur only after a fresh approval verdict.

## Role-by-role knowledge trace

**Solomiia — context-spine designer.** Solomiia saved the one-case evidence trace, source identity, framework seams, 12,000-token perception budget, exact-read requirement, and runtime gaps in `lanes/solomiia-context-spine.md`. Those conclusions are present in the canonical perception contract; this review preserves her warning that compact retrieval cannot replace provenance or current requirements.

**Taras — employee mission and onboarding designer.** Taras saved the first-thirty-minute journey, mission card, daily support, escalation, handoff, and employee outcome measures in `lanes/taras-employee-mission.md`. Today, Work, and the onboarding workflow reflect that knowledge. The remaining role-binding finding asks the machine contract to become as explicit as this human design.

**Kateryna — Crew Desk product designer.** Kateryna saved the case-first studio, configuration surface, responsive containment, accessibility requirements, receipts, and contextual-operator direction in `lanes/kateryna-crew-studio.md`. Six routes, mobile containment, form alignment, local import/export, and non-authoritative Taras guidance pass independent visual and browser review.

**Maksym — integrator and maker.** Maksym reconciled the alternatives into seven layers, 21 roles, ten workflow packs, typed fixtures, framework contracts, four diagrams, documentation, Crew Desk, and verification evidence. The canonical role/state, TurboVec projection, role-task completeness, import typing, and scope-packet repairs remain maker responsibilities; Halyna made none of them.

**Iryna — action and contract validator.** Iryna's read-only REVISE packet exposed the first reviewer-binding, optional smoke, route, evidence, manual, landing, link, and hygiene defects. Seven of eight are fully repaired; the TurboVec evidence finding remains open in one current YAML projection.

**Halyna — independent reviewer.** Halyna independently reran the bounded core, browser, responsive, visual, parsing, link, safety, diff, configuration, and cross-contract checks. She saved this REVISE verdict without changing maker output and added exact repair evidence for the still-divergent admission plane, role-task contract, imported boolean, and admitted Git scope.

## Skills and methods evidenced

`codebase-design` shaped the canonical seams; `design-an-interface` produced three alternatives; `dispatching-parallel-agents` preserved exclusive maker lanes; `imagegen` supplied art bases while exact labels remain in SVG; `browser-qa-performance-a11y` drove the 24-route and 28-layer matrices; and `task-handout` preserved role, evidence, gap, and next-action lineage. Review methods included source-authority triage, cross-contract comparison, negative fixture testing, maker/reviewer separation, visual readback, and FACT / INTERPRETATION / HYPOTHESIS / GAP calibration.

## Exact next safe action

1. Maksym repairs all P1/P2 findings in one bounded maker pass: canonicalize/map the admission roles and states; complete or supersede the July contract; enforce schema/profile/workflow cross-contract validation; calibrate the LlamaIndex TurboVec evidence; materialize role input/output/skill/reviewer/handoff bindings; reject non-boolean TurboVec imports; and align the context capsule with Maksym and the exact WikiLLM scope.
2. Rerun the deterministic core, workflow cross-checks, JSON/YAML/SVG/image/link checks, public safety, diff hygiene, six-route browser smoke, 24 route/viewport matrix, 28 landing-layer matrix, and negative import fixtures.
3. Freeze the repaired candidate and dispatch Halyna for a fresh review-only verdict. Do not overwrite this report; record the next verdict as a separate review iteration or clearly append an immutable re-review section.
4. Only after APPROVE: stage only admitted files, rerun the suite against the staged snapshot, commit, perform the owner-authorized Git push, and read back the exact remote hash.

Do not deploy, activate providers, ingest private sources, connect live Obsidian/Orbit, promote TurboVec, or perform any non-Git external writeback in this repair.
