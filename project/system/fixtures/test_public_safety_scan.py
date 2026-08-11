#!/usr/bin/env python3
"""Focused clean/negative tests for the value-free public safety scanner."""

from __future__ import annotations

import json
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCANNER = ROOT / "scripts" / "public_safety_scan.py"


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def init_repo(root: Path) -> None:
    result = run(["git", "init", "--quiet"], root)
    if result.returncode != 0:
        raise AssertionError("temporary Git initialization failed")


def write_png(path: Path, text_payload: str | None = None) -> None:
    def chunk(kind: bytes, payload: bytes) -> bytes:
        body = kind + payload
        return struct.pack(">I", len(payload)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

    chunks = [
        chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 6, 0, 0, 0)),
        chunk(b"IDAT", zlib.compress(b"\x00\x00\x00\x00\x00")),
    ]
    if text_payload is not None:
        chunks.insert(1, chunk(b"tEXt", b"Comment\x00" + text_payload.encode("utf-8")))
    chunks.append(chunk(b"IEND", b""))
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + b"".join(chunks))


def invoke(root: Path, denylist: Path | None = None) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(SCANNER), "--root", str(root)]
    if denylist is not None:
        command.extend(["--denylist", str(denylist)])
    return run(command, root)


def assert_clean_case() -> None:
    with tempfile.TemporaryDirectory(prefix="archflow-scan-clean-") as temporary:
        root = Path(temporary)
        init_repo(root)
        (root / "README.md").write_text(
            "# Public tool\n\nA bounded workflow with a public https://example.com reference.\n",
            encoding="utf-8",
        )
        (root / "role.json").write_text(
            json.dumps({"id": "bounded_worker", "call_name": "BoundedWorker", "title": "Bounded Worker"}),
            encoding="utf-8",
        )
        (root / ".env.example").write_text("SERVICE_API_KEY=\nADMIN_EMAILS=\n", encoding="utf-8")
        (root / "config.py").write_text(
            "TOKEN_ENDPOINT = 'https://example.com/token'\n"
            "payload = {'client_secret': config.client_secret}\n"
            "fixture = {'client_secret': 'fixture-client-credential'}\n",
            encoding="utf-8",
        )
        write_png(root / "diagram.png")
        result = invoke(root)
        if result.returncode != 0 or result.stdout.strip() != "Public safety scan passed." or result.stderr:
            raise AssertionError("clean fixture did not pass")


def assert_negative_categories_and_value_free_output() -> None:
    with tempfile.TemporaryDirectory(prefix="archflow-scan-negative-") as temporary:
        root = Path(temporary)
        init_repo(root)
        credential = "sk-" + ("S" * 24)
        email = "synthetic.operator" + "@" + "private.invalid"
        local_path = "/" + "Users" + "/synthetic-operator/workspace"
        private_url = "user" + "://" + "synthetic-record"
        non_english = chr(0x0410)
        marker = "synthetic-sensitive-marker"

        (root / "credential.env").write_text("SERVICE_API_KEY=" + credential + "\n", encoding="utf-8")
        (root / "leaked.py").write_text("SERVICE_TOKEN = 'concrete-non-placeholder-value'\n", encoding="utf-8")
        (root / "identity.json").write_text(
            json.dumps({"user_id": "synthetic-user-001", "contact": email}),
            encoding="utf-8",
        )
        (root / "boundary.md").write_text(
            "Private route: " + private_url + "\nLocal source: " + local_path + "\nLetter: " + non_english + "\n" + marker,
            encoding="utf-8",
        )
        (root / "role.json").write_text(
            json.dumps({"role_id": "test_operator", "call_name": "SyntheticAlias"}),
            encoding="utf-8",
        )
        (root / "role.yaml").write_text(
            "roles:\n  - role_id: review_operator\n    call_name: SyntheticReviewer\n",
            encoding="utf-8",
        )
        (root / ".DS_Store").write_bytes(b"synthetic metadata")
        write_png(root / "annotated.png", "synthetic metadata")
        (root / ".gitignore").write_text(".scanner-denylist\n", encoding="utf-8")
        denylist = root / ".scanner-denylist"
        denylist.write_text(marker + "\n", encoding="utf-8")

        result = invoke(root, denylist)
        expected_categories = {
            "caller_denylist.literal",
            "credential.nonempty_assignment",
            "credential.openai_key",
            "email.address",
            "identity_input.structured_value",
            "local_path.posix_user_home",
            "metadata.image_text_chunk",
            "metadata.os_artifact",
            "non_english.letter",
            "persona_pattern.call_name_mismatch",
            "private_url.local_scheme",
        }
        output = result.stdout + result.stderr
        missing = [category for category in sorted(expected_categories) if f"category={category} " not in output]
        if result.returncode != 1 or missing:
            raise AssertionError("negative fixture missed required categories")
        forbidden_echoes = {credential, email, local_path, private_url, non_english, marker}
        if any(value in output for value in forbidden_echoes):
            raise AssertionError("scanner output disclosed a matched value")

        force_add = run(["git", "add", "-f", ".scanner-denylist"], root)
        if force_add.returncode != 0:
            raise AssertionError("temporary tracked-denylist setup failed")
        rejected = invoke(root, denylist)
        if rejected.returncode != 2 or "must be ignored and untracked" not in rejected.stderr:
            raise AssertionError("tracked caller denylist was not rejected")
        if marker in rejected.stdout + rejected.stderr:
            raise AssertionError("denylist configuration error disclosed a literal")


def main() -> int:
    assert_clean_case()
    assert_negative_categories_and_value_free_output()
    print("public safety scanner fixtures passed: clean=1 negative=1 denylist_boundary=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
