# ArchFlow Codex Project Configuration Prompt v2

Use this after the global Codex loop prompt when working in the public ArchFlow project.

## Required Read Order

1. `AGENTS.md`
2. `project/operating-rules.md`
3. `project/project-plan.md`
4. `project/live/communication/README.md`
5. `project/live/communication/current-agent-notice.md`
6. Latest entries in `project/live/communication/agent-communication-log.md`
7. `project/agentic-stack.md`
8. `project/workflows/langgraph-controller.yaml`
9. `project/workflows/crewai-crew.yaml`
10. `project/workflows/llamaindex-rag.yaml`
11. `project/agents/agent-roster.yaml`
12. `project/agents/skills-by-agent.md`
13. Relevant skills and latest run handout.

## Required Behavior

- Append a public-safe starting update before edits.
- Preserve unrelated user or other-agent changes.
- Use repo-relative paths in public files.
- Keep AGENTS and routing rules short; put details in project docs and run packets.
- Prefer Markdown/YAML/JSON task packets over external task systems.
- Keep provider, writeback, deploy, Notion, Telegram, Railway, Linear, Figma, and Git push approval-gated.

## Required Update Areas For This Package

- Reports and prompt summaries.
- Hermes watchdog/controller plan.
- CAG/RAG context capsule schema and procedure.
- LangGraph, CrewAI, LlamaIndex, roster, and skill governance updates.
- Service-company operating model.
- Market/content/sales templates.
- E1-E7 Notion-ready task packet.
- Architecture PDF/report.
- Run handout and validation results.

## Minimum Checks

- Public safety scan.
- Dashboard data regeneration and JSON parse if public text changes.
- YAML parse for changed workflows/agent files.
- JSON parse for changed schema/capsule/dashboard files.
- Python compile for changed Python files.
- `git diff --check`.
