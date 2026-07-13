# Implementation Plan

Status: approval-gated

## Phase 0 - Secure authorization and freeze scope

1. Confirm the private-domain location.
2. Confirm whether a persistent model-disabled local monitor may be installed and started.
3. Confirm whether TurboVec may be installed into the isolated project runtime for a sanitized benchmark.
4. Confirm whether the strategic-system coordination registry may be updated for parallel lanes.
5. Recheck active public file claims and preserve all unrelated changes.

Exit gate: explicit owner approval recorded; no conflicting file claims.

## Phase 1 - Preserve the previous setup

1. Create a timestamped private history snapshot.
2. Copy the current root, public, Claude, Cursor, hook, architecture, workflow, source-boundary, goal, loop, and role routing files without modifying the originals.
3. Write a manifest with file hashes, snapshot time, restore order, and verification commands.
4. Test a non-destructive restore comparison.

Exit gate: complete manifest and hash verification.

## Phase 2 - Establish private/public domains

1. Create the sibling private ArchFlow layer with separate `raw`, `knowledge`, `indexes`, `runtime`, `runs`, `issues`, `decisions`, and `history` zones.
2. Define visibility metadata: `public`, `private`, `restricted`, and `promotion_candidate`.
3. Keep the public repository executable and testable without the private layer.
4. Create a one-way promotion packet that emits only reviewed sanitized summaries with source lineage.

Exit gate: boundary fixtures reject private paths and public operation passes with the private layer absent.

## Phase 3 - Prompt and agent routing

1. Keep `AGENTS.md`, Claude routing, and Cursor rules compact.
2. Route substantial behavior to one detailed private operating contract plus the public contract for public work.
3. Add a routing-only prompt hook that announces required preflight, state classification, task handout, and approval gates without storing raw prompts.
4. Add deterministic preflight and instruction-drift validation.

Exit gate: syntax, routing, no-secret, and rollback checks pass.

## Phase 4 - Executable LangGraph state controller

1. Implement typed goal/task/runtime state.
2. Add durable local SQLite checkpoints and stable thread IDs.
3. Add fan-out only for independent bounded tasks; use reducers for merged state.
4. Add owner interrupts before installs, persistent-service changes, provider calls, data promotion, or external writeback.
5. Emit a sanitized heartbeat and state summary.
6. Run pause/resume, crash/restart, retry-cap, kill-switch, and conflicting-branch fixtures.

Exit gate: model-disabled fixtures pass and state can resume after restart.

## Phase 5 - LlamaIndex and TurboVec trial

1. Preserve the current lexical baseline.
2. Fix a local embedding model, dimension, chunk schema, and stable IDs.
3. Install a pinned TurboVec release only in the isolated runtime.
4. Use the official LlamaIndex adapter with metadata filters and local ignored persistence.
5. Run the existing 20-query set plus private-boundary rejection cases.
6. Compare retrieval quality, provenance, latency, index size, update time, deletion, and fallback behavior.

Exit gate: no critical safety or provenance regression and a measurable benefit. Otherwise revert to the baseline and classify TurboVec as deferred.

## Phase 6 - Parallel execution and continuous monitoring

1. Register one integrator, bounded worker lanes, and an independent reviewer.
2. Enforce one shared-file writer.
3. Run a model-disabled parallel branch fixture and merge review.
4. If separately approved, install a local persistent monitor with explicit start/stop/uninstall and retention controls.
5. Keep Codex execution interactive and approval-bound; the monitor may queue and report tasks but must not impersonate an always-on Codex endpoint.

Exit gate: heartbeat, state, recovery, coordination, and stop controls are verified.

## Phase 7 - Promotion and closeout

1. Update instructions only after the runtime and boundary checks pass.
2. Regenerate affected public derived data only after active lane handoff.
3. Run workflow validation, public-safety scan, diff hygiene, benchmark, and independent review.
4. Record decisions, issues, run notes, handouts, rollback, and remaining gaps.
5. Do not deploy, push, activate providers, or write externally without action-specific approval.

## Proof wording

- `documented`: contract exists.
- `configured`: files parse and point to the intended component.
- `fixture-proven`: bounded deterministic test passed.
- `runtime-active`: process and health proof exist now.
- `continuous`: persistence, heartbeat, restart, and monitoring proof exist across a defined observation window.
- `production-ready`: security, auth, storage, recovery, budget, deployment, and owner acceptance gates passed.
