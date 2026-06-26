# Run - LangSmith And Public WikiLLM Setup

Date: 2026-06-25

## Task

Configure LangSmith tracing using project ID `masked_langsmith_project_id`, keep execution on Ollama only, and set up WikiLLM inside the public project.

## Inputs

- User-provided LangSmith project ID.
- Existing public ArchFlow project structure.
- Current Ollama/Qwythos local model state.

## Outputs

- `project/config/langsmith.env.example`
- `project/.env.langsmith.local`
- `project/langsmith-setup.md`
- `project/config/model-routing.yaml`
- `project/workflows/langgraph-controller.yaml`
- `project/reports/2026-06-25-chat-execution-report.md`
- `wiki/index.md`
- `wiki/memory.md`
- `wiki/insights.md`
- `wiki/log.md`
- `wiki/rules/public-wikillm-contract.md`
- `wiki/decisions/2026-06-25-codex-ollama-langsmith-boundary.md`
- `wiki/issues/2026-06-25-langsmith-api-key-missing.md`

## Checks

- Ollama inventory found Qwythos.
- Qwythos generated text through Ollama.
- Real LangSmith API key was not stored.
- Cloud model keys were not added.

## Remaining Gaps

- LangSmith API key must be added manually.
- Runtime packages are not installed.
- No trace has been sent to LangSmith yet.

