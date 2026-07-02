# Priority Task Lane Setup Handout

## Title and Purpose

Set up two recurring morning automation lanes (00:30 and 06:30) that do deterministic task prioritization from `project/project-plan.md` and generate a standardized handoff packet for the next operator.

## Human Summary

The following was implemented in this run:

- New automation entries in `project/agents/agent-roster.yaml` for 00:30 and 06:30.
- New dedicated skill `priority-task-operator`.
- New selector script `project/scripts/priority-task-operator.py`.
- New automation contract `project/automation/archflow-priority-task-operator-lane.md`.
- Skill registry updates in `project/agents/skills-by-agent.md` and `skills/skills-used.md`.

## Execution Continuation Prompt

You are the next Codex/operator for this setup. On the next run:

1. Ensure `project/scripts/priority-task-operator.py` parses plan rows correctly after any plan format changes.
2. Let one full scheduled cycle run at 00:30 and one at 06:30.
3. Open produced `project/runs/<run-id>/selected-task.md` and `pitagent-chat-prompt.md`.
4. If a task is selected, execute it or prepare a concrete follow-up packet.
5. Verify that KB (`wiki/log.md`) and Notion packet steps are generated as handoff-ready, not silently skipped.
6. Push only when execution outputs exist and `scripts/public_safety_scan.py` is clean.

## Checks

- `python3 scripts/public_safety_scan.py` (recommended before every publication).
- Manual review of generated task packet and PitAgent prompt.
