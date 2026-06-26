# Log

## 2026-06-25

- Public project was created and published.
- Codex was set as primary operator layer.
- Ollama was connected as local model execution layer.
- Qwythos was verified as present and generating text.
- LangSmith tracing env was configured with project ID `057edf33-a328-4186-9425-3306186149ef`.
- Public WikiLLM structure was created inside the repository.
- Educational setup summary and agent plan were added under `project/reports/`.
- Integrated knowledge-operation plan and Git pre-push public-safety hook were added.
- LangSmith SDK was installed locally in ignored runtime and a sanitized smoke trace was submitted.
- Phase 2 local dashboard was added for read-only monitoring of WikiLLM, LangGraph, CrewAI, LlamaIndex, LangSmith, env/config, and project activity.

## 2026-06-26

- LangGraph was installed in the project local runtime and a sanitized smoke workflow passed with approved status.
- Pydantic and PyYAML workflow validation was added for workflow and routing configuration.
- LlamaIndex was installed and an approved-public-corpus retrieval proof returned 58 documents and source-path results.
- CrewAI was installed and a config/import check was added without running LLM tasks.
- CrewAI guard execution was bounded to ignored project-local runtime storage with telemetry/tracking disabled.
- The saved `archflow-e1-runtime-guard` skill was added and connected to the Git pre-push hook.
- The pre-push runtime guard passed: workflow validation, LangGraph smoke, LlamaIndex corpus, and CrewAI config.
- A sanitized E1.2 preparation packet was created under `project/runs/2026-06-26-june24-next-steps-proof/`.
