# CrewAI / LangGraph Operations

Status: Prompt 2 operations contract

## Current Runtime Split

FACT:
- LangGraph is the controller for routing, state, gates, review stops, and output packets.
- CrewAI organizes role/task structure.
- CrewAI Level 3 direct runtime has proof status `proof_passed_not_default_runtime`.
- OpenRouter provider runtime is disabled.

INTERPRETATION:
- The dashboard can show CrewAI direct-proof readiness without making CrewAI the default runtime.
- Provider-backed worker execution is a later activation lane, not part of this MVP.

GAP:
- No approved backend/local bridge.
- No server-side secret store.
- No provider-backed ledger proof.
- No live budget guard against real provider pricing.
- No live Notion/WikiLLM/GitHub/Telegram writeback.

## OpenRouter Budget Rules

- Daily hard cap: `5.00` USD.
- Per-run hard stop: `1.99` USD.
- Each run must stay under `2.00` USD.
- Over-cap behavior: stop and request owner approval.
- Browser JavaScript must never read provider keys.

## API Boundary

`services/jarvis-api/` is a provider-disabled FastAPI contract. It may return review packets and health/config state. It must not call providers or write external systems until a later approved activation pass.

## CrewAI Proof Boundary

The proof run used a deterministic local fixture and recorded zero provider calls, zero external writeback, and zero spend. It does not prove provider-backed runtime, production runtime, or default runtime.
