# Landing Typography And Calculator Balance

Status: complete for the bounded local visual refinement.

## Scope

- Refined the public landing page typography toward the supplied Sandstone reference.
- Rewrote the first-screen message for a more precise product value statement.
- Increased calculator label, input, result, and explanatory text sizes.
- Rebalanced calculator controls for desktop and mobile, including larger horizontal range thumbs and tracks.

## Files changed

- `index.html`
- `site.css`

## Boundaries preserved

- Calculator formulas and JavaScript behavior were not changed.
- No provider calls, external writes, deployment, or publication actions were performed.
- Existing unrelated worktree changes remain untouched.

## Checks

- `git diff --check` passed.
- `node --check site.js` passed.
- HTML parser check passed for `index.html`.
- Public safety scan passed.
- Desktop Chrome capture passed for the landing hero at 1440px.
- Mobile Chrome capture passed for the landing hero at 390px after a viewport-overflow repair.
- Direct ROI anchor capture was incomplete in headless file-mode, so no false full-section visual claim is made; calculator CSS and DOM contract checks passed.

## Next safe action

- Review the responsive screenshots, repair only blocking visual defects, then run the public safety scan if the public change is accepted for release.
