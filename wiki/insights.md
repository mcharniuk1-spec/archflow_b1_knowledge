# Insights

## Public System Design

The safest current architecture separates three concerns:

- Codex supervises work and publication.
- Ollama runs local models.
- LangSmith observes traces after public-safety filtering.

This avoids mixing operator authentication, model credentials, and observability credentials.

## Block 1 Execution Insight

The project should prove one internal workflow before adding customer-facing claims:

1. Take a sanitized source summary.
2. Produce context digest.
3. Produce PRD.
4. Produce responsibility matrix.
5. Produce KB update.
6. Produce review report.
7. Publish only approved public-safe outputs.

## LangSmith Insight

LangSmith should receive structured run metadata and trace spans, not raw private material. The first useful trace should be a synthetic or sanitized proof run, not an unfiltered private transcript.

## Implementation Sequencing Insight

The lowest-risk order is: verify LangSmith trace with a sanitized run, install LangGraph runtime, add LlamaIndex retrieval, then add CrewAI execution. This keeps workflow control and public-safety gates stable before adding team automation.

## E1.2 Proof Insight

The first full proof should not start as a market research task. It should start as a controlled source-to-artifact workflow: source inventory, context digest, sole summary, PRD, responsibility matrix, KB update, retrieval log, and review report. Market and web research become useful after this proof defines explicit questions.

## CrewAI Boundary Insight

CrewAI imports can create app-data storage by default. In this project, CrewAI guard checks must override runtime storage to ignored project-local storage and disable telemetry/tracking. CrewAI should organize roles while LangGraph controls routing, revision loops, and approval gates.

## Dashboard Sequencing Insight

The dashboard should lag the proof workflow, not lead it. A read-only readiness dashboard is useful now because it exposes config health and memory activity without freezing early assumptions. A full control panel should wait until LangGraph, LlamaIndex, CrewAI, WikiLLM writes, and LangSmith traces have produced at least one complete proof run.

## E1.2 Streaming Insight

For public operational reports, streaming should mean observable graph state and progress: node names, state deltas, artifact paths, tool results, warnings, and review decisions. It should not mean saving hidden reasoning text. This keeps debugging useful without weakening the public-safety boundary.

## E1.2 Agent Configuration Insight

The first production-like agent setup should keep AF Tools, AF Review, and AF Publisher deterministic; allow only modest variance for AF Context, AF Manager, AF Knowledge, and technical trend analysis; and keep CrewAI LLM task execution behind LangGraph until one artifact-generating run passes review.

## E1.2 To E1.3 Handoff Insight

The correct transition gate is owner acceptance plus KB readback, not more artifact generation. E1.3 should prove that the approved PRD and agent history can be written into public-safe memory and retrieved by a future agent before Obsidian mirror expansion, Nexus live writes, or broader research layers are activated.

## Loop And Memory Architecture Insight

Loop Engineering should wrap the current LangGraph/CrewAI/LlamaIndex stack rather than replace it. The reliable pattern is state plus stop conditions: source boundary, attempt caps, maker/checker separation, budget, run log, review, handout, and memory promotion. WikiLLM remains the truth layer; Cognee and turbovec are useful only when they are fed approved artifacts and can be rebuilt or reset.

## Market Engine Insight

The first sellable market wedge is not generic AI productivity or "make a PRD." It is reducing ambiguity, PM/BA cleanup time, rework, weak handoffs, scope creep, and lost decision memory for service companies that repeatedly convert client/customer conversations into buildable work. E2 should therefore produce account-level evidence cards and ICP scores before content or outreach claims.

## Demand Validation Insight

Validated demand requires buyer risk: paid diagnostic, prepayment, approved paid start, source packet plus timeline/scope, budget-owner referral, or proposal request. Attention, compliments, category counts, social interest, and internal proof do not validate demand.
