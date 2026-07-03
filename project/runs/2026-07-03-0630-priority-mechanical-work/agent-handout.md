# Agent Handout: Priority Mechanical Work E4 Profile Packet

## Title And Purpose

This handout covers the 06:30 priority mechanical-work lane for the selected E4 social-profile packaging task. It is for the next operator who needs to continue profile preparation without redoing project-plan and content-gate discovery.

## Human Summary

The deterministic priority selector was rerun against `project/project-plan.md`. It again selected `Package social profiles for LinkedIn, X, and Threads` as the highest-ranked unfinished task, with score `282`.

This run converted the basic selector output into a concrete public-safe profile package. It added channel-specific profile field drafts for LinkedIn, X, and Threads, recorded the evidence boundary, and created a review gate. The drafts use ArchFlow company voice and the Product Discovery-to-Production PRD Pack positioning for B2B SaaS product teams.

No live platform, Notion, provider, network, Git push, deployment, or publication action was performed. The draft remains blocked until owner decisions are recorded.

## Current State

- Task status: still `In Progress`.
- Main output: public-safe profile draft packet under this run folder.
- Publication status: blocked.
- Runtime/provider status: not used.
- External writes: none.

## Agent Continuation Prompt

```text
You are the next ArchFlow E4 content/profile operator. Start from `project/runs/2026-07-03-0630-priority-mechanical-work/`. Review `profile-field-drafts.md`, `review-gate.md`, `selected-task.md`, and `kb-notion-github-packet.md`. Do not open or edit live social accounts, publish content, write to Notion, push Git, call providers, or use network tools unless explicit owner approval is present. If approval is available, convert the draft into final profile fields, preserve all public-safety boundaries, and record the channel update without storing private account IDs or URLs. If approval is not available, leave the task `In Progress` and record the missing decision.
```

## Execution Trace

FACT: Required live communication preflight was read before edits.

FACT: The priority operator selected the E4 social-profile packaging row.

FACT: Existing E1.5 content rules require LinkedIn-first, company-voice, evidence-labeled content and owner approval before publication.

INTERPRETATION: The safe mechanical action was preparing drafts and gates, not editing social accounts.

GAP: Owner decisions are still needed before live updates.

## Decisions

- Use ArchFlow company voice by default.
- Keep demand, ROI, customer, revenue, and market-validation claims out of profile copy.
- Keep profile link target and personal-vs-company voice as owner decisions.
- Keep live social updates blocked until approval.

## Artifacts

- `selected-task.md`: refreshed ranking and selected-task evidence.
- `profile-field-drafts.md`: LinkedIn, X, and Threads draft fields.
- `review-gate.md`: mechanical AF Review precheck and owner-decision list.
- `pitagent-chat-prompt.md`: next-operator prompt and stop conditions.
- `kb-notion-github-packet.md`: safe KB, Notion, and GitHub payload.
- `agent-handout.md`: this continuation handout.

## Validation

- Checks pending at handout creation; run public-safety scan before final closeout.
- No scripts were edited.

## Next Actions

1. Run public-safety scan.
2. Record concise KB/log and live-communication completion.
3. Ask owner to choose company-only versus personal profile lane, link target, visual usage, and timing before any live platform edit.

## Safety Boundary

Do not ingest, copy, publish, or log private profile URLs, account IDs, private screenshots, credentials, raw source material, local paths, customer names, target-account names, or any demand/ROI claim without E6/E7 evidence.
