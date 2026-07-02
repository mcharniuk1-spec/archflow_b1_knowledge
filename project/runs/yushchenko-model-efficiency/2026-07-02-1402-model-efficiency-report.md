# Yushchenko Model Efficiency Report

Observer: Yushchenko Model Efficiency Observer

Run window: 2026-07-02 14:02 EEST

## Evidence Inspected

- `project/operating-rules.md`
- `project/live/communication/README.md`
- `project/live/communication/current-agent-notice.md`
- `project/live/communication/agent-communication-log.md`
- `project/config/model-routing.yaml`
- `project/reports/2026-07-01-openrouter-model-routing-plan.md`
- `project/agents/model-efficiency-advice.md`
- `project/agents/model-efficiency-issues.md`
- `project/runs/2026-07-01-openrouter-model-routing/agent-handout.md`
- `project/runs/2026-07-01-june30-transfer-provider-dashboard/run-summary.md`
- `project/runs/2026-07-01-infra-status-and-next-setup/agent-handout.md`
- `project/runs/2026-07-02-crewai-level-3-proof/agent-handout.md`
- `project/runs/2026-07-02-crewai-level-3-proof/review-report.md`
- `project/runs/2026-07-02-crewai-level-3-proof/runtime-proof.json`
- `project/runs/2026-07-02-crewai-level-3-proof/model-call-ledger.jsonl`
- `project/runs/yushchenko-model-efficiency/2026-07-02-1014-model-efficiency-report.md`
- `project/runs/yushchenko-model-efficiency/2026-07-02-1112-model-efficiency-report.md`
- `wiki/log.md`
- `wiki/memory.md`

## Models Used

FACT: No active OpenRouter runtime evidence was found in the public-safe evidence set.

FACT: A separate local deterministic proof ledger exists for CrewAI direct runtime verification.

Provider observed in model-use evidence: `local_deterministic`

Observed model IDs in the proof ledger:

- `archflow-deterministic-crewai-proof`
- `af_review_deterministic_local`

## Task And Purpose

Task: observe model efficiency and token-use evidence for the ArchFlow public project.

Purpose: separate actual runtime evidence from static routing plans, then report whether any active OpenRouter usage exists and whether the available evidence supports cost-efficient model use.

## Token And Cost Evidence

FACT: The local deterministic proof ledger records measured token fields and zero provider cost.

- `prompt_tokens`: 106
- `output_tokens`: 58
- `context_window_tokens`: 0
- `actual_or_estimated_cost`: 0.0 USD
- `budget_cap`: 1.99 USD
- `daily_budget_cap`: 5.0 USD

FACT: A second proof ledger entry records the reviewer-side deterministic call.

- `prompt_tokens`: 159
- `output_tokens`: 46
- `context_window_tokens`: 0
- `actual_or_estimated_cost`: 0.0 USD

GAP: No OpenRouter token, cost, or per-call runtime log was found in the public-safe project evidence.

## Outcome Quality

FACT: The direct CrewAI proof passed and wrote a public-safe model-call ledger.

FACT: The proof demonstrates local deterministic runtime mechanics, not OpenRouter activation.

INTERPRETATION: The evidence quality is good for proving a bounded local execution path, but it is still not a measurement of provider-backed efficiency.

HYPOTHESIS: Once a canonical provider-backed ledger exists, future observer runs will be able to compare local deterministic proof, cheap execution, and frontier review more cleanly.

## Efficiency Score

Efficiency score: `4`

Reason: deterministic evidence collection and the local proof ledger are efficient and useful, but OpenRouter runtime remains absent, so the observer still cannot measure provider-backed token spend.

## Waste Or Overuse Risks

- A local proof ledger can be mistaken for provider-backed OpenRouter usage if reports do not label it clearly.
- Frontier models can be overused for routine extraction, validation, or formatting if the routing contract is not enforced.
- Missing provider runtime logs can hide budget drift until a later activation pass.

## Missing Logging Fields

Missing for provider-backed OpenRouter runs:

- provider request ID
- provider latency
- provider model-list snapshot
- provider pricing source URL
- provider runtime source
- human gate status on each external call

Missing for the current public-safe evidence set:

- any actual OpenRouter invocation record
- any OpenRouter cost record
- any OpenRouter runtime trace

## Cheaper Substitute

Recommended cheaper substitute: keep using Codex file inspection, deterministic scripts, and local deterministic proof ledgers for routing review and validation until a provider-backed ledger exists.

## Frontier Escalation

Recommended frontier escalation: only for strategy, architecture, public claims, memory promotion, pricing, or payment verdicts after provider-backed evidence exists and the task truly needs a frontier reviewer.

## Next Actions

1. Keep reporting that no active OpenRouter runtime evidence is present until a real provider-backed call appears.
2. Treat the CrewAI proof ledger as separate local evidence, not as OpenRouter activation.
3. Add a canonical provider-backed model-call ledger before any future OpenRouter activation.
4. Keep Telegram delivery skipped unless an approved sender becomes available outside the public repo.

## Telegram Delivery

Telegram send skipped - approved sender unavailable.
