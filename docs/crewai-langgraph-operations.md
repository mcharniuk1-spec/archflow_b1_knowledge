# CrewAI and LangGraph Operations

Status: current provider-disabled framework contract

## Responsibility split

| System | Owns | Does not own |
|---|---|---|
| CrewAI | Role, goal, task, role-safe knowledge input, tools, expected output, delegation, reviewer, handoff | Case truth, permission, durable memory, transitions, approval |
| LangGraph | Typed case state, reducers, routes, checkpoints, interrupts, repair loops, terminal states | Knowledge authority, requirement approval, business truth |
| Solution/action memory | Reviewed reusable meaning, provenance, freshness, and supersession | Task execution or graph state |
| LlamaIndex-compatible retrieval | Manifest-bound candidates with source and chunk identity | Approval or promotion |

## CrewAI parameters

```yaml
process: sequential_contract
memory: false
cache: false
planning: false
execution_policy:
  default_mode: contract_only_no_automatic_execution
  provider_mode: disabled
  network_calls: 0
  external_writes: 0
  exact_retrieval_manifest_schema: "3.0"
```

The YAML declares 13 bounded role/task entries drawn from the canonical 21-role catalog. It describes order, ownership, expected packet paths, and reviewer separation; it does not launch a crew. The operating model allows at most three parallel branches, but parallelism is not a CrewAI default: outputs and file ownership must be independent, and one integrator owns merge order. A role binding never expands case authority.

## LangGraph parameters

```yaml
provider_mode: disabled
network_calls: 0
external_writes: 0
checkpointer: none_by_default
runtime_packets_root: project/local/run-packets
maximum_revision_loops: 2
maximum_attempts_per_item: 3
maker_can_be_final_reviewer: false
human_approval_required_for_external_effects: true
retrieval_manifest_schema: "3.0"
```

The public file is a provider-disabled route contract. It describes how a future optional LangGraph runtime can materialize typed state, gates, bounded revisions, and stops; it is not evidence of a live checkpointer, persistent service, or resumed interrupt.

Any later interrupt implementation must keep side effects after the approval boundary and make external actions replay-safe. The current release prepares action proposals only and performs no external effect.

## Provider boundary

Provider execution remains disabled in the public config. A future activation needs server-side secrets, exact provider/data disclosure rules, hard budgets, persistent ledgers, replay-safe spend accounting, quality evaluation, and explicit accountable-authority approval. Browser JavaScript never reads provider keys.

## Proof boundary

The public validator proves contract shape and eligible/blocked decisions. It does not prove provider-backed CrewAI kickoff, persistent interrupt resume, production tenancy, external writeback, or live cost controls.

Primary references:

- [CrewAI](https://docs.crewai.com/)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [LangGraph subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
