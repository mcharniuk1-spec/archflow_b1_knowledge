# Public WikiLLM Contract

## Purpose

This folder is the durable public memory layer for the ArchFlow Block 1 repository.

## Required Files

- `index.md`
- `memory.md`
- `insights.md`
- `log.md`
- `rules/`
- `runs/`
- `decisions/`
- `issues/`

## Write Rules

For substantial work:

1. Add a run file under `runs/`.
2. Append `log.md`.
3. Add or update `memory.md` only for stable future-use facts.
4. Add or update `insights.md` only for reusable reasoning or design meaning.
5. Add a decision file when a durable choice is made.
6. Add an issue file when a blocker remains.

## Safety Rules

- Do not store real API keys.
- Do not store private links.
- Do not store local absolute paths.
- Do not store raw private source material.
- Keep content English-only.
- Keep paths repo-relative.

## Layer Rules

- Codex is the primary operator.
- Ollama is local model execution.
- LangSmith is tracing only.
- LangGraph is workflow control.
- CrewAI is role/task organization.
- LlamaIndex is bounded retrieval.

