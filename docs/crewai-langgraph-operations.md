# CrewAI and LangGraph Operations

Status: current provider-disabled framework contract

## Responsibility split

| System | Owns | Does not own |
|---|---|---|
| CrewAI | Role, goal, task, role-safe knowledge input, tools, expected output, delegation, reviewer, handoff | Case truth, permission, durable memory, transitions, approval |
| LangGraph | Typed case state, reducers, routes, checkpoints, interrupts, repair loops, terminal states | Knowledge authority, requirement approval, business truth |
| WikiLLM/Obsidian | Reviewed durable meaning and human semantic review | Task execution or graph state |
| LlamaIndex/TurboVec | Retrieval candidates with source/node identity | Approval or promotion |

## CrewAI parameters

```yaml
process: sequential
memory: false
cache: true
planning: false
delegation_default: false
maximum_parallel_tasks: 3
knowledge_input: role_safe_perception_capsule_only
provider_execution: disabled
```

Parallel work is permitted only when outputs and file ownership are independent. One integrator owns merge order. A role binding never expands case authority.

## LangGraph parameters

```yaml
public_checkpointer: none
local_single_user: sqlite_after_migration_and_recovery_proof
team_runtime: postgresql_after_tenancy_backup_and_recovery_proof
thread_id: case_id
subgraph_persistence: per_invocation_by_default
maximum_repair_attempts: 3
maximum_same_failure: 2
maker_can_be_final_reviewer: false
side_effect_position: after_interrupt_only
side_effect_idempotency: action_id_replay_protection
```

Interrupts cover requirement-owner decisions, external-action approval, private-source requests, irreversible changes, and material contradictions.

An interrupted node restarts when resumed. Therefore no side effect may occur before the interrupt, and every action must tolerate replay via its action ID.

## Provider boundary

Provider execution remains disabled in the public config. A future activation needs server-side secrets, exact provider/data disclosure rules, hard budgets, persistent ledgers, replay-safe spend accounting, quality evaluation, and explicit owner approval. Browser JavaScript never reads provider keys.

## Proof boundary

The public validator proves contract shape and eligible/blocked decisions. It does not prove provider-backed CrewAI kickoff, persistent interrupt resume, production tenancy, external writeback, or live cost controls.

Primary references:

- [CrewAI](https://docs.crewai.com/)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [LangGraph subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
