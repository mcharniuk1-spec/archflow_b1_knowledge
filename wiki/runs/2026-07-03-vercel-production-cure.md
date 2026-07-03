# 2026-07-03 Vercel Production Cure

Status: complete for production-current guarded cloud review flow

## FACT

- The exact public dashboard URL now points to the current Vercel production deployment.
- Production dashboard data is current for this cure run and was regenerated during the final deployment sync.
- Vercel same-origin Jarvis API health, Architecture 1, Architecture 2, voice-text, and role config routes passed.
- Railway Jarvis deployed successfully with the service directory as archive root and Nixpacks as builder.
- Railway health, CORS, Architecture 1, Architecture 2, voice-text, role config, and role-update candidate routes passed.
- Both Vercel and Railway report `MODEL_PROVIDER=openrouter`.
- Provider calls remained `0`; external writeback remained `0`.
- Provider-approved route tests returned review packets with `openrouter_api_key_missing`.
- No legacy Vercel project was deleted because safe deletion evidence was not complete.

## INTERPRETATION

The public cloud surface is now reliable for Epic 1's guarded review-flow scope: current dashboard, Vercel API, Railway API, and architecture-specific Jarvis packets. It is not yet a full product runtime because provider execution, auth, persistence, durable writeback, raw voice, and buyer proof remain gated.

## GAP

- Explicit approval is required before storing the OpenRouter key in Vercel/Railway environment variables.
- A provider-backed run still needs a model-call ledger, sanitized input class, and low-cost hard stop.
- Vercel legacy cleanup needs a separate owner-approved inventory before deletion.

## OUTPUTS

- `project/reports/2026-07-03-vercel-production-cure-report.md`
- `project/runs/2026-07-03-vercel-production-cure/agent-handout.md`
- `project/runs/2026-07-03-vercel-production-cure/notion-update-packet.md`
- Updated E1.7, Epic 1, cloud retrospective, and Railway setup reports.
