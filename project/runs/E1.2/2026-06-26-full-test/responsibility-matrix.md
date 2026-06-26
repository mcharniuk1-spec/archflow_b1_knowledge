# Responsibility Matrix

Date: 2026-06-26
Run: E1.2 full public-safe proof test

| Task | Owner | Support | Output | Gate |
|---|---|---|---|---|
| E1.2.1 Source inventory | AF Tools | AF Review | `source-inventory.md` | No raw private source in public files. |
| E1.2.2 Retrieval log | AF Context | AF Tools | `retrieval-log.md` | Source paths present; corpus boundary matches config. |
| E1.2.3 Context digest | AF Context | AF Knowledge | `context-digest.md` | FACT/INTERPRETATION/HYPOTHESIS/GAP used. |
| E1.2.4 Full-test graph | LangGraph controller | AF Runtime Debug | `e1_2_langgraph_output.json`, `e1_2_stream_events.jsonl` | Approved status required. |
| E1.2.5 PRD | AF Manager | AF Architecture Review | `E1.2_PRD.md`, `E1.2_PRD.pdf` | Scope, non-goals, and acceptance criteria clear. |
| E1.2.6 Streaming report | AF Tools | AF Review | `E1.2_Streaming_report.md`, `E1.2_Streaming_report.pdf` | Observable stream only; no hidden reasoning. |
| E1.2.7 System report | AF Architecture Review | Technical Tendencies Analyst | `E1.2_System_report.md`, `E1.2_System_report.pdf` | Roles, models, temperatures, layers, KB, Graphify, Nexus reviewed. |
| E1.2.8 KB update | AF Knowledge | AF Manager | `kb-update.md`, WikiLLM run note | Durable facts only. |
| E1.2.9 Review | AF Review | AF Tools | `review-report.md` | Scans and runtime guard pass. |
| E1.2.10 Publish | AF Publisher | Codex operator | commit and push | Push only after validated change list. |

## Parallel Work Blocks

| Parallel Block | Branches | Merge Point |
|---|---|---|
| Expert analysis | architecture, runtime, knowledge, agents, trends | `merge_findings` |
| Report creation | PRD, streaming report, system report | AF Review |
| Validation | safety scan, runtime guard, PDF text extraction, dashboard regeneration | AF Publisher |

## Consequent Work Blocks

1. Source boundary before retrieval.
2. Retrieval before synthesis.
3. Parallel analysis before report pack.
4. Reports before review.
5. Review before commit.
6. Commit before push.
