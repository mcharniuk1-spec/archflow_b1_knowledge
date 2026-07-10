# Provider Setup

This project supports four provider concepts:

1. Ollama local model provider.
2. Codex operator authentication.
3. OpenRouter as a future hosted orchestration/model provider.
4. Mistral as a future hosted quality/synthesis provider.

They are not the same thing.

## Current Verified State

The dated entries in this section are historical local evidence, not a claim that a provider, hosted endpoint, credential, or deployment is currently available. Current hosted or provider readiness must be rechecked in a separately approved run without copying secrets or private target details into this repository.

As of 2026-06-25:

- Ollama CLI is installed.
- Ollama server is started through the local Homebrew service.
- Local Ollama manifests include a Qwythos model: `Qwythos-9B-Claude-Mythos-5-1M-GGUF` with `Q4_K_M` quantization.
- Qwythos appears in `ollama list`, but the smoke test failed at model load time with an Ollama 500 error.
- Qwythos now loads and generates text through Ollama.
- `gemma4:e4b` remains the fallback model.
- Codex is available as the operator runtime.
- Codex auth should not be treated as an exportable API key.
- LangSmith tracing is configured; the API key is present only in the ignored local env file and one sanitized smoke trace has been submitted.

As of 2026-07-01:

- The ignored ArchFlow workspace `.env.local` contains `OPENROUTER_API_KEY` and `MISTRAL_API_KEY`; the public repo root `.env.local` is separate ignored local deploy material.
- The Markdown file that temporarily contained those values was deleted.
- The local OpenAI key file created during the June 30 setup lane was deleted.
- Ignored env files were restricted to owner-only permissions.
- No provider key is tracked by Git, shown in dashboard JSON, or stored in public WikiLLM notes.
- The static dashboard must not call OpenRouter, Mistral, OpenAI, or Ollama directly because browser JavaScript cannot safely hold provider secrets.

## Recommended Mode

Use Codex authentication as the main project operator and publication path. Use Ollama only for local minor/background tasks:

- `ARCHFLOW_PROVIDER_MODE=codex_auth_main`
- `CODEX_OPERATOR_MODE=codex_app`
- `CODEX_AUTH_EXPORTS_API_KEY=false`
- `CODEX_GITHUB_PUBLICATION=codex_operated_git_ssh`
- `OLLAMA_CHAT_MODEL=hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M`
- `OLLAMA_FALLBACK_CHAT_MODEL=gemma4:e4b`
- `OLLAMA_TASK_SCOPE=minor_background_tasks`
- `LANGSMITH_PROJECT_ID=masked_langsmith_project_id`
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

## OpenRouter / Mistral Status

OpenRouter and Mistral are available only as local secret material for future approved tests. They are not active dashboard runtimes.

Allowed future route:

1. static dashboard creates a browser-local packet;
2. Codex or an approved local bridge reviews the packet;
3. a backend/local bridge reads provider keys from ignored env or secret store;
4. the provider call uses only sanitized, approved input;
5. `OPENROUTER_MODEL` is explicitly selected from a fresh model/pricing check;
6. budget and ledger paths are verified before the call;
7. the result returns as a reviewed run note, issue, decision, or dashboard data update.

Blocked route:

- no provider key in client JavaScript;
- no provider call from the static Vercel page;
- no raw transcript/audio/screen/private document upload to a provider;
- no automatic Notion/GitHub/WikiLLM writeback after a model response.

## Activation-Time Model And Budget Gate

OpenRouter model IDs, availability, capabilities, and pricing are drift-prone. Do not promote target model names in this repository to active selections. Before any approved server-side activation, the assigned executor and Yushchenko observer must record a public-safe review packet that:

1. Retrieves the current OpenRouter Models API metadata and selects a canonical model ID that satisfies the task capability and approved budget.
2. Records the selection rationale, input/output/reasoning price dimensions, timeout and retry policy, and an explicit per-run hard stop without storing key material.
3. Confirms the response usage/cost fields and a durable ledger path before any result can proceed to an external-action role.
4. Requires an independent safety reviewer and owner approval before a provider result is written outside the bounded run artifact.

OpenRouter documents its Models API, model capabilities and pricing fields, response usage/cost accounting, and key-level limits at public URLs. The project uses those sources only at activation time; this documentation update does not query a key, select a model, or activate the provider.

## Railway / Always-Online Prerequisite Gate

Railway is a future deployment target, not evidence of an always-online ArchFlow service. Before a Railway or any equivalent long-running deployment can be described as ready, an approved deployment packet must prove: a service-specific build/start configuration; bind to the platform-provided port; a readiness endpoint that returns HTTP 200 during deployment; secret isolation in the platform configuration; explicit CORS/auth behavior; provider-disabled-first operation; logs and observability; a rollback/recovery procedure; and post-deploy endpoint verification.

Railway documents that healthchecks control traffic switching during deployment and are not continuous monitoring. Accordingly, a deployment-time health response alone is insufficient for an always-online claim.

## LangSmith Status

LangSmith is configured for tracing only.

- Local editable file: `project/.env.langsmith.local`.
- Public example: `project/config/langsmith.env.example`.
- Project name: `ArchFlow`.
- Project ID: `masked_langsmith_project_id`.
- API key status: present only in ignored local env.
- Smoke trace status: submitted with sanitized Ollama-only metadata.
- Model execution: Ollama only.

## Qwythos Status

Qwythos is installed and now usable through the server.

Operational routing:

- Active local model: Qwythos.
- Fallback local model: `gemma4:e4b`.
- Codex remains the review and execution layer.
