# ArchFlow Public Evening Skill And Hook Update

Automation ID: `archflow-public-evening-skill-update`

Status: active in Codex app automation.

Schedule: daily at 21:00.

Contract source: `project/agents/agent-roster.yaml` (`archflow_evening_skill_and_hook_update`).

## Purpose

Run a bounded, no-amnesia nightly maintenance lane that keeps skill registries and handout hook contracts aligned and updates only when needed.

## Scope

Read:

- `project/agents/agent-roster.yaml`
- `project/agents/skills-by-agent.md`
- `skills/skills-used.md`
- `skills/evening-skill-registry-update/SKILL.md`
- `.codex/hooks.json`
- `skills/task-handout/SKILL.md`
- `project/scripts/task-handout-hook.py`
- `project/live/communication/README.md`
- `project/live/communication/current-agent-notice.md`
- `project/live/communication/agent-communication-log.md`
- `wiki/log.md` and `project/runs/` as needed for continuity.
- `project/automation/archflow-public-evening-skill-and-hook-update.md`

Write:

- `project/agents/agent-roster.yaml` (if needed),
- `project/agents/skills-by-agent.md` (if needed),
- `skills/skills-used.md` (if needed),
- `project/runs/<run-id>/run-summary.md`,
- `project/runs/<run-id>/agent-handout.md`,
- `project/live/communication/agent-communication-log.md`.

Where `<run-id>` is date-based and can include `skill-registry` to signal scope.

## Long-Term Relevance Review Gate

At the end of every run, the lane must decide whether any recurring helper actions were ineffective in this cycle:

- `graphify` regeneration for registry-only maintenance.
- broad network probes used as maintenance proof.
- model-provider calls for file sync.
- full-repo scans where only registry files changed.

Ineffective tools are moved into the lane's recurring `do-not-repeat` list and promoted to wiki memory only when repeated across cycles.

## Procedure

1. Read the two communication files and append a `starting` update before edits.
2. Load the `evening-skill-registry-update` skill contract from `skills/evening-skill-registry-update/SKILL.md`.
3. Run registry drift checks:
   - each skill used in configured agents must have a SKILL contract,
   - each scheduled skill must be auditable through run artifacts,
   - hook command path must still target `project/scripts/task-handout-hook.py`.
4. Apply only targeted edits.
5. Run minimal safety checks on edited files.
6. Append a `complete` update in the live communication log with:
   - files touched,
   - what stayed unchanged,
   - and next safe actions.
7. Create or update the same-day run summary and agent handout.

## Required Review Standards

- No broad scope changes by default.
- No model provider calls.
- No production deployment activity.
- No private credentials, paths, or external IDs in public files.
- The hook remains a reminder, not an auto-writing executor.

## Failure Handling

- If a file is missing, report exact `GAP` and do not continue speculative edits.
- If hook script path is invalid, create a corrective task in the same run summary and stop after logging the blocker.
