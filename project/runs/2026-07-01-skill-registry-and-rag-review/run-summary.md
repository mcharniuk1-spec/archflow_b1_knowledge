# Skill Registry And Daily RAG Review Hardening

Date: 2026-07-01
Status: complete

## Task

Separate the recurring daily automation lanes so each has independent schedule intent and run scope, while preserving the daily retrospective/RAG focus and adding durable inefficiency controls.

## Findings

FACT: The previous configuration grouped both the evening registry maintenance and the daily retrospective review into one automation block (`evening_skill_registry_update`), which reduced schedule clarity for the 21:00/22:30 split.

FACT: Both lanes already had dedicated SKILL contracts and dedicated automation docs, but the roster lacked explicit execution separation and lane-local long-term knowledge gate language.

FACT: The `.codex/hooks.json` trigger remained aligned to `project/scripts/task-handout-hook.py` throughout this pass; no contract change was required in the hook file.

INTERPRETATION: Stable long-term reliability needs explicit schedule-by-lane ownership, because both runs can be review-only but serve different outputs.

HYPOTHESIS: Separating the automation registry blocks and forcing explicit inefficiency gates in both lanes will lower recurring false-positive churn and improve global knowledge carry-forward quality.

GAP: The live automation definitions outside this repo are not updated by this pass; this pass only normalized in-repo scheduling intent and lane contracts.

## Changes Made

- Split `project/agents/agent-roster.yaml` automation block into:
  - `archflow_evening_skill_and_hook_update` (`21:00`) with registry/hook maintenance targets, and
  - `daily_skill_rag_retrospective` (`22:30`) with review/RAG/KB/memory targets.
- Added/updated explicit lane identities in:
  - `project/automation/archflow-public-evening-skill-and-hook-update.md`,
  - `project/automation/daily-skill-retrospective-and-rag-knowledge-review.md`.
- Updated both SKILL contracts with explicit schedule/contract lineage and long-term inefficiency-to-memory gate rules:
  - `skills/evening-skill-registry-update/SKILL.md`,
  - `skills/daily-public-project-review/SKILL.md`.
- Strengthened recurring lane-level irrelevance lists in `skills/skills-used.md` for durable no-repeat behavior.
- Kept `skills-by-agent.md` and other registry files unchanged because they already matched current contracts after this split.

## Validation

- Read-through and consistency checks of all edited registry, skill, and automation documents.
- Confirmed all targets in both blocks remain public-safe and bounded.
- No provider calls, provider keys, deploy actions, or new data writes outside public-safe contract files.

## Next Actions

1. Append this hardening block to the next scheduled communication update with a clear `complete` handoff.
2. Ensure the nightly/late-evening automation definitions outside this repo map to `archflow_evening_skill_and_hook_update` and `daily_skill_rag_retrospective`.
3. During next-day execution, ensure both lanes emit their own inefficiency/blacklist notes to the appropriate memory surfaces.
