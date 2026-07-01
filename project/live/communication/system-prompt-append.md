# System Prompt Append: ArchFlow Agent Communication

Append this section to the current ArchFlow agent system/developer prompt.

```text
ArchFlow Public Project Live Communication Rule

Before starting or continuing any ArchFlow public project work, read:

- project/operating-rules.md
- project/live/communication/README.md
- project/live/communication/current-agent-notice.md
- the latest entries in project/live/communication/agent-communication-log.md

Before editing files, append a short `starting` update to project/live/communication/agent-communication-log.md. Include the task, files likely to change, files claimed, expected output, blockers, and next step.

During work, append an update before editing shared files or changing scope. If another agent has claimed the same file or task, pause and coordinate in the communication log before editing.

After work, append a `complete`, `blocked`, or `handoff` update with files changed, checks run or skipped, remaining gaps, and the next safe action.

For substantial work, also create or update the relevant project/runs/<run-id>/agent-handout.md. The live communication folder coordinates active work; run handouts record durable completion state.

All updates must be public-safe. Do not store secrets, private URLs, account IDs, local absolute paths, raw private source text, screenshots, credentials, or personal identifiers.

Any change to this communication pattern must be recorded in project/live/communication/pattern-change-log.md and announced in project/live/communication/agent-communication-log.md.
```
