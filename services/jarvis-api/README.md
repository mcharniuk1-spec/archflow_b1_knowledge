# Jarvis API Service

Guarded FastAPI contract for the ArchFlow Jarvis owner console.

Current state:

- `MODEL_PROVIDER=none` and `JARVIS_ENABLE_PROVIDER_CALLS=false` are the defaults.
- A dated Railway E1.7 baseline record exists for hosted health, CORS, chat, PRD/ICP, agent-orchestra, role config, and voice-safe text packet routes. It is historical evidence only, not current hosted-freshness, availability, or always-online proof.
- The 2026-07-07 dashboard contract uses text chat and bounded file attachments through `/api/chat`.
- `/api/voice/*` now returns disabled packets; voice mode is off in the main dashboard.
- OpenRouter credentials are server-side only. Provider execution is currently disabled even if the provider switch is requested; activation requires a server-enforced single-use nonce plus durable projected/actual spend enforcement.
- The browser can search the public OpenRouter catalog, but search results do not become executable until their model ID is added to `OPENROUTER_ALLOWED_MODELS`.
- The browser never receives the provider key or stores the owner token. It sends the owner token only to the same origin or an HTTP loopback API. Current budget values are configuration envelopes, not consumption controls.
- CrewAI Level 3 is represented only as `proof_passed_not_default_runtime`.
- Browser requests create review packets; they do not write Git, Notion, WikiLLM, Telegram, or deployment state.

Run locally after installing dependencies in an approved environment:

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8787
```

Required endpoints are implemented in `app.py`. Main Jarvis chat uses `/api/chat`, `/api/models` exposes public-safe route metadata and the execution allowlist, and PRD/ICP and Agent Orchestra screens keep their lane endpoints.

Railway deploy root:

```bash
railway up services/jarvis-api --path-as-root --service jarvis-api --environment production --detach
```

Public reports must not store Railway account IDs, deployment IDs, or service-domain metadata. Record endpoint status and safety state instead.

Railway configuration is a future deployment prerequisite, not deployment authorization. A later approved provider implementation must add an atomic short-lived nonce bound to the request/model, reject replay, and reconcile projected plus actual cost against a durable ledger or provider-enforced key limit. It must separately prove `/health`, auth/CORS, logs, rollback/recovery, and ongoing observability. A deployment healthcheck is not continuous monitoring.
