# Agent Handout: Dashboard Jarvis Vercel Shell

Date: 2026-06-30
Status: continue from review, commit, and private task sync

## Summary

The dashboard is now a Jarvis-first static command shell for Vercel preview. It supports live in-page refresh of deployed `data.json`, normal/interview mode, browser-local voice authorization, browser-local file metadata packet creation, and downloadable research/check/content packets.

This is not a backend. Durable writes still require Codex or a future Railway/API layer.

Canonical review route:

- protected Vercel preview dashboard route, masked in this public artifact

Use only the explicit preview deployment for review. An initial Vercel CLI deploy without `--prod` was recorded by Vercel as target `production`; keep it out of review and keep future deploy commands explicit with `--target preview`.

## Changed Files

- `project/dashboard/index.html`
- `project/dashboard/app.js`
- `project/dashboard/styles.css`
- `project/dashboard/README.md`
- `project/dashboard/data.json`
- `vercel.json`
- `.vercelignore`
- `project/content/templates/`
- `project/runs/E1.5/2026-06-30-content-agent-templates/`
- `project/runs/E1.5/2026-06-30-dashboard-jarvis-vercel/`

## Current Decisions

- Vercel hidden-link preview first.
- Railway later after live backend needs are real.
- Google auth later; no client-side password screen.
- One ICP lane remains active.
- Voice is authorized by the user/browser before use.
- Static Jarvis can stage packets, not write persistent memory.
- Content can be prepared from reviewed task proof, but public publishing still needs AF Review plus owner approval.

## Continue Prompt

Continue from the public repository root.

1. Run validation:
   - `python3 project/scripts/generate-dashboard-data.py`
   - `node --check project/dashboard/app.js`
   - `python3 -m json.tool project/dashboard/data.json`
   - `python3 -m json.tool vercel.json`
   - `python3 scripts/public_safety_scan.py`
2. Verify `/project/dashboard/` locally.
3. Review the combined diff from all parallel agents.
4. Commit and push public-safe files only after review.
5. Use the canonical Vercel preview route above; do not store deployment IDs, org IDs, local env values, or provider keys in public files.
6. Update Notion E1.3.9, E1.3.10, E1.5, and the June 30 execution report with the deployment state, current limits, and next blockers.

## Safety Boundary

Do not read, print, commit, or upload private key files, local env files, raw transcripts, private Notion links, private uploads, or provider credentials.
