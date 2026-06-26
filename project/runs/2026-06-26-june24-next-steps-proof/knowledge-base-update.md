# Knowledge Base Update

## Memory Candidates

- E1.1 runtime spine is now validated by a pre-push guard: public safety, workflow YAML validation, LangGraph smoke, LlamaIndex approved-corpus retrieval, and CrewAI config check.
- CrewAI must run with project-local runtime storage and telemetry disabled during guard checks.
- E1.2 should begin only with sanitized source packets and derived public-safe outputs.
- The June 24 source supports the company workflow: meeting input to summary, PRD, task segmentation, KB update, and review.
- Market research, ICP, content testing, and website changes are downstream of the first proof workflow.

## Insight Candidates

- The builder/operator and market/content positions should be treated as complementary analysis lenses.
- The proof workflow should preserve disagreement and gaps instead of collapsing all meeting material into a confident roadmap.
- LangGraph should own routing and gates, while CrewAI owns role assignment.
- LlamaIndex should retrieve approved public context but should not become durable memory.

## Decision Candidates

- Keep public WikiLLM as canonical durable memory for the public project.
- Keep LlamaIndex as runtime retrieval over approved public files.
- Keep CrewAI as role/task configuration until the first approved LangGraph-wrapped CrewAI run.
- Keep Tavily and broader web research out of Block 1 runtime setup; use them in the research layer after E1.2 proof outputs exist.

## Issue Candidates

- Full vector retrieval is not generated yet.
- Speaker-specific attribution remains inferred, not proved.
- Obsidian/Nexus live mirror is not executed in this run.
- Market demand is not validated.

## Required Memory Writes

- Update `wiki/index.md` runtime layer statuses.
- Update `wiki/memory.md` with the runtime guard and E1.2 source boundary.
- Update `wiki/insights.md` with the proof-workflow sequencing insight.
- Append `wiki/log.md` with this run.
