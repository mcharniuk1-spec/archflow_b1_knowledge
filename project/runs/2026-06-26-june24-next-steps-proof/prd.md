# Product Requirements Document

## Product

ArchFlow Block 1 Dialogue-to-PRD Knowledge Engine.

## Problem

Strategic conversations contain useful product, market, and execution decisions, but they are messy, multi-topic, and difficult for agents or developers to act on reliably. The project needs a repeatable process that converts private meeting inputs into public-safe execution artifacts without leaking sensitive context.

## Goal

Create the first repeatable proof workflow that transforms one approved internal meeting source into a structured summary, PRD, agent task plan, knowledge-base update, and review report.

## Non-Goals

- Do not ingest broad private workspaces.
- Do not copy raw transcripts into public files.
- Do not build the full dashboard as the primary brain.
- Do not claim customer demand before validation.
- Do not switch to another agent runtime before the first LangGraph/LlamaIndex/CrewAI proof works.

## Users

| User Type | Need |
|---|---|
| Founder/operator | Convert strategy discussions into reliable execution tasks. |
| Product builder | Get PRDs, acceptance criteria, and implementation sequence from messy context. |
| Research operator | Identify market questions and later research tasks without mixing them into setup. |
| Agent reviewer | Approve, revise, or block outputs based on evidence and safety. |

## Functional Requirements

1. Accept a sanitized source packet.
2. Validate source boundary and approved corpus.
3. Retrieve relevant public project context through LlamaIndex.
4. Run parallel topic analysis before synthesis.
5. Produce a single summary document.
6. Produce a PRD with goals, scope, non-goals, requirements, and acceptance criteria.
7. Produce agent-segmented tasks.
8. Produce a knowledge-base update packet.
9. Run a review gate that can approve, revise, or block.
10. Save public-safe outputs into the project run folder.

## LangGraph State

| Field | Purpose |
|---|---|
| `run_id` | Stable execution identifier. |
| `source_packet_id` | Sanitized source reference. |
| `source_boundary_status` | `pass` or `fail`. |
| `retrieved_context` | Source-path grounded public context. |
| `parallel_findings` | Topic analysis outputs. |
| `context_digest_path` | Path to the digest. |
| `summary_path` | Path to the sole summary document. |
| `prd_path` | Path to the PRD. |
| `task_matrix_path` | Path to the responsibility matrix. |
| `kb_update_path` | Path to the knowledge-base update. |
| `review_report_path` | Path to the review output. |
| `approval_status` | `approved`, `revise`, or `blocked`. |
| `gaps` | Open issues or missing evidence. |

## LangGraph Nodes

| Node | Owner | Function |
|---|---|---|
| `intake_validate` | AF Tools | Validate source packet, language, public boundary, and requested outputs. |
| `retrieve_context` | AF Context | Query LlamaIndex over approved public files and return source paths. |
| `analyze_strategy` | AF Context | Extract direction, decisions, and sequencing. |
| `analyze_product` | AF Manager | Extract product requirements and proof workflow. |
| `analyze_market` | AF Research | Extract ICP, demand, positioning, and research questions. |
| `analyze_content` | AF Research | Extract content and website implications. |
| `analyze_operations` | AF Tools | Extract runtime, dashboard, and tooling implications. |
| `merge_context` | AF Manager | Merge parallel outputs into one structured digest. |
| `write_summary` | AF Context | Produce the sole public-safe summary document. |
| `draft_prd` | AF Manager | Produce requirements, acceptance criteria, and scope. |
| `task_segmentation` | AF Manager | Split work by agent and execution segment. |
| `write_kb_update` | AF Knowledge | Produce durable memory and decision candidates. |
| `review_gate` | AF Review | Approve, request revision, or block. |
| `publish_or_revise` | AF Publisher | Prepare public-safe output or route back for repair. |

## Acceptance Criteria

- LangGraph smoke path passes with approved status.
- LlamaIndex approved-corpus retrieval returns source paths.
- CrewAI config imports and validates without LLM execution.
- Public safety scan passes.
- Pre-push runtime guard passes.
- Run folder contains source inventory, digest, summary, PRD, task matrix, KB update, retrieval log, and review report.
- Raw private source material is absent from public files.

## Next Execution

E1.2 starts as the first full proof run. It should use the node sequence above and later expand the current smoke graph into parallel topic analysis and document generation.
