# Architecture Metrics

Do not report improvement percentages until the same task set has run on both the baseline and candidate architecture.

## Evaluation groups

| Group | Metrics |
|---|---|
| Outcome quality | Acceptance pass rate, independent-review pass rate, defect severity, unsupported-claim count. |
| Execution reliability | Completion rate, retry count, loop convergence, blocked accuracy, recovery success, state-resume success. |
| Prompt/context | Input/output/cache tokens, context utilization, irrelevant-context ratio, compression loss, instruction-conflict count. |
| Retrieval | Recall@k, precision@k, MRR, nDCG, citation/provenance coverage, stale-result rate, lexical fallback success. |
| Memory | Promotion precision, duplicate/conflict rate, freshness, readback accuracy, orphan rate, provenance completeness. |
| Parallel work | Wall time, branch success, merge-conflict rate, duplicate work, coordination overhead, reviewer load. |
| Safety/governance | Boundary violations, blocked destructive fixtures, secret/path findings, unapproved side effects, false blocks. |
| Cost/performance | Wall time, provider/model cost, compute time, storage/index size, index build/update time, retrieval latency. |
| Human effort | Clarifications, approvals, repair minutes, manual reconciliations, handoff completeness. |

## Benchmark contract

Define the smallest fixture set that covers the architecture's claimed workload, then freeze it before comparing implementations. Include answer keys or expected states, source boundaries, stop conditions, and at least one adversarial safety case for each authority the system could exercise.

Run baseline and candidate with the same inputs, budgets, provider state, and reviewers. Report raw denominators with every percentage. Save traces only to a caller-supplied ignored local directory when they are public-safe; otherwise retain only sanitized aggregates and hashes.

An offline fixture may measure context bytes, role activation counts, source recall, deterministic gate behavior, provider-call count, and external-write count. It does not prove billed-token savings, runtime speed, memory quality, or production reliability unless those dimensions were directly observed.

## Graduation rules

- No critical safety regression.
- No reduction in provenance coverage.
- Statistically or operationally meaningful quality/reliability gain, or a clear cost/latency gain without quality loss.
- Rollback and fallback demonstrated.
- Known limitations and workload boundary recorded.
- Result validates against the declared schema or deterministic checker, with an action receipt only when an action actually ran.
