# Future Actions And Parameters

This file lists the next implementation choices and the parameters that should be reviewed before changing the setup.

## Immediate Actions

1. Keep the public project synchronized with GitHub.
   - Current verified route: Codex-operated Git SSH push.
   - Alternative: configure local GitHub CLI auth, then push over HTTPS.
   - Do not store tokens in this repository.

2. Repair or replace Qwythos.
   - Option A: re-pull the configured Qwythos model.
   - Option B: keep Qwythos as intended model and use `gemma4:e4b` until repaired.
   - Option C: replace Qwythos with a smaller supported local model.
   - Current optimal: keep Codex as main and use `gemma4:e4b` only for minor/background local tasks.

3. Run the first proof workflow.
   - Input: sanitized dialogue or project context summary.
   - Output: fill all templates in `project/outputs/templates/`.
   - Review: AF Review must approve before anything is published.

4. Expand the installed runtime packages into the first full proof workflow.
   - LangGraph: expand the smoke graph into the E1.2 proof graph.
   - CrewAI: keep config/import proof complete; run LLM tasks only inside the approved graph path.
   - LlamaIndex: keep approved-corpus retrieval source-path grounded.

5. Activate LangSmith tracing after manual API key insertion.
   - Add the key only to `project/.env.langsmith.local`.
   - Run a sanitized proof workflow.
   - Confirm the trace appears in the `ArchFlow` project.
   - Do not send raw private material to LangSmith.

## Provider Options

| Provider | Best Use | Current Status | Approval Needed |
|---|---|---|---|
| Codex operator auth | Main execution, review, edits, and supervised publication. | Active. | No new approval for normal project work. |
| Ollama local | Minor/background local tasks. | Started; Qwythos works; fallback remains. | Approval needed for new model install. |
| OpenAI API | Direct framework calls from LangGraph, CrewAI, or LlamaIndex. | Not configured. | Explicit API key setup approval required. |
| LangSmith | Tracing and debugging LangGraph runs. | Configured; sanitized traces submitted. | No new approval for sanitized traces. |

## LangGraph Parameters To Review

| Parameter | Current Value | Why It Matters |
|---|---|---|
| checkpointer | none_for_now | Add persistence only when graph runs need resume/retry. |
| max_revision_loops | 2 | Prevents infinite revise loops. |
| human_approval_required_before_publication | true | Keeps public release gated. |
| state fields | defined in workflow YAML | Makes every handoff explicit. |
| review gate | required | Blocks unsafe or unsupported outputs. |
| LangSmith project ID | 057edf33-a328-4186-9425-3306186149ef | Routes traces to the selected project after API key insertion. |

## CrewAI Parameters To Review

| Parameter | Current Value | Options |
|---|---|---|
| process | sequential | hierarchical later if a manager agent is needed. |
| memory | false | enable only after public/private memory boundaries are tested. |
| cache | true | disable if cached tool output creates stale conclusions. |
| planning | false | enable when tasks become larger or less deterministic. |
| output_log_file | project/outputs/crew-log.json | keep logs public-safe or write only sanitized summaries. |
| max_rpm | null | set if a cloud LLM/API is added. |

## LlamaIndex Parameters To Review

| Parameter | Current Value | Options |
|---|---|---|
| approved corpus | project, history, skills | add docs only after public-safety review. |
| chunk_size | 800 | tune smaller for precise source citation, larger for narrative docs. |
| chunk_overlap | 120 | tune if answers lose context across chunks. |
| similarity_top_k | 5 | raise for research, lower for focused answering. |
| persist_dir | project/local/rag_index | ignored by Git; do not publish vector stores by default. |
| require_source_paths | true | keeps answers auditable. |

## UI Options

| UI | Ease | Fit For This Project |
|---|---|---|
| Codex chat/operator | easiest | Current optimal setup for strategy, edits, review, and publication. |
| CLI scripts | moderate | Good for repeatable local checks and RAG builds. |
| Streamlit local UI | moderate | Good future choice for manual upload, prompt, and output review. |
| Web app dashboard | highest effort | Useful after the workflow is proven and needs non-technical users. |

## Done Criteria For Next Implementation Step

- `.env.local` remains ignored.
- No public file contains secrets, private links, or local paths.
- First proof run produces the full output set.
- Review report explicitly approves or blocks publication.
- WikiLLM run log is updated under `wiki/runs/`.
