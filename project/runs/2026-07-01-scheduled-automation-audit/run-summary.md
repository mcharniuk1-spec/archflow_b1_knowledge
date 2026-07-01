# Scheduled Automation Audit

Date: 2026-07-01
Status: complete

## Task

Check the local scheduled Codex automations against current ArchFlow public operating rules, live communication requirements, task-handout expectations, and each automation's stated goal.

## Findings

FACT: Four local automation definitions were present: three active scheduled jobs and one paused Real Estate health-check job.

FACT: The Yushchenko model-efficiency observer was active, scheduled every five hours, and already pointed at the ArchFlow public project root.

FACT: The ArchFlow public evening skill and hook update was active at 21:00 daily, but its working directory did not match the repo-relative paths in its prompt. It was updated to run from the public project root.

FACT: The daily skill retrospective and RAG knowledge review was active at 22:30 daily, but its working directory did not match its LangGraph strategic-system workspace. It was updated to run from that workspace.

FACT: The paused Real Estate health-check automation remains paused. It was not changed because it is outside the active ArchFlow schedule shown in the current audit and has a different project scope.

INTERPRETATION: The two active daily jobs were likely to fail or drift because their prompts used project-local relative paths from a different starting directory.

HYPOTHESIS: The next scheduled runs should now reach their expected files without path-recovery guesswork.

GAP: This audit checked definitions and referenced files, not a live scheduled execution trace.

## Changes Made

- Updated the ArchFlow public evening automation to run from the public project root.
- Added explicit live communication and task-handout preflight to the ArchFlow public evening automation prompt.
- Updated the daily LangGraph/RAG retrospective automation to run from its strategic-system workspace.
- Recorded this audit in the live communication log.

## Validation

- Parsed all local automation TOML definitions successfully.
- Confirmed required ArchFlow public files referenced by the active automations exist.
- Confirmed required LangGraph strategic-system routing files referenced by the daily retrospective exist.
- Ran `python3 scripts/public_safety_scan.py` from the public project.

## Next Actions

1. Let the next scheduled ArchFlow evening run validate that its no-op or update path works from the corrected root.
2. Let the next daily retrospective verify that it can write to the LangGraph course-support outputs.
3. Keep the Real Estate health-check automation paused unless that project lane is intentionally resumed.
