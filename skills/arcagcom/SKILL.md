---
name: arcagcom
description: ArchFlow public project live-agent communication contract. Use before parallel work, role-based work, Prompt 2.1/Prompt 3 coordination, shared-file edits, Git closeout, or handoff.
---

# Arcagcom

## Purpose

Use `arcagcom` to coordinate ArchFlow public project agents through `project/live/communication/`.

The goal is simple: no silent overlap, no private data in public logs, no contradictory status claims, and no final Git merge before active lanes have posted completion or handoff state.

## Required Read Order

Before editing files, read:

1. `project/operating-rules.md`
2. `project/live/communication/README.md`
3. `project/live/communication/current-agent-notice.md`
4. latest entries in `project/live/communication/agent-communication-log.md`

## Starting Update

Append a `starting` entry before editing. Include:

- task;
- files likely to change;
- files claimed;
- expected output;
- blockers;
- next step.

Claim only the files needed for the current task. Do not claim broad folders unless the task truly owns the whole folder.

## During Work

Append an update before:

- editing a shared file another lane may touch;
- expanding scope;
- changing runtime, provider, deployment, Telegram, Notion, Git, or WikiLLM claims;
- moving from review to commit/push.

If another agent has claimed the same file or task, pause and coordinate in the log before editing.

## Completion Update

Append `complete`, `blocked`, or `handoff` with:

- files changed;
- checks run;
- checks skipped and why;
- status changes;
- remaining gates;
- next safe action.

For substantial work, also create or update `project/runs/<run-id>/agent-handout.md`.

## Public-Safety Rules

Never store these in communication logs:

- secrets, tokens, keys, cookies, passwords, credentials;
- private URLs or Notion page URLs;
- local absolute paths;
- account, workspace, project, deployment, chat, or user IDs;
- raw transcripts, raw private source text, screenshots, PDFs, or browser logs;
- private customer, user, or owner identifiers.

Use repo-relative paths and public-safe summaries.

## Prompt 2.1 / Prompt 3 Coordination

Prompt 2.1 owns:

- Notion/task architecture;
- runtime docs;
- local Jarvis stack contracts;
- project skills;
- reporting templates;
- final task-state truth.

Prompt 3 owns:

- public website visual/code implementation;
- website QA artifacts;
- visual assets and layout.

Prompt 2.1 must not edit website visual files unless it only updates links/status text and logs coordination first.

Prompt 3 must not edit Notion/runtime/skill/reporting files unless it logs coordination first.

Before final main merge or branch cleanup:

1. both lanes post completion or handoff updates;
2. check branch relation;
3. check conflicts;
4. run public safety and runtime guard;
5. avoid force push;
6. do not delete branches until both lanes confirm their work is represented on main.

## Checks

Default checks after communication/skill/reporting changes:

- `python3 scripts/public_safety_scan.py`
- `python3 -c "import json; json.load(open('project/dashboard/data.json'))"` after dashboard data regeneration
- `git diff --check`
- workflow/runtime guard when workflow, runtime, provider, or dashboard data changed

Record intentionally skipped checks with reason.
