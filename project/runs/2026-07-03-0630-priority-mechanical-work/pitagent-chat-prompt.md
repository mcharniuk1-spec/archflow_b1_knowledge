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

## E4 profile-package execution prompt

Use this exact scope unless the owner explicitly widens it:

```text
You are the ArchFlow E4 profile-package operator. Work only from public-safe repo artifacts. Prepare profile field drafts for LinkedIn, X, and Threads, but do not open or edit live social accounts, do not publish posts, do not use network calls, and do not write to Notion unless an approved connector and explicit owner approval are available.

Start by reading `project/project-plan.md`, `project/content/templates/README.md`, `project/runs/E1.5/2026-06-30-public-reporting-gate/public-reporting-gate.md`, and this run folder. Preserve the current offer frame: Product Discovery-to-Production PRD Pack for B2B SaaS product teams. Keep all demand, ROI, customer, revenue, and market-validation claims blocked before E6/E7 proof.

Expected output:
- `profile-field-drafts.md` with LinkedIn, X, and Threads field drafts.
- `review-gate.md` using `project/content/templates/review-gate-template.md`.
- A short KB/log update and handout entry.

Stop conditions:
- If a live account edit, private profile URL, external write, account ID, private screenshot, or owner voice decision is needed, record GAP and stop.
- If any draft needs personal positioning rather than ArchFlow company voice, record owner-decision-needed and stop.
```

## Notion packet
- Task status target: `In Progress` before execution, `Done/Review` after execution.
- Blocked fields: keep GAP notes in a separate bullet if task cannot be executed automatically.
- Safe status recommendation from this mechanical run: keep the task `In Progress` until field drafts and AF Review exist. Move to `Review` only after owner-ready drafts are saved. Do not mark `Done` until approved live profile updates or an explicit owner decision are recorded.

## Git packet
- `git status --short`
- `git add -A`
- `git commit -m "Run: priority task operator execution"`
- `git push`
