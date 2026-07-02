# Test Meeting PRD Runbook

Status: owner-approval gated

## Purpose

Run a controlled PRD/ICP test cycle using `docs/testmeeting.md` and the approved discovery-call source link only after the owner approves the test input boundary.

## Inputs

- Test meeting fixture: `docs/testmeeting.md`
- Public discovery-call source: `https://www.youtube.com/watch?v=k8K6wQLxooU`
- Discovery-call theory references reviewed for structure:
  - `https://www.youtube.com/watch?v=V0NZ_4GoLJM`
  - `https://www.youtube.com/watch?v=OTkP2JDeGWM`
- PRD structure reference: `https://freeprd.ai/`

## Gated Preconditions

- Owner approval for using the fixture.
- Source boundary review.
- No raw private transcript copied into public files.
- `MODEL_PROVIDER=none` unless a separate provider run is approved.
- OpenRouter daily cap remains `5.00` USD and run hard stop remains `1.99` USD.
- Provider ledger is required before any provider call.

## Steps

1. Confirm owner approval and source boundary.
2. Produce Meeting Summary, Product Context, Stakeholders, ICP, Pains/JTBD, Existing Workflow, Proposed Workflow, Requirements, Decisions, Questions, Risks, Next Tasks, Backlog, and Success Metrics.
3. Generate suggested Jira/GitLab backlog rows.
4. Generate missing-info questions.
5. Run AF Review for safety, source support, and runtime boundary.
6. Save a run note and handout only after checks pass.

## Stop Conditions

- Raw private source appears in output.
- Provider route is requested without backend, secret, ledger, budget, and approval.
- Telegram, Notion, GitHub, WikiLLM, or deployment writeback is requested without explicit approval.
