# Knowledge Operator Dashboard Manual

Status: current public V3 surface
Runtime boundary: static and browser-local until a separate server gate proves otherwise

The dashboard is the visible operating surface for the ArchFlow public tool. Its five primary routes are **Documentation**, **Project**, **Roles & Skills**, **Setup**, and **Evidence**. Four secondary routes—**Four Schemas**, **Knowledge & Memory**, **Research → Define → Act**, and **Configuration**—hold the technical detail. The hidden **Communication Center** receives browser handoffs. The dashboard prepares reviewable work; it does not silently execute it.

## Start

```bash
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/`.

Direct-file mode is supported through `project/dashboard/index.html`. The page loads `data.js` before trying `data.json`, and all dashboard/Jarvis routes choose a relative file path or hosted path based on the protocol. No action links to `/` as a “public surface.” The repository action is an explicit HTTPS GitHub link.

## Documentation

Documentation is the default route. It answers four questions before presenting framework detail:

1. Which operating problem does ArchFlow solve?
2. How does one case move from research to maintained knowledge?
3. Which parts work without keys, providers, or external writes?
4. Which proof is required before a capability may be described as active?

The page is intentionally paragraph-led. It explains the relationship between sources, decisions, role ownership, state, review, actions, receipts, and memory rather than presenting a collection of status cards without a narrative.

## Project

Project prepares a V3 browser-local case contract.

Required fields:

- **Objective** — the smallest useful outcome;
- **Requested output** — the named artifact and acceptance shape.

Strongly recommended fields:

- decision supported;
- public reference or non-sensitive label;
- exact allowed evidence;
- explicit exclusions;
- independent reviewer role;
- authority, safety, budget, delivery, retry, stop, and rollback conditions.

A reference is a label only. The static dashboard does not fetch, clone, inspect, upload, or send it. Select **Prepare review packet** to validate the contract, mark it `review_required`, and open Communication Center.

The state rail explains the complete route:

`Frame → Ground → Define → Act → Verify → Remember`

Research → Define → Act is the user-facing summary. Verify and Remember remain explicit gates rather than disappearing into “Act.”

## Communication Center

Jarvis and Project use one exact handoff key and schema:

```text
sessionStorage key: archflow.public.v3.handoff
schema_version: 3.0
kind: archflow_public_handoff
state: review_required
```

The dashboard validates the packet again, imports it in memory, and removes the transit key. Values are escaped before rendering. No packet data appears in a URL. An imported packet can populate the case, download as JSON, or be cleared. Communication Center is hidden from primary navigation but remains available from Project, Jarvis, or its direct hash route; without a packet it shows an honest empty state.

Local notifications describe browser actions only. “Packet prepared,” “handoff accepted,” or “draft cleared” is not a runtime, Git, provider, deployment, or writeback claim.

## Roles & Skills

The public roster uses functional identifiers and titles. A role is activated only when a task contract assigns:

- exact responsibility;
- approved sources;
- packaged skills and method checklists;
- tool ceiling;
- one owned output;
- independent reviewer;
- handoff target;
- stop and escalation rules.

The V3 catalog contains 21 functional roles, four smallest-responsible role packs, and ten portable public skills. Project-maintenance schedules, retired service wrappers, private skills, and method names that are not packages stay outside the catalog.

An “agent” card does not prove a running model or service. One person may coordinate several low-risk contracts, but high-risk maker and reviewer contracts remain separate.

## Setup

The dashboard presents three tiers.

### 1. Static Public Core

No keys. Documentation, four schemas, case packets, Communication Center, functional roles, portable skills, downloads, and provider-disabled validation.

### 2. Validated Local Runtime

An isolated environment may add schema validation, bounded lexical retrieval, LangGraph route fixtures, CrewAI role/task materialization, and local Jarvis contract tests. Install only the profile you need and keep tracing off by default.

### 3. Gated Server Integrations

Google authentication, model providers, observability, checkpoints, databases, deployment, and external actions are separate extensions. Documenting an environment name or adapter state is not proof that a value exists or a service is callable.

## Admin Access

There is no client-selectable role mode. The dashboard never offers an Admin/Guest selector and never accepts a pasted owner token.

**Admin access** begins the server route. A verified session requires authorization code, state, nonce, PKCE S256, Google ID-token validation, a server-side subject/email allowlist, a signed short-lived `__Host-archflow_admin` cookie, exact-origin enforcement, CSRF protection, and logout cookie clearing. Stateless sessions cannot be individually revoked before expiry; changing `ARCHFLOW_AUTH_SESSION_EPOCH` or rotating the signing key invalidates all issued sessions, while individual revocation requires a server-side session store.

The session endpoint returns only the minimum public contract—authenticated state, role, and CSRF value. It does not return an email address, Google subject, allowlist, secret state, or credential-presence signal.

Authentication is necessary for administrator-only controls but insufficient for provider calls, spending, Git mutation, deployment, publication, or external writeback. Each remains a separate authorization and effect gate.

## Evidence

Every metric card has:

- label and value;
- numerator/denominator or exact comparator;
- fixture scope and date;
- limitation;
- provider-call and external-write counts.

Current V3 fixture results:

- 98.6% lower UTF-8 context input against the declared full-manifest comparator;
- 75.0% fewer activated role slots against all-role fan-out;
- 4/4 expected source hits in lexical top five;
- 8/8 expected semantic gate decisions;
- zero provider calls;
- zero external writes.

Do not transform these into memory-saved, billed-token, speed, labor, ROI, production-accuracy, or universal-safety claims.

## Four Schemas And Their Distribution

All four are available together under **Technical views → Four Schemas**. Each also appears next to the task it explains:

1. **Seven-layer knowledge crew** — system map and complete architecture.
2. **Input and perception flow** — Knowledge & Memory.
3. **Output, validation, and receipts** — Evidence.
4. **Onboarding and teamwork** — Roles & Skills and Communication.

On small screens, the dashboard shows a contained full-width preview, a text summary, and a link to the full-resolution editable SVG. The diagram is never the only explanation.

## Browser Storage

V3 uses only the `archflow.public.v3.*` namespace.

- case drafts and local event summaries use local storage;
- the Jarvis transit packet uses session storage and is removed after dashboard import;
- no identity, credential, raw uploaded file, provider result, or durable canonical memory is stored.

On first V3 load, the page removes only the allowlisted retired ArchFlow dashboard/Jarvis prefixes and the exact retired shared-session key. Unrelated site storage remains untouched.

Use browser site-data controls to clear the V3 draft. Never enter sensitive material into either public surface.

## Proof Vocabulary

| State | Meaning |
|---|---|
| Documented | Maintained explanation and source exist |
| Configured | Contract parses with explicit defaults |
| Locally tested | Fixed fixture ran and produced evidence |
| Independently reviewed | Separate reviewer verified the frozen candidate |
| Approved action | Exact actor, target, operation, data class, rollback, and approval exist |
| Read back | The exact target state was observed after the action |
| Promoted knowledge | Reusable meaning was reviewed with lineage and freshness |

Never infer a stronger state from a weaker one.

## Verification

```bash
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
python3 project/scripts/benchmark-actionable-agents.py
python3 project/scripts/auth-contract-smoke.py
node --check project/dashboard/app.js
node --check jarvis.js
python3 scripts/public_safety_scan.py
```

Responsive browser proof covers 1440, 1024, 768, 390, and 320 pixels for every primary route, the four-schema gallery, Communication Center, forms, tables, images, and Jarvis. Reduced-motion checks must find no continuing animation. Root overflow, clipped controls, overlapping text, duplicate IDs, unlabeled form controls, and direct-file unsafe routes are release blockers.

## Troubleshooting

| Symptom | Explanation | Safe response |
|---|---|---|
| A direct-file link opens the filesystem root | Old absolute-root navigation is cached or an old release is open | Use the V3 files; never weaken file URL restrictions |
| `data.json` cannot be fetched in file mode | Expected browser restriction | Regenerate and use the bundled `data.js` fallback |
| Jarvis does not hand off | Required fields, confirmation, or public-safety validation failed | Correct the packet; do not place it in the URL |
| Communication Center has no packet | It was consumed, cleared, invalid, or created in another tab | Prepare it again in the same tab |
| Admin returns setup unavailable | OAuth is not securely configured | Configure the server values and exact callback; rerun negative and live tests |
| A provider remains blocked | Correct default | Finish the provider-specific nonce, allowlist, spend ledger, approval, and readback gates |
| A downloaded packet produced no change | Correct public behavior | Hand it to an approved operator/controller and record maker/reviewer evidence |
