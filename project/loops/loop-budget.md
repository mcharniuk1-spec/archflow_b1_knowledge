# Loop Budget

The public default is provider-disabled and external-write-disabled.

| Resource | Default cap | Rule |
|---|---:|---|
| Revision loops | 2 | Stop after the second repair route. |
| Item attempts | 3 | Stop the item after three failed attempts. |
| Parallel branches | 3 | Use only for independent, file-safe work. |
| Provider spend | 0 | A provider needs separate adapter, source, budget, and authority approval. |
| External writes | 0 | One exact approved action requires rollback or idempotency and readback. |

Pause when a cap would be exceeded, a provider or persistent service is requested, a broad corpus is proposed, or new information changes the source or authority boundary. Record the gap and next safe action instead of silently broadening the loop.
