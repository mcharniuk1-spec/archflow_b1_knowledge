# Cross-Block Boundary Repair And Live Release

Date: 2026-07-13

Status: complete for public website repair and Vercel production release.

## Facts

- The architecture block now handles short desktop viewports without allowing its sticky content to be covered by the next service block.
- Landing typography, layer card, stepper, and calculator work remain browser-local and provider-free.
- Jarvis and dashboard mobile views now constrain headlines, paragraphs, messages, bullets, panels, and controls to the viewport.
- The production alias is `https://archflowautomate.vercel.app`.
- Syntax checks, diff check, public safety scan, local captures, and production captures passed.

## Interpretation

The supplied boundary failure was caused by a sticky frame whose minimum height exceeded a shallow desktop viewport. The repair uses a dedicated short-height scale and explicit mobile containment rules so section boundaries remain visually legible across the public views.

## Gap

Figma baseline sync remains pending because the external-capture workflow requires Playwright MCP and that server was not available in this run. The existing Figma sync state was not falsely updated.

## Next safe action

Connect the approved Playwright MCP and run `workflow/automation/codex-vercel-figma-sync.md` against the current production alias.
