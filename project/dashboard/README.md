# Architecture Console

The ArchFlow dashboard is a documentation-first, public-safe view of the maintained knowledge and agent architecture. It reads generated project evidence, supports browser-local workflow editing and export, and keeps execution, provider calls, durable writeback, and promotion behind separate gates.

Canonical routes:

```text
/project/dashboard/
/dashboard  -> redirects to /project/dashboard/
/jarvis
```

## Current Views

- `#overview` — architecture status, proof, gates, and current activity.
- `#architecture` — the seven grouped layers and end-to-end contract.
- `#knowledge` — retrieval cascade, RAG parameters, corpus boundaries, and provenance.
- `#agents` — role contracts, skill assignments, and governance.
- `#operations` — Knowledge Service and Agent Control sequence, review-bundle preparation, and handoff gates.
- `#data` — generated public catalog and read-only SQL-like preview.
- `#runs` — configuration, execution, review, promotion, and evidence states.
- `#reference` — editable parameter families, source registry, and operating guidance.
- `#schema` — full-screen, browser-local workflow editor and review-packet export.
- `#manual` — developer-facing operating guide: inputs, parameters, current boundaries, handoffs, skills, and FAQs.

The separate `/jarvis` page is the text-only review console. It can inspect public-safe state and prepare bounded requests. Serverless owner guards reject unacknowledged or unallowlisted requests and fail closed until replay-safe durable controls exist. Provider calls and durable writeback remain disabled by default.

The default dashboard view is `#manual`. Start there when joining an active project or a parallel-chat lane. It explains the current Knowledge Service and Agent Control flows, browser-local administrator/guest preview labels, safe review-bundle handoff, and the live communication protocol. Both preview modes prepare Knowledge Service before Agent Control; the labels are not authentication and do not create individual durable memory.

For parallel work, use one lead integrator and bounded sidecar chats. Each sidecar must read `project/live/communication/`, claim one exclusive file scope, return exact evidence and gaps, and stop if the scope overlaps or requires provider, private-data, deployment, or external-write authority. The integrator reconciles findings and reruns checks after merge. See [`docs/dashboard-operating-manual.md`](../../docs/dashboard-operating-manual.md) and [`project/live/communication/README.md`](../live/communication/README.md).

## Run Locally

From the public repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/`.

## Source And Refresh Contract

- Dashboard data: `project/dashboard/data.json`
- Data generator: `project/scripts/generate-dashboard-data.py`
- UI: `project/dashboard/index.html`, `app.js`, and `styles.css`
- Workflows: `project/workflows/`
- Model routing: `project/config/model-routing.yaml`
- Public memory: `wiki/`

Regenerate `data.json` after changing public workflow, configuration, report, run, or WikiLLM content. The deployed console can refresh newly deployed data in-page; it cannot observe unpublished local files.

## Verification

Install the optional workflow-validation dependency first when it is not already available:

```bash
python3 -m pip install -r project/requirements-dev.txt
```

Run:

```bash
python3 scripts/public_safety_scan.py
node --check project/dashboard/app.js
project/local/venv/bin/python project/scripts/validate-workflows.py
project/local/venv/bin/python project/scripts/dashboard-static-smoke.py --timeout 20 --retries 2
project/local/venv/bin/python project/scripts/jarvis-api-contract-smoke.py
project/local/venv/bin/python project/scripts/jarvis-serverless-owner-guard-smoke.py
python3 project/scripts/pre-push-runtime-guard.py
```

The static smoke renders every current dashboard view, including `#manual`, and proves no provider call or writeback occurs. Responsive and interaction QA additionally covers desktop, mobile, reduced motion, fullscreen editor access, dialog focus restoration, browser-local review bundles, Jarvis input behavior, and API-origin blocking. Exact current results and limitations are recorded in [`project/reports/20260715-architecture-test-results.md`](../reports/20260715-architecture-test-results.md).

## Deployment Boundary

Deploy from the public repository root. The parent workspace uses a different Vercel project and must not be used for this release. `vercel.json` redirects the short `/dashboard` alias to the canonical asset-safe route and applies no-cache and no-index headers.

The public console is not authentication. Do not expose private source text, credentials, raw transcripts, account identifiers, private links, or local paths. Do not describe configured or planned runtime capability as proven execution.

## Writeback And Provider Boundary

Browser-local edits and packets are drafts until an approved executor validates and promotes them. The current public release does not prove:

- provider-backed completions;
- Nexus, Notion, GitHub, or WikiLLM writeback from the browser;
- durable storage, replay-safe spend accounting, or autonomous actions;
- private uploads, raw audio processing, or background workers.

These capabilities require explicit owner approval, server-side secrets, bounded budgets, durable controls, provenance, review, and readback evidence.
