# 2026-07-08 Run Note: Post-Execution Skill Update Hook

Status: complete.

## Task

Add a controlled post-execution skill-update mechanism to the existing ArchFlow public evening skill and hook lane.

## Current Setup Discovered

- Existing prompt hook: `.codex/hooks.json` calls `project/scripts/task-handout-hook.py` on `UserPromptSubmit`.
- Existing automation lane: `project/automation/archflow-public-evening-skill-and-hook-update.md`.
- Existing retrospective lane: `project/automation/daily-skill-retrospective-and-rag-knowledge-review.md`.
- Existing project-local skills live under `skills/`.
- Existing public run records live under `project/runs/` and `wiki/runs/`.
- Existing validation includes workflow validation, public safety scan, Python compile checks, and diff checks.

## Change

Added a deterministic script and support files so completed run folders or run notes can be reviewed for reusable skill lessons without creating a new automation layer.

## Boundary

The new mechanism defaults to `NO_UPDATE` unless evidence supports a reusable update. It never creates new skills automatically and does not rewrite `SKILL.md` files.

## Validation

Validation passed for Python compile, script smoke, workflow validation, public safety scan, and diff check. Detailed results are recorded in the matching project run summary and handout.
