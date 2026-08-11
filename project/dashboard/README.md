# ArchFlow Knowledge Operator Dashboard

This folder contains the restored responsive Knowledge Operator, its exact public corpus manifest, and a generated generic data projection.

## Routes

```text
/project/dashboard/          canonical hosted dashboard
/dashboard                   hosted redirect to the canonical route
/jarvis.html                 static-server-safe work-packet intake (`/jarvis` is the hosted rewrite)
project/dashboard/index.html direct-file dashboard with data.js fallback
```

The five primary routes are:

- `#manual` — **Documentation**, with product explanation;
- `#operations` — **Project**, with one bounded case;
- `#agents` — **Roles & Skills**, with functional roles and portable skills;
- `#setup` — **Setup**, with the zero-key core and gated integrations;
- `#runs` — **Evidence**, with measured fixtures and receipt rules.

The four technical routes are `#architecture` (**Four Schemas**), `#knowledge` (**Knowledge & Memory**), `#workflow` (**Research → Define → Act**), and `#configuration` (**Configuration**). `#communication` is hidden from primary navigation; it receives Project or Jarvis session handoffs and otherwise shows an empty state.

## Files

- `index.html`, `styles.css`, `app.js` — responsive browser surface;
- `corpus-manifest.json` — exact generic source allowlist;
- `data.json` — generated HTTP payload;
- `data.js` — content-identical direct-file fallback.

The generator never expands directories. Runs, reports, live logs, history, personal memory, local paths, private URLs, emails, credentials, and environment values remain outside the payload.

## Generate And Validate

```bash
python3 project/scripts/generate-dashboard-data.py
python3 project/scripts/validate-dashboard-data.py
python3 project/scripts/benchmark-actionable-agents.py
node --check project/dashboard/app.js
```

The validator proves data/JavaScript parity, exact manifest hashes, ten portable skills, role/pack resolution, provider-disabled defaults, credential-value/presence exclusion, benchmark comparator contracts, and direct-file/GitHub link safety.

## Browser State

V3 stores only:

- the local case draft;
- short local event summaries;
- a same-tab Jarvis transit packet, removed after import;
- one migration marker.

All keys use `archflow.public.v3.*`. On first load, the app removes only known legacy ArchFlow dashboard/Jarvis prefixes and the old shared-session key. It never stores an identity, secret, credential state, raw uploaded file, or canonical project memory.

## Administrator Boundary

There is no client Admin/Guest selector. Admin access starts the server Google OIDC route. The dashboard trusts only the minimal session response and never exposes or persists an email address, Google subject, allowlist, or secret state. Authentication still does not approve providers, spending, Git, deployment, publication, or writeback.

## Jarvis Contract

```text
key: archflow.public.v3.handoff
schema_version: 3.0
kind: archflow_public_handoff
state: review_required
```

The packet contains an objective, requested output, and optional decision, public reference, evidence boundary, exclusions, functional reviewer, constraints, and timestamp. Jarvis validates it; the dashboard validates it again and removes the transit key. No packet appears in a URL or network request.

## Responsive Release Gate

Test 1440, 1024, 768, 390, and 320 pixels across every primary view, Communication Center, the four-schema gallery, all forms/tables, and Jarvis. Release fails on root overflow, clipped text, overlapping controls, uncontained images, duplicate IDs, unlabeled fields, unsafe direct-file navigation, continuing reduced-motion animations, or a browser console error.

See [the operating manual](../../docs/dashboard-operating-manual.md), [quickstart](../../docs/quickstart.md), and [performance evidence](../../docs/performance-evidence.md).
