# Integrated Knowledge Operations Plan

Status: configured and partially runtime-verified as the public project contract.

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
| LangGraph | Runtime installed; sanitized smoke workflow passed. |
| CrewAI | Runtime installed; config/import check passed without LLM execution. |
| LlamaIndex | Runtime installed; approved-corpus retrieval proof passed. |
| Graphify | Public repo graph generated and linked from dashboard. |
| Obsidian mirror | Planned as sanitized mirror only. |
| Nexus | Planned after target vault and live schema are clear. |

## Seven Task Execution Status

1. LangSmith key handling: complete. The key is present only in the ignored local env file.
2. LangSmith trace test: complete. A sanitized smoke trace was submitted with Ollama-only metadata.
3. LangGraph runtime: installed and smoke-tested.
4. LlamaIndex approved corpus: installed and keyword retrieval proof passed.
5. First proof run: E1.2 preparation packet exists; full graph-wrapped generation is next.
6. Graphify public repo: generated from public-only source copy.
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
project/scripts/pre-push-runtime-guard.py
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

## Next Execution Needed

The next run should:

1. Expand the minimal LangGraph graph into the full E1.2 proof path.
2. Use LlamaIndex retrieval over the approved public corpus.
3. Wire CrewAI role outputs inside the graph without exposing raw private input.
4. Run one graph-wrapped proof workflow and review gate.
