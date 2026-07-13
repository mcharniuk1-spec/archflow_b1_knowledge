# Research And Check Task Template

Use for E2 research, ICP checks, market-signal review, account-evidence cards, or any task where a claim must be separated into fact, interpretation, hypothesis, and gap before it informs content or outreach.

## Template Metadata

- Task:
- Epic:
- Research/check owner:
- Source run folder:
- Target audience: B2B SaaS product leaders
- Offer frame: forcing-moment Product Knowledge Reliability Setup
- Status: planned / executed / AF Review / blocked / promoted

## Eligible Subtopics

- Enterprise questionnaire/RFP, onboarding/hiring, and key-person-departure knowledge bottlenecks.
- Public-signal breakdowns for funding, hiring, senior-product departure, and enterprise/security motion.
- Buyer-ownership checks across Product, Security, Sales Engineering, and RevOps.
- Competitor positioning around enterprise knowledge, product operations, agent context, retrieval, and generated delivery packs.
- Public social-language themes as hypothesis only.
- Account evidence cards for future E6 outreach.
- Claim downgrade when evidence is weak or stale.

## Source Boundary

Allowed sources:

- Public company websites.
- Public job pages.
- Public product pages and case studies.
- Public reviews and directories.
- Approved search API summaries when legal and source boundaries are documented.
- Authorized public social views for language hypotheses only.

Blocked sources:

- Private channels, private LinkedIn data, private emails, scraped personal data without approval, raw transcripts, credentials, private URLs, operational IDs, or named target accounts in public files.

## Research Card Structure

```md
# Research Check: <topic>

Date:
Epic/task:
Source boundary:
Save location:

## Question

What claim, signal, or assumption is being checked?

## Evidence Table

| Source | Date checked | Signal | Source grade | Evidence label | Notes |
|---|---|---|---|---|---|
|  |  |  | A/B/C/D | FACT/INTERPRETATION/HYPOTHESIS/GAP |  |

## Claim Status

FACT:
INTERPRETATION:
HYPOTHESIS:
GAP:

## Content Angle If Approved

- Main lesson:
- Product-leader relevance:
- Artifact or visual:
- CTA:

## Outreach Use If Approved

- Role relevance:
- Pain hypothesis:
- Required second signal:
- Blockers:
```

## Proof Required

- At least one source for any FACT.
- At least two independent public signals before account qualification or outreach handoff.
- Date checked for every source.
- Source grade for every row.
- Explicit downgrade to HYPOTHESIS when the evidence is social-language only.
- Explicit GAP when role verification, source freshness, or permission is missing.

## Copy Blocks

### Public-Safe Research Summary

```text
FACT: [source-backed observation]
INTERPRETATION: [what this may mean for knowledge continuity or handoff]
HYPOTHESIS: [how this may map to B2B SaaS product leaders]
GAP: [what is not yet verified]
```

### Content Hook

```text
A recurring knowledge bottleneck is not the document format. It is weak source lineage: teams cannot tell which answer came from customers, internal decisions, assumptions, or unresolved gaps.
```

## Approval Checklist

- Source acquisition method is allowed.
- Every source row has date, grade, signal, and label.
- Named accounts or target people are excluded from public files unless separately approved.
- No outreach claim is promoted without at least two independent public signals.
- AF Review approved claim status and public-safety boundary.
- Owner approval exists before using research in a public post or outreach asset.

## Save After Execution

- Research card: `project/runs/E2/<date-run-name>/research-check.md`
- Source inventory: `project/runs/E2/<date-run-name>/source-inventory.md`
- Review gate: `project/runs/E2/<date-run-name>/review-gate.md`
- Content draft, if approved: `project/runs/E2/<date-run-name>/content-angle.md`
- Outreach handoff, if approved: `project/runs/E2/<date-run-name>/outreach-evidence-handoff.md`
