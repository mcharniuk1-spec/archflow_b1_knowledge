# Run - LangSmith And WikiLLM Setup

Date: 2026-06-25
Scope: public project folder

## Task

Configure LangSmith tracing for the public ArchFlow project with project ID `masked_langsmith_project_id`, keep model execution on Ollama only, update current reports, and set up WikiLLM inside the public project.

## Outputs

- `project/config/langsmith.env.example`
- `project/.env.langsmith.local`
- `project/langsmith-setup.md`
- `project/config/model-routing.yaml`
- `project/workflows/langgraph-controller.yaml`
- `project/reports/2026-06-25-chat-execution-report.md`
- `wiki/`

## Status

FACT: LangSmith is configured for tracing only.

FACT: The API key is not stored in Git.

FACT: Qwythos now loads and generates text through Ollama.

FACT: LangGraph remains a configured workflow contract, not an installed runtime.

GAP: No trace has been sent to LangSmith yet because the API key is not present.

