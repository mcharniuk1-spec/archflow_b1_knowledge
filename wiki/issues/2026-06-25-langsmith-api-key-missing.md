# Issue - LangSmith API Key Missing

Date: 2026-06-25
Status: closed

## Issue

LangSmith tracing was configured before the local API key was added.

## Impact

Resolved for smoke tracing. LangGraph, CrewAI, and LlamaIndex runtime traces still require those runtime packages to be installed and wired into a proof workflow.

## Resolution

The real key was added locally to:

`project/.env.langsmith.local`

Do not commit the key.

Verification:

- The local env file is ignored by Git.
- A sanitized LangSmith smoke trace was submitted.
