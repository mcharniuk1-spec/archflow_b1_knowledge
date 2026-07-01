# Live Agent Communication

Purpose: this folder is the shared public-safe communication channel for ArchFlow agents working in parallel.

Every active agent must read this folder before changing project files, then append short status updates while working. The goal is to prevent contradictory edits, duplicate work, stale assumptions, and silent file ownership conflicts.

## Required Files

| File | Purpose |
|---|---|
| `agent-communication-log.md` | Append-only working dialogue between agents. |
| `current-agent-notice.md` | Current notice that every agent must read before work. |
| `message-template.md` | Required update format. |
| `pattern-change-log.md` | Append-only record of changes to this communication pattern. |
| `system-prompt-append.md` | Copy-ready prompt section to add to agent system/developer prompts. |

## Agent Rule

Before starting work, each agent must:

1. Read `project/operating-rules.md`.
2. Read this `README.md`.
3. Read `current-agent-notice.md`.
4. Read the latest section of `agent-communication-log.md`.
5. Append a `starting` update that names the task, files likely to change, expected output, and blockers.

During work, each agent must:

- Append a short update before editing shared files.
- Mark files as claimed only for the narrow task being handled.
- Check the log before editing any file another agent has claimed.
- Use `FACT`, `INTERPRETATION`, `HYPOTHESIS`, and `GAP` when the update changes strategy, state, or risk.
- Keep raw private sources, secrets, local absolute paths, private URLs, IDs, screenshots, and credentials out of this folder.

After work, each agent must:

- Append a `complete`, `blocked`, or `handoff` update.
- List files changed.
- List checks run or skipped with reason.
- State the next safe action.
- Update the relevant run handout under `project/runs/` when the task is substantial.

## Pattern Changes

Any change to this communication pattern must be recorded in `pattern-change-log.md` and announced in `agent-communication-log.md`. Agents must treat the latest pattern-change entry as the current coordination contract.

## Current Execution Pointer

2026-07-01, Codex Jesus continuation: June 30 transfer, dashboard/Jarvis/provider cleanup, Notion task-property sync, and subagent review integration are locally complete. Use `agent-communication-log.md` for the detailed handoff. Current branch remains uncommitted/unpushed; merge, deploy, Railway/local bridge, provider activation, and owner-device voice proof remain gated.
