# Agentic Stack

## Layer Decision

Use this structure:

```text
Codex-authenticated operator prompt
  -> LangGraph path and state controller
  -> Loop Engineering run contract
  -> LlamaIndex bounded retrieval
  -> CrewAI named team tasks
  -> LangGraph review gate
  -> public-safe project outputs
```

## Tool Responsibilities

| Tool | Responsibility | Public Project Use |
|---|---|---|
| Codex | Operator runtime, editor, verifier, approval boundary. | Default interface for now. |
| LangGraph | Path control, state, conditional routing, review gates. | Full Block 1 workflow controller. |
| Loop Engineering | State, attempt caps, budget, maker/checker split, stop conditions. | L1 report-only loop contract under `project/loops/`. |
| CrewAI | Named roles and task execution. | AF Tools, AF Context, AF Research, AF Manager, AF Knowledge, AF Copy, AF Review, AF Publisher. |
| LlamaIndex | Bounded retrieval and RAG. | Search only approved public-safe project and sanitized history. |
| turbovec | Future local vector store under LlamaIndex. | Deferred until stable source IDs, embeddings, metadata, and benchmark exist. |
| WikiLLM | Canonical curated memory. | Source of truth for approved runs, decisions, memory, insights, and issues. |
| Cognee | Future operational recall and knowledge graph. | Deferred until E1.3 readback passes; never replaces WikiLLM. |
| Ollama | Local model serving. | Minor/background tasks only; active model is Qwythos and fallback is `gemma4:e4b`. |
| Mistral | Optional cloud quality pass. | Disabled until credentials, sanitized inputs, budget, model metadata logging, and AF Review approval exist. |
| LangSmith | Observability and trace review. | Configured for tracing only; waits for manual API key insertion. |

## Agent Hooks

| Hook | Use |
|---|---|
| AF Graph | Full controlled workflow. |
| AF RAG | Source-grounded retrieval over approved corpus. |
| AF Crew | Team-mode work split by role. |
| AF Research | E2 market evidence extraction, scoring, and ICP synthesis. |
| AF Copy | E3/E4/E6 positioning, content, and outreach drafts from approved evidence. |
| AF Review | Final public-safety and evidence gate. |

## Public Corpus Rules

Allowed by default:

- `project/`
- `history/`
- `skills/`
- `wiki/`

Not allowed by default:

- Raw private exports.
- Legacy root files.
- Private Notion pages.
- Local machine paths.
- Credentials.
- Private or scraped profile data.

## Loop And Parallelism Rules

- Default loop level is L1 report-only.
- `max_revision_loops` remains 2.
- Item-level retry cap is 3.
- A maker cannot approve its own high-risk output.
- Parallel work is allowed only for independent extraction tasks such as E2 website parsing, job-signal capture, review mining, and social-language mining.
- Synthesis, role verification, memory promotion, Notion updates, outreach, and payment verdicts remain sequential and reviewed.

## Model Routing

Current default:

- Codex is the operator/reviewer.
- Ollama/Qwythos is the bounded local minor/background model path.
- `gemma4:e4b` is fallback.
- Cloud model execution is disabled by default.

Future gated route:

- Mistral Small for sanitized batch normalization and draft variants.
- Mistral Medium for final strategy, PRD, ICP, proposal, or copy quality passes after facts are fixed.
- Mistral OCR only after a live model-name and privacy preflight.

## Proof Run Baseline

The first completed proof runs used sanitized internal source summaries, not raw transcripts.

Current public-safe proof folders:

- `project/runs/2026-06-26-june24-next-steps-proof/`
- `project/runs/E1.2/2026-06-26-full-test/`

Baseline proof outputs:

- context digest
- PRD
- task and responsibility matrix
- KB update note
- review report
- agent handout

## Current Workflow Configs

- `workflows/langgraph-controller.yaml`
- `workflows/crewai-crew.yaml`
- `workflows/llamaindex-rag.yaml`
- `workflows/market-research-engine.yaml`
- `loops/LOOP.md`
- `langsmith-setup.md`
- `../wiki/index.md`

## Output Documents

Templates are present under `outputs/templates/`.
Completed proof runs now live under `project/runs/` and provide the current public-safe reference for future E1.3 work.
