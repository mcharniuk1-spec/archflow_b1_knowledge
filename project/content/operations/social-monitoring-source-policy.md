# Social Monitoring Source Policy

Status: planning policy
Date: 2026-07-10

## Purpose

This policy defines what content operations may learn from public social and web sources without crossing into unsafe collection, scraping, or unsupported claims.

## Allowed Sources

- Public company and product pages.
- Public blogs, docs, changelogs, and newsletters.
- Public pricing pages and public help-center pages.
- Public directories and review pages, when terms allow review.
- Search-result summaries used only as routing hints before opening primary sources.
- Manually observed public posts used as language or format examples.
- Official APIs only after approval, current terms review, scope definition, and budget/rate-limit proof.

## Blocked Sources And Methods

- Private communities, private groups, private messages, or private workspaces.
- Scraped personal profiles, comments, followers, or engagement graphs.
- Downloaded social videos or screenshots from private contexts.
- Raw personal identifiers or account-level details not approved for public use.
- Automated collection from LinkedIn, X, Threads, Instagram, TikTok, or Reels-style surfaces without explicit API/terms approval.
- Social-only demand, ROI, customer, revenue, conversion, or willingness-to-pay claims.

## Safe Social Use

Allowed use:

- Language hypotheses.
- Format hypotheses.
- Objection themes.
- CTA experiments.
- Topic backlog candidates.

Required record:

- Source category.
- Public URL when allowed.
- Date checked.
- Source grade.
- Theme extracted.
- Claim status: hypothesis unless independently validated.

## Outreach Claim Rule

Outreach-facing claims require at least two independent public signals and a review gate. A social signal can support a hypothesis, but it cannot be the sole proof for buyer pain, demand, revenue impact, customer proof, or ROI.

## Storage Rule

Store only public-safe summaries in run folders. Do not store private screenshots, raw comments, raw profile text, raw engagement data, account IDs, private URLs, or local absolute paths.
