# Retrieval Log

## Method

The first LlamaIndex proof loads approved public Markdown and YAML files into LlamaIndex `Document` objects and runs deterministic keyword scoring. It does not call cloud embeddings and does not ingest raw private material.

## Command

```bash
project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py
```

## Result

```text
llamaindex_documents=ok
document_count=58
llamaindex_query=ok
source=project/reports/2026-06-25-current-setup-methods-and-agent-plan.md score=53
source=project/reports/2026-06-25-dashboard-setup-and-operation-report.md score=33
source=project/project-plan.md score=19
source=project/future-actions-and-parameters.md score=17
source=skills/archflow-task-breakdown/SKILL.md score=15
persisted=project/local/rag_index/approved-corpus-summary.json
```

## Boundary

The persisted summary is ignored local runtime state. Public files record only document count, source paths, and scores.

## Next Retrieval Step

Add local embeddings only after the approved corpus and proof workflow are stable. The first candidate embedding model remains the local embedding model named in the public config.
