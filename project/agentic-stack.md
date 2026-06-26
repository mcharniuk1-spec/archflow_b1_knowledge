# Agentic Stack

## Layer Decision

Use this structure:

```text
Codex-authenticated operator prompt
  -> LangGraph path and state controller
  -> LlamaIndex bounded retrieval
  -> CrewAI named team tasks
  -> LangGraph review gate
  -> public-safe project outputs
```

## Tool Responsibilities

| Tool | Responsibility | Public Project Use |
|---|---|---|
| Codex | Operator runtime, editor, verifier, approval boundary. | Default interface for now. |
| LangGraph | Path control, state, conditional routing, review gates. | Full Block 1 workflow controller. |
| CrewAI | Named roles and task execution. | AF Tools, AF Context, AF Manager, AF Knowledge, AF Review. |
| LlamaIndex | Bounded retrieval and RAG. | Search only approved public-safe project and sanitized history. |
| Ollama | Local model serving. | Minor/background tasks only; active model is Qwythos and fallback is `gemma4:e4b`. |
| LangSmith | Observability and trace review. | Configured for tracing only; waits for manual API key insertion. |

## Agent Hooks

| Hook | Use |
|---|---|
| AF Graph | Full controlled workflow. |
| AF RAG | Source-grounded retrieval over approved corpus. |
| AF Crew | Team-mode work split by role. |
| AF Review | Final public-safety and evidence gate. |

## Public Corpus Rules

Allowed by default:

- `project/`
- `history/`
- `skills/`
- `wiki/`

Not allowed by default:

- Raw private exports.
- Legacy root files.
- Private Notion pages.
- Local machine paths.
- Credentials.

## First Proof Run

The first proof run should use a sanitized internal source summary, not a raw transcript.

Output files should go to:

`project/runs/2026-06-25-first-kb-proof/`

Required outputs:

- context digest
- PRD
- task and responsibility matrix
- KB update note
- review report

## Current Workflow Configs

- `workflows/langgraph-controller.yaml`
- `workflows/crewai-crew.yaml`
- `workflows/llamaindex-rag.yaml`
- `langsmith-setup.md`
- `../wiki/index.md`

## Output Documents

Templates are present under `outputs/templates/`.

No finished first proof-run output exists yet. The first real run should create a dated folder under `outputs/runs/` or `project/runs/` and fill the templates with source-grounded content.
