# Unified Operating Architecture

Status: canonical summary
Last verified: 2026-08-05
Supersedes: numbered `Architecture 1` / `Architecture 2` as top-level concepts

ArchFlow operates one Knowledge Case Controller with seven connected layers, one typed case, adaptive role packs, requirement/action validation, exact receipts, and reviewed knowledge promotion.

The complete specification is [Responsive Knowledge Crew Architecture](responsive-knowledge-crew-architecture.md).

![Seven-layer responsive knowledge crew](../project/assets/architecture/knowledge-crew-tower.png)

## One case, six behavioral operations

| Operation | Result | Never does |
|---|---|---|
| `orient_case` | admitted case or named gap | retrieve, execute, or infer authority |
| `assemble_perception` | role-safe context with sources, contradictions, and gaps | make retrieval authoritative |
| `plan_role_work` | smallest crew, tasks, checks, reviewer, and handoffs | expand permission |
| `evaluate_action` | eligible, repair, approval wait, blocked, or verified | execute |
| `record_result` | exact verification/action/readback receipt | infer success from command completion |
| `propose_knowledge_update` | promotion, supersession, freshness task, or no promotion | copy raw traces or secrets |

## Seven layers

1. Case authority and employee scope.
2. Reviewed knowledge and source spine.
3. Bounded context perception.
4. Adaptive role crew.
5. Specialist research and delivery.
6. Graph control, validation, and review.
7. Receipts, outcomes, and maintained knowledge.

## Framework boundaries

- WikiLLM is portable reviewed durable memory.
- Obsidian is an optional private human semantic workspace.
- LlamaIndex manages allowlisted documents/nodes, metadata, routing, ranking, and source return.
- TurboVec is an optional compact vector candidate behind LlamaIndex, never authority or the current default.
- Orbit and Graphify provide generated structural evidence followed by exact reads.
- CrewAI expresses roles/tasks and receives only a role-safe context capsule.
- LangGraph owns typed state, routes, reducers, interrupts, repair loops, and optional persistence.
- The Crew Desk is a browser-local human projection and review-packet exporter.

## Canonical executable contracts

- `project/system/contracts/operating-model.json`
- `project/system/contracts/knowledge-crew-config.json`
- `project/system/contracts/role-catalog.json`
- `project/system/contracts/role-workflows.json`
- `project/system/schemas/knowledge-case.schema.json`
- `project/system/schemas/role-task-binding.schema.json`
- `project/system/schemas/action-proposal.schema.json`

## Core proof

```bash
python3 project/system/validate_system.py
```

The provider-disabled fixture keeps a bounded proposal eligible and blocks stale requirements, unknown authority, target escape, reviewer spoofing, and malformed packets. It performs no action.
