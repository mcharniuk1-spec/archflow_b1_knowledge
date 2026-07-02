# ArchFlow Priority Task Operator Lane

Automation IDs: `archflow-priority-task-operator-0030`, `archflow-priority-task-operator-0630`

Status: active in Codex app automation.

Schedule: daily at 00:30 and 06:30.

Contract source: `project/agents/agent-roster.yaml` (`archflow_priority_task_operator_midnight` and `archflow_priority_task_operator_morning` job lanes).

## Purpose

Run a recurring deterministic task-selection and handoff lane that keeps execution moving by urgency and importance, while preserving full audit evidence.

The lane does not invent private identifiers, raw links, or private completion claims.

## Scope

Read:

- `project/agents/agent-roster.yaml`
- `project/project-plan.md`
- `skills/priority-task-operator/SKILL.md`
- `project/scripts/priority-task-operator.py`
- `project/live/communication/agent-communication-log.md`
- `project/runs/` (latest run artifacts)
- `wiki/log.md`

Write:

- `project/runs/<run-id>/selected-task.md`
- `project/runs/<run-id>/pitagent-chat-prompt.md`
- `project/runs/<run-id>/run-summary.md`
- `project/live/communication/agent-communication-log.md`
- `wiki/log.md`

## Procedure

1. Run the selector:

`python3 project/scripts/priority-task-operator.py --plan project/project-plan.md --run-id <run-id> --max-recent-completed 8`

2. Require the script outputs to contain:

- ranked candidates
- completed-task context block
- one selected task
- `pitagent` handoff prompt path

3. If selected task has explicit execution details in the source plan, append a follow-up execution packet in the same run folder. Otherwise, keep a safe no-op update and include the missing details as `GAP`.

4. Generate a PitAgent handoff packet (`pitagent-chat-prompt.md`) for the next operator chat.

5. In that chat packet:

- review completed tasks from this lane
- validate selected task execution readiness
- run KB update checks
- prepare Notion payload and repository push status

6. Update `project/live/communication/agent-communication-log.md` with concise facts and blockers.

7. If public safety constraints pass, append a short status line to `wiki/log.md`.

## Notion / KB / GitHub follow-up protocol

- The lane is responsible for preparing signed payload artifacts:
  - `KB update packet` (short summary and evidence references)
  - `Notion payload template` (status text and task ID updates)
  - `git push command list` (commands that can be executed after approval)
- A Notion or GitHub write is considered complete only when connector evidence is captured.
- If no connector is available, output `GAP` and keep the command list in a safe handoff packet for the next chat.

## Validation

- `python3 scripts/public_safety_scan.py`
- `python3 project/scripts/priority-task-operator.py --plan project/project-plan.md --run-id <run-id> --max-recent-completed 8`
- YAML/JSON parse for modified automation and log artifacts in the same cycle.

## Failure Handling

- If `project-plan.md` format changes and parsing fails, create a `GAP` entry and preserve the last successful selected-task packet.
- If parsing succeeds but no actionable task exists, output a `GAP: no active tasks found` and skip task execution.
- If Notion or GitHub connectors are not configured, keep the lane in evidence mode and assign the handoff to the next operator chat.
