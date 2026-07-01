# Pattern Change Log

Append-only record of changes to the ArchFlow agent communication pattern.

## 2026-07-01 - Live communication folder created

Status: active

Change:

- Added `project/live/communication/` as the shared live channel for ArchFlow public project agents.
- Required agents to read the folder before work, append a starting update, claim expected files, coordinate conflicts, and report completion or handoff.
- Kept run-specific `agent-handout.md` files as durable completion records after substantial work.

Reason:

- Parallel agents need a single current channel to prevent contradictions and silent overlapping edits.

Applies to:

- AF Tools
- AF Context
- AF Manager
- AF Research
- AF Knowledge
- AF Copy
- GloomyLord
- AF Review
- AF Publisher
- Any Codex, Claude Code, Cursor, or sidecar agent working on the public ArchFlow project.
