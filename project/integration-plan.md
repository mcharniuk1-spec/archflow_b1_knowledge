# Integrated Knowledge Operations Plan

Status: configured as public project contract.

## Goal

Operate ArchFlow as one coordinated system while keeping each knowledge layer responsible for a different job.

## How The Layers Work Together

```text
Codex
  -> WikiLLM public memory
  -> public-safety scan
  -> LangGraph state workflow
  -> LlamaIndex approved retrieval
  -> CrewAI role outputs
  -> LangGraph review gate
  -> LangSmith trace
  -> WikiLLM run/decision/issue updates
  -> Git pre-push safety hook
  -> GitHub
```

## Current Execution Status

| Layer | Status |
|---|---|
| Codex | Active operator. |
| WikiLLM | Active under `wiki/`. |
| Ollama/Qwythos | Active local model. |
| LangSmith | Key present locally; SDK installed in ignored local runtime; smoke trace submitted. |
| LangGraph | Contract configured; runtime missing. |
| CrewAI | Contract configured; runtime missing. |
| LlamaIndex | Contract configured; runtime missing. |
| Graphify | Planned after runtime code exists. |
| Obsidian mirror | Planned as sanitized mirror only. |
| Nexus | Planned after target vault and live schema are clear. |

## Seven Task Execution Status

1. LangSmith key handling: complete. The key is present only in the ignored local env file.
2. LangSmith trace test: complete. A sanitized smoke trace was submitted with Ollama-only metadata.
3. LangGraph runtime: not installed; contract is ready.
4. LlamaIndex approved corpus: contract is ready; runtime index not built.
5. First proof run: pending runtime or Codex-supervised manual run.
6. Graphify public repo: planned after runtime files exist.
7. Obsidian/Nexus integration: planned after sanitized vault target is explicit.

## Why Not Push The API Key

The API key must stay in `project/.env.langsmith.local`, which is ignored by Git.

The public repository contains only:

- env examples with blank key fields
- routing configuration
- instructions
- run reports

## Git Safety Hook

The repo now uses a tracked hook path:

```text
.githooks/pre-push
```

That hook runs:

```text
scripts/public_safety_scan.py
```

The scan blocks:

- non-empty secret env values
- common API key patterns
- local machine paths
- private Notion/app links
- raw/private/secrets folders
- `.env` files accidentally staged
- local runtime files
- `.DS_Store`

## Next Approval Needed

To continue execution, approve installing the remaining runtime packages in the ignored local environment:

```text
Approve installing LangGraph, LlamaIndex, and CrewAI in the ignored local Python environment for the public project.
```

After that, the next run should:

1. Implement a minimal LangGraph graph.
2. Build an approved-corpus LlamaIndex.
3. Wire CrewAI role outputs inside the graph.
4. Run one manual or automated proof workflow.
