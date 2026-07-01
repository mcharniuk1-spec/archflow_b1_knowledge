# Agent Handout: Minimal Public PRD/ICP Services Landing

Date: 2026-07-01
Owner lane: Ronaldo
Status: deployed, Figma-synced, Notion-updated, source-aligned in public worktree

## Current State

The public ArchFlow Automate site now serves a minimal PRD/ICP services landing at:

- `https://archflowautomate.vercel.app/`

The diagnostic route is:

- `https://archflowautomate.vercel.app/quiz?step=4`

Vercel clean URLs redirect `/quiz.html` to `/quiz`.

The operator dashboard is live at:

- `https://archflowautomate.vercel.app/dashboard`

## Positioning

ArchFlow is presented as a service-led operating layer for B2B SaaS product teams with scattered product context.

The offer is:

- source inventory;
- source-backed PRD packet;
- ICP evidence review;
- acceptance criteria and task handoff;
- approval-gated agent operating layer.

The site does not present ArchFlow as a full roadmap platform, feedback repository, enterprise search tool, or generic PRD generator replacement.

## Page Structure

Homepage blocks:

1. Hero: PRDs from your project knowledgebase.
2. System: three service outputs.
3. Proof/trust: E1-E7 delivery spine and public boundaries.

Subpage:

- Diagnostic flow for first-package recommendation, knowledgebase readiness, agent readiness, planning estimate, approval gates, and optional follow-up.

## Important Design Notes

- Use only one primary arch visual on the landing.
- Keep the dark flow panel.
- Keep copy laconic.
- Avoid decorative overload.
- Mobile buttons now tilt toward the tap/click point through `hover-depth.js`.
- Desktop hover-depth remains active for fine pointers.

## Files In Scope

- root `index.html`
- root `main.js`
- root `styles.css`
- root `hover-depth.js`
- root `quiz.html`
- root `quiz.js`
- root `site.webmanifest`
- root `dashboard.html`
- public brand/icons/arch assets under `assets/`
- `workflow/automation/latest-figma-sync.json`
- `public/project/reports/2026-07-01-public-website-market-research-and-minimal-copy.md`
- this run handout and matching run/wiki notes

## Files Out Of Scope

Dashboard implementation and smoke-test files remain with LOL/Jesus:

- `public/project/dashboard/*`
- `public/project/scripts/dashboard-static-smoke.py`

Provider/backend/runtime work remains out of scope:

- no provider activation;
- no Railway runtime claim;
- no durable writeback;
- no browser-side provider calls.

## Checks Passed

- JS syntax: `main.js`, `quiz.js`, `hover-depth.js`.
- Manifest JSON parse.
- Local route HEAD checks for `/` and `/quiz.html?step=4`.
- Desktop and mobile Playwright layout checks.
- Mobile button click-depth variable check.
- Public safety scan.
- `git diff --check`.
- Vercel production deploy.
- Custom alias `archflowautomate.vercel.app` repointed.
- Deployed homepage and diagnostic DOM verified with headless Chrome.
- Final public-source deployment verified `/`, `/quiz?step=4`, `/quiz.html`, `/dashboard`, and dashboard data route.
- Vercel SSO protection was disabled for the public project so the live alias is publicly reachable.
- Jesus follow-up review: homepage calculator expanded into PRD/ICP ROI and KB-readiness modes.
- Jesus follow-up review: quiz save action is browser-local and root/quiz scripts contain no `/api` or `fetch()` calls.
- Chrome layout measurement: homepage mobile overflow `0`; quiz step 4 mobile overflow `0`.

## Figma

Figma sync frame:

- `https://www.figma.com/design/xxKd3iT3uxGIATN7hR92jb?node-id=122-2`

Capture nodes:

- landing desktop: `120:2`
- landing mobile: `119:2`
- diagnostic desktop: `118:2`
- diagnostic mobile: `121:2`

## Notion

Updated tasks:

- `JDB-10`: Done for accepted static dashboard/Jarvis scope.
- `E3.3.1`: Done for public PRD/ICP landing, diagnostic, dashboard route, Figma sync record, and deployed source alignment.
- `E3.3.1A`: Done for source/deploy alignment resolution.
- `E3.3.1B`: Done for deploy/Figma/Notion/Git closeout.
- `JDB-7`, `E1.3.9`, and `E1.3.10`: kept in Review with updated evidence because branch promotion and provider/backend/security gates remain future decisions.

Final Git source proof: commit `3cdefba` was pushed to `origin/review-jarvis-agentbrowser-blockschema-20260630`.

## Guardrails

- No guaranteed ROI.
- No validated demand before E5/E6/E7 proof.
- No provider-backed Jarvis.
- No Railway runtime.
- No browser-side provider calls.
- No autonomous writeback.
- No full Productboard/Aha/Dovetail replacement claim.

## Next Safe Action

Redeploy the accepted Jesus calculator/local-save enhancement from the public worktree, then update Notion with the new final commit. Future backend/provider/writeback work remains a separate gated lane.
