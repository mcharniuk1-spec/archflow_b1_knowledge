# E5.3 Inbound Qualification Scoring Packet

Date: 2026-07-06
Status: prepared for review
Scope: no-code qualification rules for ArchFlow inbound signals

## Purpose

This packet defines how ArchFlow should classify inbound signals before any lead
is treated as demand evidence. It extends the E5.2 funnel and diagnostic event
schema without installing analytics, collecting real leads, writing to external
systems, or claiming validated demand.

## Qualification Principle

Inbound interest becomes useful only when it shows buyer-risk evidence or a
concrete workflow problem. Attention alone stays separate from demand.

FACT:
- The project plan defines validated demand as a paid diagnostic, prepayment,
  approved paid start, or firm paid intent with source packet, timeline, scope,
  and budget-owner path.
- The E5.2 packet separates visitor, engagement, diagnostic starter, qualified
  lead, conversation, paid-intent lead, and verdict input.

INTERPRETATION:
- E5.3 should decide whether a signal deserves owner review, follow-up,
  exclusion, or E7 tracking.

HYPOTHESIS:
- The strongest early lead quality signal is source-packet willingness paired
  with a first-ICP role or team fit and a concrete PRD, rework, handoff, or
  decision-memory pain.

GAP:
- No real leads, diagnostics, conversations, paid starts, or payment verdicts
  are captured in this run.

## Score Model

| Dimension | Score | Rule |
|---|---:|---|
| First ICP fit | 0-20 | Product leadership or senior PM/product-ops role inside B2B SaaS scaleup context gets the highest score. Adjacent lanes stay lower. |
| Trigger clarity | 0-20 | Concrete workflow pain beats generic AI interest. Examples: PRD rework, customer research overload, handoff loss, decision-memory gap, PM team growth. |
| Source-packet willingness | 0-20 | Willingness to share redacted source material or workflow context is a strong buyer-risk signal. |
| Buyer-risk signal | 0-25 | Paid diagnostic interest, proposal request, budget-owner path, or approved paid start are strongest. |
| Privacy and source-boundary clarity | 0-10 | Clear redaction/security constraints improve qualification because the delivery path is knowable. |
| Timing and next-action clarity | 0-5 | A concrete next step or near-term trigger raises priority. |

Maximum score: `100`.

## Qualification Bands

| Band | Score | Status | Action |
|---|---:|---|---|
| Strong qualified | 75-100 | `qualified` | Prepare owner-reviewed follow-up and route to E6/E7 tracking if buyer-risk evidence exists. |
| Review needed | 55-74 | `needs_review` | Ask one clarifying question or prepare diagnostic-call review. |
| Monitor | 35-54 | `monitor` | Keep as attention or learning evidence; do not claim demand. |
| Not fit | 0-34 | `not_fit` or `disqualified` | Exclude from outreach unless owner overrides with a specific reason. |

## Disqualification Rules

- The signal is only a like, view, follow, generic compliment, or vague interest.
- The lead is outside the first ICP and has no warm proof opportunity.
- The person asks for generic AI automation unrelated to PRD, discovery,
  handoff, KB, or product-team workflow.
- The source boundary cannot be made safe enough for a diagnostic.
- The lead asks for unsupported outcomes such as guaranteed ROI, production
  claims, or unapproved provider/runtime behavior.

## Minimal Qualification Record

| Field | Type | Rule |
|---|---|---|
| lead_id | generated string | Use a non-identifying internal ID in public artifacts. |
| qualification_score | integer | 0-100 using the scoring model above. |
| qualification_band | enum | `strong_qualified`, `needs_review`, `monitor`, `not_fit`. |
| segment_fit_reason | string | Public-safe summary of why the lead matches or does not match the first ICP. |
| pain_signal | enum | `prd_rework`, `research_overload`, `handoff_loss`, `decision_memory_gap`, `pm_team_growth`, `generic_interest`, `unknown`. |
| buyer_risk_signal | enum | `none`, `source_packet`, `paid_diagnostic`, `proposal_request`, `budget_owner`, `paid_start`. |
| next_action | enum | `owner_review`, `ask_clarifying_question`, `diagnostic_call`, `proposal`, `monitor`, `exclude`. |
| evidence_label | enum | `FACT`, `INTERPRETATION`, `HYPOTHESIS`, `GAP`. |

## Example Classification Logic

| Signal pattern | Score band | Classification |
|---|---|---|
| Product leader asks about turning customer calls into a reviewed PRD and is willing to share redacted source material. | Strong qualified | Route to owner-reviewed diagnostic follow-up. |
| Senior PM likes a proof post and asks a general question about AI tools. | Monitor | Record as attention unless a workflow pain appears. |
| Founder outside the ICP asks for broad automation help without source or budget context. | Not fit | Exclude from first ICP lane; optionally store as later-lane learning. |
| Product ops lead asks about privacy constraints and existing-tool handoff for discovery notes. | Review needed | Ask clarifying question about source packet, timing, and desired output. |

## Review Checklist

- Keep personal identifiers and raw lead text out of public artifacts.
- Keep attention metrics separate from demand metrics.
- Use this score only as an owner-review aid, not as an automated sales action.
- Do not send outreach, write CRM records, update Notion, or store live lead
  data without explicit approval.
- Downgrade unsupported buyer claims to HYPOTHESIS until E6/E7 evidence exists.
