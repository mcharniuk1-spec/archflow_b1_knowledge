# Run - Codex Main Agentic Workflow Setup

Date: 2026-06-25
Scope: public project folder

## Task

Set Codex authentication as the main setup and publication path, keep Ollama for local minor/background tasks, and make the LangGraph, CrewAI, LlamaIndex, agent, and output-document layers explicit.

## Outputs

- `project/config/model-routing.yaml`
- `project/config/providers.env.example`
- `project/provider-setup.md`
- `project/agentic-stack.md`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/workflows/llamaindex-rag.yaml`
- `project/outputs/`
- `project/reports/2026-06-25-layer-setup-report.md`
- `project/future-actions-and-parameters.md`

## Status

FACT: Codex is the primary operator and publication layer.

FACT: Ollama is connected for local minor/background tasks.

FACT: Qwythos remains installed but not loadable in the current smoke test.

FACT: `gemma4:e4b` is the verified local fallback model.

INTERPRETATION: The public project is now structured enough to run the first proof workflow, but LangGraph, CrewAI, and LlamaIndex are not installed as runtime packages yet.

GAP: The first proof-run output documents have templates but no completed source-grounded run content yet.

