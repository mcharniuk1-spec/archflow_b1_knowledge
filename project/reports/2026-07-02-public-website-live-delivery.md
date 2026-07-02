# Public Website Live Delivery Report

Date: 2026-07-02
Status: live, verified, and Figma-synced

## Scope

This pass completed the public website delivery for the live ArchFlow Automate URL. It did not edit Notion, dashboard backend, provider routing, Telegram, Railway runtime, model-routing files, CrewAI/LangGraph config, skills, or Prompt 2.1 task-state docs.

## Live Result

- Public alias: `https://archflowautomate.vercel.app`
- Vercel project deployed from the public repo root.
- The alias was updated to point at the new public repo deployment. The source deployment URL is omitted from public-safe records because it includes account/project slug text.

## Website Sections Delivered

- First screen: transparent 3D arch object, visual process stages, balanced white/blue/brand-color layout, and wide `Readiness Diagnostic` button directly below the arch/stage visual.
- ICP section: copy aligned to B2B SaaS product teams, Series B-D, 50-500 employees, 2-5 PMs, and Director/VP Product ownership of PRD quality and speed.
- Calculator section: `Estimate the first useful wedge` remains a stable usable tool surface with no calculator hover-depth effects.
- Oversight/reporting sections: cautious public copy around structured knowledge base, PRD/ICP output, multi-agent oversight, reliable reporting rhythm, and production-ready clarity.

## Assets Used

- `assets/3d-arcs/archflow-3d-arc-06-modular-viaduct-segment.webp`

## Deployment And Alias Notes

FACT:
- A workspace-root deploy targeted a different linked Vercel project and did not update the requested public alias.
- The correct deploy root for `archflowautomate.vercel.app` was the public repo root.
- The public repo deployment was promoted to the requested alias after verification.

INTERPRETATION:
- Future public website deploys should run from the public repo root, or the workspace-level deploy wrapper should be checked before use.

GAP:
- No provider, Railway-hosted backend, voice, Telegram, or Notion writeback runtime was verified in this website-only delivery.

## Figma Sync

Figma file: `https://www.figma.com/design/xxKd3iT3uxGIATN7hR92jb`

Captured nodes:

- Landing desktop: `123:2`
- Landing mobile: `124:2`
- Quiz desktop: `125:2`
- Quiz mobile result: `126:2`
- Sync summary frame: `127:2`

The captures used Figma MCP HTML-to-design through headless browser submission and the sync summary page was updated through the Figma Plugin API.

## Validation

Passed before final push:

- `node --check main.js`
- `node --check hover-depth.js`
- `node --check quiz.js`
- `python3 scripts/public_safety_scan.py`
- `python3 project/scripts/pre-push-runtime-guard.py`
- `git diff --check`
- Live alias content-marker check for the current hero title, 3D arch asset, and `Readiness Diagnostic` CTA.
- Live 3D arch asset HTTP check.
- Playwright desktop smoke at 1440px: no horizontal overflow; calculator hover-depth disabled.
- Playwright mobile smoke at 390px: no horizontal overflow; first-screen arch/stages/CTA balanced; calculator hover-depth disabled.

Skipped or bounded:

- Impeccable-specific live/edit scripts were not run because this pass stayed in read-only/design-safe validation.
- Notion, Telegram, Railway/backend, provider routing, and model-runtime checks were out of scope.

## Remaining Risks

- Provider/runtime and Railway claims remain gated by Prompt 2.1 status and are not public website delivery facts.
- The root deploy wrapper should be reviewed before future public website deploys because this pass found a deploy-root mismatch.
