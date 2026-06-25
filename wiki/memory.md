# Memory

## Stable Project Direction

ArchFlow Block 1 is the first public solution:

`dialogue/chat/meeting material -> structured context -> PRD -> responsibility plan -> agent-ready knowledge base`

## Current Runtime Decisions

- Codex is the primary operator, review, file-edit, and publication layer.
- Codex authentication is not exported as an API key.
- Ollama is the only model execution provider for now.
- Qwythos is the active local model after the latest smoke test generated text.
- `gemma4:e4b` remains the local fallback.
- LangSmith is tracing only, not a model provider.
- No cloud model credentials are configured.

## Public Repo Rules

- All active project work goes under `project/`.
- Sanitized previous history goes under `history/`.
- Public WikiLLM memory goes under `wiki/`.
- Used/setup skills only go under `skills/` and `project/agents/`.
- Env files with real keys stay ignored.

## LangSmith Memory

- Project name: `ArchFlow`.
- Project ID: `057edf33-a328-4186-9425-3306186149ef`.
- Endpoint: `https://eu.api.smith.langchain.com`.
- Local editable env: `project/.env.langsmith.local`.
- Public example env: `project/config/langsmith.env.example`.
- API key status: missing until manually inserted.

## Workflow Memory

- LangGraph controls path/state/review gates.
- CrewAI organizes named agents and expected outputs.
- LlamaIndex connects agents to bounded public-safe retrieval.
- LangSmith will trace workflow execution after the API key is added.

