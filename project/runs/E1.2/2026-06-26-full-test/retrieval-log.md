# Retrieval Log

Date: 2026-06-26
Run: E1.2 full public-safe proof test

## Method

The retrieval layer used the existing LlamaIndex approved-corpus script. It loads public Markdown/YAML files into LlamaIndex `Document` objects, attaches repo-relative source paths, and runs deterministic keyword scoring. It does not call cloud embeddings and does not ingest raw private material.

## Approved Corpus

| Corpus | Status |
|---|---|
| `project/` | approved |
| `history/` | approved |
| `skills/` | approved |
| `wiki/` | approved |

## Command

```bash
project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py
```

## Expected Evidence

```text
llamaindex_documents=ok
llamaindex_query=ok
source=<repo-relative path> score=<integer>
persisted=project/local/rag_index/approved-corpus-summary.json
```

## E1.2 Graph Retrieval Event

```text
retrieve_context:
  selected:
    - project/workflows/langgraph-controller.yaml
    - project/workflows/crewai-crew.yaml
    - project/workflows/llamaindex-rag.yaml
    - project/workflows/knowledge-integration.yaml
    - wiki/memory.md
    - wiki/insights.md
    - graphify-out/GRAPH_REPORT.md
```

## Boundary

The persisted retrieval summary is ignored local runtime state. Public files record only document counts, source paths, scores, and selected public context.
