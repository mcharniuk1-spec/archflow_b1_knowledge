# Performance Evidence

Status: provider-disabled V3 fixtures
Source: `project/benchmarks/actionable-agents-v3-results.json`

The benchmark measures four narrow properties of the current generic public tool. It does not measure customer ROI, production answer quality, wall-clock speed, labor savings, durable-memory deletion, billed tokens, or live-provider cost.

## Results

| Measure | Result | Numerator / denominator | Comparator | Limitation |
|---|---:|---:|---|---|
| Context input reduction | 98.6% | 1,040,631 / 1,055,632 UTF-8 bytes avoided | Top-five lexical chunks versus a full 55-file manifest packet for each of four tasks | Input bytes only; not model-exact/billed tokens, latency, answer quality, or memory size |
| Role activation reduction | 75.0% | 63 / 84 role slots avoided | Smallest declared pack versus all 21 roles on each of four tasks | Contract selection, not compute, labor, speed, or throughput |
| Expected source hit at five | 4 / 4 | 4 / 4 fixed queries | Expected canonical source present in deterministic lexical top five | Source-hit fixture, not general retrieval or semantic answer accuracy |
| Expected semantic gate decision | 8 / 8 | 8 / 8 fixed packets | One valid and seven unsafe/incomplete packets | Bounded abuse fixture, not a universal safety rate |
| Provider calls | 0 | 0 observed | Entire V3 benchmark | Does not measure a provider-enabled path |
| External writes | 0 | 0 observed | Entire V3 benchmark | Local result-file creation is the benchmark artifact, not an external write |

## Context Comparator

For each fixed query, the baseline carries the full exact manifest. The candidate carries the five lexical chunks returned by the provider-disabled retrieval function. The comparator is deliberately naive and must never be described as a previous release, best alternative, model context window, or realistic production RAG baseline.

Formula:

```text
reduction = (full_manifest_bytes - selected_chunk_bytes) / full_manifest_bytes
```

The measurement uses exact UTF-8 bytes. No byte-to-token proxy is published in V3.

## Role Comparator

The baseline activates all 21 declared role slots for each task. The candidate activates the exact role IDs in four predefined role packs. The reduction measures contract narrowing only.

Formula:

```text
reduction = (all_role_slots - selected_role_slots) / all_role_slots
```

## Retrieval Fixtures

The four queries target:

1. source-boundary and no-source/no-evidence rules;
2. the canonical run envelope and recovery fields;
3. the smallest-responsible role-pack contract;
4. provider-registry truth states and browser boundary.

The expected source must appear in the deterministic lexical top five. The test does not synthesize an answer.

## Semantic Fixtures

The gate accepts one complete public-safe packet and rejects packets with:

- no objective;
- no requested output;
- an email address in the reference;
- an assigned credential-like value;
- no reviewer;
- maker and reviewer collapsed into one role;
- an external action without exact approval.

The fixtures are transparent and finite. Unknown attacks and real operational errors remain outside the denominator.

## Reproduce

```bash
python3 project/scripts/benchmark-actionable-agents.py
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
```

Any change to the manifest, roles, packs, fixtures, chunking, or retrieval logic requires a rerun. The publication visual and LinkedIn copy must match the exact committed result hash.

## Safe Wording

Safe:

> On four fixed provider-disabled public tasks, ArchFlow carried 98.6% fewer UTF-8 input bytes than a deliberately naive full-manifest packet, selected 75.0% fewer role slots than all-role fan-out, found the expected source in 4/4 lexical top-five checks, and matched 8/8 semantic gate decisions. No provider was called and no external system was written.

Do not claim:

- memory saved;
- billed or model-exact tokens saved;
- faster delivery or lower labor;
- production accuracy or safety;
- customer ROI;
- provider spend efficiency;
- universal performance.
