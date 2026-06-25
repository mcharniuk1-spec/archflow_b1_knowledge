# Resetup Summary - 2026-06-24

The resetup created a clearer operating model for the project.

## Accepted Direction

The active solution is the knowledge-base and PRD engine:

1. Intake dialogue, chat, meeting notes, or transcript.
2. Summarize into structured context.
3. Produce a PRD.
4. Extract tasks, responsibilities, metrics, and blockers.
5. Update the knowledge base.
6. Review for evidence, public safety, and next action.

## Agentic Stack

| Layer | Role |
|---|---|
| LangGraph | Controls reasoning path, state, and approval gates. |
| CrewAI | Organizes agents as a team. |
| LlamaIndex | Connects agents to bounded data and RAG. |
| Codex | Operates locally, edits files, verifies outputs, and handles approvals. |
| Ollama | Local model provider after approval. |

## Public Project Rule

All new active work goes under `public/project`.
Prior work is represented under `public/history` as summaries only.
