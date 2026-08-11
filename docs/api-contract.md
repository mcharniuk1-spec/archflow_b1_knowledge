# API And Packet Contract

Status: V3 browser handoff current; network actions fail closed

The public Knowledge Operator and Jarvis work without an API. They prepare a bounded packet in the current browser tab, and the dashboard consumes it once in the Communication Center. Packet content never enters the URL.

## Browser handoff

Session key: `archflow.public.v3.handoff`

```json
{
  "schema_version": "3.0",
  "kind": "archflow_public_handoff",
  "state": "review_required",
  "objective": "Prepare a source-linked onboarding architecture brief.",
  "decision": "Choose the smallest safe onboarding workflow.",
  "public_reference": "Public documentation",
  "allowed_evidence": "Approved public sources and reviewed summaries.",
  "exclusions": "Credentials, private URLs, customer material, raw transcripts, and local paths.",
  "requested_output": "A brief with facts, gaps, recommendation, and reviewer handoff.",
  "reviewer": "Independent reviewer",
  "constraints": "No provider call or external write. Stop when the source or authority boundary is unclear.",
  "created_at": "<ISO-8601 timestamp>"
}
```

Jarvis and the dashboard revalidate the version, kind, required fields, lengths, and public-safety patterns. The dashboard deletes the transit key after import and renders values through escaped text. Browser state is not an account, approval, checkpoint, shared database, or action receipt.

## Administrator session

The UI has no Admin/Guest switch and accepts no pasted owner token. Administrator access begins at:

- `GET /api/auth/google/start`;
- `GET /api/auth/google/callback`;
- `GET /api/auth/session`;
- `POST /api/auth/logout`.

The server uses Authorization Code, state, nonce, PKCE S256, verified Google ID tokens, a server-side subject or verified-email allowlist, a short-lived signed `__Host-archflow_admin` cookie, exact-origin checks, CSRF, expiry, and logout cookie clearing. Missing configuration fails closed. Public responses never return an identity, allowlist, credential value, or credential-presence signal. Stateless sessions cannot be individually revoked before expiry; changing `ARCHFLOW_AUTH_SESSION_EPOCH` or rotating the signing key invalidates all issued sessions, while individual revocation requires a server-side session store.

Authentication establishes identity only. It does not approve a provider call, spending, Git mutation, deployment, publication, or external writeback.

## Compatibility routes

The current serverless compatibility routes include `/api/chat`, `/api/lanes/prd-icp`, `/api/lanes/agent-orchestra`, and `/api/config/roles`. Their read-only `GET` projections are public. A `POST` is authenticated before its JSON body is read, and any authority comes from trusted server context rather than a body field. Provider execution remains disabled in the public release.

Any future effect request must include:

- case, run, and action IDs;
- authenticated actor and accountable owner;
- exact operation, target class, target, and data class;
- current requirement and decision versions;
- tool and permission scope;
- side effects, reversibility, rollback, and replay protection;
- deterministic preflight and postcondition;
- independent reviewer and target-specific approval;
- exact readback and result receipt.

Missing, stale, ambiguous, or body-supplied authority fails closed.

## Public readback

`/api/health` and `/api/models` may expose only stable public contract state. They must not report whether a key, identity, allowlist, model credential, or private integration exists. A model name in documentation is not runtime proof.
