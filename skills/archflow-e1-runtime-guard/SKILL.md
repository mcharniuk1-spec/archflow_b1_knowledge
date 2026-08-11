---
name: archflow-e1-runtime-guard
description: Validate the portable ArchFlow runtime before integration or Git publication. Use after changing workflows, role or skill contracts, provider configuration, retrieval boundaries, dashboard data, or runtime code to run provider-disabled safety, schema, import, and smoke checks without installing packages or activating services.
---

# ArchFlow Runtime Guard

The package ID retains `e1` for compatibility. The workflow is a generic, side-effect-light guard for the public tool.

## Runtime spine

Validate this order:

`public safety -> workflow and schema parse -> provider registry -> system fixture -> LangGraph smoke -> LlamaIndex corpus check -> CrewAI config check -> dashboard data check -> Git diff`

The guard validates contracts. It does not install dependencies, start a service, discover credentials, call a model, trace private data, push Git, deploy, or write externally.

## Canonical inputs

- `project/config/provider-registry.json` is the only provider inventory. Do not create a competing provider-routing file.
- `project/workflows/` defines provider-neutral orchestration and retrieval contracts.
- `project/database/` and `project/system/schemas/` define state, receipt, review, memory, action, and role bindings.
- `project/dashboard/corpus-manifest.json` defines the exact dashboard source boundary.
- `project/agents/` and `skills/` define role and skill contracts.

## Required checks

Run the smallest applicable retained commands in this order:

```bash
python3 scripts/public_safety_scan.py
python3 project/scripts/validate-workflows.py
python3 project/system/validate_system.py
python3 project/scripts/langgraph-smoke-run.py
python3 project/scripts/llamaindex-approved-corpus.py
python3 project/scripts/crewai-config-check.py
python3 project/scripts/validate-dashboard-data.py
python3 project/scripts/pre-push-runtime-guard.py
git diff --check
```

Skip a command only when its input surface was not changed or its declared dependency is unavailable. Record the exact reason; do not translate a skipped check into a pass.

## Provider boundary

Parse `project/config/provider-registry.json` and confirm:

- the default provider remains `none`;
- the default observability state remains `off`;
- browser access is false for every secret-bearing adapter;
- only environment-variable names, never values or presence, appear in public artifacts;
- documented adapters keep their declared activation gates.

Optional local or remote adapters remain inactive during this guard. Import availability is not execution proof, and an environment variable is not authorization.

## Runtime dependency checks

Use the pinned project requirements when a local environment already exists. Check imports without installing anything inside a hook. Keep all generated caches, smoke state, and traces in a caller-supplied ignored local output directory.

If a dependency is missing, report a GAP with the exact package group and setup command documented by the project. Do not download or repair it automatically.

## Failure order

1. Resolve public-safety findings.
2. Resolve malformed JSON, YAML, or schema references.
3. Resolve role, skill, workflow, and provider-registry inconsistencies.
4. Resolve missing local dependencies through a separately approved setup step.
5. Re-run the affected smoke and deterministic validators.
6. Regenerate dashboard data only when its allowlisted inputs changed.
7. Run the integrated guard and `git diff --check` again.

Stop after the same failure signature appears twice without new evidence.

## Evidence contract

Return a check matrix with command, scope, result, evidence reference, provider calls, external writes, gaps, and next safe action. Use `project/database/action-receipt.schema.json` only for actions that actually ran and were independently reviewed. Save auxiliary output only to a caller-supplied ignored directory or return it inline.

The guard passes only when every required in-scope check passes, skipped checks are justified, provider calls and external writes remain zero, and no public file contains a secret, private identity, private URL, local absolute path, or raw private source material.
