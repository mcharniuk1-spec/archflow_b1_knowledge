# New PitAgent Handoff

You are the next operator for the ArchFlow priority-task lane.
Use this packet to review previous automation output, verify execution,
and run reliability checks before closing the task.

## Context
- Selected task: `Package social profiles for LinkedIn, X, and Threads`
- Epic: `E4 - Content`
- Planned due: `2026-06-28`
- Current state: public-safe drafts and review gate already exist in `project/runs/2026-07-03-0630-priority-mechanical-work/`; this run adds the owner-decision and operator-side checklist packet.

## Required checks
1. Confirm task scope is still valid in `project/project-plan.md`.
2. Validate all prerequisites from this task row are available.
3. Record KB update evidence in `wiki/log.md` and task-packet fields.
4. Prepare Notion status payload and repository push packet.
5. Mark this task complete only if execution output is observable in repository and checks are documented.

## Continuation prompt

```text
You are the next ArchFlow E4 profile operator. Start from `project/runs/2026-07-03-0630-priority-mechanical-work/` and `project/runs/2026-07-04-0030-priority-mechanical-work/`. Do not open or edit live social accounts, publish content, write to Notion, push Git, call providers, use network tools, or store private account data unless explicit owner approval is present. If approval is absent, keep the task `In Progress`, use `owner-decision-request.md` to ask for the missing choices, and stop. If approval is present, use `operator-side-profile-checklist.md` to perform only the approved profile-field updates and record public-safe completion evidence.
```

## Notion packet
- Task status target: `In Progress` before execution, `Done/Review` after execution.
- Blocked fields: keep GAP notes in a separate bullet if task cannot be executed automatically.
- Safe status recommendation: keep the task `In Progress` until owner choices are recorded; move to `Review` only after final approved field copy exists; mark `Done` only after approved live update or explicit owner closeout.

## Git packet
- `git status --short`
- `git add -A`
- `git commit -m "Run: priority task operator execution"`
- `git push`
