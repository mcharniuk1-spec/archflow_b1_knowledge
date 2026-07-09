# Context Layer

Status: active planning and execution context layer.

This folder holds Controlled Context Assembly Generation (CAG) files and context capsules for bounded ArchFlow work.

## Rules

- CAG is controlled context assembly, not uncontrolled ingestion.
- RAG is task-specific retrieval from the approved public-safe corpus only.
- LlamaIndex retrieves evidence; it is not durable memory.
- WikiLLM remains durable memory only after AF Review and promotion.
- Context capsules are run artifacts unless a reviewed conclusion is promoted through the KB rules.
- Subagents receive compact capsules and task contracts, not broad repo dumps.

## Files

- `cag-core.yaml` - stable context used before task-specific retrieval.
- `context-capsule.schema.json` - schema for run/task capsules.
- `retrieval/source-boundary-policy.yaml` - retrieval allowlist and rejection policy.
- `capsules/` - per-run or per-task context capsules.

## Approval Gates

The context layer never authorizes provider calls, Notion mutation, Linear sync, Telegram send, Railway action, deployment, production promotion, Figma sync, Git push, or external writeback. Those actions still require explicit owner approval.
