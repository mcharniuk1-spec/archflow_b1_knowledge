# Decision: Live Dashboard Voice Hosting And Onyx Boundary

Date: 2026-06-30
Status: accepted planning baseline

## Decision

ArchFlow remains the workflow brain and canonical memory system. Onyx may be tested later as a read-only portal/search/connector layer over approved artifacts after readback and retrieval benchmarks exist.

The first implementation target is a hosted static dashboard. Vercel is preferred for that first stage because the current dashboard is static, generated, and read-only. Railway is reserved for live service needs such as API state, background workers, queues, websocket/SSE streams, and voice-service orchestration.

Voice starts local and read-only. Any write action, deployment, external connector change, outreach action, or memory promotion requires human approval and AF Review.

## Rationale

The current project risk is not lack of platform power. The risk is losing source boundaries, creating unreviewed memory, leaking credentials, or activating live writes before the workflow is proven.

The staged path keeps each layer accountable:

- Dashboard: visibility and status.
- LangGraph and Loop Engineering: control and stop conditions.
- WikiLLM: durable memory.
- Vercel: static hosted UI.
- Railway: live worker/API layer when needed.
- Onyx: later user-facing search/connector option.

## Consequences

- Do not replace LangGraph/WikiLLM with Onyx.
- Do not connect broad private sources into Onyx.
- Do not put real keys into GitHub.
- Do not activate unattended voice writes.
- Do not publish carousel reports without a public-safety review.

## Open Questions

1. Should the dashboard be public, hidden-link, or auth-gated?
2. What proof is required before the dashboard can display live run state?
3. Which voice commands are allowed in read-only mode?
4. Which provider owns live API state if Railway is introduced?
5. Which social report types are public-safe by default?
