# Independent Release Review — Responsive Knowledge Crew and Crew Desk

Run: `20260805-responsive-knowledge-crew-dashboard`
Review date: 2026-08-05
Reviewer lane: Iryna, review only
Verdict: **REVISE**

No P0 security defect or private-data leak was found. The provider-disabled core, six dashboard routes, responsive containment, four diagrams, public-safety scan, and adversarial proposal fixtures passed. Release approval is withheld because the frozen candidate contains role-authority, canonical-contract, evidence-lineage, documentation, and Git-hygiene inconsistencies.

This reviewer changed no maker artifact. This file is the review lane's only repository output.

## Findings

### P1 — The run assigns independent review to the wrong canonical role

The canonical catalog binds Iryna to `action_validator` and Halyna to `independent_reviewer` in `project/system/contracts/role-catalog.json:91` and `project/system/contracts/role-catalog.json:105`. The run contract instead states that Iryna independently reviews the candidate at `project/runs/20260805-responsive-knowledge-crew-dashboard/task-contract.md:36`; the same expansion appears in `agent-handout.md:25` and `execution-report.md:40`.

Consequence: a release verdict issued under this run contract does not preserve the role identity and authority boundary that the candidate itself declares canonical. This fails acceptance criterion 2 and prevents this report from serving as final release approval.

Required repair: keep Iryna as the action validator, bind the release-review lane to Halyna / `independent_reviewer`, update the run records, and obtain a fresh review-only Halyna verdict after maker repairs.

### P1 — The optional LangGraph smoke can pass an incompatible state model

The canonical state registry is defined at `project/system/contracts/operating-model.json:25`. The optional smoke emits unregistered states including `admitted`, `perceived`, `committed`, `candidate_ready`, `eligible`, `verified`, `reviewed`, `read_back`, and `promotion_reviewed` at `project/scripts/langgraph-smoke-run.py:47`, `:54`, `:66`, `:75`, `:90`, `:97`, `:106`, `:115`, and `:125`. Its fixture also uses the non-catalog role `documentation_maker` at `project/scripts/langgraph-smoke-run.py:183` and `:195`.

Consequence: when optional dependencies are enabled, the script can print `langgraph_smoke=ok` without proving conformance to the canonical Knowledge Case states or role catalog. It also does not exercise the declared interrupt, repair, reducer, or `action_id` behavior.

Required repair: make the smoke consume the canonical model/catalog/fixture, reject unregistered states and roles, and prove at least valid, blocked, repair/approval-wait, review, readback, and no-side-effect routes using the declared identifiers.

### P1 — The canonical dashboard contract still describes nine routes while the product has six

`project/system/contracts/knowledge-crew-config.json:246` defines nine dashboard sections: `home`, `case`, `tasks`, `crew`, `knowledge`, `research`, `reviews`, `receipts`, and `settings`. The validator explicitly enforces that old set at `project/system/validate_system.py:206`. The implemented primary interface defines six routes—`today`, `work`, `knowledge`, `team`, `review`, and `setup`—at `project/dashboard/app.js:8`.

Consequence: the purported canonical configuration and its passing validator disagree with the shipped non-technical surface. Future generators or adapters cannot determine which navigation contract is authoritative.

Required repair: replace the nine-section contract with the six current route IDs, or rename the nine items as non-navigation capabilities and introduce one canonical six-route projection validated against the dashboard.

### P1 — Exact TurboVec trial numbers lack a matching public evidence receipt

The canonical contract publishes a 12-document/10-query trial and recall values of `1.0` and `0.6` at `project/system/contracts/knowledge-crew-config.json:145`; the canonical architecture repeats the 12-document/10-query proof claim at `docs/responsive-knowledge-crew-architecture.md:40`. The available public report records a 10-query synthetic result with recall `1.00` and MRR `0.8167`, but does not support the asserted document count or lexical recall baseline at `project/reports/20260713-secured-runtime-architecture-report.md:104`.

Consequence: the calibrated verdict `optional_trial_not_default` is correct, but some exact performance evidence is not publicly traceable. This weakens acceptance criteria 3, 4, and 10.

Required repair: add a public-safe benchmark receipt containing fixture/query identity, hashes, metric definitions, candidate and lexical results, persistence/filter checks, and verdict, or remove the unmatched exact numbers and cite only the evidence already published.

### P1 — The public adaptability claim links to a license that does not exist

`README.md:197` links to `LICENSE`, but that file is absent. The changed-Markdown link check reports exactly this missing target.

Consequence: the README is broken at release, and a public repository without an explicit license does not reliably grant the reuse/adaptation permissions promised by the product positioning.

Required repair: obtain the owner's license choice and add the matching file, or remove the broken link and explicitly state that reuse rights remain undecided. Do not infer a license.

### P2 — One current-looking manual still teaches the retired two-screen Jarvis model

`docs/dashboard-local-jarvis-stack-manual.md:3` labels itself an operating manual rather than historical/superseded, while `:12` and `:13` present Screen 1 PRD/ICP Flow and Screen 2 Agent Orchestra as current behavior. That conflicts with the canonical six-route Crew Desk and embedded guidance.

Required repair: rewrite it for the current model or mark it `historical — superseded` with a prominent link to `docs/dashboard-operating-manual.md`.

### P2 — The current landing-page tower still uses a second generic layer vocabulary

The public landing page labels its seven architecture steps `Measure`, `Remember`, `Verify`, `Execute`, `Orchestrate`, `Connect`, and `Govern` at `index.html:74`, rather than the seven accountable layer names. This preserves the generic visual vocabulary the owner explicitly asked to replace and creates a second current architecture story beside the README and Crew Desk.

Required repair: project the same L1-L7 accountable layer names and descriptions on the landing page, or clearly demote that component from architecture to a non-authoritative historical/marketing illustration.

### P2 — The candidate fails diff hygiene

`git diff --check` reports trailing whitespace in eight status lines: `docs/dashboard-integration-plan.md:3`, `docs/dashboard-operating-manual.md:3`, `docs/dashboard-role-configuration.md:3`, `docs/index.md:3`, `docs/onboarding-knowledge-agent.md:3`, `docs/unified-operating-architecture.md:3`, `docs/unified-operating-architecture.md:4`, and `project/system/README.md:3`.

Required repair: remove the trailing spaces and require `git diff --check` and `git diff --cached --check` to pass before commit.

## Acceptance table

| Criterion | Verdict | Evidence |
|---|---|---|
| 1. One case/state spine | **REVISE** | Canonical contracts use one case, but the current-looking old manual and landing tower retain competing projections. |
| 2. Twenty-one named responsibility roles | **REVISE** | Twenty-one unique English-letter call names exist and role ownership is explicit; this run misbinds Iryna/Halyna for final review. |
| 3. Non-overlapping framework jobs and truthful parameters | **REVISE** | WikiLLM, Obsidian, LlamaIndex, TurboVec, Orbit/Graphify, CrewAI, LangGraph, and Crew Desk jobs are well separated; TurboVec evidence and optional graph proof need reconciliation. |
| 4. Bounded perception and TurboVec calibration | **REVISE** | The 12,000-token budget, exact reads, metadata, lexical fallback, and promotion gate are solid; exact trial metrics need a public receipt. |
| 5. Prior specialist methods preserved | **PASS** | Ten packs cover onboarding, requirements/market/pain/PRD, tasking, outreach, content, design, implementation, reporting, knowledge, and release. |
| 6. Skill cleaning/update lifecycle | **PASS** | Lifecycle, Skill Spectre limits, and Video Spectre pattern are explicit without claiming unavailable semantic/tool execution. |
| 7. Four precise diagrams | **PASS** | Four SVG/PNG pairs parse and visually show architecture, inputs, outputs/receipts, onboarding/teamwork, captions, and directional connections. |
| 8. Responsive non-technical dashboard | **PASS** | Six rendered routes pass. True 390px measurement showed document width equal to viewport width and all six navigation targets contained; the apparent clipping in the earlier macOS `--window-size=390` image was caused by Chrome's 500px minimum outer window, not page overflow. Forms, labels, wrapping, truth states, and reduced-motion rules are present. |
| 9. Configuration import/export and bridge boundary | **PASS WITH GAP** | Import rejects unknown fields, oversize files, invalid numeric ranges, and remote bridge origins; only same-origin or HTTP loopback is accepted. Packets remain browser-local proposals. A real authenticated bridge is intentionally absent. |
| 10. Deterministic/adversarial/browser/public-safety evidence | **REVISE** | Core, adversarial, six-route render, JSON, SVG, YAML parse, and safety checks pass; optional framework execution is unproved and the LangGraph smoke contract is inconsistent. |
| 11. Exact Git release readiness | **REVISE** | Work remains unstaged/uncommitted/unpushed; diff hygiene and the broken license link fail. Remote readback is pending. |

## Checks run

- `python3 project/system/validate_system.py` — PASS; one eligible proposal, four adversarial proposals blocked/rejected, `executed: false` throughout.
- `node --check project/dashboard/app.js` — PASS.
- `python3 project/scripts/dashboard-static-smoke.py --skip-browser` — PASS.
- `python3 project/scripts/dashboard-static-smoke.py` — PASS for Today, Work, Knowledge, Team, Review, and Set up.
- `python3 project/scripts/pre-push-runtime-guard.py` — PASS for the mandatory standard-library core; optional framework runtime not requested.
- `python3 scripts/public_safety_scan.py` — PASS.
- System JSON parse and all four architecture SVG XML parses — PASS.
- Independent YAML parse for the three current workflow files — PASS.
- True 390px browser box measurement — PASS for page containment and six reachable nav items.
- Changed-Markdown relative-link check — FAIL only for absent `LICENSE`.
- `git diff --check` — FAIL on eight trailing-whitespace lines listed above.
- Git staging, commit, push, and remote-hash readback — not performed by this reviewer.

## Calibrated gaps

- The optional project-local LangGraph/LlamaIndex/CrewAI runtime was not proved in this review. The mandatory guard correctly labels it not requested; prior bounded import attempts are documented as a GAP rather than a pass.
- TurboVec remains an optional trial. The 20-query promotion gate, full citation retention, allowlist filters, persistence parity, and independent verdict have not passed.
- Live Obsidian, Orbit, Graphify freshness, private retrieval, SQLite/PostgreSQL recovery, shared identity, providers, deployment, and writeback are not proved by the public clone.
- Employee comprehension and operational improvement remain hypotheses until a representative onboarding pilot.
- The owner-authorized Git push is still pending and no deployment is authorized by this run.

## Reviewed agents and durable knowledge

**Solomiia — context-spine designer.** Solomiia saved the one-case trace, source identity, framework boundaries, 12,000-token capsule design, exact-read rule, and release-guard gaps in `lanes/solomiia-context-spine.md`. Those conclusions are materially present in the contracts and perception documentation.

**Taras — employee mission and onboarding designer.** Taras saved the first-30-minute path, mission card, daily support, escalation rules, handoffs, and employee outcome measures in `lanes/taras-employee-mission.md`. Those conclusions are visible in Today, Work, and the onboarding pack.

**Kateryna — Crew Desk product designer.** Kateryna saved the configurable studio, source/crew/flow/bridge/receipt model, responsive containment, accessibility requirements, and contextual-operator direction in `lanes/kateryna-crew-studio.md`. The six-route interface and local configuration proposal reflect that work.

**Maksym — integrator and maker.** Maksym reconciled the alternatives into the seven-layer contracts, 21 roles, ten workflow packs, schema/validator, workflow YAML, four diagrams, strategic documentation, Crew Desk, and run evidence. Maker repairs remain his responsibility.

**Iryna — this review lane.** Iryna independently checked the frozen candidate and saved this REVISE verdict without repairing it. Because the canonical catalog reserves independent review for Halyna, this report is a repair packet, not the final release approval.

## Skills evidenced

`codebase-design` shaped the canonical contracts and seams; `design-an-interface` produced three materially different alternatives; `dispatching-parallel-agents` kept exclusive maker lanes; `imagegen` supplied the art bases while SVG retained exact text; `browser-qa-performance-a11y` drove route, viewport, label, wrapping, and overflow checks; and `task-handout` preserved role-by-role evidence, gaps, and next actions.

## Exact next safe action

1. Maksym repairs every P1 and P2 item without widening provider, private-data, deployment, or writeback scope.
2. Rerun the core/adversarial, YAML/JSON/SVG, six-route browser, true 320px/390px responsive, link, public-safety, and diff-hygiene checks.
3. Freeze the repaired candidate and dispatch Halyna / `independent_reviewer` for a fresh review-only verdict.
4. If Halyna approves, stage only intended files, run the same checks against the staged snapshot, commit, perform the already authorized Git push, and read back the exact remote hash.

Do not deploy, activate providers, ingest private sources, connect live Obsidian/Orbit, or perform any non-Git external writeback as part of this repair.
