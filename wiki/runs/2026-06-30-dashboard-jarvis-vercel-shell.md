# Run: Dashboard Jarvis Vercel Shell

Date: 2026-06-30
Status: implemented, validated, preview deployed behind Vercel authentication

## Summary

The public dashboard was extended from a static read-only status board into a Jarvis-first command shell for Vercel preview. The shell adds normal/interview modes, a bottom command input, manual and timed refresh, browser-local voice authorization, metadata-only file packet creation, current-session event history, and packet downloads.

The implementation keeps the public boundary clear: static Vercel can stage session packets and refresh deployed `data.json`, but durable writes wait for Codex or a future Railway/backend service. Unauthenticated smoke checks currently redirect to Vercel SSO.

Canonical review route:

- protected Vercel preview dashboard route, masked in this public artifact

An initial Vercel CLI deploy without `--prod` was recorded by Vercel as target `production`; the explicit `--target preview` deployment is the only approved review target.

## Artifacts

- `project/dashboard/`
- `vercel.json`
- `.vercelignore`
- `project/content/templates/`
- `project/runs/E1.5/2026-06-30-dashboard-jarvis-vercel/`
- `project/runs/E1.5/2026-06-30-content-agent-templates/`

## Status

FACT: E1.3 remains Review with readback proof passed.

FACT: E1.4 remains Backlog.

FACT: E1.5 is In Progress with reporting gates, content templates, and dashboard/Jarvis shell.

FACT: E2 remains gated to one ICP lane and reviewed evidence cards.

FACT: E5 remains active for operations and ROI discipline.

## Next

Review the combined public diff, then sync private task/report state. Do not store deployment IDs, account IDs, or provider secrets in public files.
