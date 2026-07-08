# PitAgent Continuation Prompt

You are the next operator for the ArchFlow priority mechanical-work lane.

Goal:
- Review the 2026-07-06 06:30 packet and continue only with safe mechanical
  work that needs no owner confirmation.

Context files:
- `project/project-plan.md`
- `project/runs/2026-07-06-0630-priority-mechanical-work/selected-task.md`
- `project/runs/2026-07-06-0630-priority-mechanical-work/e5-3-inbound-qualification-scoring.md`
- `project/runs/2026-07-06-0630-priority-mechanical-work/e5-3-review-gate.md`
- `project/runs/2026-07-06-0030-priority-mechanical-work/e5-2-lead-funnel-metrics.md`
- `project/runs/2026-07-06-0030-priority-mechanical-work/e5-2-diagnostic-event-schema.md`

Current decision:
- The selector ranked `Package social profiles for LinkedIn, X, and Threads`
  first at score `300`.
- That live task remains owner-gated and already packetized by prior runs.
- This run prepared E5.3 inbound qualification scoring as the next useful
  no-approval artifact after E5.2.

Constraints:
- Do not perform network calls, provider/API calls, live crawls, production
  deploys, Git push, credential edits, private-source ingestion, live account
  changes, external writes, Notion writes, analytics activation, CRM writes,
  lead capture, outreach, or publication.
- Keep all artifacts public-safe and repo-relative.
- Preserve attention versus demand separation.

Expected continuation:
1. Run AF Review on the E5.3 scoring model.
2. If accepted, draft the E3 diagnostic field map or E6 outreach review
   criteria as a new no-approval packet.
3. If not accepted, revise weights and bands without collecting real leads.

Stop conditions:
- Stop if owner decisions, external accounts, real lead data, analytics
  tooling, CRM storage, Notion writes, or publication are required.
