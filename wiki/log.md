# Log

## 2026-06-25

- Public project was created and published.
- Codex was set as primary operator layer.
- Ollama was connected as local model execution layer.
- Qwythos was verified as present and generating text.
- LangSmith tracing env was configured with project ID `masked_langsmith_project_id`.
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
- A reusable `task-handout` skill was added, and the E1.1/E1.2 execution received an agent-readable handout with human summary, continuation prompt, decisions, validation, and next actions.
- The `task-handout` skill was connected to a prompt hook and workflow rule for prompts or executions that use one or more agents or solve one or more subtasks.
- E1.2 full-test graph ran and produced the PRD, streaming report, system report, task matrix, KB update, review report, and agent handout.
- Tracked public files now mask operational project identifiers.
- The approved LlamaIndex corpus now explicitly includes public WikiLLM files under `wiki/`.
- E1.2 Notion status sync prepared the owner next-steps document, report links, and evidence-backed state map: E1.2 parent in Review, E1.2.1 through E1.2.7 Done, and E1.3 ready after owner acceptance.
- The evening skill refresh corrected stale current-state proof-run wording in `project/agentic-stack.md`, confirmed the public skill registries already matched the configured skills, and recorded the automation pass under `project/runs/` and `wiki/runs/`.

## 2026-06-27

- The evening skill audit confirmed the public skill registries still matched the current saved skills and workflow setup.
- Lightweight validation found non-ASCII generated glyphs in `graphify-out/GRAPH_REPORT.md`; the report was normalized to ASCII-safe punctuation and the maintenance pass was recorded under `project/runs/` and `wiki/runs/`.

## 2026-06-28

- The evening status refresh confirmed the public skill registries still matched the current saved skills and workflow setup, so no registry edits were needed.
- The maintenance pass refreshed stale current-state wording in the June 25 setup and dashboard reports so they now match the saved runtime validation and proof artifacts.
- `project/dashboard/data.json` was regenerated after the report refresh, and lightweight YAML, public-safety, ASCII, and ignored-path checks passed on the public project scope.

## 2026-06-29

- The June 29 tool and market reports were integrated into the current E1-E7 plan.
- Loop Engineering was added as the L1 report-only operating contract under `project/loops/`.
- `project/workflows/market-research-engine.yaml` was added for E2 account evidence, signal extraction, ICP scoring, role verification, and reviewed outreach handoff.
- The agent roster now includes AF Research and AF Copy roles.
- Cognee, turbovec, and Mistral were documented as gated future layers, not activated runtime dependencies.
- The plan now treats product/software/AI service agencies as the first ICP hypothesis and Client Discovery-to-Backlog Pack as the first offer hypothesis.
- Targeted Notion E2 updates were applied after product-owner verification: E2 parent and related E2.1/E2.2/E2.3/E2.5 pages received append-only notes, and three Backlog research tasks were added.
