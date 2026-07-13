# Architecture Layers

Use this order unless a documented decision justifies a change.

| Layer | Contract | Canonical artifact |
|---|---|---|
| 0. Authority | Owner, allowed sources/files/actions, forbidden side effects, approval boundary. | Operating rules and task contract. |
| 1. Goal | One objective, observable done condition, verifier, budget, lifecycle, stop/kill conditions. | `project/goals/`. |
| 2. Context | Stable CAG core plus bounded task-specific retrieval. | `project/context/`. |
| 3. Plan | Dependency graph, critical path, parallel-safe branches, artifact contracts. | Run packet and task board. |
| 4. Orchestration | LangGraph owns state transitions, checkpoints, retries, and human gates. | Workflow config and state schema. |
| 5. Execution | Minimal role pack performs a bounded task. | Role registry and task handout. |
| 6. Loop | Maker/checker repair within attempt, token, time, and cost limits. | `project/loops/`. |
| 7. Verification | Deterministic checks first, independent reviewer second, safety/claim review third. | Check output and review packet. |
| 8. Memory | Promote reviewed deltas; preserve provenance and superseded history. | WikiLLM; Obsidian links; Graphify rebuild. |
| 9. External action | Schema, target, secret, budget, approval, rollback, and readback proof. | Action-specific gate. |
| 10. Measurement | Quality, cost, latency, context, retrieval, conflict, safety, and recovery metrics. | Benchmark ledger. |

## Architecture factory

Use the same architecture to create another architecture:

1. Normalize the requested business outcome.
2. Select a prebuilt department template.
3. Gather only source material needed for that template.
4. Generate a goal contract and proof ledger.
5. Generate a dependency graph, role pack, skill pack, retrieval profile, and state machine.
6. Run threat modeling and tool-adoption gates.
7. Execute a deterministic/provider-disabled fixture.
8. Run independent verification and red-team review.
9. Parameterize only the dimensions that can be safely changed.
10. Promote the accepted architecture as a versioned template, never as an unqualified universal default.

## Editable parameters

- `objective`, `done_condition`, `evidence_state`
- `risk_level`, `autonomy_level`, `approval_boundary`
- `allowed_corpus`, `retrieval_mode`, `top_k`, `fallback_mode`
- `roles`, `skills`, `maker`, `checker`, `integrator`
- `max_attempts`, `max_revision_loops`, `max_parallel_branches`
- `token_budget`, `time_budget`, `cost_budget`
- `provider_policy`, `model_route`, `privacy_class`
- `memory_write_policy`, `retention`, `promotion_gate`
- `external_actions`, `rollback`, `readback_check`
