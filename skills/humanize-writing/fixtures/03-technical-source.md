---
title: API retry note
version: 1.2
---

Use the `retry_after` value when the service returns HTTP 429.

```python
def retry_after(response):
    return int(response.headers["retry_after"])
```
