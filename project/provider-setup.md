# Provider Setup

This project supports two provider concepts:

1. Ollama local model provider.
2. Codex operator authentication.

They are not the same thing.

## Current Verified State

As of 2026-06-25:

- Ollama CLI is installed.
- Ollama server is started through the local Homebrew service.
- Local Ollama manifests include a Qwythos model: `Qwythos-9B-Claude-Mythos-5-1M-GGUF` with `Q4_K_M` quantization.
- Qwythos appears in `ollama list`, but the smoke test failed at model load time with an Ollama 500 error.
- Qwythos now loads and generates text through Ollama.
- `gemma4:e4b` remains the fallback model.
- Codex is available as the operator runtime.
- Codex auth should not be treated as an exportable API key.
- LangSmith tracing is configured but awaiting an API key in an ignored local env file.

## Recommended Mode

Use Codex authentication as the main project operator and publication path. Use Ollama only for local minor/background tasks:

- `ARCHFLOW_PROVIDER_MODE=codex_auth_main`
- `CODEX_OPERATOR_MODE=codex_app`
- `CODEX_AUTH_EXPORTS_API_KEY=false`
- `CODEX_GITHUB_PUBLICATION=codex_operated_git_ssh`
- `OLLAMA_CHAT_MODEL=hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M`
- `OLLAMA_FALLBACK_CHAT_MODEL=gemma4:e4b`
- `OLLAMA_TASK_SCOPE=minor_background_tasks`
- `LANGSMITH_PROJECT_ID=057edf33-a328-4186-9425-3306186149ef`
- `LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com`

Codex authentication is not an API key for LangGraph, CrewAI, LlamaIndex, or other frameworks. It is the authenticated operator channel in this workspace. If direct framework API calls are needed later, they require separately approved provider credentials stored outside public files.

GitHub publication is operated from Codex through the verified Git SSH transport. HTTPS push was blocked by missing shell credentials; no token is stored in this repository.

## Approval Needed

Completed:

1. Started the local Ollama server through the Homebrew service.
2. Verified the Qwythos model through `ollama list`.
3. Created `.env.local` from `config/providers.env.example`.
4. Ran a public-safe local model smoke test.

No secret values are needed for Ollama.

If later cloud APIs are used, API keys must be created and stored outside public files.

## LangSmith Status

LangSmith is configured for tracing only.

- Local editable file: `project/.env.langsmith.local`.
- Public example: `project/config/langsmith.env.example`.
- Project name: `ArchFlow`.
- Project ID: `057edf33-a328-4186-9425-3306186149ef`.
- API key status: not present, waiting for manual insertion.
- Model execution: Ollama only.

## Qwythos Status

Qwythos is installed and now usable through the server.

Operational routing:

- Active local model: Qwythos.
- Fallback local model: `gemma4:e4b`.
- Codex remains the review and execution layer.
