# ArchFlow Responsive Knowledge Crew

Status: canonical provider-disabled public core
Supersedes: numbered `Architecture 1` / `Architecture 2` as top-level architecture labels

## Contracts

- `contracts/operating-model.json` — controller operations, states, gates, repair, adapters.
- `contracts/knowledge-crew-config.json` — seven layers, framework parameters, context budget, research, skills, dashboard.
- `contracts/role-catalog.json` — twenty-one stable roles, Ukrainian call names in English letters, and canonical task defaults.
- `contracts/role-workflows.json` — ten adaptive workflow packs using stable role IDs.
- `schemas/knowledge-case.schema.json` — typed shared case with materialized role bindings.
- `schemas/role-task-binding.schema.json` — per-role inputs, output, skill/tool ceiling, permission boundary, typed gap references, review route, resolvable handoff payload, and stops.
- `schemas/action-proposal.schema.json` — action validation packet.
- `fixtures/` — synthetic eligible and adversarial examples.

## Validate

```bash
python3 project/system/validate_system.py
```

The validator checks schema definitions and instances, exact state-registry equality, role names/defaults, workflow/review closure, role task bindings, admission projections, layer order, context budget, LlamaIndex parameters, TurboVec calibration/promotion gate, CrewAI defaults, LangGraph interrupts/idempotency, and eligible/blocked/adversarial behavior.

The test performs no provider call, writeback, or action.

## Architecture

Read [Responsive Knowledge Crew Architecture](../../docs/responsive-knowledge-crew-architecture.md).
