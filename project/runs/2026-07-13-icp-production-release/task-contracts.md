# ICP Product Surface Production Release — Task Contracts

## R1 — Release Manifest And Local Gate

- Owner: primary Codex operator
- Inputs: reviewed ICP implementation, public operating rules, release context capsule
- Output: explicit staged-file manifest and passing local quality matrix
- Acceptance: no unrelated Graphify or private runtime files are staged; public-safety, syntax, workflow, API-contract, static, responsive, accessibility, and interaction checks pass
- Stop condition: unresolved public-safety finding, broken primary interaction, or conflicting file claim

## R2 — Independent Review

- Owner: read-only reviewer agent
- Inputs: release diff and QA evidence
- Output: bounded risk and acceptance assessment
- Acceptance: no critical release blocker; all non-blocking gaps recorded
- Stop condition: reviewer identifies an unverified material claim, unsafe artifact, or broken release contract

## R3 — Git And Production Deployment

- Owner: primary Codex operator
- Inputs: accepted staged manifest and local QA
- Output: pushed Git commit and current Vercel production deployment
- Acceptance: remote push succeeds; production routes return and visibly match the committed release; provider execution remains disabled by default
- Stop condition: wrong Vercel project, failed deployment, unexpected alias, or production freshness mismatch

## R4 — Figma Baseline Sync

- Owner: primary Codex operator
- Inputs: verified production deployment
- Output: updated `03 Codex Website Sync` page and local sync state record
- Acceptance: required landing and quiz desktop/mobile captures are represented and linked in the target Figma file
- Stop condition: production is not current or the target Figma file/page cannot be verified

## R5 — Notion Delivery Update

- Owner: primary Codex operator
- Inputs: Git, production, QA, and Figma evidence
- Output: bounded updates to the relevant dashboard/public-surface tasks
- Acceptance: completion language reflects proven evidence; provider execution and other gated capabilities remain explicitly incomplete
- Stop condition: ambiguous target page or inability to read back the mutation

## R6 — Durable Closeout

- Owner: primary Codex operator
- Inputs: completed external actions and independent review
- Output: QA report, task handout, communication closeout, and WikiLLM run record
- Acceptance: changed files, checks, gaps, and next safe action are explicit and public-safe
