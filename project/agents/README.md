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
| Model-Efficiency Observer | Recurring model/token efficiency review and advice. |

See `skills-by-agent.md` and `agent-roster.yaml`.

Live communication:

- `../live/communication/README.md`
- `../live/communication/current-agent-notice.md`
- `../live/communication/agent-communication-log.md`

Every agent must read the live communication notice and append a starting update before editing project files.

Workflow contracts:

- `../workflows/langgraph-controller.yaml`
- `../workflows/crewai-crew.yaml`
- `../workflows/llamaindex-rag.yaml`

Model-efficiency observer:

- `model-efficiency-advice.md`
- `model-efficiency-issues.md`
- `../automation/yushchenko-model-efficiency-observer.md` (legacy file name; functional role is Model-Efficiency Observer)

The observer runs on a five-hour cadence through a Codex app automation. It reports actual model/token evidence only. If OpenRouter has no active runtime evidence, it must say that plainly instead of estimating usage.
