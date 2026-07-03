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

## Public-safe execution boundary

- Do not log in to LinkedIn, X, Threads, or any external account without owner approval.
- Do not publish or update live profiles from this prompt alone.
- Do not store handles, private links, account IDs, credentials, recovery details, or screenshots in public files.
- Draft only public-safe profile components: positioning line, short bio, offer summary, CTA, proof boundary, and profile consistency checklist.

## Suggested mechanical output

Create or update a run note for the E4 profile-packaging task with:

- platform-by-platform copy slots for LinkedIn, X, and Threads,
- a profile asset checklist,
- a content-launch readiness checklist,
- a blocked external-action list,
- and a concise approval request for live account edits.

## Notion packet
- Task status target: keep `In Progress` until live profile packaging is approved and observable; use `Review` only after the owner can inspect prepared copy/assets.
- Blocked fields: keep GAP notes in a separate bullet if task cannot be executed automatically.

## Git packet
- `git status --short`
- `git add -A`
- `git commit -m "Run: priority task operator execution"`
- `git push`
