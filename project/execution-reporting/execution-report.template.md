# Execution report: <run-id>

Status: `configured | planned | locally_tested | executed | reviewed | promoted | blocked | not_recorded`

## Run identity

- Objective:
- Execution type:
- Risk:
- Integrator:
- Reviewer:
- Started / completed:
- Stop condition:

## Actor and skill ledger

| Lane | Actor | Executed state | Claimed scope | Skills used | Deliverables | Reviewer |
|---|---|---|---|---|---|---|
| <lane> | <actor> | <state> | <repo-relative scope> | `<skill>` (`used/configured_only/not_recorded`) | `<path>` | <reviewer> |

## Architecture evidence

| Component | State | Evidence | Criteria / metric | Result | Interpretation |
|---|---|---|---|---|---|
| LangGraph | | run/node/route/checkpoint | `langgraph_state_evidence` | | |
| CrewAI | | role/task/runtime level | `crewai_role_evidence` | | |
| LlamaIndex | | corpus/retrieval/fallback/benchmark | `llamaindex_source_evidence` | | |
| Parallel execution | | claims/handoffs/merge | `parallel_conflict_free` | | |
| Maintained knowledge | | solution/action-memory candidate and promotion state | `memory_promotion` | | |

## Deliverables and checks

| Deliverable or check | Path / command | Status | Evidence result |
|---|---|---|---|

## Interpretation

FACT:

INTERPRETATION:

HYPOTHESIS:

GAP:

## Memory and next action

- Reviewed memory destination:
- Promotion status and reason:
- Next conclusive gate:
