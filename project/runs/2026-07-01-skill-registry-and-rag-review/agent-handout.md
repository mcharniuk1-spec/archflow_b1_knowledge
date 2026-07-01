# Skill Registry And Daily RAG Review Hardening Handout

## Title and Purpose

This handout records the 2026-07-01 hardening pass that separated the two recurring maintenance lanes:

- ArchFlow public evening skill and hook update (21:00),
- Daily Skill Retrospective and RAG Knowledge Review (22:30).

## Human Summary

The recurring maintenance system now has explicit dual-lane separation in `agent-roster.yaml`, with distinct schedules and target files. Both automation contracts now carry explicit long-term inefficiency gates and stronger tool-relevance constraints, so each lane records what should not be repeated and escalates durable constraints to long-term knowledge surfaces.

## Current State

Status: complete.

Configured scheduled lane coverage after this pass:

- `archflow_evening_skill_and_hook_update`:
  - `public/project/agents/agent-roster.yaml` evening target block,
  - `public/project/automation/archflow-public-evening-skill-and-hook-update.md`,
  - `public/skills/evening-skill-registry-update/SKILL.md`.
- `daily_skill_rag_retrospective`:
  - `public/project/agents/agent-roster.yaml` daily retrospective block,
  - `public/project/automation/daily-skill-retrospective-and-rag-knowledge-review.md`,
  - `public/skills/daily-public-project-review/SKILL.md`.

Key note: `.codex/hooks.json` was checked for alignment and remains unchanged; the required hook path is still `project/scripts/task-handout-hook.py`.

## Agent Continuation Prompt

Continue with:

- the new dual-lane automation boundary,
- lane-local no-op summaries when no target change exists,
- explicit recording of repeated non-value steps in the lane blacklist and daily knowledge update gates,
- escalation to `wiki/memory.md` and `wiki/insights.md` after repeated constraints are confirmed.

## Execution Trace

FACT: `project/agents/agent-roster.yaml` now has two distinct automation blocks for the requested lanes.

FACT: Both lane SKILL contracts were updated to include:
- lane-specific contract source identity,
- run-output checks,
- efficiency/irrelevance gates,
- and long-term knowledge update triggers.

INTERPRETATION: This separation makes scheduled intent explicit without changing the public-safe scope of the files being governed.

## Decisions

- keep `daily_evening` time split explicit in file comments and docs (`21:00`, `22:30`);
- keep each lane's no-op output explicit and avoid forcing changes when no drift is detected;
- preserve the existing hook path unless a separate migration issue is opened.

## Artifacts

- `public/skills/evening-skill-registry-update/SKILL.md`
- `public/skills/daily-public-project-review/SKILL.md`
- `public/project/automation/archflow-public-evening-skill-and-hook-update.md`
- `public/project/automation/daily-skill-retrospective-and-rag-knowledge-review.md`
- `public/project/agents/agent-roster.yaml`
- `public/skills/skills-used.md`
- `public/project/runs/2026-07-01-skill-registry-and-rag-review/run-summary.md`

## Validation

- Registry/doc alignment check completed across all edited files.
- No provider calls, no runtime starts, and no external deployment actions were performed.
- All edits remain public-safe and on targeted documentation/config files.

## Safety Boundary

This handout and all reviewed files include no credentials, secrets, private paths, private IDs, or raw private source material.
