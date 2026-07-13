# Block 1 Architecture And ROI Refinement

Status: production deployment complete; Figma baseline sync remains pending because external Playwright MCP is unavailable.

## Objective

Make the seven-layer tower explain the current ArchFlow knowledge-continuity and bounded-agent architecture while making the ROI scenario readable, draggable, bounded, and responsive.

## Implementation

- Reframed Block 1 around enterprise readiness, onboarding/hiring, and key-person continuity.
- Named and sharpened all seven architecture layers: Govern, Connect, Orchestrate, Execute, Verify, Remember, and Measure.
- Synchronized layer titles, pain statements, outcomes, methods, status, stepper state, and tower movement.
- Kept the supplied transparent tower assets as the visual source and made the complete assembly visible at desktop, tablet, and mobile states.
- Replaced numeric ROI text fields with range controls for people, recovery hours, hourly cost, tool surfaces, and setup investment.
- Set working ranges to 1-100 people, 0.5-20 recovery hours, EUR20-EUR350 hourly cost, 1-100 tools/surfaces, 0-100% recovery, and EUR2,000-EUR30,000 setup investment.
- Added visible live values, range-track progress, larger desktop values, mobile density controls, readiness gradient, and outcome-card lightness feedback.
- Added a small ROI preview query state for repeatable visual QA without changing the default public route.

## Changed files

- `index.html`
- `site.css`
- `site.js`
- `project/live/communication/agent-communication-log.md`

## Validation

- `node --check site.js` passed.
- `git diff --check` passed.
- Desktop 1440px, tablet 1024px, and mobile 390px landing captures reviewed.
- Desktop and mobile ROI preview captures reviewed.
- Production alias returned HTTP 200 and live desktop/mobile captures were reviewed.
- Range controls rendered with live values and no numeric text inputs remain in the calculator.
- Supplied seven-layer transparent assets remain the tower source.
- Public safety scan is the final pre-deploy gate.

## Boundaries

- The calculator remains browser-local and directional; no guaranteed ROI or customer result is claimed.
- Provider calls, writeback, source crawling, and external action remain unchanged and gated.
- Figma baseline sync remains pending until external Playwright MCP is available.

## Release closeout

- Production alias: `https://archflowautomate.vercel.app`
- Live captures: `tmp/live-block1-desktop.png`, `tmp/live-block1-mobile.png`, `tmp/live-roi-desktop.png`, `tmp/live-roi-mobile.png`
- Figma baseline sync: not claimed complete; external Playwright MCP is unavailable in this runtime.
