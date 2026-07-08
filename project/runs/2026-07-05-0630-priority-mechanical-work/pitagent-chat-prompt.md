# New PitAgent Handoff

You are the next operator for the ArchFlow priority-task lane.
Use this packet to review previous automation output, verify execution,
and run reliability checks before closing the task.

## Context
- Selected task: `Package social profiles for LinkedIn, X, and Threads`
- Epic: `E4 - Content`
- Planned due: `2026-06-28`

## Required checks
1. Confirm task scope is still valid in `project/project-plan.md`.
2. Validate all prerequisites from this task row are available.
3. Record KB update evidence in `wiki/log.md` and task-packet fields.
4. Prepare Notion status payload and repository push packet.
5. Mark this task complete only if execution output is observable in repository and checks are documented.

## Notion packet
- Task status target: `In Progress` before execution, `Done/Review` after execution.
- Blocked fields: keep GAP notes in a separate bullet if task cannot be executed automatically.

## Git packet
- `git status --short`
- `git add -A`
- `git commit -m "Run: priority task operator execution"`
- `git push`
