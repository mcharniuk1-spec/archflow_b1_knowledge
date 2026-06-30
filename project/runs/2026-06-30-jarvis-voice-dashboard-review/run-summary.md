# Run: Jarvis Voice Dashboard Review Branch

Date: 2026-06-30
Status: review branch, not merged to main

## Summary

The dashboard review branch extends the static Jarvis shell without enabling backend writes or provider execution.

## Implemented On Review Branch

- Added hash-addressable dashboard views:
  - `#jarvis`
  - `#history`
  - `#schema`
  - `#config`
  - `#plan`
- Added current-session Jarvis chat history with export and clear controls.
- Added browser-local speech output toggle using Web Speech synthesis where supported.
- Kept browser-local voice input through Web Speech recognition where supported.
- Added a block-schema page showing the owner-to-Codex interaction flow and downstream graph/review/memory flow.
- Added a configuration/subprompting page with browser-local prompt candidates and exportable review packets.
- Added a project-plan page showing the E1-E7 spine and current source links.
- Updated the dashboard README with the new page links and voice verification boundary.
- Regenerated dashboard data from public-safe source files.

## Boundaries

- Static dashboard JavaScript still cannot write to GitHub, Notion, WikiLLM, or local files.
- Voice input and output are browser/device dependent.
- Raw audio, raw transcripts, raw uploaded documents, and private source material are not persisted.
- OpenAI, Mistral, Railway, local bridge execution, persistent uploads, and browser writeback remain approval-gated.
- The review branch is not production and should be reviewed before any merge to `main`.

## Verification

- `node --check project/dashboard/app.js`
- dashboard JSON parse
- `git diff --check`
- `python3 scripts/public_safety_scan.py`
- `project/local/venv/bin/python project/scripts/validate-workflows.py`
- Local HTTP 200 checks for dashboard HTML and `data.json`
- Desktop screenshots for Jarvis, block-schema, and config pages
- Mobile screenshot for Jarvis page

## Remaining Gaps

- Physical microphone and speaker behavior requires an interactive browser permission test on the owner's device.
- Human-quality voice depends on installed browser voices until an approved local TTS or provider voice runtime exists.
- Backend persistence, queueing, screen capture, and live Codex bridge require separate auth, storage, data policy, and approval design.
