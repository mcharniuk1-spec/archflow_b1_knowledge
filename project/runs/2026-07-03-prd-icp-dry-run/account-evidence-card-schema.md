# E2.0A Account Evidence Card Schema

Date: 2026-07-03
Status: accepted dry-run schema on 2026-07-03
Basis: `project/workflows/market-research-engine.yaml` account_card_schema, extended with provenance fields required by the E1.4 KB update principle.

## Card Fields

| Field | Type | Rule |
|---|---|---|
| account_id | stable domain id | Derived from domain; never an internal or private ID |
| company_name | string | Public name only |
| domain | string | Public website domain |
| segment_primary | string | From segment model (B2B SaaS product teams first) |
| segment_secondary | string | Optional adjacent segment |
| source_seed | string | Which public directory/list produced the account |
| website_signal | string | English summary of public website evidence |
| job_signal_score | integer 0-20 | From public job postings only |
| linkedin_signal_summary | string | Authorized summary only; no raw profile text |
| social_signal_summary | string | HYPOTHESIS-only field; never graded above C |
| pain_type | enum | customer_research_overload, prd_rework, roadmap_ambiguity, handoff_loss, decision_memory_gap |
| decision_roles | string | Role names and currentness status; verify live before outreach |
| offer_fit | enum | prd_pack, product_ops_workflow_review, ai_kb_handoff |
| evidence_grade | A/B/C/D | Per source-grade rubric |
| independent_signal_count | integer | Must be >= 2 before any outreach claim |
| provenance | list | Public URL or repo-relative reference per signal |
| risk_notes | string | Disqualifiers, compliance flags, stale evidence |
| next_action | enum | exclude, monitor, enrich, verify_people, draft_outreach, interview |
| card_status | enum | draft, reviewed, approved, blocked |
| reviewed_by | string | AF Review or owner; required before card_status=approved |

## Card Rules

- A card without provenance entries is invalid.
- A card whose only signals are social is capped at HYPOTHESIS and next_action=monitor.
- Cards are run evidence. They become durable knowledge only if a reviewed insight or decision is promoted to WikiLLM per the E1.4 principle; raw cards stay in the run folder.
- No card may contain a personal identifier beyond a public role title.
