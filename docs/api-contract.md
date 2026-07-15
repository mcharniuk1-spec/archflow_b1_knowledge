# Guarded API Contract

The public API files provide a review-packet contract. They are not evidence of a running hosted service, provider-backed completion, durable spend ledger, or external writeback.

## Browser-local report contract

Before a guarded API route is considered, the dashboard and Jarvis can prepare two browser-local artifacts:

1. **Knowledge Service report** — goal, declared public/safe project reference, source boundary, requested output, reviewer, constraints, FACT / INTERPRETATION / HYPOTHESIS / GAP sections, and a `review_required_not_executed` state.
2. **Agent Control handoff** — reuses the report ID and proposes roles, packaged skills, method checklists, sources, review gate, stop conditions, and suggested files marked `created: false` and `requires_operator_review: true`.

Those downloads are generated in the browser. They carry no API base, owner token, provider key, repository write, agent launch, or external-write receipt. Guest preview does not show API/token controls or load a model catalog automatically. Admin preview can optionally ask a same-origin/HTTP-loopback guarded route for a contract-status review; that request sends a minimal status descriptor, not the report body, source boundary, project reference, or chat history, and does not turn provider execution or writeback on.

## Shared response envelope

Every current route returns a JSON envelope with `kind`, `status`, `created_at`, `runtime`, `budget`, and `payload`.

- `runtime.provider_calls` and `runtime.external_writeback` remain zero in the default contract.
- `budget` explains the configured guard state; it is not a durable cross-instance spend ledger.
- Responses may contain a review packet or a blocked reason. They never fabricate a model response when provider execution is unavailable.

## Routes

| Route | Purpose | Accepted input | Side effects | Current behavior |
|---|---|---|---|---|
| `GET /health` | Read the guarded contract state. | None. | None. | Reports provider/writeback and durable-control boundaries. |
| `POST /api/chat` | Prepare a general Jarvis review packet. | Request, architecture, selected model, optional acknowledgement. | None by default. | Returns a blocked/guarded review packet when provider conditions are not met. |
| `POST /api/lanes/prd-icp` | Prepare a PRD/ICP lane packet. | Bounded request and source references. | None by default. | Returns output structure, questions, and gates—not a provider execution claim. |
| `POST /api/lanes/agent-orchestra` | Prepare an Agent Control lane packet. | Bounded operator request and architecture metadata. | None by default. | Returns roles, route context, and approval conditions. |
| `POST /api/voice/chat` | Guarded voice-lane review contract. | Sanitized transcript/request only. | None by default. | Remains subject to the same provider and writeback gates. |
| `GET /api/config/roles` | Read public-safe role configuration. | None. | None. | Configuration inspection only. |

## Authorization and provider gate

An owner token is compared server-side when configured. A per-request acknowledgement may be recorded, but it is not replay protection or provider authorization by itself. Provider execution remains blocked until all server-side conditions are met, including:

1. allowed provider route and model allowlist;
2. owner authentication;
3. explicit per-request acknowledgement;
4. server-side secret handling;
5. bounded budgets; and
6. a durable nonce and spend ledger.

The current contract intentionally stops at the durable-control gate. Do not use it to spend provider budget or to claim completion.

## No writeback

Git, deployment, Notion, Nexus, WikiLLM, customer systems, and other external writeback are disabled in the public API contract. A code path or endpoint label is not authorization. Every future external action needs separate target/schema proof, an approved owner, rollback/recovery plan, and post-action verification.

## Error handling and operator response

- **Unavailable API:** preserve a browser-local review packet and provide it to an approved operator.
- **Unauthorized or unacknowledged:** do not retry with secrets in the browser; confirm the intended local/same-origin configuration.
- **Provider blocked:** record the reason and stop. Do not substitute a fabricated response.
- **Missing evidence:** return a question or gap rather than promote a conclusion.

See [operations](operations.md) and [security boundaries](security-and-data-boundaries.md) for the handoff rules.
