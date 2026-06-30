# Decision: Dashboard Jarvis Vercel Shell

Date: 2026-06-30
Status: accepted for first hosted dashboard

## Decision

Use a Vercel preview as the first hosted dashboard target. The dashboard is public-safe and read-only at the hosted data layer, with a browser-local Jarvis command shell for normal/interview mode, current-session voice transcript commands, file metadata packet preparation, and local packet downloads.

Railway remains deferred until the system needs server-side auth, live APIs, event streams, durable uploads, background workers, persistent state, model-provider calls, or write actions.

## Rationale

The current dashboard is static and already uses generated public-safe `data.json`. Vercel can host that safely if the data remains public-safe and no secrets/private state are emitted. A hidden link helps review but is not authentication; Vercel preview authentication is acceptable for this first review pass.

Canonical review route:

- `https://public-mcharniuk1-4994-mcharniuk1-4994s-projects.vercel.app/project/dashboard/`

An initial Vercel CLI deploy without `--prod` was recorded by Vercel as target `production`; the explicit `--target preview` deployment above is the approved review target. Future deploy commands stay explicit with `--target preview` until owner approval for production.

## Consequences

- Add `noindex` and no-cache headers for the dashboard.
- Do not add a client-side password as security.
- Do not put private data in `data.json` or client JavaScript.
- Do not write to GitHub, Notion, WikiLLM, Obsidian, or local files from static browser code.
- Do not read or store uploaded document bodies in the static dashboard.
- Keep browser packets/events session-only unless the user downloads a packet manually.
- Use Codex or a future Railway backend for durable writeback.
- Keep voice and file handling browser-local until storage/privacy/auth rules are implemented.

## Follow-Up

Google account auth, Railway API, SSE/websocket events, upload processing, model-provider calls, and write actions remain separate gated work.
