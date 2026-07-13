# Issue - Jarvis Durable Execution Controls

Date opened: 2026-07-13
Status: open; provider execution blocked

## FACT

- Jarvis can search public model metadata and prepare reviewed request packets.
- Both API implementations enforce owner token, request acknowledgement, server allowlist, CORS, and writeback-off checks.
- Configured daily/run budget values do not track actual consumption.
- A replayable request acknowledgement is not an atomic single-use approval.
- The current API therefore returns `durable_nonce_and_spend_ledger_required` before any provider call.

## Required resolution

1. Issue a server-side approval nonce bound to owner, sanitized request hash, model, cap, and expiry.
2. Consume it atomically once and reject replay, mismatch, expiry, and concurrent reuse.
3. Reserve projected spend before the provider request and reconcile actual usage/cost after the response.
4. Enforce daily and per-run limits in durable storage or with a provider-enforced key limit plus a local receipt ledger.
5. Record a sanitized provider/action receipt without raw secret or private prompt content.
6. Test forgery, replay, concurrency, model mismatch, budget exhaustion, provider error, timeout, and rollback.
7. Obtain explicit owner approval for one low-cost local test; keep public provider access disabled.

## Close gate

Close only when the unsafe fixtures and one owner-approved, ledgered provider call pass with zero writeback and an independently reviewed receipt.
