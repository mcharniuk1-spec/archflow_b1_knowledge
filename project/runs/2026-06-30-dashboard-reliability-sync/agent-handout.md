# Agent Handout: Dashboard Reliability Sync

## Human Summary

The dashboard reliability state has been synchronized into the public GitHub knowledge layer. The current dependable mode is a protected Vercel static preview backed by committed source files and regenerated `project/dashboard/data.json`.

## Current State

FACT:
- Dashboard preview is protected and read-only.
- GitHub holds the public-safe source and KB records.
- Notion should receive append-only summaries and proof links after verification.
- Railway, OpenAI/Mistral app runtime, live Codex bridge, uploads, voice persistence, and browser writeback are not enabled.

INTERPRETATION:
- The minimal reliable next operating mode is not a new backend; it is disciplined source sync, validation, push, Notion sync, and web-view verification.

GAP:
- Always-on live execution needs a separate backend/auth/secret/data-policy decision.

## Files To Review

- `project/dashboard/README.md`
- `project/runs/2026-06-30-dashboard-reliability-sync/run-summary.md`
- `wiki/runs/2026-06-30-dashboard-reliability-sync.md`
- `wiki/memory.md`
- `wiki/log.md`
- `project/dashboard/data.json`

## Continuation Prompt

Continue from the dashboard reliability sync. Verify `project/dashboard/data.json`, run public safety/workflow/runtime checks, push the public repo, update Notion append-only with the final commit and preview status, then keep Railway/model/backend work gated until owner approval covers scope, auth, secret storage, and data policy.

## Next Action

Run E2.0 internal research-engine dry run from approved public sources, or start a separate backend planning task if live always-on API behavior is explicitly approved.
