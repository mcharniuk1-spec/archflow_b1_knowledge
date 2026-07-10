# Jarvis API Service

Provider-disabled FastAPI contract for the ArchFlow dashboard MVP.

Current state:

- `MODEL_PROVIDER=none` is the default.
- A dated Railway E1.7 baseline record exists for hosted health, CORS, chat, PRD/ICP, agent-orchestra, role config, and voice-safe text packet routes. It is historical evidence only, not current hosted-freshness, availability, or always-online proof.
- The 2026-07-07 dashboard contract uses text chat and bounded file attachments through `/api/chat`.
- `/api/voice/*` now returns disabled packets; voice mode is off in the main dashboard.
- OpenRouter is server-side only and disabled until owner approval, server-side secrets, fresh pricing, ledger proof, and budget guard are live.
- CrewAI Level 3 is represented only as `proof_passed_not_default_runtime`.
- Browser requests create review packets; they do not write Git, Notion, WikiLLM, Telegram, or deployment state.

Run locally after installing dependencies in an approved environment:

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8787
```

Required endpoints are implemented in `app.py`. Main Jarvis chat uses `/api/chat`; PRD/ICP and Agent Orchestra screens keep their lane endpoints.

Railway deploy root:

```bash
railway up services/jarvis-api --path-as-root --service jarvis-api --environment production --detach
```

Public reports must not store Railway account IDs, deployment IDs, or service-domain metadata. Record endpoint status and safety state instead.

Railway configuration is a future deployment prerequisite, not deployment authorization. A later approved deployment must separately prove the current `/health` result, auth/CORS and secret handling, provider-disabled-first behavior, logs, rollback/recovery, and ongoing observability. A deployment healthcheck is not continuous monitoring.
