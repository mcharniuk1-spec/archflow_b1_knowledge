#!/usr/bin/env python3
"""Smoke-test the provider-disabled Jarvis API contract in-process."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from fastapi.testclient import TestClient


REPO_ROOT = Path(__file__).resolve().parents[2]
SERVICE_ROOT = REPO_ROOT / "services" / "jarvis-api"


def main() -> int:
    os.environ["JARVIS_API_ALLOWED_ORIGIN"] = "http://127.0.0.1:8765"
    sys.path.insert(0, str(SERVICE_ROOT))
    from app import app  # pylint: disable=import-outside-toplevel

    client = TestClient(app)
    checks = [
        ("GET", "/health", None),
        ("GET", "/api/models", None),
        (
            "POST",
            "/api/chat",
            {
                "request": "test",
                "architecture": "service",
                "conversation": [{"role": "user", "source": "smoke", "text": "previous"}],
                "attachments": [
                    {
                        "id": "smoke-attachment",
                        "name": "sample.txt",
                        "mime_type": "text/plain",
                        "size": 24,
                        "transfer_mode": "text_excerpt",
                        "text_excerpt": "public smoke attachment",
                    }
                ],
            },
        ),
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

    guarded_env = {
        "MODEL_PROVIDER": "openrouter",
        "JARVIS_ENABLE_PROVIDER_CALLS": "true",
        "JARVIS_OWNER_TOKEN": "smoke-owner-token",
        "OPENROUTER_API_KEY": "smoke-provider-placeholder",
        "OPENROUTER_ALLOWED_MODELS": "qwen/qwen3.7-plus",
        "OPENROUTER_DAILY_BUDGET_USD": "5.00",
        "OPENROUTER_RUN_BUDGET_USD": "1.00",
        "OPENROUTER_RUN_HARD_STOP_USD": "1.00",
    }
    original_env = {name: os.environ.get(name) for name in guarded_env}
    try:
        os.environ.update(guarded_env)
        forged = client.post(
            "/api/chat",
            json={
                "request": "forged browser approval",
                "owner_approval": True,
                "provider_approval": True,
                "model_id": "qwen/qwen3.7-plus",
            },
        ).json()
        forged_result = forged.get("payload", {}).get("provider_result", {})
        if forged_result.get("provider_executed") is not False or forged_result.get("reason") != "owner_auth_required":
            failures.append("forged body approval bypassed or did not reach owner_auth_required")

        wrong_token = client.post(
            "/api/chat",
            headers={"Authorization": "Bearer wrong-token"},
            json={
                "request": "wrong token",
                "provider_approval": True,
                "model_id": "qwen/qwen3.7-plus",
            },
        ).json()
        wrong_result = wrong_token.get("payload", {}).get("provider_result", {})
        if wrong_result.get("provider_executed") is not False or wrong_result.get("reason") != "owner_auth_required":
            failures.append("wrong bearer token bypassed owner guard")

        no_call_approval = client.post(
            "/api/chat",
            headers={"Authorization": "Bearer smoke-owner-token"},
            json={
                "request": "valid owner but no call approval",
                "provider_approval": False,
                "model_id": "qwen/qwen3.7-plus",
            },
        ).json()
        no_call_result = no_call_approval.get("payload", {}).get("provider_result", {})
        if no_call_result.get("provider_executed") is not False or no_call_result.get("reason") != "per_request_provider_acknowledgement_required":
            failures.append("valid owner token bypassed per-request acknowledgement gate")

        complete_body = {
            "request": "otherwise complete provider request",
            "provider_approval": True,
            "model_id": "qwen/qwen3.7-plus",
        }
        complete_headers = {"Authorization": "Bearer smoke-owner-token"}
        first = client.post("/api/chat", headers=complete_headers, json=complete_body).json()
        second = client.post("/api/chat", headers=complete_headers, json=complete_body).json()
        for index, response in enumerate([first, second], start=1):
            result = response.get("payload", {}).get("provider_result", {})
            if result.get("provider_executed") is not False or result.get("reason") != "durable_nonce_and_spend_ledger_required":
                failures.append(f"durable execution-control blocker missing on replay probe {index}")

        bad_origin = client.post(
            "/api/chat",
            headers={"Origin": "https://untrusted.example"},
            json={"request": "origin probe"},
        )
        if bad_origin.status_code != 403 or bad_origin.json().get("detail") != "origin_not_allowed":
            failures.append(f"disallowed origin did not return 403: {bad_origin.status_code}")
    finally:
        for name, value in original_env.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value

    if failures:
        print("jarvis_api_contract_smoke=failed")
        print(json.dumps(results, ensure_ascii=True, indent=2))
        print("failures=" + "; ".join(failures))
        return 1

    print(
        "jarvis_api_contract_smoke=ok "
        f"endpoints={len(results)} owner_guard_cases=5 replay_blocked=1 cors_403=1 provider_calls=0 writeback=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
