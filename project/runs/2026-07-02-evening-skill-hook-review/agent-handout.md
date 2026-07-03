# Evening Skill And Hook Review Handout

## Title And Purpose

This handout records the July 2 evening review of ArchFlow public skill registries, hook contracts, and reusable project-local skill coverage.

## Human Summary

The review found one concrete registry drift item. Recent public work added two project-local skills, `arcagcom` for live-agent communication and `archflow1` for the local Jarvis dashboard stack contract. They were already listed in `skills/skills-used.md` and public run notes, but the per-agent registry and machine-readable roster did not yet expose them.

The fix was intentionally narrow. `project/agents/skills-by-agent.md` now has a shared project coordination section for these cross-role skills, and `project/agents/agent-roster.yaml` now has a `project_local_skills` section that records their scope, paths, users, and safety rules.

No hook behavior was expanded. The task-handout hook remains a routing reminder that writes only an ignored local marker. Provider activation, OpenRouter calls, Railway deployment, live Nexus/writeback, voice proof, Git push, and external publication stayed out of scope.

## Current State

- Status: complete.
- Registry state: `arcagcom` and `archflow1` are now represented in both the human-readable registry and machine-readable roster.
- Hook state: unchanged and aligned with `skills/task-handout/SKILL.md`.
- Runtime state: provider-disabled and registry-only; no services were started.
- Worktree note: unrelated OpenRouter/model-routing changes, priority mechanical-work run folders, and later live-log entries were present or appeared outside this run and were left untouched.

## Agent Continuation Prompt

Continue the ArchFlow public evening skill and hook maintenance lane. First read `AGENTS.md`, `README.md`, `project/README.md`, `project/operating-rules.md`, `project/live/communication/README.md`, `project/live/communication/current-agent-notice.md`, the latest communication log entries, `skills/evening-skill-registry-update/SKILL.md`, and this handout.

Check only for actual drift between `skills/`, `project/agents/skills-by-agent.md`, `project/agents/agent-roster.yaml`, `skills/skills-used.md`, `.codex/hooks.json`, and hook-backed workflow claims. Do not create speculative skills. Do not run network, provider, deployment, push, service-start, or private-source operations. If no drift exists, leave a no-op run note and completion log. If drift exists, update only the narrow public-safe files needed and run the lightweight validations.

Stop and record a `blocked` entry if a required registry or hook file is missing, if public-safety validation fails, or if another live communication entry claims the same file scope.

## Execution Trace

FACT:

- Required preflight files were read before edits.
- A starting live communication entry was appended before registry edits.
- `skills/task-handout/SKILL.md` and `skills/evening-skill-registry-update/SKILL.md` were read because this lane reviews subtasks, hooks, and registry drift.
- The actual `skills/` tree was compared with `skills/skills-used.md`, `project/agents/skills-by-agent.md`, and `project/agents/agent-roster.yaml`.
- Hook config, hook script, Git hooks, and workflow validation claims were inspected.
- Registry drift was limited to missing `arcagcom` and `archflow1` representation in the registry/roster.

INTERPRETATION:

- `arcagcom` and `archflow1` are shared project-local skills, not single-role AF skills.
- The existing task-handout hook contract is still appropriate and should not be expanded without a new explicit trigger, script change, and validation boundary.

## Decisions

- Added `arcagcom` and `archflow1` to a shared project coordination section in `project/agents/skills-by-agent.md`.
- Added `project_local_skills` to `project/agents/agent-roster.yaml` for machine-readable coverage.
- Left `skills/skills-used.md` unchanged because it already listed both skills.
- Did not create a new skill because no new repeated reusable workflow was found.
- Did not change `.codex/hooks.json` or `project/scripts/task-handout-hook.py` because their trigger, script path, and safety boundary remain aligned.

## Artifacts

| File | Purpose |
|---|---|
| `project/runs/2026-07-02-evening-skill-hook-review/summary.md` | Concise run summary with facts, interpretation, gaps, and files changed. |
| `project/runs/2026-07-02-evening-skill-hook-review/agent-handout.md` | Continuation context for the next operator or scheduled run. |
| `project/agents/skills-by-agent.md` | Human-readable registry updated with shared project-local skills. |
| `project/agents/agent-roster.yaml` | Machine-readable roster updated with `project_local_skills`. |

## Validation

Final validation outcomes:

- `.codex/hooks.json` JSON parse: passed.
- `project/agents/agent-roster.yaml` YAML parse: passed.
- Hook script bytecode compile: passed.
- Workflow validation: passed.
- Task-handout hook readiness probe: passed.
- Public safety scan: passed.
- Ignored local env/runtime checks: passed.
- Tracked text ASCII check: passed.
- `git diff --check`: passed.
- `git status --short`: showed this run's files plus unrelated OpenRouter/model-routing changes, priority mechanical-work run folders, and other live-log activity outside this run.

## Next Actions

1. On the next evening run, verify whether any new SKILL contracts were added after this handout.
2. Keep `arcagcom` and `archflow1` in shared project-local skill coverage unless an explicit deactivation decision is recorded.
3. Continue treating provider/runtime activation as out of scope for this maintenance lane.

## Safety Boundary

Keep public files English-only and repo-relative. Do not store secrets, credentials, private URLs, local absolute paths, account identifiers, raw private source material, screenshots, personal identifiers, provider values, or deployment metadata.
