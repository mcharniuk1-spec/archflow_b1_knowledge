# Bounded Loop Contract

Every loop is a task-local projection of `project/database/run-envelope.schema.json`; it is not a second state machine. The default public core prepares and reviews local artifacts with providers and external writes disabled.

## Levels

| Level | Meaning | Default |
|---|---|---|
| L0 | One draft with no governed mutation | Allowed for low-risk exploration |
| L1 | Report-only loop with state, review, and handoff | Default |
| L2 | Exact local file changes after admission and file claim | Allowed when the task authorizes implementation |
| L3 | Persistent or unattended execution | Disabled until separately implemented and approved |

## Required state

Each loop records the case and task IDs, approved source references, experience phase, lifecycle state and revision, immutable contract hashes, attempt counters, maker and reviewer roles, exact read/write targets, unsupported claims, gaps, approval state, failure signature, evidence delta, memory decision, blocked reason, and next safe action.

## Attempt and review rules

- Maximum revision loops: 2.
- Maximum attempts per item: 3.
- Maximum independent branches: 3.
- Stop immediately on a source-boundary or authority failure.
- Stop after the same failure repeats twice without new evidence.
- A changed contract hash creates a new revision; stale state is not resumed.
- A high-risk maker cannot be the independent reviewer.

The `admission_controller` selects the route. Makers produce only their owned candidate. The `action_validator` checks eligibility, the `verifier` runs readback, and the `independent_reviewer` issues the frozen-candidate verdict. The `integrator` reconciles accepted outputs but does not replace independent review.

## Memory rule

Working state stays in the run envelope or browser session. Reusable meaning may become a solution-memory candidate only with source lineage, reuse and anti-use conditions, freshness, review, and supersession. An exact bounded action uses an append-only action receipt. Retrieval indexes and browser drafts are rebuildable working artifacts, not durable memory.

## Side-effect gate

Provider calls, Git actions, deployments, external messages, shared-system changes, spending, destructive changes, and durable writeback require a separate exact authority check, idempotency or rollback, independent review when risk warrants it, and post-action readback.
