# Cross-Block Boundary Repair And Live Release

Status: public repair and Vercel production release complete; Figma baseline sync is pending an external-capture tool.

## Scope

- Repair the architecture-to-service transition when the desktop viewport is short enough to expose the sticky frame boundary.
- Keep the architecture copy, layer card, stepper, and tower contained in the first block.
- Review landing desktop/mobile, quiz result, Jarvis, and dashboard entry views before publication.

## Changed files

- `index.html`
- `site.css`
- `project/live/communication/agent-communication-log.md`
- `jarvis.html`
- `jarvis.css`
- `project/dashboard/index.html`
- `project/dashboard/styles.css`

## Boundaries preserved

- No calculator formulas, provider calls, API credentials, writeback, or backend behavior were changed.
- Unrelated worktree changes remain untouched.

## Local checks

- `git diff --check` passed.
- `node --check site.js` passed.
- HTML parser check passed.
- Public safety scan passed.
- Landing capture reviewed at 2048x512, 1440x900, and 390x900.
- Quiz result capture reviewed at 1440x900.
- Jarvis and dashboard production captures reviewed at desktop and 390px mobile sizes.
- The short desktop capture shows the full architecture card before the block boundary.

## Release evidence

- Vercel: production READY and assigned to `https://archflowautomate.vercel.app`.
- Figma baseline: pending; external capture requires Playwright MCP, which was not available in this run.

## Remaining gaps

- Figma external capture and sync-page update remain the only release gap.
