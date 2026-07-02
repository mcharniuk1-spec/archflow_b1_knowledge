# Test Meeting PRD Runbook

Status: owner-approval gated

## Purpose

Run a controlled PRD/ICP test cycle using the private root `docs/testmeeting.md` and the private root `discovery materials.docx` methodology packet. Public repo outputs may store only sanitized English summaries and derived artifacts.

## Inputs

- Private test meeting fixture: root `docs/testmeeting.md`
- Private discovery methodology packet: root `discovery materials.docx`
- PRD structure reference: `docs/prd-icp-output-template.md`
- Dashboard operating reference: `docs/dashboard-operating-manual.md`

## Gated Preconditions

- Owner approval for using the private fixture locally.
- Source boundary review.
- No raw private transcript copied into public files.
- `MODEL_PROVIDER=none` unless a separate provider run is approved.
- OpenRouter daily cap remains `5.00` USD and run hard stop remains `1.99` USD.
- Provider ledger is required before any provider call.
- External provider comparison requires explicit owner approval after data-exfiltration risk review.

## Steps

1. Confirm owner approval and source boundary.
2. Run `project/scripts/e1_2_8_testmeeting_run.py` for the local/Codex package.
3. Produce Meeting Summary, Product Context, Stakeholders, ICP, Pains/JTBD, Existing Workflow, Proposed Workflow, Requirements, Decisions, Questions, Risks, Next Tasks, Backlog, and Success Metrics.
4. Generate suggested Jira/GitLab backlog rows.
5. Generate missing-info questions.
6. Run AF Review for safety, source support, and runtime boundary.
7. Save a run note and handout only after checks pass.
8. Run OpenRouter only if the owner explicitly approves the external comparison after risk review; use only the sanitized digest.

## Stop Conditions

- Raw private source appears in output.
- Provider route is requested without backend, secret, ledger, budget, and approval.
- External provider call is rejected by the approval reviewer.
- Telegram, Notion, GitHub, WikiLLM, or deployment writeback is requested without explicit approval.
