# Architecture Benchmark Contract

Status: defined, not yet executed.

## Claim rule

This run does not claim measured gains in quality, token use, cost, latency, memory, retrieval, or safety. The target architecture is a hypothesis until it is paired against the existing baseline with the same task set and budgets.

## Test set

- 20 approved-corpus retrieval questions with expected source paths.
- 12 role tasks across knowledge, PRD/ICP, engineering, content, finance, and media planning.
- 8 loop cases with recoverable defects and stop conditions.
- 6 safety fixtures for destructive commands, secrets/local paths, unauthorized writes, source-boundary failure, and self-approval.
- 4 parallel packages with independent Luna branches and one Terra integration step.
- 3 checkpoint resume/recovery cases.

## Required metrics

- acceptance and independent-review pass rates;
- retry, loop convergence, block accuracy, recovery, and state-resume results;
- input/output/cache tokens, context utilization, irrelevant-context ratio, and compression loss;
- Recall@k, Precision@k, MRR, nDCG, source coverage, stale results, and fallback success;
- memory promotion precision, duplicate/conflict rate, freshness, readback, orphans, and provenance;
- parallel wall time, duplicate work, merge conflicts, coordination overhead, and reviewer load;
- boundary violations, destructive fixture blocks, false blocks, secret/path findings, and side effects;
- wall time, provider cost, compute time, storage/index size, index update time, and retrieval latency;
- human clarifications, approvals, repair time, and handoff completeness.

## Controls

- Same inputs, source snapshot, role outputs, budgets, provider/model settings, and reviewers.
- Deterministic seed/config where supported.
- Raw traces retained only in the approved private layer; public output contains sanitized aggregates.
- Lexical retrieval remains the fallback.
- Any critical safety regression fails the candidate regardless of speed or token improvement.

## Candidate trials

Run separately so attribution remains possible:

1. Goal contract versus legacy task prompt.
2. CAG plus role-specific skills versus repeated full context.
3. Terra/Luna topology versus uncoordinated parallel writers.
4. Hybrid/vector retrieval versus lexical baseline.
5. Cognee versus current WikiLLM plus retrieval for operational recall.
6. TurboVec versus the selected baseline vector store.
7. Command guard plus platform approvals versus platform approvals alone.
8. CrewAI task team versus direct LangGraph worker functions.
