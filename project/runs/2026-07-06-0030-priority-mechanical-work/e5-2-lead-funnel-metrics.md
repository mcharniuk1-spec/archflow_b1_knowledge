# E5.2 Lead Funnel Metrics Packet

Date: 2026-07-06
Status: prepared for review
Scope: no-code measurement contract for ArchFlow lead quality

## Purpose

This packet defines the lead funnel and demand-quality metrics that should exist
before E4 content, E3 diagnostic forms, or E6 outreach create meaningful inbound
traffic. It is a planning artifact only. It does not install analytics, collect
leads, write to external systems, or claim validated demand.

## Funnel Stages

| Stage | Definition | Required evidence | Owner-safe next action |
|---|---|---|---|
| Visitor | A person reaches an approved public page or content route. | Page route, source channel, observed date. | Measure route quality only. |
| Engaged visitor | A visitor reads, clicks, saves, replies, or interacts with a diagnostic/calculator. | Event name, page/asset, channel, evidence label. | Route to content review, not demand claim. |
| Diagnostic starter | A visitor begins a diagnostic or submits an initial workflow question. | Segment, trigger event, current tools, source-boundary concern. | Check fit before any sales claim. |
| Qualified lead | A lead matches the first ICP hypothesis and gives a concrete workflow signal. | Segment fit, role category, pain type, source-packet willingness, privacy notes. | Prepare owner-reviewed follow-up. |
| Conversation | A qualified lead agrees to discuss source material, diagnostic scope, timeline, or budget path. | Conversation date, topic summary, buyer-risk signal. | Log learning and next action. |
| Paid-intent lead | The lead shows buyer risk. | Paid diagnostic interest, proposal request, budget-owner referral, source packet plus timeline/scope, or approved paid start. | Move to E7 verdict tracking. |
| Verdict input | The lead outcome is clear enough for the August 1 decision. | Paid / firm intent / no / no-response / disqualified plus reason. | Feed E7 payment-vs-attention decision. |

## Demand Quality Metrics

| Metric | Counts as demand? | Notes |
|---|---|---|
| Source-packet willingness | Yes, if paired with role or team fit. | Strong signal because the buyer risks real workflow context. |
| Paid diagnostic interest | Yes. | Strongest pre-payment signal before a signed start. |
| Proposal request | Yes. | Strong if scope and timeline are concrete. |
| Budget-owner referral | Yes. | Strong if a named role path exists without storing private identifiers in public artifacts. |
| Existing-tool integration question | Maybe. | Useful when tied to source workflow, not generic tool curiosity. |
| Privacy or source-boundary objection | Maybe. | Treat as qualification evidence and E3 copy input. |
| Likes, views, shares, follows, comments | No by default. | Attention only unless the response contains buyer-risk evidence. |
| Compliments or generic interest | No. | Do not upgrade without source, scope, timing, or budget signal. |

## Minimal Lead Record

| Field | Type | Rule |
|---|---|---|
| lead_id | generated string | Use a non-identifying internal ID in public artifacts. |
| observed_date | date | Date the signal was observed or entered. |
| source_channel | enum | `website`, `linkedin`, `x`, `threads`, `referral`, `direct`, `other`. |
| source_asset | string | Public-safe page, post, diagnostic, or campaign label. |
| segment_fit | enum | `first_icp`, `adjacent`, `later_lane`, `unknown`, `disqualified`. |
| role_category | enum | `product_leader`, `product_ops`, `senior_pm`, `founder`, `agency`, `other`, `unknown`. |
| trigger_event | enum | `prd_rework`, `customer_research_overload`, `handoff_loss`, `decision_memory_gap`, `pm_team_growth`, `unknown`. |
| source_packet_willingness | enum | `yes`, `maybe`, `no`, `unknown`. |
| privacy_concern | enum | `none_stated`, `redaction_needed`, `cannot_share_sources`, `security_review_needed`, `unknown`. |
| current_tools | string | Summarize tools only if public-safe and volunteered. |
| buyer_risk_signal | enum | `none`, `source_packet`, `paid_diagnostic`, `proposal_request`, `budget_owner`, `paid_start`. |
| qualification_status | enum | `new`, `needs_review`, `qualified`, `not_fit`, `blocked`, `converted`, `lost`. |
| next_action | enum | `monitor`, `ask_clarifying_question`, `owner_review`, `diagnostic_call`, `proposal`, `exclude`. |

## Stage Gates

FACT:
- E5.2 can define funnel and lead-quality rules without collecting real leads.
- The project plan defines validated demand as paid diagnostic, prepayment, approved paid start, or firm paid intent with source packet, timeline, scope, and budget-owner path.

INTERPRETATION:
- The lead funnel should optimize for buyer-risk signals, not public attention. This keeps E4 content and E3 diagnostics from overstating demand before E6/E7.

HYPOTHESIS:
- The strongest early predictor is source-packet willingness combined with a concrete PRD/rework/handoff pain.

GAP:
- Analytics implementation, diagnostic form wiring, CRM/storage choice, live lead capture, real conversations, paid diagnostics, and payment verdicts remain unproven.

## Review Checklist

- Confirm fields align with E3 diagnostic questions before form implementation.
- Confirm public artifacts never store personal identifiers or private source text.
- Confirm attention metrics remain separate from demand metrics in weekly review.
- Confirm any external analytics or CRM tool requires owner approval before activation.
- Confirm E7 verdict only counts buyer-risk outcomes, not content engagement.
