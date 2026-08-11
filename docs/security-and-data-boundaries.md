# Security and Data Boundaries

## Public repository

Only files in `public-product-manifest.json` belong in the clean release. That allowlist contains public-safe contracts, documentation, generic schemas, generated public projections, fixed synthetic fixtures, and example configuration. It excludes prior reports and runs, live coordination, personal or project memory, credentials, private URLs, local paths, account identifiers, raw transcripts, customer documents, browser logs, model traces, and private corpus content.

## Browser

The dashboard stores drafts and packet state in browser storage. Treat that data as local to the browser profile, not as durable operational memory. Downloaded review bundles still need human review before they enter a repository or another system.

## Providers and APIs

Provider keys belong in server-side or locally ignored environment configuration, never static JavaScript, browser inputs, Markdown, catalog data, or Git. The public provider registry documents extension points, but no provider-execution adapter is implemented in this release. Any future adapter remains blocked until its authentication, replay protection, durable spend controls, bounded inputs, logging policy, and approval checks are proved.

## Knowledge and retrieval

Use the smallest approved corpus. Reviewed solution and action memory stores durable conclusions; manifest-bound retrieval supplies task context; a structural index remains generated evidence. Do not treat a configured connector, similarity score, graph edge, or retrieved snippet as permission to write or as verified truth.

## External action

Git push, deployment, knowledge-system writeback, provider calls, production promotion, and destructive operations require a named approval, target/schema proof, a rollback or recovery path, and post-action verification. The public dashboard cannot perform these actions.

## Reporting a vulnerability

Use the process in [SECURITY.md](../SECURITY.md). Do not put sensitive findings in public issues.
