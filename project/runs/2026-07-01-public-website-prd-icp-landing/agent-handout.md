# Agent Handout: Minimal Public PRD/ICP Services Landing

Date: 2026-07-01
Owner lane: Ronaldo
Status: deployed, Figma-synced, Notion-updated, pending final Git/source alignment review

## Current State

The public ArchFlow Automate site now serves a minimal PRD/ICP services landing at:

- `https://archflowautomate.vercel.app/`

The diagnostic route is:

- `https://archflowautomate.vercel.app/quiz?step=4`

Vercel clean URLs redirect `/quiz.html` to `/quiz`.

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

## Figma

Figma sync frame:

- `https://www.figma.com/design/xxKd3iT3uxGIATN7hR92jb?node-id=122-2`

Capture nodes:

- landing desktop: `120:2`
- landing mobile: `119:2`
- diagnostic desktop: `118:2`
- diagnostic mobile: `121:2`

## Notion

Updated task:

- `E3.3.1 - Public PRD/ICP services landing and diagnostic deployment closeout`

Status remains Review because final Git/source alignment and active-lane closeout are still pending.

## Guardrails

- No guaranteed ROI.
- No validated demand before E5/E6/E7 proof.
- No provider-backed Jarvis.
- No Railway runtime.
- No browser-side provider calls.
- No autonomous writeback.
- No full Productboard/Aha/Dovetail replacement claim.

## Next Safe Action

Messi should use the Notion update and this handout for PM review. LOL/Jesus can continue dashboard work without touching the root website lane. Final branch/source alignment should happen after active lanes close or hand off.
