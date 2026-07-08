# Jarvis Chat API Rebuild Handout

## Title And Purpose

This handout covers the 2026-07-07 Jarvis dashboard rebuild that makes the first screen a large text-first chat, disables voice mode, adds bounded file transfer to Jarvis chat, and checks Railway/Vercel API state.

## Human Summary

The dashboard Jarvis tab was changed from a hero-style command center with voice controls into a large chat-first workspace. The first screen now shows the conversation, architecture selector, mode selector, attachment tray, file attach control, and send box. The old fixed bottom composer is hidden on the Jarvis tab so there is one primary chat surface.

Voice mode is disabled in the dashboard UI and API contract. Browser mic, browser speech synthesis, STT, TTS, and `/api/voice/*` runtime behavior are no longer presented as active Jarvis features. The backend voice routes now return disabled packets and point operators back to `/api/chat`.

File handling now stages pending attachments for the next Jarvis message. Text-like files transfer a bounded text excerpt; binary or unsupported files transfer metadata only. The dashboard does not write uploaded content durably.

Live production was checked but not redeployed. The production Vercel API still reports the older July 3 contract and ignores the new attachment payload. Railway is deployed and running from the prior provider-disabled baseline, but it was not mutated or redeployed in this run.

## Current State

- Task status: local implementation complete; production deployment not performed.
- Main dashboard chat: implemented under `project/dashboard/app.js` and `project/dashboard/styles.css`.
- Main API route: `/api/chat`.
- File transfer: bounded text excerpts or metadata-only attachment summaries.
- Voice: disabled in UI and API contract.
- Provider calls: still zero by default.
- External writeback: still zero.
- Railway: prior `jarvis-api` deployment is successful and running; no 2026-07-07 redeploy.

## Agent Continuation Prompt

Continue the Jarvis chat/file/API deployment lane from `project/runs/2026-07-07-jarvis-chat-api-rebuild/`. First read `project/operating-rules.md`, `project/live/communication/README.md`, `project/live/communication/current-agent-notice.md`, the latest live log entries, `project/dashboard/README.md`, `services/jarvis-api/README.md`, and `skills/archflow1/SKILL.md`.

Goal: if owner approval is given for deployment, publish the updated dashboard/API without activating provider calls or writeback. Use the approved Vercel deploy script when possible and follow the Figma sync rule after a successful Codex-initiated Vercel deploy. Then verify hosted `/health`, hosted `/api/chat` with one bounded attachment payload, and hosted `/api/voice/chat` returning disabled status. Do not expose Railway IDs, service domains, deployment IDs, account IDs, secrets, private URLs, or raw uploaded file content in public files.

Stop conditions: missing deployment approval, failed public safety scan, failed JS/API smoke, Railway/Vercel auth blocker, or any request to activate providers/writeback without separate approval.

## Execution Trace

FACT:
- Skill Spectre scanned the global ArchFlow dashboard readiness skill and the project-local `archflow1` skill. Both were low-risk static scans; semantic LLM scanning was unavailable.
- The live communication start entry was appended before edits.
- The dashboard first screen was rebuilt around `Jarvis Chat`.
- `/api/chat` payloads now include recent conversation context and pending attachments.
- Vercel serverless and Railway FastAPI contracts were updated for attachments and disabled voice behavior.
- The public `archflow1` skill and dashboard/API docs were updated to match the new voice-disabled policy.
- Railway MCP showed the ArchFlow project and `jarvis-api` service; latest deployment status is successful from 2026-07-03.
- Production Vercel `/health` still reports the July 3 API version and voice as browser text mode, proving production is not yet on the 2026-07-07 local code.

INTERPRETATION:
- The local source is ready for review as a text-chat and file-transfer Jarvis surface.
- Live production remains on the previous contract until a deployment is explicitly approved and completed.

GAP:
- No Vercel deploy, Railway deploy, Git push, provider activation, durable writeback, auth hardening, persistence, or Figma sync was performed.

## Decisions

- Keep voice disabled instead of retaining fallback mic/speaker controls.
- Use `/api/chat` for the main Jarvis conversation.
- Keep PRD/ICP and Agent Orchestra screens on their existing lane endpoints.
- Do not inspect Railway variables because that would expose secret values.
- Do not deploy production without explicit approval.

## Artifacts

- `project/dashboard/app.js`: chat-first Jarvis UI, attachment handling, `/api/chat` route.
- `project/dashboard/styles.css`: chat layout, attachment chips, responsive behavior.
- `api/_jarvis_contract.py`: Vercel serverless chat attachment and disabled voice contract.
- `services/jarvis-api/app.py`: FastAPI chat attachment and disabled voice contract.
- `project/scripts/dashboard-static-smoke.py`: updated route markers for chat-first Jarvis.
- `project/scripts/jarvis-api-contract-smoke.py`: attachment payload coverage.
- `project/dashboard/README.md`: updated operating docs.
- `services/jarvis-api/README.md`: updated API contract docs.
- `skills/archflow1/SKILL.md`: updated voice-disabled skill policy.
- `project/runs/2026-07-07-jarvis-chat-api-rebuild/railway-state.md`: Railway state note.

## Validation

- Pass: `node --check project/dashboard/app.js`.
- Pass: Python compile for Vercel API, Railway API, and smoke scripts.
- Pass: `jq -e 'type == "object"' project/dashboard/data.json`.
- Pass: `python3 project/scripts/dashboard-static-smoke.py` with approved local HTTP/headless Chrome permission: `routes=8 provider_calls=0 writeback=0`.
- Pass: `project/local/venv/bin/python project/scripts/jarvis-api-contract-smoke.py`: `endpoints=17 provider_calls=0 writeback=0`.
- Pass: `python3 scripts/public_safety_scan.py`.
- Pass: `git diff --check`.

## Next Actions

1. Get explicit approval before any production deploy or Git push.
2. If deployment is approved, deploy with the approved Vercel flow and perform the required Figma sync.
3. Verify hosted Vercel API version changes to the 2026-07-07 contract.
4. If Railway should serve as the main API base, deploy the updated `jarvis-api` service and verify it separately.
5. Keep provider activation, durable upload storage, auth, and writeback as separate gates.

## Safety Boundary

Do not store secrets, Railway IDs, service domains, deployment IDs, account IDs, private links, local absolute paths, raw uploaded file contents, private source text, credentials, provider variable values, or private screenshots in public files. Do not activate providers, writeback, Telegram, Notion, GitHub, or production promotion without explicit approval.
