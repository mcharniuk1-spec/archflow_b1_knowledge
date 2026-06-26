# Public ArchFlow Agent Contract

Operate from this public folder first.

Read:

1. `README.md`
2. `project/README.md`
3. `project/operating-rules.md`
4. `project/project-plan.md`
5. `project/agentic-stack.md`
6. `project/provider-setup.md`
7. `project/workflows/langgraph-controller.yaml`
8. `project/workflows/crewai-crew.yaml`
9. `project/workflows/llamaindex-rag.yaml`
10. `project/reports/2026-06-25-layer-setup-report.md`
11. `project/future-actions-and-parameters.md`
12. `wiki/index.md`
13. `wiki/memory.md`
14. `wiki/rules/public-wikillm-contract.md`
15. `skills/task-handout/SKILL.md` when the prompt hook asks for it, when using one or more agents, or when solving one or more subtasks.

Rules:

- Use English only.
- Keep outputs public-safe.
- Do not write secrets or private workspace references.
- Do not use absolute local paths in public files.
- Put all new active work under `project/`.
- Put sanitized prior-work summaries under `history/`.
- Do not copy raw legacy files into this folder unless they pass a public-safety review.
- Codex authentication is the main operator/publication path.
- Ollama is only for local minor/background tasks unless later approved.
- Provider actions that start local services, create env files, install packages, repair models, or connect external API credentials require explicit approval.
- Record substantial public-safe work in `wiki/runs/` and append `wiki/log.md`.
- If `.codex/hooks.json` emits `TASK_HANDOUT_HOOK_TRIGGER=required`, read `skills/task-handout/SKILL.md` and maintain a run handout before final response.
- Any execution that uses one or more agent roles or solves one or more subtasks must create or update `agent-handout.md` beside the run artifacts.
- Before pushing, run `scripts/public_safety_scan.py`; the tracked pre-push hook also runs it automatically.
