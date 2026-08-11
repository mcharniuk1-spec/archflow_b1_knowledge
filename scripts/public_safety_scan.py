#!/usr/bin/env python3
"""Value-free public repository safety scan.

The scanner evaluates publishable Git files (tracked files plus non-ignored
untracked files) and reports only category counts. It never prints a matched
value. Repository-specific identities can be supplied through an ignored,
untracked denylist instead of being embedded in this public source file.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import unicodedata
import zlib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
TEXT_FREE_SUFFIXES = {
    ".avif",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".mov",
    ".mp3",
    ".mp4",
    ".otf",
    ".ttf",
    ".webp",
    ".woff",
    ".woff2",
}
OPAQUE_DOCUMENT_SUFFIXES = {".doc", ".docm", ".docx", ".pdf", ".ppt", ".pptm", ".pptx", ".xls", ".xlsm", ".xlsx"}
OPAQUE_ARCHIVE_SUFFIXES = {".7z", ".gz", ".rar", ".tar", ".tgz", ".zip"}
PLACEHOLDER_VALUES = {
    "change-me",
    "change_me",
    "empty",
    "example",
    "not-set",
    "not_set",
    "replace-me",
    "replace_me",
    "unset",
}


@dataclass(frozen=True)
class Rule:
    category: str
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class Finding:
    category: str
    path: Path


class ScanConfigurationError(ValueError):
    """Raised for an unsafe or unusable local scanner configuration."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Git worktree to scan (defaults to this repository).",
    )
    parser.add_argument(
        "--denylist",
        type=Path,
        help="Optional newline-delimited literal denylist; it must be outside the worktree or both ignored and untracked.",
    )
    return parser.parse_args(argv)


def run_git(root: Path, args: list[str], *, check: bool = False) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        check=check,
    )


def git_files(root: Path) -> list[Path]:
    try:
        result = run_git(
            root,
            ["ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ScanConfigurationError("The scan root is not an available Git worktree.") from exc

    paths: list[Path] = []
    for raw_path in result.stdout.split(b"\0"):
        if raw_path:
            paths.append(root / os.fsdecode(raw_path))
    return paths


def path_is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def load_caller_denylist(root: Path, denylist: Path | None) -> tuple[str, ...]:
    if denylist is None:
        return ()

    supplied = denylist.expanduser()
    if supplied.is_symlink():
        raise ScanConfigurationError("The caller denylist is missing or is not a regular file.")
    try:
        candidate = supplied.resolve()
        is_file = candidate.is_file()
        size = candidate.stat().st_size if is_file else 0
    except OSError as exc:
        raise ScanConfigurationError("The caller denylist is missing or is not a regular file.") from exc
    if not is_file:
        raise ScanConfigurationError("The caller denylist is missing or is not a regular file.")
    if size > 262_144:
        raise ScanConfigurationError("The caller denylist exceeds the bounded size limit.")

    if path_is_within(candidate, root):
        relative = candidate.relative_to(root).as_posix()
        tracked = run_git(root, ["ls-files", "--error-unmatch", "--", relative]).returncode == 0
        ignored = run_git(root, ["check-ignore", "-q", "--", relative]).returncode == 0
        if tracked or not ignored:
            raise ScanConfigurationError("A worktree-local caller denylist must be ignored and untracked.")

    try:
        lines = candidate.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ScanConfigurationError("The caller denylist could not be read as UTF-8 text.") from exc

    values: list[str] = []
    for line in lines:
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        if len(value) < 3:
            raise ScanConfigurationError("Caller denylist literals must contain at least three characters.")
        values.append(value)
    if len(values) > 500:
        raise ScanConfigurationError("The caller denylist exceeds the bounded entry limit.")
    return tuple(dict.fromkeys(values))


def compile_rules(caller_values: Iterable[str]) -> list[Rule]:
    definitions = [
        (
            "credential.github_token",
            r"(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9_]{20,}",
            0,
        ),
        (
            "credential.openai_key",
            r"(?<![A-Za-z0-9_])sk-(?:proj-)?[A-Za-z0-9_-]{20,}",
            0,
        ),
        (
            "credential.langsmith_key",
            r"(?<![A-Za-z0-9_])ls(?:v2|__)[A-Za-z0-9_.-]{20,}",
            0,
        ),
        (
            "credential.slack_token",
            r"(?<![A-Za-z0-9_])xox[baprs]-[A-Za-z0-9-]{20,}",
            0,
        ),
        (
            "credential.aws_access_key",
            r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])",
            0,
        ),
        (
            "credential.jwt",
            r"(?<![A-Za-z0-9_-])eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])",
            0,
        ),
        (
            "credential.private_key_block",
            r"-----BEGIN (?:EC |OPENSSH |RSA )?PRIVATE KEY-----",
            0,
        ),
        (
            "credential.connection_uri",
            r"\b(?:mongodb(?:\+srv)?|mysql|postgres(?:ql)?|redis)://[^/\s:@]+:[^@\s/]+@",
            re.IGNORECASE,
        ),
        (
            "credential.nonempty_assignment",
            r"(?m)^[ \t]*(?:export[ \t]+)?[A-Z0-9_]*(?:API_KEY|TOKEN|PASSWORD|SECRET|PRIVATE_KEY|CLIENT_SECRET|COOKIE)[A-Z0-9_]*[ \t]*=[ \t]*(?![ \t]*(?:$|#|<|\$\{|CHANGE[_-]?ME|REPLACE[_-]?ME|EXAMPLE|EMPTY|UNSET))['\"]?[^'\"\s#]{4,}",
            0,
        ),
        (
            "credential.structured_assignment",
            r"(?m)^[ \t-]*['\"]?(?:access[_-]?token|api[_-]?key|authorization|client[_-]?secret|cookie|password|private[_-]?key|refresh[_-]?token|secret|token)['\"]?[ \t]*:[ \t]*(?![ \t]*(?:$|#|<|\$\{|CHANGE[_-]?ME|REPLACE[_-]?ME|EXAMPLE|EMPTY|UNSET))['\"]?[^'\"\s#]{4,}",
            re.IGNORECASE,
        ),
        (
            "identity_input.nonempty_assignment",
            r"(?m)^[ \t]*(?:export[ \t]+)?[A-Z0-9_]*(?:ADMIN_EMAILS?|GOOGLE_SUBJECTS?|ALLOWED_USERS?|USER_IDS?|ACCOUNT_IDS?|WORKSPACE_IDS?|TENANT_IDS?|ORGANIZATION_IDS?|DEPLOYMENT_IDS?)[A-Z0-9_]*[ \t]*=[ \t]*(?![ \t]*(?:$|#|<|\$\{|CHANGE[_-]?ME|REPLACE[_-]?ME|EXAMPLE|EMPTY|UNSET))['\"]?[^'\"\s#]{2,}",
            0,
        ),
        (
            "identity_input.structured_assignment",
            r"(?m)^[ \t-]*['\"]?(?:account[_-]?id|admin[_-]?emails?|deployment[_-]?id|email(?:[_-]?address)?|google[_-]?subjects?|organization[_-]?id|owner[_-]?email|subject[_-]?id|tenant[_-]?id|user[_-]?(?:email|id)|workspace[_-]?id)['\"]?[ \t]*:[ \t]*(?![ \t]*(?:$|#|<|\$\{|CHANGE[_-]?ME|REPLACE[_-]?ME|EXAMPLE|EMPTY|UNSET))['\"]?[^'\"\s#]{2,}",
            re.IGNORECASE,
        ),
        (
            "email.address",
            r"(?<![A-Za-z0-9.!#$%&'*+/=?^_`{|}~-])[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+(?![A-Za-z0-9-])",
            0,
        ),
        (
            "private_url.local_scheme",
            r"\b(?:collection|file|notion|obsidian|user|view)://[^\s<>\"']+",
            re.IGNORECASE,
        ),
        (
            "private_url.private_host",
            r"\bhttps?://(?:[^/\s:@]+:[^@\s/]+@|(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2}|[^/\s.:]+\.(?:corp|home|internal|lan|local))(?::\d{1,5})?(?:[/\s]|$))",
            re.IGNORECASE,
        ),
        (
            "private_url.private_workspace",
            r"\bhttps?://app\.notion\.com/(?!robots\.txt(?:\b|/))[^\s<>\"']+",
            re.IGNORECASE,
        ),
        (
            "local_path.posix_user_home",
            r"(?<![A-Za-z0-9])/(?:Users|home)/[^/\s\"'<>]+(?:/[^\s\"'<>]*)?",
            0,
        ),
        (
            "local_path.private_tmp",
            r"(?<![A-Za-z0-9])/private/(?:tmp|var)/[^\s\"'<>]*",
            0,
        ),
        (
            "local_path.windows_user_home",
            r"(?<![A-Za-z0-9])[A-Za-z]:\\Users\\[^\\\s\"'<>]+(?:\\[^\s\"'<>]*)?",
            0,
        ),
        (
            "local_path.shell_user_folder",
            r"(?:^|[\s(\"'=])~/(?:Desktop|Documents|Downloads|Library)(?:/[^\s\"'<>]*)?",
            re.MULTILINE,
        ),
        (
            "metadata.operational_uuid",
            r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b",
            0,
        ),
        (
            "persona_pattern.explicit_declaration",
            r"(?m)^[ \t]*(?:agent[_ -]?alias|human[_ -]?name|persona(?:[_ -]?name)?)[ \t]*[:=][ \t]*['\"]?[A-Za-z][A-Za-z -]{1,}",
            re.IGNORECASE,
        ),
    ]
    rules = [Rule(category, re.compile(pattern, flags)) for category, pattern, flags in definitions]
    rules.extend(
        Rule("caller_denylist.literal", re.compile(re.escape(value), re.IGNORECASE))
        for value in caller_values
    )
    return rules


def blocked_path(path: Path, root: Path) -> str | None:
    relative = path.relative_to(root).as_posix()
    parts = path.relative_to(root).parts
    base = path.name
    lower_base = base.lower()

    if base == ".DS_Store" or lower_base in {"desktop.ini", "thumbs.db"} or base.startswith("._"):
        return "metadata.os_artifact"
    if "__pycache__" in parts or path.suffix.lower() in {".pyc", ".pyo"}:
        return "metadata.runtime_cache"
    if any(part in {".terraform", ".vercel"} for part in parts):
        return "metadata.deployment_state"
    if relative.endswith(".idea/workspace.xml"):
        return "metadata.editor_state"
    if base in {".env.example", ".env.sample", ".env.template"}:
        return None
    if base == ".env" or base.startswith(".env."):
        return "credential.env_file"
    if any(part == "local" for part in parts) and parts[:2] == ("project", "local"):
        return "metadata.local_runtime"
    if any(part == "raw" for part in parts):
        return "metadata.raw_source"
    if any(part == "private" for part in parts):
        return "metadata.private_folder"
    if any(part == "secrets" for part in parts):
        return "credential.secrets_folder"
    if path.suffix.lower() in OPAQUE_DOCUMENT_SUFFIXES:
        return "metadata.opaque_document"
    if path.suffix.lower() in OPAQUE_ARCHIVE_SUFFIXES:
        return "metadata.opaque_archive"
    return None


def bounded_decompress(data: bytes, limit: int = 1_048_576) -> bytes:
    decoder = zlib.decompressobj()
    output = decoder.decompress(data, limit + 1)
    if len(output) > limit or decoder.unconsumed_tail:
        raise ValueError("compressed metadata exceeds limit")
    return output


def png_metadata(path: Path) -> tuple[str, list[str]]:
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "", ["metadata.malformed_png"]

    cursor = 8
    text_parts: list[str] = []
    categories: list[str] = []
    while cursor + 12 <= len(data):
        length = int.from_bytes(data[cursor : cursor + 4], "big")
        chunk_type = data[cursor + 4 : cursor + 8]
        payload_start = cursor + 8
        payload_end = payload_start + length
        if length > 16_777_216 or payload_end + 4 > len(data):
            categories.append("metadata.malformed_png")
            break
        payload = data[payload_start:payload_end]
        if chunk_type in {b"tEXt", b"iTXt", b"zTXt"}:
            categories.append("metadata.image_text_chunk")
            try:
                if chunk_type == b"tEXt":
                    decoded = payload.decode("utf-8", errors="replace")
                elif chunk_type == b"zTXt":
                    _, compressed = payload.split(b"\0", 1)
                    decoded = bounded_decompress(compressed[1:]).decode("utf-8", errors="replace")
                else:
                    fields = payload.split(b"\0", 5)
                    if len(fields) < 6:
                        raise ValueError("malformed iTXt")
                    compressed_flag = fields[1]
                    body = fields[5]
                    if compressed_flag == b"\x01":
                        body = bounded_decompress(body)
                    decoded = body.decode("utf-8", errors="replace")
                text_parts.append(decoded)
            except (ValueError, zlib.error):
                categories.append("metadata.malformed_png_text")
        cursor = payload_end + 4
        if chunk_type == b"IEND":
            break
    return "\n".join(text_parts), categories


def binary_metadata_categories(path: Path) -> list[str]:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        with path.open("rb") as handle:
            data = handle.read(4_194_304)
        return ["metadata.image_exif"] if b"Exif\x00\x00" in data or b"http://ns.adobe.com/xap/1.0/" in data else []
    if suffix == ".webp":
        with path.open("rb") as handle:
            data = handle.read(4_194_304)
        return ["metadata.image_exif"] if b"EXIF" in data or b"XMP " in data else []
    return []


def read_publishable_text(path: Path) -> tuple[str, list[str]]:
    if path.is_symlink():
        target = os.readlink(path)
        category = "metadata.external_symlink" if Path(target).is_absolute() or ".." in Path(target).parts else ""
        return target, [category] if category else []

    suffix = path.suffix.lower()
    if suffix == ".png":
        try:
            return png_metadata(path)
        except OSError:
            return "", ["metadata.unreadable_file"]
    if suffix in TEXT_FREE_SUFFIXES:
        try:
            return "", binary_metadata_categories(path)
        except OSError:
            return "", ["metadata.unreadable_file"]

    try:
        return path.read_text(encoding="utf-8"), []
    except UnicodeDecodeError:
        return "", ["metadata.opaque_binary"]
    except OSError:
        return "", ["metadata.unreadable_file"]


def normalized_key(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower()).strip("_")


def is_concrete_scalar(value: Any) -> bool:
    if isinstance(value, bool) or value is None:
        return False
    if isinstance(value, (int, float)):
        return True
    if not isinstance(value, str):
        return False
    stripped = value.strip().strip("'\"")
    if not stripped:
        return False
    lowered = stripped.lower()
    if lowered in PLACEHOLDER_VALUES or stripped.startswith("${") or (stripped.startswith("<") and stripped.endswith(">")):
        return False
    return True


def has_concrete_value(value: Any) -> bool:
    if isinstance(value, (list, tuple, set)):
        return any(is_concrete_scalar(item) for item in value)
    return is_concrete_scalar(value)


def functional_call_name(role_id: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in re.split(r"[_-]+", role_id) if part)


def structured_categories(path: Path, text: str) -> set[str]:
    if path.suffix.lower() != ".json" or not text.strip():
        return set()
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        return set()

    credential_keys = {
        "access_token",
        "api_key",
        "apikey",
        "authorization",
        "client_secret",
        "cookie",
        "password",
        "private_key",
        "refresh_token",
        "secret",
        "token",
    }
    identity_keys = {
        "account_id",
        "admin_email",
        "admin_emails",
        "deployment_id",
        "email",
        "email_address",
        "google_subject",
        "google_subjects",
        "organization_id",
        "owner_email",
        "subject_id",
        "tenant_id",
        "user_email",
        "user_id",
        "workspace_id",
    }
    persona_keys = {"agent_alias", "human_name", "persona", "persona_name"}
    categories: set[str] = set()

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            normalized = {normalized_key(key): value for key, value in node.items()}
            for key, value in normalized.items():
                if key in credential_keys and has_concrete_value(value):
                    categories.add("credential.structured_value")
                if key in identity_keys and has_concrete_value(value):
                    categories.add("identity_input.structured_value")
                if key in persona_keys and has_concrete_value(value):
                    categories.add("persona_pattern.explicit_declaration")

            call_name = normalized.get("call_name")
            role_id = normalized.get("role_id", normalized.get("id"))
            if is_concrete_scalar(call_name):
                if not isinstance(role_id, str) or not re.fullmatch(r"[a-z][a-z0-9_-]*", role_id):
                    categories.add("persona_pattern.unbound_call_name")
                elif call_name != functional_call_name(role_id):
                    categories.add("persona_pattern.call_name_mismatch")

            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(document)
    return categories


def python_source_categories(path: Path, text: str) -> set[str]:
    """Detect concrete Python literals without treating safe expressions as secrets."""

    if path.suffix.lower() != ".py":
        return set()
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return {"metadata.malformed_python"}

    credential_parts = {
        "api_key",
        "apikey",
        "client_secret",
        "cookie",
        "password",
        "private_key",
        "secret",
        "token",
    }
    identity_parts = {
        "account_id",
        "admin_email",
        "admin_emails",
        "deployment_id",
        "email",
        "email_address",
        "google_subject",
        "google_subjects",
        "organization_id",
        "subject_id",
        "tenant_id",
        "user_email",
        "user_id",
        "workspace_id",
    }
    safe_name_parts = {"bytes", "clock", "endpoint", "field", "issued", "max", "min", "name", "pattern", "regex", "session", "skew", "suffix", "transaction", "ttl", "url", "window"}

    def key_kind(raw: str) -> str | None:
        key = normalized_key(raw)
        segments = set(key.split("_"))
        if key in identity_parts:
            return "identity"
        if key in credential_parts or any(part in key for part in ("api_key", "client_secret", "private_key")):
            if not segments.intersection(safe_name_parts):
                return "credential"
        if "token" in segments or "password" in segments or "secret" in segments or "cookie" in segments:
            if not segments.intersection(safe_name_parts):
                return "credential"
        return None

    def concrete_literal(node: ast.AST) -> bool:
        if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
            return False
        value = node.value.strip().strip("'\"")
        if not value or value.startswith(("${", "<")):
            return False
        lowered = value.lower()
        if lowered in PLACEHOLDER_VALUES or lowered.startswith(("example", "fixture", "synthetic", "test-", "test_")):
            return False
        return len(value) >= 4

    categories: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name) and concrete_literal(value):
                    kind = key_kind(target.id)
                    if kind == "credential":
                        categories.add("credential.nonempty_assignment")
                    elif kind == "identity":
                        categories.add("identity_input.nonempty_assignment")
        if isinstance(node, ast.Dict):
            for key_node, value_node in zip(node.keys, node.values):
                if not isinstance(key_node, ast.Constant) or not isinstance(key_node.value, str):
                    continue
                if not concrete_literal(value_node):
                    continue
                kind = key_kind(key_node.value)
                if kind == "credential":
                    categories.add("credential.structured_assignment")
                elif kind == "identity":
                    categories.add("identity_input.structured_assignment")
    return categories


def yaml_persona_categories(path: Path, text: str) -> set[str]:
    if path.suffix.lower() not in {".yaml", ".yml"}:
        return set()

    field_pattern = re.compile(
        r"^(?P<prefix>[ \t]*(?:-[ \t]*)?)(?P<key>id|role_id|call_name)[ \t]*:[ \t]*(?P<value>[^#\r\n]+)$"
    )
    contexts: dict[int, dict[str, str]] = {}
    categories: set[str] = set()
    for line in text.splitlines():
        match = field_pattern.match(line)
        if not match:
            continue
        indent = len(match.group("prefix").expandtabs(2))
        for existing_indent in list(contexts):
            if existing_indent > indent:
                del contexts[existing_indent]
        context = contexts.setdefault(indent, {})
        key = match.group("key")
        value = match.group("value").strip().strip("'\"")
        context[key] = value
        if key != "call_name" or not is_concrete_scalar(value):
            continue
        role_id = context.get("role_id", context.get("id"))
        if role_id is None or re.fullmatch(r"[a-z][a-z0-9_-]*", role_id) is None:
            categories.add("persona_pattern.unbound_call_name")
        elif value != functional_call_name(role_id):
            categories.add("persona_pattern.call_name_mismatch")
    return categories


def contains_non_english_letter(text: str) -> bool:
    for character in text:
        if unicodedata.category(character).startswith("L") and not (
            "A" <= character <= "Z" or "a" <= character <= "z"
        ):
            return True
    return False


def scan(root: Path, rules: list[Rule]) -> list[Finding]:
    findings: list[Finding] = []
    for path in git_files(root):
        if not path.exists() and not path.is_symlink():
            continue
        reason = blocked_path(path, root)
        if reason:
            findings.append(Finding(reason, path))
            continue
        if not path.is_file() and not path.is_symlink():
            continue

        relative = path.relative_to(root).as_posix()
        for rule in rules:
            if rule.pattern.search(relative):
                findings.append(Finding(rule.category, path))
        if contains_non_english_letter(relative):
            findings.append(Finding("non_english.letter", path))

        text, direct_categories = read_publishable_text(path)
        findings.extend(Finding(category, path) for category in set(filter(None, direct_categories)))
        if text:
            for rule in rules:
                if path.suffix.lower() == ".py" and rule.category in {
                    "credential.nonempty_assignment",
                    "credential.structured_assignment",
                    "identity_input.nonempty_assignment",
                    "identity_input.structured_assignment",
                }:
                    continue
                if rule.pattern.search(text):
                    findings.append(Finding(rule.category, path))
            if contains_non_english_letter(text):
                findings.append(Finding("non_english.letter", path))
            findings.extend(Finding(category, path) for category in structured_categories(path, text))
            findings.extend(Finding(category, path) for category in python_source_categories(path, text))
            findings.extend(Finding(category, path) for category in yaml_persona_categories(path, text))
    return findings


def render_findings(findings: list[Finding]) -> str:
    counts = Counter(finding.category for finding in findings)
    file_counts: dict[str, int] = {}
    for category in counts:
        file_counts[category] = len({finding.path for finding in findings if finding.category == category})
    lines = ["Public safety scan failed."]
    for category in sorted(counts):
        lines.append(f"category={category} files={file_counts[category]}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.expanduser().resolve()
    try:
        caller_values = load_caller_denylist(root, args.denylist)
        findings = scan(root, compile_rules(caller_values))
    except ScanConfigurationError as exc:
        print(f"Public safety scan configuration failed: {exc}", file=sys.stderr)
        return 2

    if findings:
        print(render_findings(findings), file=sys.stderr)
        return 1

    print("Public safety scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
