# Task Contracts

Status: prepared for owner approval; no lanes dispatched

## Shared authority

- The owner approves the private/public boundary, persistent local runtime, package installation, and any write outside the public repository.
- Codex is the lead integrator and only shared-file writer.
- LangGraph owns workflow state after the executable controller passes its model-disabled fixture.
- All provider calls, external writeback, deploys, pushes, and production changes remain disabled.
- Each worker must use public live communication for public-file work and the strategic-system coordination registry when that workspace is involved.
- Each worker receives the minimum corpus and files required for its task.

## Lane 0 - Integrator and approval controller

Role: Terra integrator

Scope:

- Recheck active file claims and dirty state.
- Register all parallel lanes.
- Fix merge order, validate outputs, reconcile contradictions, and own final instruction/runtime changes.

Stop conditions:

- Missing owner approval.
- Overlap with an active file claim.
- Secret/private-boundary finding.
- A third repeated failure in the same task.

## Lane 1 - Instruction history and routing architecture

Role: bounded instruction architect
Mode: read-only until owner approval, then private-layer writer only

Outputs:

- Exact timestamped snapshot of the prior routing/instruction set in the private history layer.
- Compact root routing contract for Codex, Claude, Cursor, and other agents.
- Detailed private operating contract and a sanitized public routing projection.
- Routing-only prompt hook with no raw prompt storage and no external side effects.

Forbidden:

- Replacing public rules with private text.
- Editing global Codex configuration.
- Storing credentials, raw private sources, or personal identifiers in instruction files.

## Lane 2 - LangGraph persistent controller and monitor

Role: orchestration engineer
Mode: model-disabled fixture first

Outputs:

- Typed state schema covering goal, task graph, branch claims, attempts, approvals, evidence, checkpoints, heartbeat, and stop state.
- Durable local SQLite checkpointer and thread-ID policy.
- Interrupt-based owner approval node before any gated action.
- Read-only heartbeat and health packet.
- Explicit start, stop, restart, retention, and rollback runbook.

Forbidden:

- Provider calls, external writes, arbitrary command execution, or automatic Codex authorization reuse.
- Claiming an always-on service before process and heartbeat proof exists.

## Lane 3 - LlamaIndex and TurboVec private/public retrieval

Role: retrieval engineer
Mode: isolated sanitized trial

Outputs:

- Two visibility domains with stable source, document, and chunk IDs.
- Lexical baseline retained for both domains.
- Version-pinned TurboVec adapter trial under LlamaIndex in ignored local storage.
- Metadata and allowlist filters that prevent private-to-public retrieval.
- Persistence, rebuild, deletion, corruption, and fallback tests.
- Paired 20-query benchmark plus size, latency, and provenance metrics.

Forbidden:

- Whole-workspace ingestion.
- Raw private data in the public index or public benchmark report.
- Default promotion if safety, provenance, or retrieval quality regresses.

## Lane 4 - Parallel-agent and state-communication contract

Role: coordination engineer
Mode: docs/config only

Outputs:

- Terra/Luna dependency graph with one writer and bounded read-only workers.
- Public and private communication routing.
- Conflict, claim, handoff, reviewer, and merge-order schemas.
- LangGraph fan-out/fan-in fixture with reducers and bounded branch count.

Forbidden:

- Multiple writers to the same file.
- Unbounded agents, retries, or background tasks.
- Treating an agent/model name as authority.

## Lane 5 - Independent security and benchmark review

Role: independent verifier and safety reviewer
Mode: read-only

Outputs:

- Dependency/provenance/license/security review.
- Public/private leakage fixtures.
- Secret/path and unauthorized-write checks.
- Checkpoint resume, rollback, and failure-recovery review.
- Final adopt, trial, defer, or reject verdict per component.

Forbidden:

- Editing maker outputs during review.
- Approving its own implementation.

## Merge order

1. Approval and history snapshot.
2. Private/public boundary and routing contracts.
3. LangGraph model-disabled controller fixture.
4. LlamaIndex baseline and metadata contract.
5. TurboVec isolated trial.
6. Parallel fan-out/fan-in fixture.
7. Independent review and benchmark.
8. Instruction promotion and optional persistent-service activation.
