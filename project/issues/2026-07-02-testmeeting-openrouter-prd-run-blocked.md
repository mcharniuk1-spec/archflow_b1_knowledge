# Testmeeting OpenRouter Comparison Resolved

Date: 2026-07-02
Status: resolved on 2026-07-03; OpenRouter comparison completed and review-gated

## Original Issue

The E1.2.8 local/Codex PRD/PDF package was complete, but the separate OpenRouter comparison was originally blocked by network/provider-approval constraints.

## Resolution

The OpenRouter comparison was rerun on 2026-07-03 using only the sanitized digest. The active route is `yushchenko.source_scope_gate`; the selected execution model is `qwen/qwen3.6-plus`, with `qwen/qwen3-235b-a22b` as fallback. The comparison wrote a model ledger, budget guard, status file, Markdown output, and PDF output. It remains review-gated until AF Review and owner acceptance.

## FACT

- The approved private meeting source was used locally.
- The approved private discovery-method source was used locally.
- Public repo outputs store only sanitized English summaries and derived artifacts.
- Local/Codex artifacts were written under `project/runs/E1.2/2026-07-02-testmeeting-local/`.
- Local PDFs were copied to `project/reports/`.
- The completed OpenRouter run used only the sanitized digest.
- Provider calls: 1.
- Provider spend: about `0.00794` USD.
- Raw private source sent: false.

## INTERPRETATION

The correct current state is split: E1.2.8 is review-ready for the local/Codex PRD package and has a completed OpenRouter comparison, but both remain review-gated until AF Review and owner acceptance. The issue is no longer an OpenRouter execution block.

## Required Follow-up

1. Review the local PRD/PDF package.
2. Review the OpenRouter comparison output and ledger.
3. Decide whether E1.2.8 can move from Review after AF Review and owner acceptance.
4. Keep Railway runtime, durable writeback, and production automation in the E1.7 lane.

## Related Artifacts

- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_Local_PRD.md`
- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_Local_PRD.pdf`
- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_OpenRouter_Comparison.md`
- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_OpenRouter_Comparison.pdf`
- `project/runs/E1.2/2026-07-02-testmeeting-local/openrouter-model-call-ledger.jsonl`
- `project/runs/E1.2/2026-07-02-testmeeting-local/openrouter-budget-guard.json`
