# Decision - Codex, Ollama, And LangSmith Boundary

Date: 2026-06-25

## Decision

Use Codex as the primary operator, Ollama/Qwythos as the local model execution layer, and LangSmith as tracing only.

## Rationale

Codex authentication is not an exportable API key for frameworks.

Ollama can run local models without cloud model credentials.

LangSmith can observe and debug future LangGraph/CrewAI/LlamaIndex runs after the API key is added, without changing model execution.

## Parameters

- Codex mode: `codex_app`
- Ollama model: `hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M`
- Ollama fallback: `gemma4:e4b`
- LangSmith project: `ArchFlow`
- LangSmith project ID: `masked_langsmith_project_id`
- LangSmith endpoint: `https://eu.api.smith.langchain.com`

## Consequences

- No OpenAI, Anthropic, or other cloud model keys are needed for current execution.
- LangSmith traces cannot be sent until the API key is manually inserted into the ignored local env file.
- Future runtime package installation remains a separate approval step.

