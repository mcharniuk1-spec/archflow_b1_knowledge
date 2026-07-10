# External Action Gate Review

Status: Git integration ready; external actions remain conditional.

| Action | Current decision | Evidence and blocker | Exact next safe action |
|---|---|---|---|
| Git commit and push | Approved after final validation | Three selective branch commits are merged locally; integrated validation passed. | Commit supervisor closeout files, rerun checks, and push `main` once. |
| Notion mutation | Pending post-Git review | Connector tools are available, but the exact workspace/pages/databases, property schema, idempotency, and rollback mapping have not yet been proven. | After pushed Git evidence, run read-only planning reviews, search/fetch targets, then mutate only if one unambiguous mapping passes all gates. |
| Linear mirror | Blocked | Linear is optional; no verified team/project/state/label/idempotency map exists. | Keep repo-native artifacts canonical; prepare a lightweight mirror only after a separate verified free-level target review. |
| Railway action | Blocked | No current target/service linkage, endpoint freshness, continuous monitoring, auth/CORS, rollback/recovery, or post-action verification packet exists in this run. | Use `branch-a/railway-prerequisite-packet.md` in a separate approved runtime task. |
| Vercel/production deploy | Blocked | No current deployment target/rollback/freshness packet was approved or verified. | Run a separate target-specific deployment contract and public-safety preflight. |
| OpenRouter/provider call | Blocked | No current model selection, capability/pricing snapshot, key/secret path proof, hard budget, usage/cost ledger readback, or sanitized call approval exists. | Follow the activation-time gate in `project/provider-setup.md`; do not call a model from this run. |
| Social API/posting | Blocked | Branch C is preparation-only; account access, API terms, credentials, owner approval, and publication packet are absent. | Use the reviewed content artifacts only after a separate publication approval. |
| Telegram/Figma/other writeback | Blocked | No target/schema/disclosure packet is part of this run. | Prepare a bounded action packet and verify target plus disclosure/safety gates first. |

No blocked action is reported as passed or complete.
