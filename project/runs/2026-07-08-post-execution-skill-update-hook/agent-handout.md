# Post-Execution Skill Update Hook Handout

## Title And Purpose

This handout covers the July 8 post-execution skill update mechanism added to the existing ArchFlow evening skill and hook lane.

## Human Summary

The project already had a prompt hook, an evening skill/hook maintenance lane, a daily retrospective lane, project-local skills, run artifacts, and validation scripts. This run did not create a new automation system. It extended the existing evening lane with a controlled post-execution review gate.

The new script reviews a completed run folder or run note and returns one of three decisions: `NO_UPDATE`, `APPEND_PATTERN`, or `PATCH_EXISTING_SKILL`. It defaults to review-only output. It appends only to existing support files when `--apply` is passed, and it refuses to create a new skill automatically.

The controlling prompt hook remains a reminder only. Skill learning is evidence-gated and routed through the existing evening skill registry update skill.

## Current State

- Status: complete.
- Main script: `project/scripts/post-execution-skill-update.py`.
- Main lane contract: `project/automation/archflow-public-evening-skill-and-hook-update.md`.
- Main skill contract: `skills/evening-skill-registry-update/SKILL.md`.
- Support files: `successful-patterns.md`, `failed-patterns.md`, `stop-rules.md`, and `candidate-patterns.md` under the evening skill folder.

## Agent Continuation Prompt

Continue the ArchFlow public evening skill and hook lane from this handout. Read `project/operating-rules.md`, the live communication files, `skills/evening-skill-registry-update/SKILL.md`, `project/automation/archflow-public-evening-skill-and-hook-update.md`, and `project/scripts/post-execution-skill-update.py`. For each completed run, call the script with the run folder or run note. Record the decision in the run summary. Use `--apply` only when the evidence is concrete, public-safe, reusable, and mapped to an existing skill support file. Stop with `NO_UPDATE` when evidence is ordinary, one-off, weak, private-source-dependent, or not reusable.

## Execution Trace

FACT:

- Existing automation, skill, hook, run, and wiki structures were inspected first.
- The root workspace is not the active Git repo; the public project folder is the scoped repo.
- The existing evening lane owns registry and hook maintenance.
- The existing daily lane owns retrospective and durable inefficiency review.

INTERPRETATION:

- The correct integration path is a bounded post-execution review inside the evening skill/hook lane, not a second automation system.

GAP:

- The script is deterministic and conservative. It does not perform semantic LLM review.

## Decisions

- Keep the prompt hook as a reminder only.
- Add a review script instead of an auto-writing prompt mutation loop.
- Keep candidate material inside the existing evening skill folder when no existing target skill is proven.
- Require evidence before any `APPEND_PATTERN` or `PATCH_EXISTING_SKILL` decision.

## Artifacts

- `project/scripts/post-execution-skill-update.py`: deterministic run evidence reviewer.
- `skills/evening-skill-registry-update/stop-rules.md`: loop and mutation stop rules.
- `skills/evening-skill-registry-update/successful-patterns.md`: append-only successful pattern target.
- `skills/evening-skill-registry-update/failed-patterns.md`: append-only failed pattern target.
- `skills/evening-skill-registry-update/candidate-patterns.md`: non-controlling candidate storage.

## Validation

- Pass: Python compile for `project/scripts/post-execution-skill-update.py`, `project/scripts/task-handout-hook.py`, and `project/scripts/validate-workflows.py`.
- Pass: script smoke on this run returned `NO_UPDATE`.
- Pass: script smoke on the July 6 daily retrospective returned `PATCH_EXISTING_SKILL` for `priority-task-operator`.
- Pass: one `--apply` smoke appended a candidate to `skills/evening-skill-registry-update/candidate-patterns.md`.
- Pass: workflow validation with the project local Python environment.
- Pass: public safety scan.
- Pass: `git diff --check`.

## Next Actions

1. Use the script in the next evening skill/hook run and record the decision.
2. Promote candidate entries only after repeated evidence or explicit review.
3. Keep the daily retrospective focused on cross-run patterns and avoid duplicating the evening hook lane.

## Safety Boundary

Do not store secrets, credential values, private links, local absolute paths, account IDs, raw private source text, screenshots, browser logs, deployment metadata, or personal identifiers in public files. Do not use this hook to create new skills automatically or rewrite controlling prompts without evidence.
