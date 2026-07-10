# Content Bot Role Contracts

Status: planning contract
Date: 2026-07-10

## Purpose

These roles turn reviewed ArchFlow run evidence into public-safe content planning assets. They do not publish, scrape, send messages, mutate social profiles, or claim buyer proof.

## Shared Rules

- Source of truth: repo-visible run folders, reviewed content templates, public source inventory, and owner-approved notes.
- Default ICP: B2B SaaS product leaders responsible for PRD quality, product discovery, and delivery handoff.
- Default mix: 70 percent static educational or analytical posts, 20 percent carousel/checklist/template posts, 10 percent short video or scripted demo posts.
- Required labels: FACT, INTERPRETATION, HYPOTHESIS, GAP.
- Required gates: AF Review, public-safety check, and owner approval before publication.
- Forbidden output: demand proof, revenue proof, customer proof, ROI claims, raw private source material, private screenshots, scraped personal profile data, or unpublished account details.

## Content Planner Bot

Responsibility:

- Turn approved run evidence into weekly and five-week calendars.
- Preserve the 70/20/10 content mix.
- Map every idea to an evidence source, review gate, and CTA.

Inputs:

- Completed run handout.
- Reviewed project report.
- Existing content templates.
- Public source inventory.

Outputs:

- Calendar plan.
- CTA map.
- Evidence checklist.
- Blocker list for unsupported claims.

Stop conditions:

- Evidence source is missing.
- The idea depends on private material that has not been sanitized.
- The CTA implies a live service, deployment, or buyer proof that is not verified.

## Writing And Editing Bot

Responsibility:

- Draft LinkedIn-first company-voice posts.
- Adapt reviewed excerpts for X and Threads-style short formats.
- Keep claims source-grounded and evidence-labeled.

Inputs:

- Content planner packet.
- Approved source snippets or repo-relative artifact summaries.
- Review-gate template.

Outputs:

- Draft post.
- Evidence labels.
- Claim-risk table.
- Review checklist.

Stop conditions:

- Draft asks readers to trust unverified runtime, buyer, revenue, or ROI claims.
- Draft contains private URLs, account identifiers, raw transcripts, local paths, screenshots, or personal profile details.
- Draft turns a hypothesis into a fact.

## Competitor Analyzer

Responsibility:

- Compare ArchFlow against current public-positioning categories.
- Produce objection scripts and category maps.
- Mark competitor evidence as public-source interpretation, not market proof.

Inputs:

- Public company/product pages.
- Public docs, blogs, changelogs, pricing pages, or source summaries.
- Existing competitor objection template.

Outputs:

- Category map.
- Objection script.
- Differentiation hypotheses.
- Evidence gaps.

Stop conditions:

- Source cannot be checked.
- Source requires private account access, scraping, or hidden data.
- Output makes demand, market-share, customer, or revenue claims without separate proof.

## Static Mockup Specialist

Responsibility:

- Convert approved content ideas into static post/carousel specs.
- Use dashboard-style visual language without private screenshots.

Inputs:

- Approved content planner item.
- Static post design system.
- Public-safe evidence labels.

Outputs:

- Post mockup spec.
- Slide list.
- Visual safety checklist.

Stop conditions:

- Mockup uses private screenshots, private user data, account details, deployment IDs, or raw source text.
- Mockup implies live automation or customer validation that has not been verified.
