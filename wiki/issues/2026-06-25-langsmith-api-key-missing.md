# Issue - LangSmith API Key Missing

Date: 2026-06-25
Status: open

## Issue

LangSmith tracing is configured, but the API key is not present.

## Impact

LangGraph, CrewAI, or LlamaIndex runtime traces cannot be sent to LangSmith yet.

## Resolution

Add the real key to:

`project/.env.langsmith.local`

Do not commit the key.

