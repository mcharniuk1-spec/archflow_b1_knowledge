---
name: priority-task-operator
description: Select the highest priority unfinished task by urgency and importance from `project-plan.md`, start the execution handoff as a fresh operator/chat packet, and prepare KB + Notion + GitHub follow-up evidence.
---

# Priority Task Operator

## Purpose

Use this skill for the 00:30 and 06:30 recurring automation lanes that must:

1. Review completed task history and all active/task pipeline rows.
2. Rank unfinished tasks by urgency and importance.
3. Start execution of the top-priority task with a compact handoff packet.
4. Prepare a fresh PitAgent handoff chat and reliability checkpoints.
5. Produce machine-readable update artifacts for KB/Notion/GitHub follow-up.

## Input scope

Read:

- `project/operating-rules.md`
- `project/project-plan.md`
- `project/automation/archflow-priority-task-operator-lane.md`
- `project/live/communication/agent-communication-log.md`
- `skills/priority-task-operator/SKILL.md`
- `project/scripts/priority-task-operator.py`

Read recent run proof artifacts for continuity where available:

- `project/runs/`
- `wiki/log.md`

## Execution Contract

1. Run the task selection script:

- `python3 project/scripts/priority-task-operator.py --plan project/project-plan.md --run-id <run-folder-name>`

2. Include all categories in the analysis:

- Completed tasks (for recency context).
- Current tasks (`In Progress`, `Review`, `To Do`, `Backlog`).
- Upcoming tasks (any row with a due date in the future and no completed status).

3. Rank with these scoring principles (exact formula is in script logic):

- urgency from due date distance (overdue tasks dominate).
- importance from type (Sales and Ops highest by default, then Website/Research, then Docs).
- active-status penalty or boost (`Done` excluded from execution, `In Progress` usually preferred when urgent and stable).

4. Write the selected task packet for automation evidence:

- `project/runs/<run-folder-name>/selected-task.md` with ranked list and rationale.
- `project/runs/<run-folder-name>/pitagent-chat-prompt.md` containing the fresh chat handoff payload.

5. Start the execution package as a new PitAgent handoff:

- do not execute arbitrary high-risk claims in `project-plan.md` without scope proof.
- if the selected task is technical/source-bound, include concrete check commands in the same prompt.
- update `project/live/communication/agent-communication-log.md` and `wiki/log.md` when execution artifacts are produced.

6. For this operator lane, reliability gates are mandatory:

- if automation output cannot be verified as completed in this cycle, mark `GAP` in the run summary.
- never mark task completion when only a handoff file exists.
- prefer no-op updates over speculative edits.

7. Notion and GitHub steps:

- include explicit Notion and GitHub action packets in the handoff prompt.
- if a connector is unavailable, report a clear `GAP: Notion push unavailable in local lane`.

## Outputs

- `project/runs/<run-folder-name>/selected-task.md`
- `project/runs/<run-folder-name>/pitagent-chat-prompt.md`
- optional `project/runs/<run-folder-name>/run-summary.md` with checks and blockers.

## Reliability Rules

- The selected task must include at least one status-aware rationale line with urgency + importance explanation.
- At least one completed-task summary row must be included in every run.
- The run must append a `task-id`/`selected_task` pointer for continuity.
- Do not mark success if KB/Notion/GitHub steps are still queued as manual actions.
