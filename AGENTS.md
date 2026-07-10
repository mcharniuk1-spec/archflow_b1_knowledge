# Public ArchFlow Agent Contract

Operate from this public folder first.

Read:

1. `README.md`
2. `project/README.md`
3. `project/operating-rules.md`
4. `project/project-plan.md`
5. `project/agentic-stack.md`
6. `project/context/README.md`
7. `project/context/cag-core.yaml`
8. `project/agents/skills-governance.md`
9. `project/provider-setup.md`
10. `project/workflows/langgraph-controller.yaml`
11. `project/workflows/crewai-crew.yaml`
12. `project/workflows/llamaindex-rag.yaml`
13. `project/reports/2026-06-25-layer-setup-report.md`
14. `project/future-actions-and-parameters.md`
15. `wiki/index.md`
16. `wiki/memory.md`
17. `wiki/rules/public-wikillm-contract.md`
18. `skills/task-handout/SKILL.md` when the prompt hook asks for it, when using one or more agents, or when solving one or more subtasks.

Rules:

- Use English only.
- Keep outputs public-safe.
- Do not write secrets or private workspace references.
- Do not use absolute local paths in public files.
- Put all new active work under `project/`.
- Put sanitized prior-work summaries under `history/`.
- Do not copy raw legacy files into this folder unless they pass a public-safety review.
- Codex authentication is the current main operator/publication path.
- Watchdog, executor, verifier, safety-reviewer, integrator, and external-action labels are bounded role contracts, not permanent assignments to a named runtime. A compatible runtime may fulfil a role only when its task contract grants the same authority and it meets that role's evidence and safety gates.
- Codex is the current local executor, reviewer, file editor, validator, and final integration boundary; this does not activate a provider, deployment, or external writeback path.
- Hermes is the current planned watchdog/controller/reviewer label. Any compatible watchdog runtime remains non-executing: it does not edit files, deploy, mutate task boards, activate providers, or approve its own high-risk output.
- Before broad or multi-agent work, assemble CAG core, retrieve bounded RAG evidence only when needed, build a context capsule, and create task contracts.
- Ollama is only for local minor/background tasks unless later approved.
- Provider actions that start local services, create env files, install packages, repair models, connect external API credentials, call providers, or write externally require explicit approval.
- Linear is optional only. Use repo-native Markdown/YAML/JSON task packets by default.
- Record substantial public-safe work in `wiki/runs/` and append `wiki/log.md`.
- If `.codex/hooks.json` emits `TASK_HANDOUT_HOOK_TRIGGER=required`, read `skills/task-handout/SKILL.md` and maintain a run handout before final response.
- Any execution that uses one or more agent roles or solves one or more subtasks must create or update `agent-handout.md` beside the run artifacts.
- Before pushing, run `scripts/public_safety_scan.py`; the tracked pre-push hook also runs it automatically.
