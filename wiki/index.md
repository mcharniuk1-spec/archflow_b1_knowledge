# ArchFlow Public WikiLLM

This is the public WikiLLM layer for the ArchFlow Block 1 knowledge project.

It stores durable public-safe project memory, decisions, run records, issues, insights, and operating rules.

## Read Order

1. `../README.md`
2. `../AGENTS.md`
3. `../project/README.md`
4. `../project/operating-rules.md`
5. `../project/config/model-routing.yaml`
6. `memory.md`
7. `insights.md`
8. `rules/public-wikillm-contract.md`
9. latest file in `runs/`
10. open files in `issues/`
11. latest files in `decisions/`

## Project Identity

| Field | Value |
|---|---|
| Project | ArchFlow Block 1 Knowledge |
| Public repository | `mcharniuk1-spec/archflow_b1_knowledge` |
| Active work folder | `project/` |
| Public history folder | `history/` |
| Skill registry | `skills/` |
| WikiLLM folder | `wiki/` |

## Active Layers

| Layer | Status |
|---|---|
| Public repository | Published. |
| Codex operator | Primary operator and review layer. |
| Ollama | Local model execution only. |
| Qwythos | Active local model after load verification. |
| LangSmith | Tracing configured; sanitized smoke traces submitted. |
| LangGraph | Runtime installed; smoke workflow passed. |
| CrewAI | Runtime installed; config/import check passed with no LLM execution. |
| LlamaIndex | Runtime installed; approved-corpus retrieval proof passed. |
| WikiLLM | Public project memory configured in this folder. |

## Safety Boundary

This wiki must not contain:

- API keys, tokens, cookies, passwords, or raw credentials.
- Private workspace links.
- Local absolute paths.
- Raw private transcripts or exports.
- Personal identifiers not needed for public project operation.
