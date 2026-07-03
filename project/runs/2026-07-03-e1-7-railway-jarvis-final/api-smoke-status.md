# API Smoke Status

Date: 2026-07-03
Status: passed

## Local Contract Smoke

The in-process FastAPI TestClient smoke passed across 17 endpoint checks. It verified that the provider-disabled contract returns review packets without provider calls or external writeback.

Summary:

```text
jarvis_api_contract_smoke=ok endpoints=17 provider_calls=0 writeback=0
```

## Hosted Smoke

The hosted Railway API passed:

- health;
- CORS preflight;
- chat;
- role config;
- PRD/ICP lane;
- agent-orchestra lane;
- voice-safe text lane.

## Boundary

The smoke does not prove:

- provider-backed model calls;
- auth;
- durable storage;
- dashboard-driven writeback;
- raw audio handling;
- client workspace isolation.
