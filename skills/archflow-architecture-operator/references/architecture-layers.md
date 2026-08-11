# Architecture Layers

Use this order unless a documented decision justifies a change.

| Layer | Contract | Canonical artifact |
|---|---|---|
| 0. Authority | Accountable role, allowed sources/files/actions, forbidden side effects, approval boundary. | Operating rules and task contract. |
| 1. Goal | One objective, observable done condition, verifier, budget, lifecycle, stop/kill conditions. | `project/goals/`. |
| 2. Context | Stable CAG core plus bounded task-specific retrieval. | `project/context/`. |
| 3. Plan | Dependency graph, critical path, parallel-safe branches, artifact contracts. | Inline plan or caller-supplied ignored local packet. |
| 4. Orchestration | LangGraph owns state transitions, checkpoints, retries, and human gates. | Workflow config and state schema. |
| 5. Execution | Minimal role pack performs a bounded task. | Role registry and task handout. |
| 6. Loop | Maker/checker repair within attempt, token, time, and cost limits. | `project/loops/`. |
| 7. Verification | Deterministic checks first, independent reviewer second, safety/claim review third. | `project/database/review-bundle.schema.json` or retained review template. |
| 8. Memory | Promote only reviewed reusable meaning; preserve source and proof references plus supersession. | `project/database/solution-memory-record.schema.json`. |
| 9. External action | Schema, target, secret, budget, approval, rollback, and readback proof. | `project/database/action-receipt.schema.json` after verified execution. |
| 10. Measurement | Quality, cost, latency, context, retrieval, conflict, safety, and recovery metrics. | Fixed fixture, validator, result, and receipt. |

## Architecture factory

Use the same architecture to create another architecture:

1. Normalize the requested business outcome.
2. Select a prebuilt department template.
3. Gather only source material needed for that template.
4. Generate a goal contract and explicit evidence requirements.
5. Generate a dependency graph, role pack, skill pack, retrieval profile, and state machine.
6. Run threat modeling and tool-adoption gates.
7. Execute a deterministic/provider-disabled fixture.
8. Run independent verification and safety/claim review.
9. Parameterize only the dimensions that can be safely changed.
10. Shape the accepted reusable delta as a solution-memory record; promotion remains a separate reviewed decision.

## Editable parameters

- `objective`, `done_condition`, `evidence_state`
- `risk_level`, `autonomy_level`, `approval_boundary`
- `allowed_corpus`, `retrieval_mode`, `top_k`, `fallback_mode`
- `roles`, `skills`, `maker`, `checker`, `integrator`
- `max_attempts`, `max_revision_loops`, `max_parallel_branches`
- `token_budget`, `time_budget`, `cost_budget`
- `provider_policy`, `provider_adapter`, `privacy_class`
- `memory_write_policy`, `retention`, `promotion_gate`
- `external_actions`, `rollback`, `readback_check`
