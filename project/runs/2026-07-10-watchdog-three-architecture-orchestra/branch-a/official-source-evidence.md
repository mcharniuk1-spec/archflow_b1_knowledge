# Branch A Official Source Evidence

Status: reference checked on 2026-07-10; documentation only, with no provider or deployment action.

## OpenRouter

- [Models API](https://openrouter.ai/docs/guides/overview/models) documents that model metadata includes canonical slugs, supported parameters, and pricing fields. Branch A therefore requires activation-time model selection rather than treating a checked-in candidate ID as current.
- [API reference](https://openrouter.ai/docs/api/reference/overview) documents normalized usage data and generation statistics. Branch A requires response usage/cost capture and a ledger before provider-backed output can cross an external-action boundary.
- [Limits reference](https://openrouter.ai/docs/api/reference/limits) documents key-level credit limits and usage fields. Branch A therefore keeps an explicit hard-stop and observer review requirement rather than inferring available budget.

## Railway

- [Railway healthchecks](https://docs.railway.com/deployments/healthchecks) documents that traffic is switched after a configured endpoint returns HTTP 200 during deployment, and that this check is not continuous monitoring. Branch A therefore treats a health response as deployment-time evidence only.
- [Railway variables](https://docs.railway.com/variables) documents staged variable changes and deployment application. Branch A therefore keeps secrets in platform configuration and does not record values in the public repository.
- [Railway build and deploy](https://docs.railway.com/build-deploy) documents distinct service, cron, and function primitives. Branch A therefore requires an explicit service/runtime design before any always-online or worker claim.

## Interpretation

These sources support gating and verification requirements. They do not prove an active ArchFlow provider account, selected model, remaining budget, Railway project, deployed endpoint, or continuous availability.
