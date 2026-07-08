# Priority Mechanical Work Handout

## Title And Purpose

This handout covers the `2026-07-06-0030-priority-mechanical-work` run. It is
for the next ArchFlow operator who needs to continue the priority mechanical
lane without redoing selector and packet discovery.

## Human Summary

The deterministic priority selector still ranked E4 social profile packaging as
the top task. That work is blocked at the live execution layer because profile
edits, social account changes, media upload, and publication require owner
approval.

Prior priority runs already prepared the useful no-approval E4 artifacts:
profile drafts, live-profile gate, operator-side checklist, five-week content
plan, and weekly content review scorecard. Repeating those drafts would not add
much future value.

This run converted the safe mechanical action into E5.2 measurement work. It
added a lead funnel metrics packet and diagnostic event-schema contract so E3
diagnostic, E4 content, E6 outreach, and E7 payment verdict work can distinguish
attention from buyer-risk evidence.

## Current State

- E4 social profiles: `In Progress`, live execution owner-gated.
- E5.2 lead funnel metrics: no-code packet prepared for review.
- Analytics, CRM, diagnostic form implementation, real lead capture, Notion
  writeback, Git push, provider calls, and external publication: not performed.

## Agent Continuation Prompt

Continue from `project/runs/2026-07-06-0030-priority-mechanical-work/`.
Read `selected-task.md`, `e5-2-lead-funnel-metrics.md`,
`e5-2-diagnostic-event-schema.md`, and `kb-notion-github-packet.md`. If the next
safe task is still measurement or diagnostics, prepare E3.4 diagnostic copy and
form-field mapping from the E5.2 schema. Stop before analytics activation, CRM
setup, real lead collection, external writes, social profile edits, provider
calls, Git push, Notion writes, or private-source ingestion.

## Execution Trace

FACT:
- Read required live communication files, project plan, recent priority packets,
  wiki log, wiki memory, wiki insights, automation memory, and the task-handout
  skill.
- Appended the required starting live-log update before edits.
- Ran the priority selector for this run ID.
- Selector output ranked E4 social profiles first with score `300`.
- Added E5.2 lead-funnel and diagnostic event-schema artifacts.

INTERPRETATION:
- The next no-approval value is the measurement layer, not duplicate profile
  drafting or live account work.

GAP:
- Real demand evidence does not exist until buyer-risk signals are captured and
  reviewed.

## Decisions

- Preserved the selector result instead of editing it away.
- Recorded E4 live execution as owner-gated.
- Prepared E5.2 artifacts because they are high-ranked, overdue, mechanical, and
  unblock future E3/E4/E6/E7 work without external action.

## Artifacts

- `project/runs/2026-07-06-0030-priority-mechanical-work/selected-task.md`:
  selector output plus execution decision.
- `project/runs/2026-07-06-0030-priority-mechanical-work/e5-2-lead-funnel-metrics.md`:
  funnel stages, demand-quality metrics, lead record, and stage gates.
- `project/runs/2026-07-06-0030-priority-mechanical-work/e5-2-diagnostic-event-schema.md`:
  future diagnostic event names, shared fields, and activation gates.
- `project/runs/2026-07-06-0030-priority-mechanical-work/kb-notion-github-packet.md`:
  public-safe KB, Notion, and GitHub packet.
- `project/runs/2026-07-06-0030-priority-mechanical-work/pitagent-chat-prompt.md`:
  continuation prompt for the next operator.

## Validation

Checks passed:

- `python3 -m json.tool project/runs/2026-07-06-0030-priority-mechanical-work/selected-task.json`
- `python3 -m py_compile project/scripts/priority-task-operator.py project/scripts/generate-dashboard-data.py`
- `python3 project/scripts/generate-dashboard-data.py`
- `python3 -m json.tool project/dashboard/data.json`
- `python3 scripts/public_safety_scan.py`
- `git diff --check`

## Next Actions

1. Review E5.2 packet for board/status update.
2. Map the E5.2 schema into E3.4 diagnostic page fields.
3. Keep E4 social profile publication blocked until owner decisions are explicit.
4. Use E5.2 demand-quality rules when E4 content or E6 outreach begins producing
   signals.

## Safety Boundary

Do not store private lead data, personal identifiers, raw source packets,
private URLs, account IDs, credentials, screenshots, browser cookies, analytics
user IDs, or local absolute paths in public artifacts. Do not activate analytics,
CRM, provider calls, Notion writes, Git push, account edits, or publication
without explicit approval.
