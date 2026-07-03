#!/usr/bin/env python3
"""Smoke-test the provider-disabled Jarvis API contract in-process."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from fastapi.testclient import TestClient


REPO_ROOT = Path(__file__).resolve().parents[2]
SERVICE_ROOT = REPO_ROOT / "services" / "jarvis-api"


def main() -> int:
    sys.path.insert(0, str(SERVICE_ROOT))
    from app import app  # pylint: disable=import-outside-toplevel

    client = TestClient(app)
    checks = [
        ("GET", "/health", None),
        ("POST", "/api/chat", {"request": "test", "architecture": "service"}),
        ("POST", "/api/chat", {"request": "test", "architecture": "control"}),
        ("GET", "/api/config/roles", None),
        ("POST", "/api/config/roles/update", {"roles": []}),
        ("GET", "/api/lanes/prd-icp", None),
        ("POST", "/api/lanes/prd-icp", {"request": "x", "architecture": "service"}),
        ("GET", "/api/lanes/agent-orchestra", None),
        ("POST", "/api/lanes/agent-orchestra", {"request": "x", "architecture": "control"}),
        ("GET", "/api/reports/daily-form", None),
        ("GET", "/api/reports/weekly-form", None),
        ("GET", "/api/reports/whole-block", None),
        ("POST", "/api/test-runs/meeting-prd", {"request": "x"}),
        ("POST", "/api/test-runs/meeting-prd", {"request": "x", "owner_approval": True}),
        ("POST", "/api/voice/transcribe", {"transcript": "x"}),
        ("POST", "/api/voice/chat", {"transcript": "x"}),
        ("POST", "/api/voice/tts", {"transcript": "x"}),
    ]

    results: list[dict[str, object]] = []
    failures: list[str] = []
    for method, path, body in checks:
        request = getattr(client, method.lower())
        response = request(path, json=body) if body is not None else request(path)
        try:
            payload = response.json()
        except json.JSONDecodeError:
            payload = {}
        result = {
            "method": method,
            "path": path,
            "status_code": response.status_code,
            "kind": payload.get("kind"),
            "status": payload.get("status"),
            "provider_calls": payload.get("runtime", {}).get("provider_calls"),
            "writeback": payload.get("runtime", {}).get("external_writeback"),
        }
        results.append(result)
        if response.status_code != 200:
            failures.append(f"{method} {path}: status {response.status_code}")
        if payload.get("runtime", {}).get("provider_calls") != 0:
            failures.append(f"{method} {path}: provider calls not zero")
        if payload.get("runtime", {}).get("external_writeback") != 0:
            failures.append(f"{method} {path}: writeback not zero")

    if failures:
        print("jarvis_api_contract_smoke=failed")
        print(json.dumps(results, ensure_ascii=True, indent=2))
        print("failures=" + "; ".join(failures))
        return 1

    print(
        "jarvis_api_contract_smoke=ok "
        f"endpoints={len(results)} provider_calls=0 writeback=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
