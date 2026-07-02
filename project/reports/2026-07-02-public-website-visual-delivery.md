# Public Website Visual Delivery Report

Date: 2026-07-02
Status: implemented and locally validated

## Scope

This pass updates the public homepage visual/code implementation only. It does not edit Notion, dashboard backend, provider routing, Telegram, model runtime, CrewAI/LangGraph config, skills, or Prompt 2.1 task-state docs.

## Changes

- Replaced the first-screen boxed system-map visual with the transparent 3D arch object `assets/3d-arcs/archflow-3d-arc-06-modular-viaduct-segment.webp`.
- Added four visible process stages around or near the arch: raw material, knowledge base, PRD/ICP output, and agent oversight.
- Moved the primary `Readiness Diagnostic` call to action under the arch/stage visual and made it wider.
- Updated homepage copy for the current ICP: B2B SaaS, Series B-D, 50-500 employees, 2-5 PMs, and Director/VP Product ownership of PRD quality and speed.
- Preserved cautious runtime wording: browser-local diagnostic first; provider runtime, Railway, voice, and writeback stay gated until verified.
- Kept the `Estimate the first useful wedge` calculator block stable and removed calculator hover-depth behavior.
- Added mobile-specific layout rules so the arch, stages, diagnostic CTA, and next-section cue fit inside a 390px viewport without horizontal overflow.

## Assets Used

- `assets/3d-arcs/archflow-3d-arc-06-modular-viaduct-segment.webp`

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
- Playwright layout smoke for desktop and mobile:
  - desktop viewport 1440: `scrollWidth=1440`
  - mobile viewport 390: `scrollWidth=390`
  - mobile diagnostic CTA visible in first screen
  - mobile next-section cue visible in first screen
  - calculator `depth-hover` class absent

Skipped or bounded:

- Production deploy, Vercel promotion, Figma sync, Notion update, Telegram send, provider calls, Railway checks, and backend runtime validation were out of scope for this website-only pass.
- Global Python workflow validation failed because the global runtime lacks `yaml`; repo-local workflow validation passed and is the relevant project check.

## Coordination

Prompt 2.1 had posted a complete handoff before this website pass started. Its handoff keeps provider runtime, Railway, voice, Telegram, writeback, and full PRD/ICP test-cycle execution gated. This website pass followed that boundary and did not modify Prompt 2.1-owned files.

Git commit, push, and main merge were not performed in this pass because the same public worktree contains pre-existing Prompt 2.1 dirty files. Stage/push should happen only after an ownership-safe decision on whether to commit website files separately or coordinate a broader Prompt 2.1 plus website commit set.

## Remaining Risks

- The homepage visual is validated locally, not deployed.
- Main still needs a coordinated commit/push decision.
- Figma sync is only required after a successful Vercel deploy; no deploy occurred in this pass.
