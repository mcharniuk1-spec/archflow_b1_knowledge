from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from http.cookies import CookieError, SimpleCookie
from http.server import BaseHTTPRequestHandler
from typing import Any, Callable, Mapping


AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
CALLBACK_PATH = "/api/auth/google/callback"
TRANSACTION_COOKIE = "__Host-archflow_oauth_txn"
SESSION_COOKIE = "__Host-archflow_admin"
TRANSACTION_TTL_SECONDS = 300
DEFAULT_SESSION_TTL_SECONDS = 14_400
MIN_SESSION_TTL_SECONDS = 300
MAX_SESSION_TTL_SECONDS = 28_800
MAX_TOKEN_BYTES = 8_192
TOKEN_ISSUED_AT_WINDOW_SECONDS = 600
TOKEN_CLOCK_SKEW_SECONDS = 60
SAFE_TOKEN_RE = re.compile(r"^[A-Za-z0-9_-]+$")
RETURN_PATHS = {
    "dashboard": "/project/dashboard/#communication",
    "jarvis": "/jarvis",
}


class AuthError(Exception):
    """Base class for errors that must be rendered without sensitive detail."""


class AuthUnavailable(AuthError):
    pass


class InvalidAuthRequest(AuthError):
    pass


class AuthenticationFailed(AuthError):
    pass


class AccessNotAuthorized(AuthError):
    pass


@dataclass(frozen=True)
class AuthConfig:
    client_id: str
    client_secret: str = field(repr=False)
    origin: str
    signing_secret: bytes = field(repr=False)
    subject_allowlist: tuple[str, ...] = field(repr=False)
    email_allowlist: tuple[str, ...] = field(repr=False)
    session_epoch: str
    session_ttl_seconds: int

    @property
    def callback_uri(self) -> str:
        return f"{self.origin}{CALLBACK_PATH}"


@dataclass(frozen=True)
class AuthorizationStart:
    location: str
    transaction_cookie: str


@dataclass(frozen=True)
class CallbackResult:
    location: str
    session_cookie: str
    clear_transaction_cookie: str


@dataclass(frozen=True)
class RequestAuthorization:
    authorized: bool
    status: int
    error: str
    session: Mapping[str, Any] | None = None


TokenExchange = Callable[[AuthConfig, str, str], str]
TokenValidator = Callable[[str, AuthConfig], Mapping[str, Any]]


def _enabled(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _csv_values(name: str, *, lowercase: bool = False) -> tuple[str, ...]:
    values: list[str] = []
    for raw in os.getenv(name, "").split(","):
        value = raw.strip()
        if not value:
            continue
        normalized = value.lower() if lowercase else value
        if normalized not in values:
            values.append(normalized)
    return tuple(values)


def _validated_origin(value: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(value.strip())
    except ValueError as exc:
        raise AuthUnavailable("invalid auth configuration") from exc
    if (
        parsed.scheme != "https"
        or not parsed.netloc
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise AuthUnavailable("invalid auth configuration")
    return f"https://{parsed.netloc}"


def _session_ttl() -> int:
    raw = os.getenv("ARCHFLOW_AUTH_SESSION_TTL_SECONDS", "").strip()
    if not raw:
        return DEFAULT_SESSION_TTL_SECONDS
    try:
        value = int(raw)
    except ValueError as exc:
        raise AuthUnavailable("invalid auth configuration") from exc
    if not MIN_SESSION_TTL_SECONDS <= value <= MAX_SESSION_TTL_SECONDS:
        raise AuthUnavailable("invalid auth configuration")
    return value


def load_auth_config() -> AuthConfig:
    if not _enabled("ARCHFLOW_AUTH_ENABLED"):
        raise AuthUnavailable("administrator sign-in unavailable")

    client_id = os.getenv("GOOGLE_OAUTH_CLIENT_ID", "").strip()
    client_secret = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET", "").strip()
    signing_value = os.getenv("ARCHFLOW_AUTH_SECRET", "")
    epoch = os.getenv("ARCHFLOW_AUTH_SESSION_EPOCH", "").strip()
    subject_allowlist = _csv_values("ARCHFLOW_ADMIN_GOOGLE_SUBJECTS")
    email_allowlist = _csv_values("ARCHFLOW_ADMIN_EMAILS", lowercase=True)

    if not client_id or not client_secret or len(signing_value.encode("utf-8")) < 32:
        raise AuthUnavailable("administrator sign-in unavailable")
    if not epoch or len(epoch) > 128:
        raise AuthUnavailable("administrator sign-in unavailable")
    if not subject_allowlist and not email_allowlist:
        raise AuthUnavailable("administrator sign-in unavailable")
    if any(not value.isascii() or len(value.encode("ascii")) > 255 for value in subject_allowlist):
        raise AuthUnavailable("administrator sign-in unavailable")
    if any(not value.isascii() or len(value.encode("ascii")) > 320 for value in email_allowlist):
        raise AuthUnavailable("administrator sign-in unavailable")

    return AuthConfig(
        client_id=client_id,
        client_secret=client_secret,
        origin=_validated_origin(os.getenv("ARCHFLOW_AUTH_ORIGIN", "")),
        signing_secret=signing_value.encode("utf-8"),
        subject_allowlist=subject_allowlist,
        email_allowlist=email_allowlist,
        session_epoch=epoch,
        session_ttl_seconds=_session_ttl(),
    )


def _now(value: float | int | None = None) -> int:
    return int(time.time() if value is None else value)


def _base64url_encode(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("ascii").rstrip("=")


def _base64url_decode(value: str) -> bytes:
    if not value or not SAFE_TOKEN_RE.fullmatch(value):
        raise AuthenticationFailed("invalid token")
    padding = "=" * (-len(value) % 4)
    try:
        return base64.urlsafe_b64decode(value + padding)
    except (ValueError, TypeError) as exc:
        raise AuthenticationFailed("invalid token") from exc


def _random_value(byte_count: int = 32) -> str:
    return _base64url_encode(secrets.token_bytes(byte_count))


def _secure_equal(left: Any, right: Any) -> bool:
    if not isinstance(left, str) or not isinstance(right, str):
        return False
    return hmac.compare_digest(left.encode("utf-8"), right.encode("utf-8"))


def _canonical_json(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def _sign_payload(payload: Mapping[str, Any], secret: bytes, purpose: bytes) -> str:
    encoded = _base64url_encode(_canonical_json(payload))
    signature = hmac.new(secret, purpose + b"." + encoded.encode("ascii"), hashlib.sha256).digest()
    return f"{encoded}.{_base64url_encode(signature)}"


def _verify_payload(token: str, secret: bytes, purpose: bytes) -> dict[str, Any]:
    if not token or len(token.encode("utf-8")) > MAX_TOKEN_BYTES or token.count(".") != 1:
        raise AuthenticationFailed("invalid token")
    encoded, supplied = token.split(".", 1)
    if not SAFE_TOKEN_RE.fullmatch(encoded) or not SAFE_TOKEN_RE.fullmatch(supplied):
        raise AuthenticationFailed("invalid token")
    expected = hmac.new(secret, purpose + b"." + encoded.encode("ascii"), hashlib.sha256).digest()
    actual = _base64url_decode(supplied)
    if not hmac.compare_digest(actual, expected):
        raise AuthenticationFailed("invalid token")
    raw = _base64url_decode(encoded)
    if len(raw) > 4_096:
        raise AuthenticationFailed("invalid token")
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AuthenticationFailed("invalid token") from exc
    if not isinstance(payload, dict):
        raise AuthenticationFailed("invalid token")
    return payload


def _cookie_header(name: str, value: str, lifetime: int) -> str:
    return f"{name}={value}; Path=/; Secure; HttpOnly; SameSite=Lax; max-age={lifetime}"


def clear_cookie_header(name: str) -> str:
    return (
        f"{name}=; Path=/; Secure; HttpOnly; SameSite=Lax; "
        "max-age=0; expires=Thu, 01 Jan 1970 00:00:00 GMT"
    )


def _read_cookie(cookie_header: str, name: str) -> str:
    if not cookie_header or len(cookie_header.encode("utf-8")) > 16_384:
        return ""
    jar = SimpleCookie()
    try:
        jar.load(cookie_header)
    except CookieError:
        return ""
    morsel = jar.get(name)
    return morsel.value if morsel else ""


def _single_query(query: Mapping[str, list[str]], name: str, *, required: bool = True) -> str:
    values = query.get(name, [])
    if len(values) > 1:
        raise InvalidAuthRequest("invalid request")
    if not values:
        if required:
            raise InvalidAuthRequest("invalid request")
        return ""
    value = values[0]
    if required and not value:
        raise InvalidAuthRequest("invalid request")
    if len(value.encode("utf-8")) > 4_096:
        raise InvalidAuthRequest("invalid request")
    return value


def _transaction_payload(config: AuthConfig, return_key: str, now: int) -> tuple[dict[str, Any], str]:
    if return_key not in RETURN_PATHS:
        raise InvalidAuthRequest("invalid request")
    verifier = _random_value(48)
    payload = {
        "v": 1,
        "state": _random_value(),
        "nonce": _random_value(),
        "verifier": verifier,
        "return": return_key,
        "iat": now,
        "exp": now + TRANSACTION_TTL_SECONDS,
    }
    token = _sign_payload(payload, config.signing_secret, b"archflow-oauth-transaction-v1")
    return payload, token


def build_authorization_start(config: AuthConfig, return_key: str = "dashboard", *, now: int | None = None) -> AuthorizationStart:
    issued_at = _now(now)
    transaction, transaction_token = _transaction_payload(config, return_key, issued_at)
    challenge = _base64url_encode(hashlib.sha256(transaction["verifier"].encode("ascii")).digest())
    parameters = {
        "response_type": "code",
        "client_id": config.client_id,
        "redirect_uri": config.callback_uri,
        "scope": "openid email",
        "state": transaction["state"],
        "nonce": transaction["nonce"],
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "access_type": "online",
        "prompt": "select_account",
    }
    return AuthorizationStart(
        location=f"{AUTHORIZATION_ENDPOINT}?{urllib.parse.urlencode(parameters)}",
        transaction_cookie=_cookie_header(TRANSACTION_COOKIE, transaction_token, TRANSACTION_TTL_SECONDS),
    )


def parse_transaction(config: AuthConfig, token: str, *, now: int | None = None) -> dict[str, Any]:
    current = _now(now)
    payload = _verify_payload(token, config.signing_secret, b"archflow-oauth-transaction-v1")
    required_strings = ("state", "nonce", "verifier", "return")
    if payload.get("v") != 1 or any(not isinstance(payload.get(key), str) or not payload[key] for key in required_strings):
        raise AuthenticationFailed("invalid transaction")
    if payload["return"] not in RETURN_PATHS:
        raise AuthenticationFailed("invalid transaction")
    if type(payload.get("iat")) is not int or type(payload.get("exp")) is not int:
        raise AuthenticationFailed("invalid transaction")
    if payload["exp"] <= current or payload["iat"] > current + TOKEN_CLOCK_SKEW_SECONDS:
        raise AuthenticationFailed("expired transaction")
    if payload["exp"] - payload["iat"] != TRANSACTION_TTL_SECONDS:
        raise AuthenticationFailed("invalid transaction")
    return payload


def exchange_google_code(config: AuthConfig, code: str, verifier: str) -> str:
    form = urllib.parse.urlencode(
        {
            "code": code,
            "client_id": config.client_id,
            "client_secret": config.client_secret,
            "redirect_uri": config.callback_uri,
            "grant_type": "authorization_code",
            "code_verifier": verifier,
        }
    ).encode("ascii")
    request = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=form,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            raw = response.read(1_048_577)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as exc:
        raise AuthenticationFailed("token exchange failed") from exc
    if len(raw) > 1_048_576:
        raise AuthenticationFailed("token response too large")
    try:
        result = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AuthenticationFailed("token response invalid") from exc
    token = result.get("id_token") if isinstance(result, dict) else None
    if not isinstance(token, str) or not token or len(token.encode("utf-8")) > MAX_TOKEN_BYTES:
        raise AuthenticationFailed("identity token missing")
    return token


def google_library_claims(token: str, config: AuthConfig) -> Mapping[str, Any]:
    try:
        from google.auth.transport import requests as google_requests
        from google.oauth2 import id_token as google_id_token
    except ImportError as exc:
        raise AuthenticationFailed("token verifier unavailable") from exc
    try:
        claims = google_id_token.verify_oauth2_token(
            token,
            google_requests.Request(),
            audience=config.client_id,
        )
    except Exception as exc:  # The library exposes several verification errors.
        raise AuthenticationFailed("identity token invalid") from exc
    if not isinstance(claims, Mapping):
        raise AuthenticationFailed("identity token invalid")
    return claims


def _claim_is_true(value: Any) -> bool:
    return value is True or (isinstance(value, str) and value.lower() == "true")


def validate_google_claims(
    claims: Mapping[str, Any],
    config: AuthConfig,
    nonce: str,
    *,
    now: int | None = None,
) -> dict[str, Any]:
    current = _now(now)
    issuer = claims.get("iss")
    if issuer not in {"https://accounts.google.com", "accounts.google.com"}:
        raise AuthenticationFailed("identity token invalid")

    audience = claims.get("aud")
    if isinstance(audience, list):
        if config.client_id not in audience or (
            len(audience) != 1 and claims.get("azp") != config.client_id
        ):
            raise AuthenticationFailed("identity token invalid")
    elif audience != config.client_id:
        raise AuthenticationFailed("identity token invalid")
    if claims.get("azp") is not None and claims.get("azp") != config.client_id:
        raise AuthenticationFailed("identity token invalid")
    if not _secure_equal(claims.get("nonce"), nonce):
        raise AuthenticationFailed("identity token invalid")

    issued_at = claims.get("iat")
    expires_at = claims.get("exp")
    if type(issued_at) is not int or type(expires_at) is not int:
        raise AuthenticationFailed("identity token invalid")
    if expires_at <= current or issued_at > current + TOKEN_CLOCK_SKEW_SECONDS:
        raise AuthenticationFailed("identity token invalid")
    if issued_at < current - TOKEN_ISSUED_AT_WINDOW_SECONDS:
        raise AuthenticationFailed("identity token invalid")

    subject = claims.get("sub")
    if not isinstance(subject, str) or not subject or len(subject) > 255:
        raise AuthenticationFailed("identity token invalid")
    return dict(claims)


def _constant_time_member(value: str, candidates: tuple[str, ...]) -> bool:
    matched = False
    for candidate in candidates:
        matched = _secure_equal(value, candidate) or matched
    return matched


def _google_authoritative_email(claims: Mapping[str, Any]) -> tuple[str, bool]:
    email = str(claims.get("email") or "").strip().lower()
    verified = _claim_is_true(claims.get("email_verified"))
    if not email or "@" not in email or not verified:
        return email, False
    domain = email.rsplit("@", 1)[1]
    authoritative = domain == "gmail.com" or bool(str(claims.get("hd") or "").strip())
    return email, authoritative


def identity_authorized(claims: Mapping[str, Any], config: AuthConfig) -> bool:
    subject = str(claims.get("sub") or "")
    if config.subject_allowlist:
        return _constant_time_member(subject, config.subject_allowlist)
    email, authoritative = _google_authoritative_email(claims)
    return authoritative and _constant_time_member(email, config.email_allowlist)


def create_session(config: AuthConfig, subject: str, *, now: int | None = None) -> tuple[str, dict[str, Any]]:
    issued_at = _now(now)
    identity_fingerprint = hmac.new(
        config.signing_secret,
        b"archflow-identity-v1." + subject.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()[:32]
    payload = {
        "v": 1,
        "role": "administrator",
        "uid": identity_fingerprint,
        "iat": issued_at,
        "exp": issued_at + config.session_ttl_seconds,
        "sid": _random_value(24),
        "csrf": _random_value(24),
        "epoch": config.session_epoch,
    }
    return _sign_payload(payload, config.signing_secret, b"archflow-admin-session-v1"), payload


def parse_session(config: AuthConfig, token: str, *, now: int | None = None) -> dict[str, Any]:
    current = _now(now)
    payload = _verify_payload(token, config.signing_secret, b"archflow-admin-session-v1")
    if payload.get("v") != 1 or not _secure_equal(payload.get("role"), "administrator"):
        raise AuthenticationFailed("invalid session")
    if not _secure_equal(payload.get("epoch"), config.session_epoch):
        raise AuthenticationFailed("invalid session")
    if type(payload.get("iat")) is not int or type(payload.get("exp")) is not int:
        raise AuthenticationFailed("invalid session")
    if payload["exp"] <= current or payload["iat"] > current + TOKEN_CLOCK_SKEW_SECONDS:
        raise AuthenticationFailed("invalid session")
    if payload["exp"] - payload["iat"] != config.session_ttl_seconds:
        raise AuthenticationFailed("invalid session")
    for key in ("uid", "sid", "csrf"):
        if not isinstance(payload.get(key), str) or not payload[key] or len(payload[key]) > 256:
            raise AuthenticationFailed("invalid session")
    return payload


def complete_google_callback(
    config: AuthConfig,
    transaction_token: str,
    returned_state: str,
    code: str,
    *,
    now: int | None = None,
    exchange: TokenExchange = exchange_google_code,
    validator: TokenValidator = google_library_claims,
) -> CallbackResult:
    current = _now(now)
    transaction = parse_transaction(config, transaction_token, now=current)
    if not _secure_equal(transaction["state"], returned_state):
        raise AuthenticationFailed("state mismatch")
    identity_token = exchange(config, code, transaction["verifier"])
    claims = validate_google_claims(
        validator(identity_token, config),
        config,
        transaction["nonce"],
        now=current,
    )
    if not identity_authorized(claims, config):
        raise AccessNotAuthorized("identity not authorized")
    session_token, _ = create_session(config, str(claims["sub"]), now=current)
    return CallbackResult(
        location=RETURN_PATHS[transaction["return"]],
        session_cookie=_cookie_header(SESSION_COOKIE, session_token, config.session_ttl_seconds),
        clear_transaction_cookie=clear_cookie_header(TRANSACTION_COOKIE),
    )


def session_from_cookie(cookie_header: str, *, now: int | None = None) -> tuple[AuthConfig | None, dict[str, Any] | None]:
    try:
        config = load_auth_config()
        token = _read_cookie(cookie_header, SESSION_COOKIE)
        if not token:
            return config, None
        return config, parse_session(config, token, now=now)
    except AuthError:
        return None, None


def session_response(cookie_header: str, *, now: int | None = None) -> dict[str, Any]:
    _, session = session_from_cookie(cookie_header, now=now)
    if not session:
        return {"authenticated": False, "role": "public"}
    return {
        "authenticated": True,
        "role": "administrator",
        "csrf": session["csrf"],
    }


def authorize_admin_post(
    cookie_header: str,
    origin: str,
    csrf: str,
    *,
    now: int | None = None,
) -> RequestAuthorization:
    config, session = session_from_cookie(cookie_header, now=now)
    if not config or not session:
        return RequestAuthorization(False, 401, "authentication_required")
    if not origin or not _secure_equal(origin, config.origin):
        return RequestAuthorization(False, 403, "request_not_authorized")
    expected_csrf = str(session.get("csrf") or "")
    if not csrf or not _secure_equal(csrf, expected_csrf):
        return RequestAuthorization(False, 403, "request_not_authorized")
    return RequestAuthorization(True, 200, "", session)


def authorize_admin_handler(handler: BaseHTTPRequestHandler, *, now: int | None = None) -> RequestAuthorization:
    return authorize_admin_post(
        handler.headers.get("Cookie", ""),
        handler.headers.get("Origin", ""),
        handler.headers.get("X-ArchFlow-CSRF", ""),
        now=now,
    )


def _security_headers() -> list[tuple[str, str]]:
    return [
        ("Cache-Control", "no-store, max-age=0"),
        ("Pragma", "no-cache"),
        ("Vary", "Cookie"),
        ("Referrer-Policy", "no-referrer"),
        ("Cross-Origin-Resource-Policy", "same-origin"),
        ("X-Content-Type-Options", "nosniff"),
        ("X-Frame-Options", "DENY"),
    ]


def send_json(
    handler: BaseHTTPRequestHandler,
    status: int,
    payload: Mapping[str, Any],
    *,
    headers: list[tuple[str, str]] | None = None,
) -> None:
    body = json.dumps(payload, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    for name, value in _security_headers() + list(headers or []):
        handler.send_header(name, value)
    handler.end_headers()
    handler.wfile.write(body)


def send_redirect(
    handler: BaseHTTPRequestHandler,
    location: str,
    *,
    status: int = 303,
    cookies: list[str] | None = None,
) -> None:
    handler.send_response(status)
    handler.send_header("Location", location)
    handler.send_header("Content-Length", "0")
    for name, value in _security_headers():
        handler.send_header(name, value)
    for cookie in cookies or []:
        handler.send_header("Set-Cookie", cookie)
    handler.end_headers()


def method_not_allowed(handler: BaseHTTPRequestHandler, allow: str) -> None:
    send_json(handler, 405, {"error": "method_not_allowed"}, headers=[("Allow", allow)])


def _handler_query(handler: BaseHTTPRequestHandler) -> dict[str, list[str]]:
    try:
        return urllib.parse.parse_qs(
            urllib.parse.urlsplit(handler.path).query,
            keep_blank_values=True,
            max_num_fields=16,
        )
    except ValueError as exc:
        raise InvalidAuthRequest("invalid request") from exc


def handle_google_start(handler: BaseHTTPRequestHandler) -> None:
    try:
        query = _handler_query(handler)
        return_key = _single_query(query, "return", required=False) or "dashboard"
        config = load_auth_config()
        result = build_authorization_start(config, return_key)
    except InvalidAuthRequest:
        send_json(handler, 400, {"error": "invalid_request"})
        return
    except (AuthUnavailable, ValueError):
        send_json(handler, 503, {"error": "administrator_sign_in_unavailable"})
        return
    send_redirect(handler, result.location, status=302, cookies=[result.transaction_cookie])


def handle_google_callback(handler: BaseHTTPRequestHandler) -> None:
    clear_transaction = clear_cookie_header(TRANSACTION_COOKIE)
    try:
        config = load_auth_config()
        query = _handler_query(handler)
        if _single_query(query, "error", required=False):
            raise AuthenticationFailed("provider denied request")
        state = _single_query(query, "state")
        code = _single_query(query, "code")
        transaction_token = _read_cookie(handler.headers.get("Cookie", ""), TRANSACTION_COOKIE)
        if not transaction_token:
            raise AuthenticationFailed("transaction missing")
        result = complete_google_callback(config, transaction_token, state, code)
    except AccessNotAuthorized:
        send_json(
            handler,
            403,
            {"error": "access_not_authorized"},
            headers=[("Set-Cookie", clear_transaction)],
        )
        return
    except AuthUnavailable:
        send_json(
            handler,
            503,
            {"error": "administrator_sign_in_unavailable"},
            headers=[("Set-Cookie", clear_transaction)],
        )
        return
    except (AuthError, ValueError):
        send_json(
            handler,
            401,
            {"error": "authentication_failed"},
            headers=[("Set-Cookie", clear_transaction)],
        )
        return
    send_redirect(
        handler,
        result.location,
        cookies=[result.clear_transaction_cookie, result.session_cookie],
    )


def handle_session(handler: BaseHTTPRequestHandler) -> None:
    send_json(handler, 200, session_response(handler.headers.get("Cookie", "")))


def handle_logout(handler: BaseHTTPRequestHandler) -> None:
    decision = authorize_admin_handler(handler)
    if not decision.authorized:
        send_json(handler, decision.status, {"error": decision.error})
        return
    send_json(
        handler,
        200,
        {"authenticated": False, "role": "public"},
        headers=[("Set-Cookie", clear_cookie_header(SESSION_COOKIE))],
    )


class QuietAuthHandler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        return
