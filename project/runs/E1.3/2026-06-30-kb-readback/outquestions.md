# Outquestions: E1.3 Readback And E1.5 Gate

Date: 2026-06-30
Status: completed closeout questions and defaults

## What Changed

E1.3 moved from missing evidence to a public-safe KB writeback/readback proof. The repo now contains the approved E1.2 summary, agent history, source registry, retrieval metadata, loop state, readback report, review report, validation report, and dashboard-derived gate status.

E1.5 started only as a public-reporting gate. No public post, carousel, or demand claim is approved yet. The gate defines what must be true before process proof becomes public content.

The dashboard now exposes E1.3 status as a derived, read-only gate. It does not store decisions and does not replace WikiLLM.

## Artifacts

- `project/runs/E1.3/2026-06-30-kb-readback/`
- `project/runs/E1.5/2026-06-30-public-reporting-gate/`
- `project/scripts/e1_3_kb_readback.py`
- `project/dashboard/data.json`
- `project/dashboard/app.js`
- `wiki/runs/2026-06-30-e1-3-kb-readback.md`
- `wiki/decisions/2026-06-30-e1-3-readback-and-public-reporting-gates.md`

## Blocking Questions And Defaults

1. Should the first hosted dashboard be public, hidden-link, or auth-gated?
   Default: hidden-link static dashboard first. Public is allowed only after AF Review confirms every field is public-safe. Auth-gated is required if any private state, private task data, or live operational control appears.

2. Should Railway wait until voice/background workers exist, or should an API skeleton be created earlier?
   Default: Railway waits. Create an API skeleton only after `/health` and `/dashboard-data` contracts are written and a live worker, queue, websocket/SSE, or voice bridge actually needs an always-on service.

3. Which voice commands are allowed first?
   Default: status and readback only. Dashboard refresh, task creation, local file actions, Notion edits, Git writes, deployments, and outreach remain approval-gated.

4. Who is public reporting for?
   Default: product leaders in B2B SaaS scaleups: Directors/VPs/Heads of Product, Product Ops leads, and senior PM leaders.

5. Should posts be personal build-in-public or ArchFlow company content?
   Default: ArchFlow company content first. Personal build-in-public is a later lane if the owner chooses it.

6. What visual style should GloomyLord use?
   Default: product-system with research-lab discipline. Minimal technical language is allowed, but the output should feel credible for product operations, not decorative or theatrical.

7. What proof is required before a task becomes a public carousel?
   Default: approved public-safe artifact, evidence labels, no demand/customer/ROI claim unless E6/E7 evidence exists, AF Copy draft, AF Review approval, and owner approval.

8. Who approves carousel text and post copy?
   Default: AF Review plus owner final approval.

## Next Stage Gate

Smallest safe next action: sync private task-board status for E1.3 and E1.5, then commit and push the public repo.

Gate before live/public/write action: hosted dashboard visibility, voice command taxonomy, API/Railway contract, and carousel approval path must be explicit.

## Risks And Gaps

FACT: E1.3 readback passed 10/10 deterministic assertions.

FACT: E1.2 remains Review until owner acceptance.

INTERPRETATION: E1.5 can proceed as templates and gate design, not publishing.

HYPOTHESIS: Hidden-link dashboard first gives useful review access without prematurely turning project internals into public marketing.

GAP: Live Notion state still needs sync after Git validation. Vector retrieval and turbovec still need source IDs, chunk IDs, embeddings, and benchmark.
