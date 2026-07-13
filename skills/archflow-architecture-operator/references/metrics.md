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

## Minimum benchmark

- 20 approved-corpus retrieval questions with answer keys and source paths.
- 12 role tasks across knowledge, PRD/ICP, engineering, content, finance, and media planning.
- 8 loop tasks containing recoverable defects and explicit stop conditions.
- 6 safety fixtures covering destructive commands, secret/path leakage, unauthorized external write, and source-boundary failure.
- 4 parallel work packages with independent branches and a controlled integration step.
- 3 resume/recovery cases from saved state.

Run baseline and candidate with the same inputs, budgets, provider settings, and reviewers. Store raw traces privately when required and only publish sanitized aggregates.

## Graduation rules

- No critical safety regression.
- No reduction in provenance coverage.
- Statistically or operationally meaningful quality/reliability gain, or a clear cost/latency gain without quality loss.
- Rollback and fallback demonstrated.
- Known limitations and workload boundary recorded.
