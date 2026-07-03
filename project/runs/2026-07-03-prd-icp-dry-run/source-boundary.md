# E2.0A Source Boundary

Date: 2026-07-03
Status: accepted dry-run boundary on 2026-07-03
Reviewer: owner (pending)

## Approved Source Types

- Public company websites (product, pricing, careers, blog pages).
- Public job postings (company career pages, public job boards).
- Public review sites (G2, Capterra-class public review text; summaries only).
- Public directories and public market lists.
- Authorized LinkedIn views summarized in English (no raw exports, no scraped profile text).
- Approved search queries over public pages.
- Internal approved corpus: `project/`, `history/`, `skills/`, `wiki/`.

## Excluded Raw Inputs

- Private transcripts, emails, chat logs, or meeting recordings.
- Scraped private profiles or logged-in-only content.
- Purchased lead databases (Apollo, Clearbit, PDL and similar remain gated per `project/workflows/market-research-engine.yaml` tool policy).
- Raw private lead data of any kind in the public repo.
- Screenshots, account IDs, private URLs.

## Private Material Handling

Private context may be read for understanding only. Anything entering this packet must be a translated public-safe English summary with a generic source description and repo-relative reference where possible.

## Public-Safe Output Level

All artifacts in this run are public-safe: no personal names of non-public individuals, no credentials, no local paths, no private identifiers. Named companies may appear only with public-evidence citations; this dry run uses schema-level placeholders instead of real accounts.

## Provider And Tool State

- No provider calls in this run. Local deterministic writing only.
- Gated tools (search APIs, crawlers, enrichment vendors) stay gated until legal, storage, rate limits, and AF Review approval are explicit.

## Evidence Rules (inherited)

- Minimum two independent signals before any outreach claim.
- Social-only claims are HYPOTHESIS, never FACT.
- Decision-maker currentness must be verified live before outreach.
