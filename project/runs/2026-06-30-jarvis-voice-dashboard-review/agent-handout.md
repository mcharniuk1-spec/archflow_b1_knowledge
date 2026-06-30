# Agent Handout: Jarvis Voice Dashboard Review Branch

Use this handout before continuing the dashboard work.

## Current Branch

`review-jarvis-voice-dashboard-20260630`

## Changed Areas

- `project/dashboard/app.js`
- `project/dashboard/styles.css`
- `project/dashboard/README.md`
- `project/dashboard/data.json`
- `project/runs/2026-06-30-jarvis-voice-dashboard-review/`

## What To Review

- Jarvis chat history and export behavior.
- Speech output toggle and browser speech synthesis behavior.
- Voice input recognition behavior in an interactive browser.
- `#schema` page flow for owner-to-Codex and graph/review/memory stages.
- `#config` page browser-local prompt/subprompt editing and export packet behavior.
- `#plan` page E1-E7 status clarity.
- Mobile layout for the expanded navigation and Jarvis chat.

## Do Not Claim Yet

- Do not claim production voice is working until physical mic/speaker behavior is tested.
- Do not claim backend writeback, Railway, model-provider execution, screen capture, or live Codex bridge is enabled.
- Do not merge to `main` without review and final approval.

## Suggested Next Check

Run an interactive browser test on the local device:

1. Open `/project/dashboard/#jarvis`.
2. Enable `Speak replies`.
3. Click `Authorize voice`, then `Start voice`.
4. Say: `open block schema`.
5. Confirm the dashboard hears the command, navigates to `#schema`, records chat history, and speaks the reply.
