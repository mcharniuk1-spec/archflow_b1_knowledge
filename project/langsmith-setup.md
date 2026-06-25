# LangSmith Setup

Status: configured; local ignored API key present; sanitized smoke trace submitted.

## Current Parameters

| Parameter | Value |
|---|---|
| Purpose | Observability and tracing only. |
| Model execution | Ollama local only. |
| Cloud model keys | Not configured. |
| Project name | `ArchFlow` |
| Project ID | `057edf33-a328-4186-9425-3306186149ef` |
| Endpoint | `https://eu.api.smith.langchain.com` |
| Local env file | `project/.env.langsmith.local` |
| Public example | `project/config/langsmith.env.example` |

## Local Env File

Store the API key only in:

`project/.env.langsmith.local`

Keep this line blank in Git-tracked files:

```env
LANGSMITH_API_KEY=
```

## Active Env Block

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
LANGSMITH_PROJECT=ArchFlow
LANGSMITH_PROJECT_ID=057edf33-a328-4186-9425-3306186149ef
LANGSMITH_API_KEY=
LANGGRAPH_CONTROL_MODE=codex_supervised
LANGGRAPH_LLM_PROVIDER=ollama_local
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_CHAT_MODEL=hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M
OLLAMA_FALLBACK_CHAT_MODEL=gemma4:e4b
OLLAMA_EMBED_MODEL=nomic-embed-text
LANGSMITH_RUN_TAGS=archflow,block1,ollama,qwythos,public-safe
LANGSMITH_TRACE_PUBLIC_SAFE_ONLY=true
```

## Operation Rule

LangSmith receives traces only after public-safety filtering. Do not send raw private transcripts, private links, local paths, secrets, or unreviewed source material to LangSmith.

## Current Check

- `project/.env.langsmith.local` exists locally and is ignored by Git.
- The real API key value is not stored in tracked files.
- A sanitized `archflow_public_smoke_trace` was submitted through the local project runtime.
- LangGraph, LlamaIndex, and CrewAI are still workflow contracts until their packages are installed in the ignored local runtime.

## References

- LangSmith docs confirm API-key based setup and tracing setup through environment variables.
- The current endpoint and env names follow the LangSmith setup screen used for this project.
