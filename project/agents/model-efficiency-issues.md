# Model Efficiency Issues

Purpose: open issues the Yushchenko Model Efficiency Observer and other agents should track until resolved.

## Open Issues

### MEI-1 - No Canonical Model-Call Ledger Yet

Status: open

FACT: The model-routing plan defines required fields, but the project does not yet have a canonical ledger file or database for model calls.
FACT: The 2026-07-01 observer run still found no active OpenRouter runtime evidence in public-safe project files.

Impact: Observer reports can only summarize available run notes and logs. Token/cost efficiency will be incomplete until model calls are logged consistently.

Needed action: create a public-safe model-call ledger schema before activating OpenRouter.

### MEI-7 - Local Proof Ledger Must Stay Separate From Provider Ledger

Status: open

FACT: The CrewAI direct runtime proof now writes a zero-cost local deterministic ledger.
FACT: That proof ledger is useful evidence, but it is not a provider-backed OpenRouter ledger.

Impact: Observer reports can overstate provider readiness if they do not label local proof runs separately from provider-backed runs.

Needed action: keep a distinct schema and reporting label for local deterministic proof ledgers and provider-backed OpenRouter ledgers.

### MEI-2 - Telegram Sender Not Proven

Status: open

FACT: The recurring automation is active, but no Telegram connector or approved sender was exposed in this session.

Impact: Reports can be saved locally, but Telegram delivery may be skipped until a sender exists.

Needed action: configure an approved Telegram sender outside the public repo and keep chat IDs, URLs, and tokens out of public files.

### MEI-3 - OpenRouter Runtime Disabled

Status: open

FACT: OpenRouter is intentionally disabled until explicit approval and a backend or local bridge exists.

Impact: Reports should say "no active OpenRouter runtime" until real usage evidence exists.

Needed action: do not activate provider calls without approval, server-side secret handling, budget caps, and logging.

### MEI-4 - Model IDs And Pricing Can Drift

Status: open

FACT: Exact OpenRouter model IDs and prices can change.

Impact: Static model recommendations may become stale.

Needed action: refresh the OpenRouter model list before any activation or cost recommendation.

### MEI-5 - Frontier Overuse Risk

Status: open

FACT: The plan intentionally uses Claude, Gemini, and OpenAI frontier models for strategy and review, but routine tasks should stay cheap.

Impact: Agents may waste budget if they use frontier models for formatting, extraction, or first drafts.

Needed action: require escalation thresholds and record why a frontier model was used.

### MEI-6 - No Runtime Context Window Telemetry

Status: open

FACT: No public-safe local logs or model usage reports currently record context-window sizes, prompt token counts, or provider endpoint runtime overhead.

Impact: Efficiency attribution cannot separate routing/benchmark changes from actual model quality or strategy quality in current runs.

Needed action: add `context_window_tokens`, `prompt_tokens`, `output_tokens`, and provider/runtime source to the model-call ledger when runtime is activated.
