# Agent Handout: Priority Mechanical Work E4 Decision Packet

## Title And Purpose

This handout covers the 00:30 priority mechanical-work lane for E4 social-profile packaging. It is for the next operator who needs to move from draft profile copy to an owner-approved live-update path without repeating prior work.

## Human Summary

The deterministic selector was rerun against `project/project-plan.md`. It still selected `Package social profiles for LinkedIn, X, and Threads` as the highest-ranked unfinished task, with score `288`.

The prior `2026-07-03-0630-priority-mechanical-work` run had already produced the safe mechanical profile drafts and review gate. This run did not duplicate that copy. It packaged the missing owner decisions and created an operator-side checklist for a future approved live-update pass.

No social platform, Notion, provider, network, Git push, deployment, credential, or publication action was performed. The task should remain `In Progress` until owner decisions are recorded.

## Current State

- Selected task: `Package social profiles for LinkedIn, X, and Threads`.
- Task status: `In Progress`.
- Draft profile copy: exists in `project/runs/2026-07-03-0630-priority-mechanical-work/profile-field-drafts.md`.
- Review gate: exists in `project/runs/2026-07-03-0630-priority-mechanical-work/review-gate.md`.
- Current run output: owner decision request plus operator-side checklist.
- External execution: blocked.

## Agent Continuation Prompt

```text
You are continuing the ArchFlow E4 social-profile setup lane. Read `project/runs/2026-07-03-0630-priority-mechanical-work/` and `project/runs/2026-07-04-0030-priority-mechanical-work/`. If owner approval is not recorded, use `owner-decision-request.md` to request choices for voice lane, link target, visual policy, timing, and status target; do not edit live accounts. If owner approval is recorded, use `operator-side-profile-checklist.md` to perform only approved profile-field updates and record public-safe completion evidence without storing private account IDs, private URLs, credentials, or screenshots.
```

## Execution Trace

FACT: Required live communication preflight was read before edits.

FACT: The priority operator selected the same E4 profile-packaging task.

FACT: The prior draft packet already contains LinkedIn, X, and Threads copy plus review checks.

INTERPRETATION: The next useful safe action was a decision and operator checklist, not another draft.

GAP: Owner decisions are still required before live platform updates.

## Decisions

- Preserve company-only ArchFlow voice as the safe default until owner chooses a personal/founder lane.
- Use no link or current website only after owner approval; diagnostic-page CTA waits for E3.4.
- Use no visual by default unless owner approves a public-safe asset.
- Keep the task `In Progress` until owner decisions are recorded.

## Artifacts

- `selected-task.md`: deterministic ranking plus this run's gate analysis.
- `owner-decision-request.md`: concise owner decision packet.
- `operator-side-profile-checklist.md`: future approved operator checklist.
- `pitagent-chat-prompt.md`: continuation prompt and stop conditions.
- `kb-notion-github-packet.md`: safe KB, Notion, and GitHub payload.
- `agent-handout.md`: this handout.

## Validation

- JSON parse: `selected-task.json`.
- Python compile: `project/scripts/priority-task-operator.py`.
- Public safety scan before closeout.
- No scripts were edited.

## Next Actions

1. Ask owner to choose voice lane, link target, visual policy, timing, and status target.
2. If approved, run only the operator-side checklist.
3. Keep publication, external writes, Notion writes, provider calls, deploys, and Git push blocked until explicitly approved.

## Safety Boundary

Do not ingest, copy, publish, or log private profile URLs, account IDs, credentials, private screenshots, raw source material, local paths, customer names, target-account names, or any demand/ROI claim without E6/E7 evidence.
