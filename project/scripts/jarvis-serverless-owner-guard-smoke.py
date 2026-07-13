#!/usr/bin/env python3
"""Verify serverless owner/model gates and mandatory execution block."""

from __future__ import annotations

import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "api"))

import _jarvis_contract as contract  # noqa: E402


class FakeHandler:
    def __init__(self, authorization: str = "") -> None:
        self.headers = {"Authorization": authorization}


def main() -> int:
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
    original = {name: os.environ.get(name) for name in guarded_env}
    failures: list[str] = []
    try:
        os.environ.update(guarded_env)
        if contract.owner_authorized(FakeHandler("Bearer wrong")):
            failures.append("wrong token authorized")
        if not contract.owner_authorized(FakeHandler("Bearer smoke-owner-token")):
            failures.append("matching token rejected")

        ready, reason, _ = contract.provider_ready(
            {"_owner_authorized": False, "provider_approval": True, "model_id": "qwen/qwen3.7-plus"}
        )
        if ready or reason != "owner_auth_required":
            failures.append("forged approval did not stop at owner guard")

        ready, reason, _ = contract.provider_ready(
            {"_owner_authorized": True, "provider_approval": False, "model_id": "qwen/qwen3.7-plus"}
        )
        if ready or reason != "per_request_provider_acknowledgement_required":
            failures.append("per-request acknowledgement gate failed")

        ready, reason, _ = contract.provider_ready(
            {"_owner_authorized": True, "provider_approval": True, "model_id": "unapproved/example"}
        )
        if ready or reason != "model_not_in_server_allowlist":
            failures.append("model allowlist gate failed")

        complete = {"_owner_authorized": True, "provider_approval": True, "model_id": "qwen/qwen3.7-plus"}
        first = contract.provider_ready(complete)
        second = contract.provider_ready(complete)
        for index, (ready, reason, model) in enumerate([first, second], start=1):
            if ready or reason != "durable_nonce_and_spend_ledger_required" or model != "qwen/qwen3.7-plus":
                failures.append(f"mandatory durable-control block failed on probe {index}")

        catalog = contract.models_payload()
        if len(catalog.get("payload", {}).get("curated", [])) != 4:
            failures.append("curated catalog contract is incomplete")
    finally:
        for name, value in original.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value

    if failures:
        print("jarvis_serverless_owner_guard_smoke=failed failures=" + "; ".join(failures))
        return 1
    print("jarvis_serverless_owner_guard_smoke=ok gates=owner,acknowledgement,allowlist,durable-controls replay_blocked=1 provider_calls=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
