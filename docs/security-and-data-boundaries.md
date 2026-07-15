# Security and Data Boundaries

## Public repository

Only public-safe contracts, generated indexes, sanitized reports, documentation, and example configuration belong here. Do not commit credentials, tokens, private URLs, account identifiers, device paths, raw transcripts, customer documents, browser logs, model traces, or private corpus content.

## Browser

The dashboard stores drafts and packet state in browser storage. Treat that data as local to the browser profile, not as durable operational memory. Downloaded review bundles still need human review before they enter a repository or another system.

## Providers and APIs

Provider keys belong in server-side or locally ignored environment configuration, never static JavaScript, browser inputs, Markdown, catalog data, or Git. A displayed model route is a preference, not permission. Provider execution remains blocked until authentication, replay protection, durable spend controls, bounded inputs, logging policy, and approval checks are proved.

## Knowledge and retrieval

Use the smallest approved corpus. WikiLLM stores reviewed durable conclusions; LlamaIndex retrieves bounded context; Graphify is generated structure; Nexus requires live-tool discovery and current runtime proof. Do not treat configured connectors, embedding scores, or retrieval snippets as permission to write or as verified truth.

## External action

Git push, deployment, Notion/Nexus writeback, provider calls, production promotion, and destructive operations require a named approval, target/schema proof, a rollback or recovery path, and post-action verification. The public dashboard cannot perform these actions.

## Reporting a vulnerability

Use the process in [SECURITY.md](../SECURITY.md). Do not put sensitive findings in public issues.
