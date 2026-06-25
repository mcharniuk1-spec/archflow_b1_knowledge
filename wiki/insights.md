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

