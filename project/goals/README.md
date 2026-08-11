# Goal Engineering Contract

Status: active design contract; provider-disabled execution baseline.

Purpose: make every substantial architecture or execution run pursue one bounded objective until it is verified complete, explicitly blocked, paused by the owner, or superseded by a reviewed decision.

## Goal versus loop

- A goal defines the objective, observable done condition, lifecycle, verifier, budget, authority, and kill switches.
- A loop is the bounded repair mechanism used inside a task while pursuing the goal.
- A LangGraph workflow owns state transitions across tasks.
- No goal may contain an unbounded loop, approve its own high-risk result, or broaden authority when it persists.

## Required artifacts

1. A state file matching `goal-state.schema.yaml`.
2. A task graph with dependencies and artifact contracts.
3. An independent verification packet.
4. A run log and handout.
5. A memory-promotion decision.

## Lifecycle

`draft -> ready -> running -> verifying -> complete`

Alternate terminal or controlled states: `blocked`, `paused`, `superseded`, `cancelled`.

## Maturity

| Level | Meaning | ArchFlow status |
|---|---|---|
| G0 | Objective exists but done condition or verifier is weak. | Legacy tasks may be here. |
| G1 | Goal contract, budget, stop rules, and verifier exist. | New default. |
| G2 | State can resume and a deterministic/provider-disabled fixture passes. | Target for architecture factory pilot. |
| G3 | Provider-backed repeated runs meet benchmark and recovery thresholds. | Blocked pending explicit provider, budget, trace, and safety approval. |

## Stop and kill rules

Stop and record `blocked` when authority, sources, target schema, or required proof is missing. Kill or supersede the goal when the budget is exhausted, the objective becomes invalid, safety boundaries fail, or two repair cycles produce no new evidence. Persistence does not authorize retries beyond the declared budget.
