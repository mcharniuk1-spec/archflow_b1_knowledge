---
title: API retry note
version: 1.2
---

When the service returns HTTP 429, use the `retry_after` value.

```python
def retry_after(response):
    return int(response.headers["retry_after"])
```
