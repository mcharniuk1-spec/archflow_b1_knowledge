# Run Note: Task Handout Skill

## Task

Add a reusable handout process for substantial ArchFlow executions and produce a handout for the completed E1.1 runtime setup plus E1.2 dialogue proof preparation.

## Outputs

- Added `skills/task-handout/SKILL.md`.
- Added `project/runs/2026-06-26-june24-next-steps-proof/agent-handout.md`.
- Updated the skill registry and agent skill routing.
- Added a prompt hook contract through `.codex/hooks.json`.
- Added `project/scripts/task-handout-hook.py` to detect prompts and executions that require the skill without storing raw prompt text.

## Decision

Future substantial runs should produce a readable handout beside the run artifacts. The handout must include a human summary, a copy-ready continuation prompt, current state, decisions, artifacts, validation evidence, next actions, and safety boundary.

The handout skill is now mandatory when a prompt hook triggers, when one or more agent roles are used, or when one or more subtasks are solved or changed.

## Status

Ready for future agents to use after large executions or handoffs.
