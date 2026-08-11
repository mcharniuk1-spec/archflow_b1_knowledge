# Quickstart

ArchFlow Knowledge Operator is useful before a provider or hosted agent runtime is configured. The default path generates a small public projection, validates its exact source boundary, opens the responsive dashboard, and prepares browser-local review packets. The generator updates only declared local product artifacts. It does not read credential values, call a model, fetch a repository, start an agent, mutate Git, deploy, write externally, or contact a provider.

## Prerequisites

- Git;
- Python 3.11 or later for the standard-library core;
- Node.js only for the optional JavaScript syntax check;
- Python 3.12 for the reviewed optional validation and agentic dependency profiles.

## 1. Clone The Generic Public Tool

```bash
git clone https://github.com/mcharniuk1-spec/archflow_b1_knowledge.git archflow
cd archflow
```

The checkout contains generic documentation, functional roles, portable skills, state/review/memory schemas, provider-disabled workflows, four architecture SVGs, a deterministic benchmark, and the browser surfaces. It does not require or reconstruct any private ArchFlow workspace.

## 2. Generate And Validate The Public Projection

```bash
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
python3 project/scripts/benchmark-actionable-agents.py
```

Expected boundaries:

- exactly the files declared in `project/dashboard/corpus-manifest.json` are indexed;
- project runs, reports, live logs, history, personal memory, local paths, private URLs, emails, and credential values are excluded;
- all 21 functional roles, four declared role packs, and ten portable skill contracts resolve;
- the provider registry defaults to `none` and reports no credential presence;
- provider calls and external writes remain zero;
- every published metric includes its comparator and limitation.

## 3. Run The Dashboard And Jarvis

```bash
python3 -m http.server 8765
```

Open:

- `http://127.0.0.1:8765/project/dashboard/` — Knowledge Operator;
- `http://127.0.0.1:8765/jarvis.html` — public-safe work-packet intake.

The dashboard also opens directly from `project/dashboard/index.html`. Its `data.js` fallback prevents local-file fetch errors, and protocol-aware links prevent a browser from navigating to the filesystem root.

## 4. Prepare One Case

In **Project**, enter:

1. the smallest useful objective;
2. the decision the output must support;
3. a public repository reference or a non-sensitive label;
4. the exact allowed evidence;
5. explicit exclusions;
6. the requested artifact;
7. an independent reviewer role;
8. authority, budget, safety, delivery, stop, and rollback conditions.

Select **Prepare review packet**. The dashboard validates the required fields, stores a versioned handoff in this browser, and opens **Communication Center**. The packet is still `review_required`; no work is represented as executed.

## 5. Use Jarvis Safely

Jarvis accepts the same public-safe contract in a focused form. It rejects local paths, file URLs, email addresses, credential-like strings, private-network URLs, bearer values, and incomplete required fields. After validation it puts the packet in this tab’s session storage and navigates—without URL payloads—to the dashboard Communication Center.

The dashboard imports and deletes the transit key. You can accept the packet into the browser-local case, download it, or clear it. Closing the tab discards unaccepted transit state.

## 6. Understand Individual And Team Use

An individual can coordinate several role contracts, but maker and independent-review responsibilities remain separate for high-risk work. Drafts can stay in one browser and be exported for review.

A team binds the same functional roles to different people or compatible runtimes and uses one writer per shared target:

```text
bounded contract
→ maker candidate
→ deterministic checks
→ independent review
→ exact approved action
→ target readback
→ maintained knowledge
```

Browser storage is not shared collaboration. Do not describe the static release as multi-user, durable, or tenant-safe until authentication, RBAC, shared persistence, audit, retention, backup, and recovery are implemented and verified.

## Setup Tiers

### Tier 1 — Static Public Core

Requires no keys. It includes the dashboard, Jarvis handoff, four schemas, generated role/skill projection, lexical retrieval fixture, semantic gates, downloads, and documentation.

### Tier 2 — Validated Local Runtime

Inspect first:

```bash
python3 project/scripts/setup-local.py --profile all
```

Install the isolated validation profile only when required:

```bash
python3.12 project/scripts/setup-local.py --profile validation --locked --install --verify
```

The optional agentic profile may add provider-disabled LangGraph, CrewAI, and LlamaIndex checks. Python 3.12 is the reviewed baseline for those dependencies; a manifest is not proof that a service or model is live.

### Tier 3 — Server-Side Integrations

Google administrator authentication, local or hosted model adapters, observability, databases, and external writeback are separate additions. Each needs exact environment names, data boundary, negative tests, budget/effect controls, approval, rollback, and readback.

## Administrator Authentication

The public UI has no Admin/Guest switch. **Admin access** starts the server route only. Missing server configuration returns a generic fail-closed error.

Environment names:

```text
ARCHFLOW_AUTH_ENABLED
GOOGLE_OAUTH_CLIENT_ID
GOOGLE_OAUTH_CLIENT_SECRET
ARCHFLOW_AUTH_ORIGIN
ARCHFLOW_AUTH_SECRET
ARCHFLOW_AUTH_SESSION_EPOCH
ARCHFLOW_ADMIN_GOOGLE_SUBJECTS
ARCHFLOW_ADMIN_EMAILS
ARCHFLOW_AUTH_SESSION_TTL_SECONDS
```

Prefer the stable Google subject allowlist. A verified-email allowlist is a deliberate bootstrap fallback. Values and account identities must stay in the deployment platform or approved secret manager, never Git, browser storage, dashboard JSON, screenshots, or logs.

The flow uses authorization code, state, nonce, PKCE S256, verified Google ID tokens, a short-lived `__Host-archflow_admin` cookie, exact-origin checks, CSRF protection, and logout cookie clearing. A verified session identifies the administrator; it does not approve provider execution, spend, Git mutation, deployment, publication, or writeback. Stateless sessions cannot be individually revoked before expiry; changing `ARCHFLOW_AUTH_SESSION_EPOCH` or rotating the signing key invalidates all issued sessions, while individual revocation requires a server-side session store.

Run the negative contract matrix:

```bash
python3 project/scripts/auth-contract-smoke.py
```

Live sign-in still requires a configured Google OAuth client, the exact deployed callback, server values, preview proof, and production readback.

## Verify A Checkout

Core checks:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
python3 project/scripts/benchmark-actionable-agents.py
python3 project/scripts/auth-contract-smoke.py
node --check project/dashboard/app.js
node --check jarvis.js
python3 scripts/public_safety_scan.py
```

Optional dependency-backed checks:

```bash
python3.12 project/scripts/setup-local.py --profile validation --locked --install --verify
python3.12 project/scripts/setup-local.py --profile agentic --locked --install --verify
python3.12 project/scripts/setup-local.py --profile jarvis --locked --install --verify
```

Do not enable a provider, tracing, private corpus, deployment, database, Git write, or external writeback as part of “verification.” Each is a different action boundary.

## Troubleshooting

| Symptom | Meaning | Safe response |
|---|---|---|
| Dashboard opens with generic fallback data | `data.json` was not served and `data.js` was missing or stale | Regenerate data; serve from the repository root; do not weaken browser security |
| Direct-file route opens the wrong place | An old absolute-root link was cached | Use the V3 files and clear only the allowlisted retired ArchFlow dashboard/Jarvis site data |
| Jarvis holds the packet | Required content is missing or a safety pattern matched | Remove private/identifying material and state the objective and output |
| Communication Center says no packet | The transit packet was consumed, cleared, invalid, or created in another tab | Prepare it again in the same tab; do not put packet content in the URL |
| Admin sign-in returns setup unavailable | Server-side OAuth values or enable flag are absent | Configure the deployment securely and rerun negative plus live callback tests |
| A provider route remains blocked | Correct default behavior | Complete the provider-specific nonce, spend, approval, and ledger gates rather than bypassing them |
| Packet downloaded but no work happened | Correct public behavior | Give it to an approved operator or state controller and record maker/reviewer evidence |
