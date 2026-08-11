#!/usr/bin/env python3
"""Deterministic abuse tests for the administrator authentication boundary."""

from __future__ import annotations

import ast
import importlib.util
import io
import json
import os
import sys
import urllib.parse
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from typing import Any, Callable, Iterator
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
API_ROOT = REPO_ROOT / "api"
sys.path.insert(0, str(API_ROOT))

import _auth_contract as auth  # noqa: E402
import _jarvis_contract as jarvis  # noqa: E402


FIXED_NOW = 2_000_000_000
AUTH_ENV_NAMES = (
    "ARCHFLOW_AUTH_ENABLED",
    "GOOGLE_OAUTH_CLIENT_ID",
    "GOOGLE_OAUTH_CLIENT_SECRET",
    "ARCHFLOW_AUTH_ORIGIN",
    "ARCHFLOW_AUTH_SECRET",
    "ARCHFLOW_ADMIN_GOOGLE_SUBJECTS",
    "ARCHFLOW_ADMIN_EMAILS",
    "ARCHFLOW_AUTH_SESSION_EPOCH",
    "ARCHFLOW_AUTH_SESSION_TTL_SECONDS",
)
BASE_AUTH_ENV = {
    "ARCHFLOW_AUTH_ENABLED": "true",
    "GOOGLE_OAUTH_CLIENT_ID": "fixture-client.apps.googleusercontent.com",
    "GOOGLE_OAUTH_CLIENT_SECRET": "fixture-client-credential",
    "ARCHFLOW_AUTH_ORIGIN": "https://console.example",
    "ARCHFLOW_AUTH_SECRET": "fixture-signing-material-at-least-32-bytes-long",
    "ARCHFLOW_ADMIN_GOOGLE_SUBJECTS": "fixture-subject",
    "ARCHFLOW_ADMIN_EMAILS": "",
    "ARCHFLOW_AUTH_SESSION_EPOCH": "fixture-epoch-1",
    "ARCHFLOW_AUTH_SESSION_TTL_SECONDS": "1800",
}


@contextmanager
def isolated_env(values: dict[str, str], names: tuple[str, ...] = AUTH_ENV_NAMES) -> Iterator[None]:
    original = {name: os.environ.get(name) for name in names}
    try:
        for name in names:
            os.environ.pop(name, None)
        os.environ.update(values)
        yield
    finally:
        for name, value in original.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value


class FakeHandler:
    def __init__(
        self,
        *,
        path: str = "/",
        headers: dict[str, str] | None = None,
        body: dict[str, Any] | None = None,
    ) -> None:
        raw = json.dumps(body or {}, ensure_ascii=True).encode("utf-8")
        self.path = path
        self.headers = dict(headers or {})
        if body is not None:
            self.headers["content-length"] = str(len(raw))
        self.rfile = io.BytesIO(raw)
        self.wfile = io.BytesIO()
        self.status: int | None = None
        self.response_headers: list[tuple[str, str]] = []
        self.route_calls: list[tuple[str, dict[str, Any], bool]] = []

    def send_response(self, status: int) -> None:
        self.status = status

    def send_header(self, name: str, value: str) -> None:
        self.response_headers.append((name, value))

    def end_headers(self) -> None:
        return

    def route(self, method: str, body: dict[str, Any]) -> dict[str, Any]:
        trusted = bool(getattr(getattr(body, "context", None), "authenticated_admin", False))
        self.route_calls.append((method, dict(body), trusted))
        return {"kind": "fixture", "runtime": {"external_effects": 0}}

    def json_body(self) -> dict[str, Any]:
        return json.loads(self.wfile.getvalue().decode("utf-8"))

    def header_values(self, name: str) -> list[str]:
        return [value for key, value in self.response_headers if key.lower() == name.lower()]


def cookie_pair(set_cookie: str) -> str:
    return set_cookie.split(";", 1)[0]


def cookie_value(set_cookie: str) -> str:
    return cookie_pair(set_cookie).split("=", 1)[1]


def tamper(token: str) -> str:
    encoded, signature = token.split(".", 1)
    replacement = "A" if signature[0] != "A" else "B"
    return f"{encoded}.{replacement}{signature[1:]}"


def expect_error(
    failures: list[str],
    label: str,
    error_type: type[BaseException],
    operation: Callable[[], Any],
) -> None:
    try:
        operation()
    except error_type:
        return
    except Exception as exc:  # noqa: BLE001
        failures.append(f"{label}: wrong error {type(exc).__name__}")
        return
    failures.append(f"{label}: accepted")


def claims_for(config: auth.AuthConfig, expected_nonce: str, **overrides: Any) -> dict[str, Any]:
    claims: dict[str, Any] = {
        "iss": "https://accounts.google.com",
        "aud": config.client_id,
        "azp": config.client_id,
        "nonce": expected_nonce,
        "iat": FIXED_NOW,
        "exp": FIXED_NOW + 300,
        "sub": "fixture-subject",
        "email": "fixture-user" + "@" + "gmail.com",
        "email_verified": True,
    }
    claims.update(overrides)
    return claims


def load_route(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    failures: list[str] = []

    with isolated_env({}):
        expect_error(failures, "disabled configuration", auth.AuthUnavailable, auth.load_auth_config)
    with isolated_env({**BASE_AUTH_ENV, "ARCHFLOW_AUTH_ENABLED": "false"}):
        expect_error(failures, "explicitly disabled configuration", auth.AuthUnavailable, auth.load_auth_config)
    with isolated_env({**BASE_AUTH_ENV, "ARCHFLOW_ADMIN_GOOGLE_SUBJECTS": ""}):
        expect_error(failures, "empty allowlist", auth.AuthUnavailable, auth.load_auth_config)
    with isolated_env({**BASE_AUTH_ENV, "ARCHFLOW_AUTH_ORIGIN": "http://console.example"}):
        expect_error(failures, "non-HTTPS origin", auth.AuthUnavailable, auth.load_auth_config)
    with isolated_env({**BASE_AUTH_ENV, "ARCHFLOW_AUTH_SECRET": "fixture-too-short"}):
        expect_error(failures, "short signing material", auth.AuthUnavailable, auth.load_auth_config)

    with isolated_env(BASE_AUTH_ENV):
        config = auth.load_auth_config()
        expect_error(
            failures,
            "unregistered return path",
            auth.InvalidAuthRequest,
            lambda: auth.build_authorization_start(config, "https://untrusted.example", now=FIXED_NOW),
        )
        start = auth.build_authorization_start(config, "dashboard", now=FIXED_NOW)
        parsed_url = urllib.parse.urlsplit(start.location)
        query = urllib.parse.parse_qs(parsed_url.query)
        required_query = {
            "response_type",
            "client_id",
            "redirect_uri",
            "scope",
            "state",
            "nonce",
            "code_challenge",
            "code_challenge_method",
            "access_type",
            "prompt",
        }
        if parsed_url.scheme != "https" or parsed_url.netloc != "accounts.google.com":
            failures.append("authorization endpoint is not the fixed Google HTTPS endpoint")
        if set(query) != required_query:
            failures.append("authorization query contract drifted")
        if query.get("response_type") != ["code"] or query.get("code_challenge_method") != ["S256"]:
            failures.append("authorization code or PKCE S256 missing")
        if query.get("scope") != ["openid email"] or "login_hint" in query:
            failures.append("OIDC scope or account-selection privacy contract failed")
        if query.get("redirect_uri") != [config.callback_uri]:
            failures.append("callback URI mismatch")
        for attribute in ("Path=/", "Secure", "HttpOnly", "SameSite=Lax"):
            if attribute not in start.transaction_cookie:
                failures.append(f"transaction cookie missing {attribute}")
        if "Domain=" in start.transaction_cookie or not start.transaction_cookie.startswith(auth.TRANSACTION_COOKIE + "="):
            failures.append("transaction cookie violates __Host boundary")

        transaction_token = cookie_value(start.transaction_cookie)
        transaction = auth.parse_transaction(config, transaction_token, now=FIXED_NOW)
        expected_challenge = auth._base64url_encode(  # noqa: SLF001
            auth.hashlib.sha256(transaction["verifier"].encode("ascii")).digest()
        )
        if query.get("state") != [transaction["state"]] or query.get("nonce") != [transaction["nonce"]]:
            failures.append("state or nonce not bound to signed transaction")
        if query.get("code_challenge") != [expected_challenge]:
            failures.append("PKCE challenge is not derived from verifier")
        expect_error(
            failures,
            "tampered transaction",
            auth.AuthenticationFailed,
            lambda: auth.parse_transaction(config, tamper(transaction_token), now=FIXED_NOW),
        )
        expect_error(
            failures,
            "expired transaction",
            auth.AuthenticationFailed,
            lambda: auth.parse_transaction(
                config,
                transaction_token,
                now=FIXED_NOW + auth.TRANSACTION_TTL_SECONDS,
            ),
        )

        exchange_calls: list[tuple[str, str]] = []

        def fake_exchange(received_config: auth.AuthConfig, code: str, verifier: str) -> str:
            if received_config != config:
                failures.append("token exchange received wrong config")
            exchange_calls.append((code, verifier))
            return "fixture-id-token"

        valid_claims = claims_for(config, transaction["nonce"])
        callback = auth.complete_google_callback(
            config,
            transaction_token,
            transaction["state"],
            "fixture-code",
            now=FIXED_NOW,
            exchange=fake_exchange,
            validator=lambda token, received: valid_claims,
        )
        if exchange_calls != [("fixture-code", transaction["verifier"])]:
            failures.append("authorization code exchange did not use signed PKCE verifier")
        if callback.location != "/project/dashboard/#communication":
            failures.append("dashboard return target is not fixed")
        if "max-age=1800" not in callback.session_cookie:
            failures.append("session cookie TTL mismatch")
        for attribute in ("Path=/", "Secure", "HttpOnly", "SameSite=Lax"):
            if attribute not in callback.session_cookie:
                failures.append(f"session cookie missing {attribute}")
        if "Domain=" in callback.session_cookie or not callback.session_cookie.startswith(auth.SESSION_COOKIE + "="):
            failures.append("session cookie violates __Host boundary")

        session_token = cookie_value(callback.session_cookie)
        session = auth.parse_session(config, session_token, now=FIXED_NOW)
        session_cookie_header = cookie_pair(callback.session_cookie)
        response = auth.session_response(session_cookie_header, now=FIXED_NOW)
        if set(response) != {"authenticated", "role", "csrf"}:
            failures.append("authenticated session response exposes extra fields")
        if response != {"authenticated": True, "role": "administrator", "csrf": session["csrf"]}:
            failures.append("authenticated session response contract failed")
        serialized_response = json.dumps(response).lower()
        for forbidden in ("email", "subject", "environment", "configured", "uid", "sid", "epoch"):
            if forbidden in serialized_response:
                failures.append(f"session response disclosed {forbidden}")
        if auth.session_response("", now=FIXED_NOW) != {"authenticated": False, "role": "public"}:
            failures.append("public session response contract failed")

        expect_error(
            failures,
            "tampered session",
            auth.AuthenticationFailed,
            lambda: auth.parse_session(config, tamper(session_token), now=FIXED_NOW),
        )
        expect_error(
            failures,
            "expired session",
            auth.AuthenticationFailed,
            lambda: auth.parse_session(config, session_token, now=FIXED_NOW + config.session_ttl_seconds),
        )
        expect_error(
            failures,
            "revoked session epoch",
            auth.AuthenticationFailed,
            lambda: auth.parse_session(replace(config, session_epoch="fixture-epoch-2"), session_token, now=FIXED_NOW),
        )

        wrong_state_exchange = mock.Mock(side_effect=AssertionError("state failure must precede exchange"))
        expect_error(
            failures,
            "state mismatch",
            auth.AuthenticationFailed,
            lambda: auth.complete_google_callback(
                config,
                transaction_token,
                "wrong-state",
                "fixture-code",
                now=FIXED_NOW,
                exchange=wrong_state_exchange,
                validator=lambda token, received: valid_claims,
            ),
        )
        if wrong_state_exchange.called:
            failures.append("state mismatch reached token exchange")

        invalid_claims = (
            ("nonce mismatch", {"nonce": "wrong"}),
            ("issuer mismatch", {"iss": "https://untrusted.example"}),
            ("audience mismatch", {"aud": "other-client"}),
            ("authorized-party mismatch", {"azp": "other-client"}),
            ("expired identity token", {"exp": FIXED_NOW}),
            ("future identity token", {"iat": FIXED_NOW + auth.TOKEN_CLOCK_SKEW_SECONDS + 1}),
            ("stale identity token", {"iat": FIXED_NOW - auth.TOKEN_ISSUED_AT_WINDOW_SECONDS - 1}),
            ("missing stable subject", {"sub": ""}),
        )
        for label, override in invalid_claims:
            candidate = claims_for(config, transaction["nonce"], **override)
            expect_error(
                failures,
                label,
                auth.AuthenticationFailed,
                lambda candidate=candidate: auth.complete_google_callback(
                    config,
                    transaction_token,
                    transaction["state"],
                    "fixture-code",
                    now=FIXED_NOW,
                    exchange=fake_exchange,
                    validator=lambda token, received, candidate=candidate: candidate,
                ),
            )

        unauthorized_claims = claims_for(config, transaction["nonce"], sub="unknown-subject")
        expect_error(
            failures,
            "subject allowlist mismatch",
            auth.AccessNotAuthorized,
            lambda: auth.complete_google_callback(
                config,
                transaction_token,
                transaction["state"],
                "fixture-code",
                now=FIXED_NOW,
                exchange=fake_exchange,
                validator=lambda token, received: unauthorized_claims,
            ),
        )

        missing = auth.authorize_admin_post("", config.origin, session["csrf"], now=FIXED_NOW)
        wrong_origin = auth.authorize_admin_post(session_cookie_header, "", session["csrf"], now=FIXED_NOW)
        foreign_origin = auth.authorize_admin_post(
            session_cookie_header,
            "https://untrusted.example",
            session["csrf"],
            now=FIXED_NOW,
        )
        wrong_csrf = auth.authorize_admin_post(session_cookie_header, config.origin, "wrong", now=FIXED_NOW)
        allowed = auth.authorize_admin_post(session_cookie_header, config.origin, session["csrf"], now=FIXED_NOW)
        if (missing.status, wrong_origin.status, foreign_origin.status, wrong_csrf.status, allowed.status) != (
            401,
            403,
            403,
            403,
            200,
        ) or not allowed.authorized:
            failures.append("POST session, Origin, or CSRF decision matrix failed")

        legacy_header = "Author" + "ization"
        legacy_value = "Bear" + "er fixture-static-token"
        legacy_credential_only = FakeHandler(
            headers={
                legacy_header: legacy_value,
                "Origin": config.origin,
                "X-ArchFlow-CSRF": session["csrf"],
            }
        )
        if auth.authorize_admin_handler(legacy_credential_only, now=FIXED_NOW).authorized:
            failures.append("legacy credential header authorized without session cookie")

        with mock.patch.object(auth.time, "time", return_value=FIXED_NOW):
            session_handler = FakeHandler(headers={"Cookie": session_cookie_header})
            auth.handle_session(session_handler)
            if session_handler.status != 200 or set(session_handler.json_body()) != {
                "authenticated",
                "role",
                "csrf",
            }:
                failures.append("session endpoint response failed")
            if "no-store" not in " ".join(session_handler.header_values("Cache-Control")):
                failures.append("session endpoint is cacheable")

            denied_logout = FakeHandler(headers={"Cookie": session_cookie_header})
            auth.handle_logout(denied_logout)
            if denied_logout.status != 403 or denied_logout.header_values("Set-Cookie"):
                failures.append("logout accepted without Origin and CSRF")

            allowed_logout = FakeHandler(
                headers={
                    "Cookie": session_cookie_header,
                    "Origin": config.origin,
                    "X-ArchFlow-CSRF": session["csrf"],
                }
            )
            auth.handle_logout(allowed_logout)
            cleared = " ".join(allowed_logout.header_values("Set-Cookie"))
            if allowed_logout.status != 200 or auth.SESSION_COOKIE not in cleared or "max-age=0" not in cleared:
                failures.append("authorized logout did not clear session")

            forged_jarvis = FakeHandler(
                headers={
                    legacy_header: legacy_value,
                    "Origin": config.origin,
                    "X-ArchFlow-CSRF": "forged-csrf",
                },
                body={"authenticated_admin": True, "action_approval": True},
            )
            jarvis.JsonHandler.do_POST(forged_jarvis)
            if forged_jarvis.status != 401 or forged_jarvis.route_calls:
                failures.append("forged Jarvis body or legacy credential header bypassed session boundary")

            valid_jarvis = FakeHandler(
                headers={
                    "Cookie": session_cookie_header,
                    "Origin": config.origin,
                    "X-ArchFlow-CSRF": session["csrf"],
                },
                body={"authenticated_admin": False, "action_approval": False},
            )
            jarvis.JsonHandler.do_POST(valid_jarvis)
            if valid_jarvis.status != 200 or len(valid_jarvis.route_calls) != 1:
                failures.append("valid administrator session did not reach Jarvis route")
            elif valid_jarvis.route_calls[0][1].get("authenticated_admin") is not False:
                failures.append("Jarvis altered the untrusted request payload")
            elif valid_jarvis.route_calls[0][2] is not True:
                failures.append("Jarvis did not pass the server decision in trusted context")

    email_auth_env = {
        **BASE_AUTH_ENV,
        "ARCHFLOW_ADMIN_GOOGLE_SUBJECTS": "",
        "ARCHFLOW_ADMIN_EMAILS": "fixture-user" + "@" + "gmail.com",
    }
    with isolated_env(email_auth_env):
        email_config = auth.load_auth_config()
        email_claims = claims_for(email_config, "fixture-nonce", sub="different-subject")
        if not auth.identity_authorized(email_claims, email_config):
            failures.append("verified authoritative email fallback rejected")
        if auth.identity_authorized({**email_claims, "email_verified": False}, email_config):
            failures.append("unverified email fallback authorized")
        if auth.identity_authorized(
            {**email_claims, "email": "fixture-user" + "@" + "example.net", "hd": ""},
            email_config,
        ):
            failures.append("non-authoritative email fallback authorized")

    owned_sources = [
        API_ROOT / "_auth_contract.py",
        API_ROOT / "_jarvis_contract.py",
        *sorted((API_ROOT / "auth").rglob("*.py")),
        Path(__file__),
    ]
    static_owner_key = "JARVIS_" + "OWNER_" + "TOKEN"
    serialized_owner_marker = "owner_" + "authorized"
    for source in owned_sources:
        text = source.read_text(encoding="utf-8")
        try:
            ast.parse(text, filename=str(source))
        except SyntaxError as exc:
            failures.append(f"syntax failed for {source.relative_to(REPO_ROOT)}: {exc.msg}")
        if static_owner_key in text:
            failures.append(f"static privileged credential contract remains in {source.relative_to(REPO_ROOT)}")
        if serialized_owner_marker in text:
            failures.append(f"serialized owner authorization remains in {source.relative_to(REPO_ROOT)}")

    route_files = {
        "auth_start": API_ROOT / "auth" / "google" / "start.py",
        "auth_callback": API_ROOT / "auth" / "google" / "callback.py",
        "auth_session": API_ROOT / "auth" / "session.py",
        "auth_logout": API_ROOT / "auth" / "logout.py",
    }
    loaded_routes: dict[str, Any] = {}
    for name, path in route_files.items():
        try:
            module = load_route(path, "archflow_smoke_" + name)
            loaded_routes[name] = module
            if not hasattr(module, "handler"):
                failures.append(f"serverless route {name} has no handler")
        except Exception as exc:  # noqa: BLE001
            failures.append(f"serverless route {name} failed import: {type(exc).__name__}")

    if len(loaded_routes) == len(route_files):
        with isolated_env(BASE_AUTH_ENV), mock.patch.object(auth.time, "time", return_value=FIXED_NOW):
            start_handler = FakeHandler(path="/api/auth/google/start?return=jarvis")
            loaded_routes["auth_start"].handler.do_GET(start_handler)
            if start_handler.status != 302:
                failures.append("start route did not redirect")
            if not " ".join(start_handler.header_values("Location")).startswith(auth.AUTHORIZATION_ENDPOINT):
                failures.append("start route did not use fixed authorization endpoint")
            if auth.TRANSACTION_COOKIE not in " ".join(start_handler.header_values("Set-Cookie")):
                failures.append("start route did not set transaction cookie")

            start_post = FakeHandler(path="/api/auth/google/start")
            loaded_routes["auth_start"].handler.do_POST(start_post)
            if start_post.status != 405 or start_post.header_values("Allow") != ["GET"]:
                failures.append("start route method boundary failed")

            excessive_query = "&".join(f"field{index}=x" for index in range(17))
            oversized_start = FakeHandler(path="/api/auth/google/start?" + excessive_query)
            loaded_routes["auth_start"].handler.do_GET(oversized_start)
            if oversized_start.status != 400:
                failures.append("start route did not reject excessive query fields")

            callback_missing_cookie = FakeHandler(
                path="/api/auth/google/callback?state=fixture-state&code=fixture-code"
            )
            loaded_routes["auth_callback"].handler.do_GET(callback_missing_cookie)
            if callback_missing_cookie.status != 401:
                failures.append("callback route accepted request without transaction cookie")
            clear_headers = " ".join(callback_missing_cookie.header_values("Set-Cookie"))
            if auth.TRANSACTION_COOKIE not in clear_headers or "max-age=0" not in clear_headers:
                failures.append("failed callback did not clear transaction cookie")

            public_session_handler = FakeHandler(path="/api/auth/session")
            loaded_routes["auth_session"].handler.do_GET(public_session_handler)
            if public_session_handler.status != 200 or public_session_handler.json_body() != {
                "authenticated": False,
                "role": "public",
            }:
                failures.append("public session route contract failed")

            session_post = FakeHandler(path="/api/auth/session")
            loaded_routes["auth_session"].handler.do_POST(session_post)
            if session_post.status != 405 or session_post.header_values("Allow") != ["GET"]:
                failures.append("session route method boundary failed")

            logout_get = FakeHandler(path="/api/auth/logout")
            loaded_routes["auth_logout"].handler.do_GET(logout_get)
            if logout_get.status != 405 or logout_get.header_values("Allow") != ["POST"]:
                failures.append("logout route method boundary failed")

            callback_post = FakeHandler(path="/api/auth/google/callback")
            loaded_routes["auth_callback"].handler.do_POST(callback_post)
            if callback_post.status != 405 or callback_post.header_values("Allow") != ["GET"]:
                failures.append("callback route method boundary failed")

    if failures:
        print("auth_contract_smoke=failed")
        print("failures=" + "; ".join(failures))
        return 1
    print(
        "auth_contract_smoke=ok "
        "flow=authorization_code,state,nonce,pkce_s256 "
        "session=host_cookie,origin,csrf,epoch "
        "negative_matrix=passed static_credential_contract=0 external_effects=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
