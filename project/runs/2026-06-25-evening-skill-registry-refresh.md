# Evening Skill Registry Refresh

Date: 2026-06-25
Automation: ArchFlow public evening skill update
Status: completed

## Scope

Refresh only public-safe project files and validate the current skill registry state.

## What Changed

- Added `archflow-task-breakdown` to `project/agents/agent-roster.yaml` for `af_manager`.
- Added the same skill to `skills/skills-used.md` because it is present in `skills/` and already referenced in the human-readable registry.

## Validation

- YAML parsing for the updated machine-readable files.
- Public-safety pattern scan for local absolute paths, private Notion links, and common secret markers in the touched files.
- Git ignored-file check for local env/runtime paths.
- Git status review.

## Notes

- No provider credentials, local env files, runtime packages, or network actions were changed.
- No other skill registry edits were needed because the remaining listed skills still match the current public project setup.
