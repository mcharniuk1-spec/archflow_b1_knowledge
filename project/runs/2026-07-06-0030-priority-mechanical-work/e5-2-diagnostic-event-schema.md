# E5.2 Diagnostic Event Schema

Date: 2026-07-06
Status: draft contract
Implementation status: not installed

## Purpose

This schema defines public-safe event names and payload fields for a future E3
diagnostic page and E5 funnel review. It is intentionally tool-neutral. No
analytics provider, database, CRM, tag manager, or external write was configured
in this run.

## Event Names

| Event | When it fires | Demand status |
|---|---|---|
| `diagnostic_viewed` | A visitor opens the diagnostic route. | Attention only. |
| `diagnostic_started` | A visitor starts answering diagnostic questions. | Attention plus weak intent. |
| `diagnostic_completed` | A visitor finishes the diagnostic. | Qualification candidate. |
| `source_packet_willingness_marked` | A visitor says whether they can share source material. | Demand signal if paired with fit. |
| `privacy_concern_marked` | A visitor selects or states a source/privacy concern. | Qualification signal. |
| `cta_clicked` | A visitor clicks a call-to-action. | Attention unless tied to buyer-risk fields. |
| `lead_review_created` | An operator creates a public-safe review packet from a submitted signal. | Internal review signal. |
| `paid_intent_marked` | A reviewed lead shows paid diagnostic, proposal, budget-owner, or paid-start signal. | Demand signal. |
| `lead_disqualified` | A lead is marked outside current scope. | Verdict input. |

## Shared Payload Fields

| Field | Type | Required | Public-safe rule |
|---|---|---:|---|
| event_name | string | yes | Use one event name from this schema. |
| event_version | string | yes | Start with `2026-07-06.v1`. |
| observed_date | date | yes | Date only is enough for public summaries. |
| source_channel | enum | yes | Website, LinkedIn, X, Threads, referral, direct, other. |
| source_asset | string | yes | Public-safe route or content label. |
| session_public_id | generated string | no | Do not expose browser cookies or private IDs in public artifacts. |
| lead_public_id | generated string | no | Use only after review packet creation. |
| segment_fit | enum | no | `first_icp`, `adjacent`, `later_lane`, `unknown`, `disqualified`. |
| role_category | enum | no | Store role category, not personal identity, in public packets. |
| trigger_event | enum | no | Use approved trigger categories from the E5.2 funnel packet. |
| buyer_risk_signal | enum | no | Use approved buyer-risk categories only after review. |
| evidence_label | enum | yes | `FACT`, `INTERPRETATION`, `HYPOTHESIS`, or `GAP`. |

## Diagnostic Question Map

| Diagnostic question area | Maps to field | Why it matters |
|---|---|---|
| Team segment and role category | `segment_fit`, `role_category` | Separates first ICP from later lanes. |
| Current product workflow bottleneck | `trigger_event` | Routes pain into E2/E3/E6 learning. |
| Current tools and output destination | `current_tools_summary` | Tests integration concern without overcollecting private data. |
| Source-packet willingness | `source_packet_willingness` | Converts interest into buyer-risk evidence. |
| Privacy/source-boundary concern | `privacy_concern` | Feeds positioning and qualification. |
| Budget-owner path or paid diagnostic interest | `buyer_risk_signal` | Routes toward E7 verdict only after review. |

## Public-Safety Constraints

- Do not store names, emails, account IDs, raw submitted documents, raw meeting notes, raw transcripts, private URLs, credentials, or screenshots in public artifacts.
- Do not record browser cookies, ad identifiers, or analytics user IDs in public run packets.
- Summarize private lead inputs only after owner-approved handling rules exist.
- Keep raw lead storage outside the public repo and behind an approved tool boundary.

## Implementation Gates

| Gate | Required before activation |
|---|---|
| E3 diagnostic page | Owner-approved form copy and source-boundary language. |
| Analytics provider | Owner-approved provider, storage policy, and public-safety review. |
| CRM or Notion writeback | Approved connector/write path and masked payload template. |
| Dashboard display | Generated public-safe aggregates only, no raw lead rows. |
| E7 verdict | Manual review of buyer-risk evidence before demand claims. |
