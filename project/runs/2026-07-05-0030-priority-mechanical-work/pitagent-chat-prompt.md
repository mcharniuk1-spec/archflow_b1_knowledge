# New PitAgent Handoff

You are the next operator for the ArchFlow priority-task lane.
Use this packet to review previous automation output, verify execution,
and run reliability checks before closing the task. This is a public-safe
no-approval packet. Do not publish, push, write to Notion, edit live profiles,
call providers, run crawlers, or collect private source material.

## Context
- Selected task: `Package social profiles for LinkedIn, X, and Threads`
- Epic: `E4 - Content`
- Planned due: `2026-06-28`
- Selector score: `294`
- Run decision: live E4 profile work is owner-gated and already packetized
  in earlier runs, so this run prepared the next safe E4.1/E4.5 content
  planning artifacts instead of repeating profile drafts.

## Required checks
1. Confirm task scope is still valid in `project/project-plan.md`.
2. Read `e4-live-profile-gate.md` before any profile-related action.
3. Review `e4-1-five-week-content-plan.md` and `e4-5-weekly-review-scorecard.md`.
4. Record KB update evidence in `wiki/log.md` and task-packet fields.
5. Mark live E4 profile execution complete only if owner decisions are recorded and execution output is observable in repository.
6. Keep E4.1/E4.5 as review-ready planning artifacts until AF Review and owner publication approval exist.

## Notion packet
- Prepare text only. Do not write to Notion from this packet.
- Suggested status target for E4 profile packaging: keep `In Progress`.
- Suggested status target for E4.1 five-week plan: `Review` only after AF Review confirms safety and owner approves use.
- Blocked fields: live profile edits, publication timing, visuals, CTA link, and public/persona voice require owner approval.

## Git packet
- Prepare commit text only if requested by the owner.
- Do not push from the automation lane.
- Local checks to run before any later commit: public safety scan, JSON parse for generated data, and whitespace diff check.
