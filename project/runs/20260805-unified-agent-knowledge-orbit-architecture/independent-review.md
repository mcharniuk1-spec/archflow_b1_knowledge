# Independent Architecture Review

Date: 2026-08-05
Lane: independent reviewer
Verdict: **APPROVE after bounded repairs and final target/reviewer re-review**
Release state: **architecture candidate approved; exact staging and clean-snapshot public-safety checks remain release-operator conditions**

## Scope reviewed

I reviewed the admitted task contract and receipt, all three maker lane reports, the new unified public documentation, public machine contracts and fixtures, layered visuals, dashboard plan, executed-role trace, narrow README/architecture changes, private system-role and boundary changes, and the configured Orbit/Obsidian seam. I did not edit any maker artifact, dashboard file, private configuration, or shared communication record.

The architectural direction is accepted: one governed Knowledge Case Controller replaces the numbered top-level split; PRD, ICP, and market research are projections produced by the bounded `requirements_and_market_research` role; onboarding answers become action proposals; and designer, qualification, copy, review, integration, release, and knowledge-promotion responsibilities remain separated. The public/private narrative is appropriately local-first and claim-calibrated in most places. The current implementation proof is not yet reliable enough to approve.

## Blocking findings

### [P1] The action validator trusts the proposal it is supposed to validate

In `project/system/validate_system.py:58-92`, authority is accepted whenever the proposal supplies `permission_scope.status: allowed`; approval is required only when the proposal itself supplies `approval.required: true`; actor role membership, actor-to-case assignment, target class, operation, case allowed/forbidden actions, coverage contents, decisions, side-effect class, and the external-action policy are not derived or cross-checked. Self-review is rejected only when the proposal labels itself `high` risk.

A focused adversarial test changed the nominal eligible fixture to an external send by an unregistered actor, used the same actor as maker and reviewer, self-declared permission as allowed, and self-declared approval as not required. `evaluate()` returned:

```json
{"verdict":"eligible","reasons":[],"executed":false}
```

This violates the central requirement that employee actions be validated against reviewed requirements and role authority. Repair must derive authority and approval class from the case and target policy, reject unknown or mismatched roles, force independent review and target-specific approval for external/high-risk classes, validate coverage against current requirements and decisions, and add this adversarial case as a permanent negative fixture.

### [P1] The schemas and validator do not enforce the advertised knowledge lineage

`project/system/schemas/knowledge-case.schema.json:6-30` does not require evidence, contradictions, gaps, source references, evidence owner/freshness, requirement review state, approval receipts, or result/readback receipts; requirement and evidence items have no enforced shape. `action-proposal.schema.json:6-26` similarly leaves nested target, permission, review, approval, coverage, and verification values largely unconstrained. Both allow arbitrary additional properties.

The validator never loads or applies either schema, yet `project/system/README.md:20` says it validates the schemas and `docs/unified-operating-architecture.md:94` says it proves schema integrity. The fixed fixtures parsing is useful but does not establish those claims or acceptance criterion 4. Repair must validate the schemas themselves, enforce the required lineage/currentness/authority/receipt fields and enumerations, cross-check role and state references, and add malformed/nested negative cases. Until then, the proof language must say only what the script actually checks.

### [P1] Orbit does not fail closed on a stale index or an additional corpus

The private constrained wrapper correctly exposes only `orbit_status` and `orbit_repo_map`; direct MCP testing confirmed that raw SQL and corpus-changing `index` are absent, and parent traversal is rejected. The current database lists only the approved public code corpus, and no vault corpus is present.

However, the wrapper's `status()` filters for one approved match but does not require the complete database list to contain exactly one entry. A database containing the approved corpus plus a second repository would still pass. `repo_map()` does not call the corpus/freshness check, compare the indexed snapshot with current repository state, or return the required `snapshot` and `freshness_state`. The current index identifies the base commit while the architecture candidate exists as later worktree changes, so a structural answer can be stale without being blocked.

Repair must require exactly one database corpus and exact resolved-root equality, verify the indexed commit plus an explicit dirty/index snapshot policy before every map operation, return snapshot/freshness metadata, block stale or ambiguous state, and negative-test a second-corpus manifest. Re-index and re-run the proof after the final architecture commit. The database and binary also need an effective local-ignore/retention rule; the current private ignore patterns do not cover the DuckDB suffix or the installed runtime binary.

## Required non-blocking repairs

### [P2] The machine role catalog is not the complete executed-role map it claims to be

The architecture audit classifies `goal_and_architecture_operator` and `surface_projection_operator` as executed roles, but they are absent from `project/system/contracts/role-catalog.json`. The private contracts also use different names for source/context, independent review, and knowledge promotion without an alias/projection map. Add the executed roles or explicitly document why they are projections of another canonical role, and add stable public/private aliases. Keep the planned packaging role marked planned rather than executed.

### [P2] The onboarding diagram merges the failure and promotion paths visually

The SVG is readable, high-contrast, versioned, and contains accessible `title`/`desc` text. In the rendered onboarding flow, the red validation-failure path passes through/behind the `REVIEWED KNOWLEDGE` box before reaching `REPAIR · ESCALATE`. This visually implies that failed validation may enter reviewed knowledge. Route failure directly to repair/block and reserve the teal result path for promotion. The unified seven-layer diagram and conceptual cover otherwise passed focused visual review.

### [P2] Live-client and release-state claims need final calibration

The Obsidian-vault configurations preserve Nexus, the constrained MCP process passed initialize/list/status/map calls, the fixed-corpus ArchFlow Orbit contract is the active `orbit` skill, and the untouched upstream package is now in a non-active reference area. This resolves the unsafe-skill-selection concern. The Obsidian/Cursor client has not yet been reloaded and proved through its live tool list, so describe the seam as configured and directly proven—not fully live—until that readback passes. The missing owner attachment keeps the GitLab Orbit identity at the documented 0.80 confidence.

`project/system/README.md` calls the contract reviewed and `docs/architecture.md` calls the model canonical before this review has passed. Keep status at candidate/revise until the blocking repairs and re-review complete.

Generated `__pycache__` files are present under the new public system and private integration folders. Exclude/remove them from the intended commit and preserve only source artifacts.

## Checks and evidence

| Check | Result |
|---|---|
| Deterministic architecture admission | PASS; provider disabled, no task/provider/external dispatch |
| JSON parse for contracts, schemas, fixtures | PASS |
| Python syntax for public validator and private wrapper | PASS |
| Nominal eligible and blocked fixtures | PASS, but insufficient because the authority-spoof adversarial test returned eligible |
| MCP initialize and tool list | PASS; exactly status and bounded repo-map tools |
| MCP status and overview | PASS for the current single public corpus |
| MCP parent traversal denial | PASS |
| Raw SQL and MCP index denial | PASS at exposed tool surface |
| No-vault-index promise | PASS for current database contents and active skill contract |
| Obsidian/Cursor config readback | PASS; live client reload/tool-list proof pending |
| Local Markdown/image links across reviewed entry docs | PASS; 9 documents, 0 missing targets |
| SVG XML and accessibility metadata | PASS |
| Full-aspect visual render | REVISE onboarding failure-path routing; other visuals pass |
| Dashboard implementation | PASS for this lane: plan only; existing dashboard worktree changes were pre-existing and unclaimed |
| Target-only public-safety scan | PASS; 27 intended source/artifact files, 0 findings |
| Repository-wide public-safety scan | FAIL from seven pre-existing findings in unrelated untracked/modified artifacts and the shared log; no target-file finding |
| Intended Git staging/push | Not yet performed; exact staged-set proof remains required |

## Public-safety and worktree note

The new public candidate sources contain no detected local absolute path, owner token, private URL scheme, credential pattern, operational UUID, or checked Cyrillic private term. The repository-wide scanner still sees unrelated pre-existing worktree material that is not part of this run. Do not clean, stage, or commit that material. Build an exact intended index, run the authoritative scanner against a clean staged snapshot, verify dashboard and unrelated files are absent, then commit and push only after re-review approval.

## Residual gaps after repair

- The owner-referenced Orbit attachment is absent; product identity remains a transparent assumption, not a closed fact.
- Orbit Local and its MCP surface are beta/experimental; pinning, schema drift checks, and upgrade re-verification remain mandatory.
- The public proof is intentionally synthetic, provider-disabled, and writeback-disabled. It does not prove a live employee agent, hosted runtime, production model quality, external action, or dashboard migration.
- A real onboarding/action case still needs operational proof combining reviewed prose, exact source read, current Orbit evidence, Graphify comparison, reviewer acceptance, and sanitized knowledge readback.

## Next safe actions

1. Repair the validator and schemas; add the authority-spoof and malformed-lineage negative fixtures.
2. Harden Orbit single-corpus and freshness checks; re-index after the final commit and prove stale/second-corpus denial.
3. Complete the role alias/catalog and diagram repair; remove generated bytecode from the intended set.
4. Reload the client and capture a sanitized live tool-list/status readback, or leave the integration explicitly configured-but-reload-pending.
5. Request independent re-review. Only an `APPROVE` verdict may unlock exact staging, clean-snapshot safety scan, commit, and owner-authorized push.

---

## Repair Re-review — 2026-08-05

Final re-review verdict: **REVISE**
Release state: **one authority-boundary blocker remains; do not push as approved**

### Repairs accepted

- **Unknown/external authority spoof:** repaired. The permanent unknown-sender fixture is blocked for unknown actor/reviewer, absent allowlist authority, self-review, approval-policy mismatch, and missing target-specific approval.
- **Schema application and nested lineage:** substantially repaired. The standard-library validator now checks its supported schema vocabulary, applies both schemas, validates registered states/roles and requirement/evidence references, rejects additional nested properties, and permanently rejects a malformed proposal fixture. Public proof claims now match the checks performed.
- **Role catalog:** repaired. The executed architecture and surface-projection roles are present, private/public aliases resolve to canonical roles, and the packaging role is explicitly marked planned.
- **Orbit corpus and freshness:** repaired for the tested profile. The wrapper requires exactly one exact corpus, clean snapshot state, matching indexed commit, and matching SHA-256 digest over the explicit public-code allowlist before both status and map operations. Focused tests reject second/wrong corpora, failed state, stale hashes, and parent traversal. Map output includes snapshot and freshness metadata. Raw SQL and `index` remain absent.
- **Orbit skill and Obsidian seam:** repaired/configured. The fixed-corpus ArchFlow contract remains the only active `orbit` skill; upstream guidance is non-active reference material. Client reload/live discovery remains explicitly pending rather than overstated.
- **Visual routing:** repaired. The red validation-failure line now reaches `REPAIR · ESCALATE` directly and no longer crosses the reviewed-knowledge node. SVG accessibility metadata and full diagram clarity remain acceptable.
- **Claim calibration and hygiene:** repaired. Architecture status remains candidate pending review. Generated bytecode is ignored and is not an intended Git artifact; private Orbit binary/corpus/DuckDB paths have explicit local ignore rules.

### Remaining blocking finding

#### [P1] Exact target and assigned reviewer are still not bound to case authority

The repaired evaluator correctly derives operation/target-class authority from `case.authority.allowed_actions`, but it does not validate the exact `target.ref` against that target class or a permitted path boundary. A focused mutation kept `target.class: public_documentation` and the allowed `propose_edit` operation but changed `target.ref` to a parent-traversing private target. Schema validation accepted it and `evaluate()` returned:

```json
{"verdict":"eligible","reasons":[],"executed":false}
```

The evaluator also does not bind `proposal.review.reviewer_role` to the reviewer assigned by the case. Replacing the eligible fixture's independent reviewer with its maker while retaining `risk: low` also returned eligible. This bypasses the case packet's explicit reviewer authority and makes the proposal's self-declared risk label control separation.

Repair must add class-specific exact-target validation (at minimum reject absolute paths, parent traversal, and references outside the declared public-documentation root), derive the reviewer from the case or an explicit case reviewer allowlist, and reject maker/reviewer equality whenever the admitted case requires separation. Add both mutations as permanent negative fixtures. This is a bounded repair; the rest of the re-reviewed architecture does not need redesign.

### Re-review checks

| Check | Result |
|---|---|
| Public schema-definition/application proof | PASS |
| Eligible, stale external, and unknown-authority fixtures | PASS |
| Malformed nested proposal | PASS; rejected |
| Parent-traversing exact-target mutation | **FAIL; returned eligible** |
| Low-risk case-reviewer replacement mutation | **FAIL; returned eligible** |
| Orbit single/exact corpus tests | PASS |
| Orbit source/snapshot freshness tests and live bounded map | PASS |
| Orbit traversal denial and exposed-tool boundary | PASS |
| Executed-role and alias coverage | PASS |
| Repaired onboarding SVG structure | PASS |
| Target-only public-safety scan | PASS; 32 intended files, 0 findings |
| Intended bytecode handling | PASS; generated files are ignored, not intended artifacts |

### Final next safe action

Repair only the exact-target and case-reviewer binding, add the two adversarial fixtures, and request one focused re-review. If both mutations then block and the exact staged-set safety scan passes, this review can advance to `APPROVE` without reopening the accepted architecture, Orbit, role, documentation, or visual work.

---

## Final Target/Reviewer Re-review — 2026-08-05

Final verdict: **APPROVE**

The last authority-boundary repair passes. The public case contract now carries explicit target prefixes; the evaluator derives maker and reviewer from the admitted case, rejects maker/reviewer equality independently of the proposal's risk label, and fails closed on absolute paths, backslashes, parent traversal, and repository-relative targets outside the allowed prefix.

### Focused proof

| Test | Result |
|---|---|
| Provider-disabled five-proposal validator | PASS |
| Permanent target-escape fixture | PASS; schema rejects it and evaluator returns `TARGET_REF_INVALID` |
| Permanent reviewer-spoof fixture | PASS; returns `CASE_REVIEWER_MISMATCH` and `SELF_REVIEW_FOR_CASE` |
| Direct parent-traversal mutation | PASS; blocked |
| Direct absolute-path mutation | PASS; blocked |
| Direct backslash-path mutation | PASS; blocked |
| Direct outside-prefix mutation | PASS; returns `TARGET_OUTSIDE_ALLOWED_PREFIX` |
| Direct low-risk self-review mutation | PASS; blocked by case reviewer binding |
| Malformed nested proposal | PASS; rejected |
| Orbit refreshed snapshot, single-corpus, freshness, map metadata, and traversal suite | PASS |
| Target-only public-safety scan | PASS; 34 intended files, 0 findings |

### Approval scope and release conditions

This approval covers the unified architecture, public machine contracts and provider-disabled fixtures, normalized roles and historical role trace, private/public seam, constrained Orbit/Obsidian configuration, documentation, and architecture visuals. Dashboard implementation remains plan-only and is not approved or claimed by this run.

The release operator must still stage only this run's intended files, exclude ignored bytecode and every unrelated pre-existing worktree change, run the authoritative public-safety scan against a clean staged snapshot, inspect the staged diff, and then use the owner's already-recorded Git-push authorization. A failure in that staged release proof reopens the release gate, not the approved architecture.

The disclosed residual gaps remain correctly bounded: the missing owner attachment leaves the GitLab Orbit identity at stated confidence; the Obsidian/Cursor client reload and live discovery are pending; Orbit is beta; and the public proof is synthetic, provider-disabled, and writeback-disabled. None is represented as production or live-agent proof.
