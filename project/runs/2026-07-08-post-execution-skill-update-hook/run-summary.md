# Post-Execution Skill Update Hook

Date: 2026-07-08
Status: complete

## Current Setup Discovered

- Existing Codex prompt hook: `.codex/hooks.json` calls `project/scripts/task-handout-hook.py`.
- Existing evening automation: `project/automation/archflow-public-evening-skill-and-hook-update.md`.
- Existing daily retrospective: `project/automation/daily-skill-retrospective-and-rag-knowledge-review.md`.
- Existing skill/prompt structure: project-local skills under `skills/`, with registry references in `skills/skills-used.md`, `project/agents/skills-by-agent.md`, and `project/agents/agent-roster.yaml`.
- Existing logs/wiki structure: active run records under `project/runs/`, durable public notes under `wiki/runs/`, and chronological state in `wiki/log.md`.
- Existing execution flow: read communication files, append a starting update, perform bounded drift/review work, run validation, append completion, and write run artifacts.

## What Changed

- Added `project/scripts/post-execution-skill-update.py`.
- Added support files under `skills/evening-skill-registry-update/`.
- Updated the evening skill and automation contract to require a post-execution decision: `NO_UPDATE`, `APPEND_PATTERN`, or `PATCH_EXISTING_SKILL`.
- Updated the automation roster and skills-used registry.
- Applied one evidence-backed candidate from the July 6 daily retrospective into `skills/evening-skill-registry-update/candidate-patterns.md`.

## What Stayed Unchanged

- No new automation system, scheduler, skill registry, or orchestration layer was created.
- `.codex/hooks.json` and `project/scripts/task-handout-hook.py` remain unchanged.
- The hook remains a reminder, not an auto-writing executor.
- No provider calls, network checks, deploys, pushes, credential changes, or external writes were performed.

## Validation

- Python compile passed for the new post-execution script and existing hook/validation scripts.
- Post-execution script smoke returned `NO_UPDATE` for this run.
- Post-execution script smoke returned `PATCH_EXISTING_SKILL` for the July 6 daily retrospective and mapped it to candidate storage.
- Workflow validation passed with the project local Python environment.
- Public safety scan passed.
- `git diff --check` passed.

## Next Safe Action

Use the script during the next evening skill/hook run and record the decision in that run summary. Promote candidates only after repeated evidence or explicit review.
