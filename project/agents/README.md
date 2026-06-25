# Agents

This folder defines only the agents and skills used or explicitly set up for the public ArchFlow project.

It does not publish the operator's full private skill library.

## Agent Team

| Agent | Purpose |
|---|---|
| AF Tools | Source and tool inventory. |
| AF Context | Structured context extraction. |
| AF Manager | PRD, backlog, responsibility, and success criteria. |
| AF Knowledge | Knowledge-base update packets. |
| AF Review | Public-safety and evidence review. |
| AF Publisher | Git/public project publishing. |

See `skills-by-agent.md` and `agent-roster.yaml`.

Workflow contracts:

- `../workflows/langgraph-controller.yaml`
- `../workflows/crewai-crew.yaml`
- `../workflows/llamaindex-rag.yaml`
