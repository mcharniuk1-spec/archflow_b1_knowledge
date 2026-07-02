# Testmeeting OpenRouter Comparison Blocked

Date: 2026-07-02
Status: local run complete; OpenRouter comparison blocked

## Issue

The E1.2.8 local/Codex `testmeeting.md` PRD/PDF package is complete. The separate OpenRouter comparison remains blocked.

## FACT

- The private root `docs/testmeeting.md` input exists and was used locally.
- The private root `discovery materials.docx` input exists and was used as methodology context.
- Public repo outputs store only sanitized English summaries and derived artifacts.
- Local/Codex artifacts were written under `project/runs/E1.2/2026-07-02-testmeeting-local/`.
- Local PDFs were copied to `project/reports/`.
- The OpenRouter run was attempted only on the sanitized digest.
- The first provider attempt hit sandbox DNS/network blocking.
- The escalation reviewer rejected the external provider call as data-exfiltration risk for derived content from private local source materials.
- No workaround was attempted.
- Provider calls: 0.
- Provider spend: 0.00 USD.

## INTERPRETATION

The correct current state is split: E1.2.8 is review-ready for the local/Codex PRD package, but blocked for the OpenRouter comparison. The OpenRouter block is not a missing-fixture issue anymore; it is an external-provider approval and data-boundary issue.

## Required Resolution

1. Review the local PRD/PDF package.
2. Decide whether E1.2.8 can be accepted as local/Codex-only for now.
3. If an OpenRouter comparison is still required, the owner must explicitly approve the external provider call after reviewing the data-exfiltration risk.
4. If approved later, send only the sanitized digest, then write model ledger, budget guard, comparison report, and AF Review.

## Related Artifacts

- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_Local_PRD.md`
- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_Local_PRD.pdf`
- `project/runs/E1.2/2026-07-02-testmeeting-local/E1.2.8_OpenRouter_blocked.md`
- `project/runs/E1.2/2026-07-02-testmeeting-local/model-call-ledger.jsonl`
- `project/runs/E1.2/2026-07-02-testmeeting-local/budget-guard.json`
