# Agent Handout: Public Website Visual Delivery

Date: 2026-07-02
Owner lane: website visual/code implementation
Status: implemented and locally validated

## Purpose

Use this handout to continue or review the public homepage visual delivery work without relying on chat history. The run is scoped to root website files and a website-specific report only.

## Human Summary

The homepage now presents ArchFlow as a service for B2B SaaS product teams that turns raw product-team material into production-ready PRD/ICP clarity through a structured knowledge base and review-gated agent oversight.

The first screen no longer uses the boxed system-map image. It uses the transparent 3D arch asset `assets/3d-arcs/archflow-3d-arc-06-modular-viaduct-segment.webp`, with four process stages placed around or near the arch and a wide `Readiness Diagnostic` button directly underneath.

The PRD/ICP calculator remains the same usable planning tool. It keeps the `Estimate the first useful wedge` section, but hover-depth behavior was removed from the calculator surface so it does not behave like a decorative card.

## Current State

- Root homepage files are updated: `index.html`, `styles.css`, `main.js`, and `hover-depth.js`.
- The selected 3D arch asset loads locally.
- Desktop and mobile visual smoke passed with exact Playwright viewports.
- Runtime/provider claims remain cautious and consistent with Prompt 2.1: browser-local diagnostic first; provider runtime, Railway, voice, and writeback remain gated until verified.
- No deploy, production promotion, Figma sync, Notion update, Telegram send, or backend/provider runtime check occurred in this pass.

## Agent Continuation Prompt

Continue the ArchFlow public website visual delivery from `project/runs/2026-07-02-public-website-visual-delivery/agent-handout.md`.

First read `project/live/communication/agent-communication-log.md` and check current file claims. Preserve Prompt 2.1 boundaries: do not edit Notion, runtime stack docs, skills, model routing, CrewAI/LangGraph config, Telegram, Railway/backend files, or dashboard backend files unless explicitly handed off.

If continuing website work, inspect `index.html`, `styles.css`, `main.js`, and `hover-depth.js`. Keep the 3D arch hero, process stages, wide diagnostic CTA, stable calculator, public-safe ICP copy, and cautious runtime claims. Validate with JS syntax checks, public safety scan, diff whitespace check, and desktop/mobile browser smoke. Stop before deploy, push, or main merge unless ownership and approval are explicit.

## Execution Trace

FACT:
- The work started after the live communication log showed Prompt 2.1 complete enough for website implementation and still gating provider/runtime claims.
- A starting update was appended before editing website files.
- The homepage was updated to use `assets/3d-arcs/archflow-3d-arc-06-modular-viaduct-segment.webp`.
- The calculator form now has `data-depth-hover-disabled`, and `hover-depth.js` no longer targets `.mini-calc` or `.calc-metrics article`.
- Exact mobile Playwright layout returned `scrollWidth=390` at a 390px viewport.

INTERPRETATION:
- The selected arch asset fits the requested white/clean visual direction better than the red-heavy twin-frame asset because red stays a restrained accent.
- The mobile hero needs a shorter title line and 320px content measure to keep the arch/stage/CTA system visible without clipping.

GAP:
- The work is not deployed or Figma-synced.
- Commit/push is still blocked by shared dirty worktree ownership.

## Decisions

- Use `archflow-3d-arc-06-modular-viaduct-segment.webp` as the primary hero visual.
- Keep blue as the continuity CTA color and use red only through the arch asset and small stage numerals.
- Keep secondary hero actions off mobile so the arch, process stages, diagnostic CTA, and next-section cue appear in the first screen.
- Do not make the calculator a hover-depth surface.

## Artifacts

- `index.html`: homepage copy, hero structure, process stages, calculator hover-disable attribute.
- `styles.css`: hero visual system, mobile responsive fit, calculator tool-surface styling.
- `main.js`: hero arch pointer motion and updated reveal selector.
- `hover-depth.js`: calculator removed from hover-depth targeting.
- `project/reports/2026-07-02-public-website-visual-delivery.md`: website execution report.

## Validation

Passed:

- `node --check main.js`
- `node --check hover-depth.js`
- `node --check quiz.js`
- `python3 scripts/public_safety_scan.py`
- `git diff --check`
- `project/local/venv/bin/python project/scripts/validate-workflows.py`
- `python3 project/scripts/pre-push-runtime-guard.py`
- Local route checks for `/`, `/quiz.html`, `/dashboard.html`, and the selected 3D arch asset.
- Playwright desktop and mobile layout smoke, including mobile `scrollWidth=390` and calculator `depth-hover=false`.

Skipped or not performed:

- Production deploy.
- Vercel promotion.
- Figma sync.
- Notion update.
- Git push.
- Provider, Railway, voice, Telegram, or writeback runtime checks.

## Next Actions

1. Decide whether to commit only website files or coordinate one broader Prompt 2.1 plus website commit set.
2. If committing website-only, stage only `index.html`, `styles.css`, `main.js`, `hover-depth.js`, `project/reports/2026-07-02-public-website-visual-delivery.md`, this handout, and the website communication-log entries.
3. Re-run public safety scan and diff whitespace check immediately before any push.
4. Deploy only after explicit approval; if a Vercel deploy succeeds, run the required Figma sync workflow.

## Safety Boundary

Do not store secrets, private URLs, account IDs, local absolute paths, raw private source text, screenshots, credentials, or personal identifiers in public files. Keep provider/runtime, Railway, voice, Telegram, Notion writeback, and autonomous writeback claims gated until separately implemented and verified.
