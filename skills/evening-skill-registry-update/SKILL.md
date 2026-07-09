---
name: evening-skill-registry-update
description: Review and align the public ArchFlow skill registry and handout hook with actual configured agents, skills, and evidence surfaces so recurring maintenance stays stable and low-entropy across days.
---

# ArchFlow Evening Skill Registry And Hook Update

## Purpose

Use this skill for the nightly ArchFlow public maintenance job that keeps:

- `project/agents/skills-by-agent.md`
- `project/agents/agent-roster.yaml`
- `skills/skills-used.md`
- `.codex/hooks.json`

in consistent sync for a stable handoff workflow and predictable daily output.

## When To Use

- In the nightly public maintenance lane before any broad report or dashboard update.
- When skill names drift between code and registry files.
- After any hook or skill contract change.
- When automation notes report that no functional change is needed and a low-entropy no-op is valid.

## Required Inputs

Read all of:

- `project/operating-rules.md`
- `project/agents/agent-roster.yaml`
- `project/agents/skills-by-agent.md`
- `skills/skills-used.md`
- `.codex/hooks.json`
- `skills/task-handout/SKILL.md`
- `project/scripts/task-handout-hook.py`
- `project/scripts/post-execution-skill-update.py`
- `skills/evening-skill-registry-update/stop-rules.md`

Optional but recommended:

- `project/runs/` for current-day artifacts from prior evening run.
- `project/live/communication/agent-communication-log.md`.

## Procedure

1. Build the actual skill registry:
   - List all skill names in `project/agents/skills-by-agent.md`.
   - List all SKILL contracts under `skills/`.
   - List automation skill names in `project/agents/agent-roster.yaml`.
2. Resolve mismatches:
   - If a configured skill has no SKILL contract, add the missing contract if it is repeatedly used.
   - If a SKILL contract is registered but no longer part of configured runs or roles, add a `GAP` note and keep it in registry until explicit deactivation or replacement.
   - Do not remove historical skill entries only because a single no-op day occurred.
3. Hook safety check:
   - Confirm `UserPromptSubmit` exists in `.codex/hooks.json`.
   - Confirm command points to `project/scripts/task-handout-hook.py`.
   - Confirm no private paths, credentials, or sender IDs are introduced.
4. Reconcile output files:
   - Ensure registry docs and skills-used files are internally consistent.
   - Keep updates minimal; if no real change is required, keep a no-op summary and a run note.
5. Document run output:
   - Record `FACT/INTERPRETATION/HYPOTHESIS/GAP`.
   - Add explicit no-op confirmation when files are intentionally unchanged.
   - Add a short "inefficiency evidence" note when a recurrent step is not value-bearing.
6. Run the post-execution skill update review:
   - Use `project/scripts/post-execution-skill-update.py --run-dir project/runs/<run-id>` for a run folder, or pass a single run note file when that is the existing artifact.
   - Use `--latest` only when the latest run folder is the intended target.
   - The script must decide one of `NO_UPDATE`, `APPEND_PATTERN`, or `PATCH_EXISTING_SKILL`.
   - Default to review-only output. Use `--apply` only when the evidence is public-safe, reusable, and points to an existing skill or support file.
   - If the target skill has no matching support file, store the candidate under this skill's `candidate-patterns.md` instead of creating a new skill or rewriting `SKILL.md`.
   - Keep `SKILL.md` edits manual and reviewed; the script appends only to support files.
7. Update the lane inefficiency list:
   - Keep a short do-not-repeat list for this lane.
   - Promote only repeated, durable non-value patterns into `wiki/insights.md` via the daily review handoff.

## Inefficiency And Relevance Controls (Long-Term)

For this lane, do not use these approaches as default:

- full-device scans, full-repo re-indexing, or broad LLM-based retrospectives;
- redeploying or re-running dashboard generation without direct dashboard-source edits;
- repeated tool-stack discovery when no dependency or source change exists.

For this lane, prefer these bounded checks:

- file-level diff checks for targeted registry files;
- parse checks only on edited YAML/JSON;
- the task-handout hook alignment check only.

## Irrelevant Tool Blacklist for Recurring Evening Maintenance

Treat these as excluded unless explicitly justified by a separate issue:

- `playwright` and browser automation tooling for registry maintenance.
- network-driven `curl`/REST checks for daily registry synchronization.
- `git push` from this lane.
- full `graphify` refresh.
- provider model calls.

## Lane Efficiency Note

This lane is expected to be low-friction. When a helper step repeatedly adds no meaningful signal:

- log the item under `Inefficiency` in the run summary,
- add it to this lane's local do-not-repeat list,
- and move durable replacements into the day-level daily-review memory handoff.

## Output

If changes are needed, update only:

- `project/agents/skills-by-agent.md`
- `project/agents/agent-roster.yaml`
- `skills/skills-used.md`
- `.codex/hooks.json`
- `skills/evening-skill-registry-update/*.md` support files
- existing target skill support files when the post-execution review produces evidence-backed `APPEND_PATTERN`

If no changes are needed, add a `run-summary` proving no drift and preserve no-op cadence.

## Failure Handling

- If required files are missing, create a `GAP` entry and stop the run after naming the exact missing file(s).
- If hook contract drift blocks execution, update `.codex/hooks.json` and the task-handout contract path together.
- Do not silently delete or rename existing SKILL contracts that still have historical evidence.

## Done Criteria

The pass is complete when:

- configured agents/skills are synchronized,
- hook command and script path are aligned,
- post-execution skill update review has produced a `NO_UPDATE`, `APPEND_PATTERN`, or `PATCH_EXISTING_SKILL` decision,
- irrelevant-tool constraints are recorded,
- and a concise report is available for next-day review.
