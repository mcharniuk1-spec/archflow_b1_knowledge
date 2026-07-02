# Priority Task Lane Setup

Date: 2026-07-01
Status: implemented

## Task

Create a recurring two-time daily automation lane for the 00:30 and 06:30 windows that selects the highest-priority unfinished task by urgency and importance, prepares a fresh PitAgent execution packet, and records continuity evidence.

## Changes Made

- Added two daily lanes to `project/agents/agent-roster.yaml`:
  - `archflow_priority_task_operator_midnight` (`00:30`)
  - `archflow_priority_task_operator_morning` (`06:30`)
- Added a new skill contract at `skills/priority-task-operator/SKILL.md`.
- Added `project/scripts/priority-task-operator.py` to parse `project-plan.md`, score tasks, and create:
  - `project/runs/<run-id>/selected-task.md`
  - `project/runs/<run-id>/pitagent-chat-prompt.md`
  - `project/runs/<run-id>/selected-task.json`
- Added a dedicated automation contract in `project/automation/archflow-priority-task-operator-lane.md`.
- Updated skill registries for consistency:
  - `project/agents/skills-by-agent.md`
  - `skills/skills-used.md`

## Validation Notes

- Changes are configuration and script scaffold only.
- Live-time execution of the new 00:30/06:30 trigger remains to be observed in the next Codex scheduler cycle.
- Notion and GitHub update connectors were not changed, so this lane now prepares handoff payloads instead of assuming direct writes.

## Output Files

- `project/agents/agent-roster.yaml`
- `skills/priority-task-operator/SKILL.md`
- `project/scripts/priority-task-operator.py`
- `project/automation/archflow-priority-task-operator-lane.md`
- `project/agents/skills-by-agent.md`
- `skills/skills-used.md`

## Next Action

- Trigger the lane at next scheduled windows and check generated packet files in `project/runs/<run-id>/`.
- Add Notion and GitHub connector checks as separate blockers or actions in the first successful run.
