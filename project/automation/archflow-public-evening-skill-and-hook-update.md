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
- `project/scripts/post-execution-skill-update.py`
- `skills/evening-skill-registry-update/stop-rules.md`
- `skills/evening-skill-registry-update/successful-patterns.md`
- `skills/evening-skill-registry-update/failed-patterns.md`
- `skills/evening-skill-registry-update/candidate-patterns.md`
- `project/live/communication/README.md`
- `project/live/communication/current-agent-notice.md`
- `project/live/communication/agent-communication-log.md`
- `wiki/log.md` and `project/runs/` as needed for continuity.
- `project/automation/archflow-public-evening-skill-and-hook-update.md`

Write:

- `project/agents/agent-roster.yaml` (if needed),
- `project/agents/skills-by-agent.md` (if needed),
- `skills/skills-used.md` (if needed),
- existing skill support files when a post-execution review has evidence,
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
4. Run the post-execution skill update gate:
   - `python3 project/scripts/post-execution-skill-update.py --run-dir project/runs/<run-id>` for the run folder or run note being closed.
   - The gate must return `NO_UPDATE`, `APPEND_PATTERN`, or `PATCH_EXISTING_SKILL`.
   - Review-only is the default. Add `--apply` only when the evidence is concrete, public-safe, reusable, and mapped to an existing skill support file.
   - If the gate returns `NO_UPDATE`, record the reason and stop skill mutation.
   - If the gate returns `PATCH_EXISTING_SKILL`, store the candidate in an existing support file or this lane's `candidate-patterns.md` unless a human-reviewed patch to the existing skill is explicitly in scope.
5. Apply only targeted edits.
6. Run minimal safety checks on edited files.
7. Append a `complete` update in the live communication log with:
   - files touched,
   - what stayed unchanged,
   - and next safe actions.
8. Create or update the same-day run summary and agent handout.

## Required Review Standards

- No broad scope changes by default.
- No model provider calls.
- No production deployment activity.
- No private credentials, paths, or external IDs in public files.
- The hook remains a reminder, not an auto-writing executor.
- The post-execution review is evidence-gated and must not create a new skill automatically.

## Failure Handling

- If a file is missing, report exact `GAP` and do not continue speculative edits.
- If hook script path is invalid, create a corrective task in the same run summary and stop after logging the blocker.
- If post-execution evidence is insufficient, choose `NO_UPDATE`.
