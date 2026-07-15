# Security Policy

## Supported public scope

This repository is a public-safe reference implementation. Static dashboard features, generated catalog data, and guarded API contracts are in scope for responsible reports. Hosted availability, provider activation, external writeback, and private integrations must not be inferred from the repository.

## Report privately

Do not file public issues for credentials, tokens, access-control bypasses, private-data exposure, or a way to trigger an external action. Contact the project owner through the private channel listed in the repository's hosting profile, with a minimal reproduction and no secret value.

## Safe disclosure expectations

- Do not test against third-party systems or data.
- Do not attempt provider spending, writeback, deployment, or destructive actions.
- Redact secrets and personal information.
- Allow time for verification and remediation before public disclosure.

The repository intentionally keeps external actions behind explicit approval gates. A configured-looking surface is not authorization.
