# Railway State - Jarvis Chat Rebuild

Date: 2026-07-07
Status: reviewed; no Railway mutation performed

## FACT

- Railway MCP account access is available.
- The account contains an ArchFlow project with one `jarvis-api` service.
- The current local directory is not linked to a Railway project, so generic Railway project-scoped calls fail unless the project is passed explicitly.
- The `jarvis-api` service has a latest successful deployment from 2026-07-03 16:50 UTC.
- Deploy logs show the container started, Uvicorn ran on port 8080, `/health` returned 200, and the Railway healthcheck succeeded.
- Recent Railway HTTP log summary tools returned no HTTP log sample for the latest deployment.
- Deploy logs show a 2026-07-07 `/favicon.ico` 404 only; this is not an API failure.
- Listing production variables was blocked by the approval reviewer because it could expose secret values. No retry or workaround was attempted.

## INTERPRETATION

- Railway is deployed for the provider-disabled Jarvis API baseline, but it is not linked to this local checkout.
- The Railway service appears running from deployment evidence, but there is no current evidence that the dashboard production URL is using Railway as its default API base.
- The production dashboard currently uses the Vercel same-origin API by default unless an operator saves a Railway origin in browser-local config.

## GAP

- No new Railway deploy was performed for the 2026-07-07 chat/file/voice-disabled changes.
- The hosted Railway service has not been updated to the 2026-07-07 local code in this run.
- Railway auth, persistence, provider budget ledger, provider activation, durable writeback, client workspace isolation, and audio runtime remain productization gates.

## NEXT

1. If production deployment is approved, deploy the updated API and dashboard through the approved Vercel/Railway path.
2. After deploy, run hosted `/health`, `/api/chat` with attachment payload, and `/api/voice/chat` disabled-packet checks.
3. Keep provider calls and external writeback at zero unless separate owner/provider approval is granted.
