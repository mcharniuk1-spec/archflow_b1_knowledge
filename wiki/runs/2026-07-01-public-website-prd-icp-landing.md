# 2026-07-01 Public Website PRD/ICP Landing

## Result

The public ArchFlow Automate website was redeployed as a minimal PRD/ICP service landing.

Public URL:

- `https://archflowautomate.vercel.app/`

Diagnostic route:

- `https://archflowautomate.vercel.app/quiz?step=4`

Dashboard route:

- `https://archflowautomate.vercel.app/dashboard`

## Positioning

ArchFlow is positioned as a service-led operating layer for B2B SaaS product teams that need source-backed PRDs, ICP evidence, acceptance criteria, task handoff, and approval-gated agent workflows from scattered project context.

## Structure

The homepage has three blocks:

1. Hero.
2. Service system.
3. Readiness/proof.

The diagnostic remains a subpage. The homepage now includes a browser-local PRD/ICP ROI and knowledgebase-readiness calculator.

## Research Summary

Competitor review shows that product-work platforms already cover customer-signal capture, AI synthesis, roadmap/product-suite operations, PRD/spec generation, knowledge assistants, and governance.

ArchFlow's safer wedge is not replacing those tools. The wedge is turning existing scattered material into reviewed delivery artifacts and a controlled agent-ready operating layer.

## Verification

- JS syntax checks passed.
- Manifest JSON parsed.
- Local route checks passed.
- Desktop/mobile Playwright checks passed.
- Mobile click-depth behavior was verified.
- Public safety scan passed.
- Vercel production deploy completed.
- `archflowautomate.vercel.app` alias was repointed.
- Headless Chrome verified deployed homepage and diagnostic DOM.
- Figma sync completed.
- Notion task was updated.
- Final public-source deployment serves website and dashboard from the same public Git source.
- Vercel SSO protection was disabled for the public project so the live alias is publicly reachable.
- Final route checks passed for `/`, `/quiz?step=4`, `/quiz.html`, `/dashboard`, and `/project/dashboard/data.json`.
- Jesus follow-up review passed: calculator enhanced, quiz save is local-only, no frontend `/api` or `fetch()` calls remain, mobile overflow measured `0` for homepage and quiz step 4.

## Figma

- Sync frame: `https://www.figma.com/design/xxKd3iT3uxGIATN7hR92jb?node-id=122-2`
- Landing desktop: `120:2`
- Landing mobile: `119:2`
- Diagnostic desktop: `118:2`
- Diagnostic mobile: `121:2`

## Notion

Updated:

- `JDB-10`: Done.
- `E3.3.1`: Done.
- `E3.3.1A`: Done.
- `E3.3.1B`: Done.
- `JDB-7`, `E1.3.9`, and `E1.3.10`: kept in Review with updated evidence.

Final Git source proof: commit `3cdefba` was pushed to `origin/review-jarvis-agentbrowser-blockschema-20260630`.

## Guardrails

- No guaranteed ROI.
- No validated demand before E5/E6/E7 proof.
- No provider-backed Jarvis.
- No Railway runtime.
- No browser-side provider calls.
- No autonomous writeback.
- No full platform replacement claim.

## Coordination

A later Jesus starting entry produced root website implementation edits. Messi reviewed and accepted them for redeploy because they strengthen the calculator while preserving static/browser-local boundaries. Future backend/provider/writeback work remains a separate gated lane.
