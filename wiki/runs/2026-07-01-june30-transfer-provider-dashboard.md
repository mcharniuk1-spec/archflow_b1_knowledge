# Wiki Run: June 30 Transfer, Provider Cleanup, And Dashboard Completion

Date: 2026-07-01
Status: local transfer and validation completed; Git commit, push, merge, and deploy remain pending

## Summary

The missing final June 30 accepted state was transferred into the ArchFlow public knowledge layer. The project now records that the accepted review branch is `d18fc55`, `JDB-8` is Done, `JDB-7` remains Review, and Telegram was not sent because external disclosure was blocked by approval review.

Provider handling was corrected. OpenRouter and Mistral keys are local ignored env material only. The temporary Markdown key file was deleted. The June 30 OpenAI local key file was deleted. Ignored env files were restricted to owner-only permissions. Static dashboard code must not access provider keys or call providers.

The dashboard was extended from the interrupted two-screen edit into explicit `(1) PRD/ICP Flow` and `(2) Agent Orchestra` schema screens. Node control panels now expose the configuration that matters for agent work: inputs, outputs, prompts, comments, last runs, connection summary, safety, persistence, memory target, trace target, and provider mode.

Added `project/scripts/dashboard-static-smoke.py` as the reusable rendered-route proof for the dashboard setup. It rendered `#jarvis`, `#history`, `#service`, `#schema`, `#config`, `#plan`, `?panel=svc-intake#service`, and `?panel=architecture-review#schema` in headless Chrome and confirmed zero provider calls/writeback.

## Durable Interpretation

ArchFlow has two active paradigms:

1. The PRD/ICP service product is what should eventually be shown and sold.
2. The local development/control system is what makes that product reliable.

Vercel preserves the last static dashboard state when local agents are off. Railway is still reserved for live backend needs. OpenRouter/Mistral are future backend/local-bridge provider options, not active static-dashboard runtime.

## Remaining Gates

- E2.0 internal research-engine dry run.
- E1.4 KB update principle.
- E5 ROI/funnel methodology.
- Browser/device mic and speaker proof.
- JDB-7 merge/deploy decision.
- Live Nexus proof.
- Backend/local bridge contract before provider calls.
- Explicit owner approval before Telegram or other external publishing.

## Checks

- Pass: dashboard JavaScript syntax.
- Pass: dashboard JSON parse.
- Pass: public safety scan.
- Pass: workflow validation.
- Pass: pre-push runtime guard.
- Pass: reusable eight-route dashboard static smoke script, including the two node-panel deep links.
- Pass: targeted provider-secret scan of public tracked/non-env files.
- Pass: Notion task-row verification after property updates for JDB-8, JDB-7, and E1.3.9. Page IDs and private URLs are intentionally not stored in this public note.
- Replaced: earlier narrow headless Chrome route smoke for `#jarvis`, `#service`, and `#schema`; temporary PNG captures were removed from the public run folder.
- Gap: interactive visual click-through of the large node control modal is still pending before merge/deploy.
- Gap: Git durability is still pending until owner-approved commit, push, merge, and deploy.

## Parallel Review Integration

- Fixed model-routing schema drift found by provider/public-safety review.
- Fixed voice-state wording so the dashboard does not claim microphone authorization before browser listening starts.
- Added keyboard activation and Escape/backdrop close behavior for schema node control panels.
- Clarified local-complete versus Git-durable status.
- Tightened the analytical writing framework with explicit decision-question and PR-FAQ sections.
- Added a status vocabulary note for E3/E4 so report states do not conflict with task-board subtask labels.
