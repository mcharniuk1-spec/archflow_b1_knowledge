# Run: Onyx Dashboard Voice Hosting Execution

Date: 2026-06-30
Status: planned and recorded

## Summary

The June 30 plan was converted into a public-safe execution baseline. ArchFlow remains the workflow brain; Onyx is a later optional portal/search layer. The dashboard should go live in stages, beginning with the current static read-only dashboard and only adding Railway/live workers when the project needs a long-running API, queue, or voice bridge.

Two private Notion tasks were created for the next work: one for the live dashboard/voice/hosting/Onyx path and one for GloomyLord to prepare the PRD, research templates, monitoring templates, backlog, ideas summary, and public visual report system.

## Outputs

- Added `skills/outquestions/SKILL.md`.
- Updated the public skill registry and agent skill map.
- Added public run note `project/runs/2026-06-30-onyx-dashboard-voice-hosting-execution.md`.
- Added public decision record `wiki/decisions/2026-06-30-live-dashboard-voice-hosting-onyx.md`.

## Decision

Vercel is the first dashboard target because the current dashboard is static and read-only. Railway is reserved for live API, worker, queue, websocket/SSE, or voice-service needs. Voice starts local and read-only with explicit approval gates before write actions.

## Next

Use `outquestions` at the end of each substantial step so the next stage cannot silently advance without answering scope, proof, privacy, owner, runtime, memory, design, and publishing questions.
