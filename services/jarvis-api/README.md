# Local Jarvis Review-Packet API

This optional FastAPI service gives local integrations a review-packet compatibility layer for the ArchFlow V3 dashboard while preserving the public product boundary. It validates bounded inputs, projects the canonical 21 functional roles from `project/database/role-catalog.json`, and returns schema `3.0` packets for human review.

It does not call an external runtime, select an execution model, read secret values, persist packets, change source files, start agents, or perform an external action. `/api/models` intentionally returns empty `providers` and `models` arrays. The local service is not an administrator boundary; hosted administrator access is enforced separately by the Google OIDC routes under `api/auth/`.

## Run locally

Install dependencies only in an approved isolated environment, then bind the development service to loopback:

```bash
uvicorn app:app --host 127.0.0.1 --port 8787
```

Set `JARVIS_API_ALLOWED_ORIGIN` to one exact browser origin when the dashboard runs on a fixed local port. When it is unset, the service accepts browser origins only from `localhost` or `127.0.0.1` with an explicit port. Stop the process to uninstall the runtime behavior; packets are not stored by the service.

## Compatibility routes

- `GET /health` and `GET /api/health` report only stable public contract state.
- `GET /api/models` returns no execution choices.
- `POST /api/chat` prepares a Communication Center handoff.
- `GET /api/config/roles` projects the canonical 21-role catalog.
- `POST /api/config/roles/update` validates a candidate but never changes the catalog.
- `GET|POST /api/lanes/prd-icp` prepares a bounded requirements-definition packet.
- `GET|POST /api/lanes/agent-orchestra` prepares a smallest-responsible role plan.

Every response reports zero provider calls and zero external writes. Route success proves packet preparation only; it does not prove shared tenancy, durable storage, administrator authorization, execution, deployment, or production availability.
