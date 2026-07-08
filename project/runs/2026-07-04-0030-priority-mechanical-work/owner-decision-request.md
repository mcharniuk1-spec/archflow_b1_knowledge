# E4 Social Profile Owner Decision Request

Status: owner decision needed before live profile updates
Related draft packet: `project/runs/2026-07-03-0630-priority-mechanical-work/`

## Purpose

This packet converts the already drafted E4 profile package into a short decision request. It is safe to use as an owner-facing prompt, but it is not approval by itself.

## Decisions Needed

| Decision | Options | Safe default |
|---|---|---|
| Voice lane | ArchFlow company-only, owner/founder personal lane, or both with separate copy | ArchFlow company-only |
| Link target | Current website, future diagnostic page, no link yet | No link yet |
| Visuals | No visual, public-safe artifact card, approved screenshot, approved brand asset | No visual |
| Launch timing | Update now after review, wait for E3 diagnostic, wait for E4.1 content plan | Wait for owner approval |
| Status target | Keep In Progress, move to Review after approved drafts, mark Done after live updates | Keep In Progress |

## Recommended Safe Path

FACT: The profile drafts already exist and passed a mechanical review gate.

INTERPRETATION: The safest next step is owner approval of company-only profile copy, no private visuals, and either no link or the current public website link. The diagnostic-page CTA should wait until E3.4 exists.

GAP: No live profile update can be proven until an approved operator performs it and records a public-safe completion note.

## Copy-Ready Owner Prompt

```text
Please choose the E4 profile setup path:

1. Voice: ArchFlow company-only, owner/founder personal lane, or both?
2. Link: current website, future diagnostic page, or no link yet?
3. Visuals: no visual, public-safe artifact card, approved screenshot, or brand asset?
4. Timing: update now after review, wait for E3 diagnostic readiness, or wait for E4.1 content plan?

No live profile updates will be made until you approve the path.
```

## Blocked Actions

- Do not log private profile URLs, account IDs, credentials, screenshots, or platform-specific private data.
- Do not claim customer demand, ROI, revenue, or market validation.
- Do not publish or edit live profiles from this packet alone.
