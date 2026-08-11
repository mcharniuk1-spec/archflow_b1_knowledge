---
name: humanize-writing
description: Polish caller-supplied, approved user-facing prose while preserving facts, citations, links, technical values, and claim limits. Use for product copy, posts, proposals, documentation, or final responses that should sound clear and natural; use full mode only when the caller explicitly requests a deeper humanized rewrite.
---

# Humanize Writing

Improve the writing without changing what the evidence supports. This is editorial work, not detector evasion or an authorship claim.

## Input contract

Accept a caller-supplied draft, audience, purpose, evidence boundary, requested mode, protected spans, and optional writing-style sample. Stop or narrow the claim when a factual source is missing. Do not retrieve personal context or send the draft to a provider.

## Modes

- **Light:** improve clarity, paragraph flow, rhythm, and audience fit while keeping the draft's structure.
- **Full:** when explicitly requested, repair repetitive signposting, inflated certainty, padded conclusions, uniform cadence, and weak argument structure.

## Workflow

1. Identify the audience, purpose, facts, uncertainty, and protected content.
2. Preserve names, numbers, citations, quotations, links, code, filenames, frontmatter, tables, and structured data unless the caller requests a factual correction.
3. For persuasive copy, map each claim to supplied evidence and keep the limitation visible.
4. Match the supplied writing style when one exists; otherwise use plain, audience-appropriate prose.
5. Rewrite passages, not isolated synonyms. Do not use translation hops, synonym engines, or detector-guided loops.
6. Compare the result with the source for factual values, meaning, protected spans, and unsupported specificity.

Read `references/patterns.md` only when a full-mode pattern audit is needed.

## Output

Return the polished copy to the caller or the dashboard Communication Center. If a file is required, write it only to `project/local/<case-id>/humanized-draft.md` unless the caller names an exact approved target.

For full mode, include a short edit note and any unresolved evidence gap. Never publish, post, send, deploy, or overwrite an approved source without a separate exact action gate and independent review.

## Local verification

Run `python3 scripts/check_fixtures.py` from this skill directory. The fixtures verify protected facts, links, citations, code, frontmatter, writing-style guidance, and an unchanged already-natural example.
