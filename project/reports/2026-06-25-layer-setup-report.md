# Layer Setup Report

Date: 2026-06-25
Status: public setup completed locally and published to GitHub.

## 1. Public Repository Layer

FACT: The public project root is this repository folder.

Parameters:

- Active folder: repo root.
- Active work folder: `project/`.
- Public history folder: `history/`.
- Skill registry folder: `skills/`.
- Ignored local config: `project/.env.local`.
- Ignored runtime state: `project/local/`.

Status:

- Public files are English-only.
- Local paths, private links, credentials, raw private source exports, and personal identifiers are excluded.
- A local Git commit exists.

## 2. Authentication And Runtime Layer

FACT: Codex is the primary operator runtime. GitHub publication is operated from Codex through verified Git SSH transport.

Parameters:

- `ARCHFLOW_PROVIDER_MODE=codex_auth_main`
- `CODEX_OPERATOR_MODE=codex_app`
- `CODEX_AUTH_EXPORTS_API_KEY=false`
- `CODEX_GITHUB_PUBLICATION=codex_operated_git_ssh`

Interpretation:

- Codex auth is used to operate this setup.
- GitHub publication uses the working Git SSH remote.
- Codex auth is not an exportable API key for Python frameworks.
- If direct OpenAI API use is needed later, a separate approved API key flow is required.

## 3. Model Provider Layer

FACT: Ollama is connected for local background tasks.

Parameters:

- `OLLAMA_BASE_URL=http://127.0.0.1:11434`
- `OLLAMA_CHAT_MODEL=hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M`
- `OLLAMA_FALLBACK_CHAT_MODEL=gemma4:e4b`
- `OLLAMA_EMBED_MODEL=nomic-embed-text`
- `OLLAMA_TASK_SCOPE=minor_background_tasks`

Status:

- Ollama service started.
- Qwythos is present in the local model inventory.
- Qwythos metadata is readable.
- Qwythos now loads and generates text through Ollama.
- `gemma4:e4b` remains the fallback model.

Operational decision:

- Codex handles orchestration, final review, and publication.
- Ollama handles minor/background local tasks with Qwythos as the active local model.

## 4. LangGraph Layer

Purpose: control the reasoning path.

Current file: `project/workflows/langgraph-controller.yaml`

Current nodes:

- intake validation
- bounded retrieval
- context digest
- PRD crew run
- task matrix
- KB update
- review gate
- publish or revise

Status:

- Configured as a workflow contract.
- Runtime package is not installed yet.
- No LangGraph execution trace exists yet.
- LangSmith tracing is configured but awaiting the API key.

## 4A. LangSmith Layer

Purpose: trace LangGraph/CrewAI/LlamaIndex execution without changing model provider.

Parameters:

- project name: `ArchFlow`
- project id: `057edf33-a328-4186-9425-3306186149ef`
- endpoint: `https://eu.api.smith.langchain.com`
- local env file: `project/.env.langsmith.local`
- public example: `project/config/langsmith.env.example`
- API key status: waiting for manual insertion
- model execution: Ollama only

Status:

- Configured.
- Not tested against LangSmith because no API key is present.

## 5. CrewAI Layer

Purpose: organize agents as a team.

Current file: `project/workflows/crewai-crew.yaml`

Current crew:

- AF Tools
- AF Context
- AF Manager
- AF Knowledge
- AF Review
- AF Publisher

Process:

- sequential
- Codex-supervised manager mode
- memory disabled for now
- cache enabled
- output log target: `project/outputs/crew-log.json`

Status:

- Configured as a crew contract.
- Runtime package is not installed yet.
- No CrewAI execution output exists yet.

## 6. LlamaIndex RAG Layer

Purpose: connect agents and LLMs to approved data.

Current file: `project/workflows/llamaindex-rag.yaml`

Current approved corpus:

- `project/`
- `history/`
- `skills/`

Current excluded corpus:

- Git internals
- local env files
- local runtime files
- raw exports
- private folders
- secrets
- temp files

Parameters:

- chunk size: 800
- chunk overlap: 120
- retrieval top k: 5
- response mode: compact
- source paths required: true
- private-source refusal: true
- index persistence target: `project/local/rag_index` ignored by Git

Status:

- Configured as a RAG contract.
- Runtime package is not installed yet.
- No vector index exists yet.

## 7. Output Document Layer

Current folder: `project/outputs/`

Templates exist for:

- source inventory
- retrieval log
- context digest
- PRD
- task and responsibility matrix
- KB update
- review report
- run summary

Status:

- Output documents are defined.
- First proof-run documents are not completed yet.

## 8. Automation Layer

Automation: ArchFlow public evening skill update.

Schedule: every evening.

Scope:

- Refresh only used or set-up skill registries.
- Write a run note only when there is meaningful public-safe change.
- Run lightweight validation.
- Do not push, install, start services, or alter credentials without later approval.

## 9. Verification Layer

Checks run:

- YAML parse for model routing and agent roster.
- ASCII-only public file check.
- Sensitive pattern scan for local paths, private links, personal names, and common secret patterns.
- Git ignored-file check for local env and runtime state.

Known gap:

- Remote publication through plain local HTTPS Git is blocked by missing GitHub credentials in the shell.
- Git SSH transport is verified and configured as the local `origin`.
- Published commit: `b73137e`.

## References Checked

- LangGraph official overview: https://docs.langchain.com/oss/python/langgraph/overview
- CrewAI crews documentation: https://docs.crewai.com/en/concepts/crews
- LlamaIndex concepts documentation: https://developers.llamaindex.ai/python/framework/getting_started/concepts/
