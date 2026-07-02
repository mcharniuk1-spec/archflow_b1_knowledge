# Jarvis API Service

Provider-disabled FastAPI contract for the ArchFlow dashboard MVP.

Current state:

- `MODEL_PROVIDER=none` is the default.
- OpenRouter is server-side only and disabled until owner approval, server-side secrets, fresh pricing, ledger proof, and budget guard are live.
- CrewAI Level 3 is represented only as `proof_passed_not_default_runtime`.
- Browser requests create review packets; they do not write Git, Notion, WikiLLM, Telegram, or deployment state.

Run locally after installing dependencies in an approved environment:

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8787
```

Required endpoints are implemented in `app.py`.
