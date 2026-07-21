#!/usr/bin/env python3
"""Resilient production monitor for OmSaravanaBhava applications."""

from __future__ import annotations

import json
import os
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

TIMEOUT_SECONDS = 20
MAX_ATTEMPTS = 3
RETRY_DELAY_SECONDS = 5

CONTROLS = [
    ("Example control", "https://example.com/"),
    ("GitHub control", "https://github.com/"),
]

ENDPOINTS = [
    {
        "name": "DivyaNexus website",
        "url": "https://divyanexus.omsaravanabhava.org/",
        "kind": "website",
    },
    {
        "name": "RamaVerse website",
        "url": "https://ramaverse.omsaravanabhava.org/",
        "kind": "website",
    },
    {
        "name": "KirthiVerse website",
        "url": "https://kirthiverse.omsaravanabhava.org/",
        "kind": "website",
    },
    {
        "name": "DivyaNexus API",
        "url": "https://api-divyanexus.omsaravanabhava.org/health",
        "kind": "api",
        "expected_service": "divyanexus-api",
    },
    {
        "name": "RamaVerse API",
        "url": "https://api-ramaverse.omsaravanabhava.org/health",
        "kind": "api",
        "expected_service": "ramaverse-api",
    },
    {
        "name": "KirthiVerse API",
        "url": "https://api-kirthiverse.omsaravanabhava.org/health",
        "kind": "api",
        "expected_service": "kirthiverse-api",
    },
]


@dataclass
class ProbeResult:
    name: str
    url: str
    kind: str
    available: bool
    http_status: int | None
    response_ms: float | None
    dns_addresses: list[str]
    tls_version: str | None
    tls_days_remaining: int | None
    attempts: int
    error_type: str | None
    error_message: str | None
    api_status: str | None = None
    service: str | None = None
    environment: str | None = None
    version: str | None = None
    request_id: str | None = None
    contract_ok: bool | None = None


def resolve_host(hostname: str) -> list[str]:
    records = socket.getaddrinfo(hostname, 443, type=socket.SOCK_STREAM)
    return sorted({record[4][0] for record in records})


def inspect_tls(hostname: str) -> tuple[str | None, int | None]:
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT_SECONDS) as raw:
        with context.wrap_socket(raw, server_hostname=hostname) as secure:
            certificate = secure.getpeercert()
            tls_version = secure.version()
            expires = certificate.get("notAfter")
            if not expires:
                return tls_version, None
            expires_at = datetime.strptime(
                expires, "%b %d %H:%M:%S %Y %Z"
            ).replace(tzinfo=timezone.utc)
            days = int((expires_at - datetime.now(timezone.utc)).total_seconds() // 86400)
            return tls_version, days


def classify_error(error: BaseException) -> str:
    text = repr(error).lower()
    if isinstance(error, socket.gaierror) or "name or service not known" in text or "temporary failure in name resolution" in text:
        return "DNS_FAILURE"
    if isinstance(error, ssl.SSLError) or "certificate" in text or "tls" in text:
        return "TLS_FAILURE"
    if isinstance(error, TimeoutError) or "timed out" in text:
        return "TIMEOUT"
    if isinstance(error, urllib.error.HTTPError):
        return "HTTP_ERROR"
    return "CONNECTION_FAILURE"


def probe(endpoint: dict[str, str]) -> ProbeResult:
    parsed = urlparse(endpoint["url"])
    hostname = parsed.hostname
    if not hostname:
        raise ValueError(f"Invalid URL: {endpoint['url']}")

    last_error: BaseException | None = None
    dns_addresses: list[str] = []
    tls_version: str | None = None
    tls_days_remaining: int | None = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        started = time.perf_counter()
        try:
            dns_addresses = resolve_host(hostname)
            tls_version, tls_days_remaining = inspect_tls(hostname)

            request = urllib.request.Request(
                endpoint["url"],
                headers={
                    "User-Agent": "OSB-Production-Monitor/1.0",
                    "Accept": "application/json,text/html;q=0.9,*/*;q=0.8",
                    "Cache-Control": "no-cache",
                },
            )
            with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                body_bytes = response.read()
                elapsed = round((time.perf_counter() - started) * 1000, 1)
                http_status = int(response.status)
                body_text = body_bytes.decode("utf-8", errors="replace")

            result = ProbeResult(
                name=endpoint["name"],
                url=endpoint["url"],
                kind=endpoint["kind"],
                available=200 <= http_status < 400,
                http_status=http_status,
                response_ms=elapsed,
                dns_addresses=dns_addresses,
                tls_version=tls_version,
                tls_days_remaining=tls_days_remaining,
                attempts=attempt,
                error_type=None,
                error_message=None,
            )

            if endpoint["kind"] == "api":
                try:
                    payload: dict[str, Any] = json.loads(body_text)
                except json.JSONDecodeError as exc:
                    result.available = False
                    result.contract_ok = False
                    result.error_type = "API_CONTRACT_FAILURE"
                    result.error_message = f"API returned non-JSON content: {exc}"
                    return result

                result.api_status = payload.get("status")
                result.service = payload.get("service")
                result.environment = payload.get("environment")
                result.version = payload.get("version")
                result.request_id = payload.get("requestId") or response.headers.get("X-Request-ID")
                expected_service = endpoint["expected_service"]
                result.contract_ok = all(
                    [
                        result.api_status == "ok",
                        result.service == expected_service,
                        result.environment == "production",
                        isinstance(result.version, str) and bool(result.version.strip()),
                    ]
                )
                if not result.contract_ok:
                    result.available = False
                    result.error_type = "API_CONTRACT_FAILURE"
                    result.error_message = (
                        f"Expected status=ok, service={expected_service}, "
                        "environment=production and a non-empty version; received "
                        f"status={result.api_status}, service={result.service}, "
                        f"environment={result.environment}, version={result.version}"
                    )

            return result

        except urllib.error.HTTPError as error:
            elapsed = round((time.perf_counter() - started) * 1000, 1)
            last_error = error
            if attempt == MAX_ATTEMPTS:
                return ProbeResult(
                    name=endpoint["name"],
                    url=endpoint["url"],
                    kind=endpoint["kind"],
                    available=False,
                    http_status=error.code,
                    response_ms=elapsed,
                    dns_addresses=dns_addresses,
                    tls_version=tls_version,
                    tls_days_remaining=tls_days_remaining,
                    attempts=attempt,
                    error_type="HTTP_ERROR",
                    error_message=str(error),
                    contract_ok=False if endpoint["kind"] == "api" else None,
                )
        except (OSError, ssl.SSLError, TimeoutError, urllib.error.URLError) as error:
            last_error = error

        if attempt < MAX_ATTEMPTS:
            time.sleep(RETRY_DELAY_SECONDS)

    assert last_error is not None
    return ProbeResult(
        name=endpoint["name"],
        url=endpoint["url"],
        kind=endpoint["kind"],
        available=False,
        http_status=None,
        response_ms=None,
        dns_addresses=dns_addresses,
        tls_version=tls_version,
        tls_days_remaining=tls_days_remaining,
        attempts=MAX_ATTEMPTS,
        error_type=classify_error(last_error),
        error_message=str(last_error),
        contract_ok=False if endpoint["kind"] == "api" else None,
    )


def markdown_report(verdict: str, controls: list[ProbeResult], results: list[ProbeResult]) -> str:
    checked_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Three-App Production Availability Report",
        "",
        f"**Checked:** {checked_at}",
        f"**Verdict:** `{verdict}`",
        "",
        "## Monitoring controls",
        "",
        "| Control | HTTP | Available | Response | Error |",
        "|---|---:|---:|---:|---|",
    ]
    for item in controls:
        lines.append(
            f"| {item.name} | {item.http_status or '—'} | {'YES' if item.available else 'NO'} | "
            f"{str(item.response_ms) + ' ms' if item.response_ms is not None else '—'} | "
            f"{item.error_type or '—'} |"
        )

    lines.extend(
        [
            "",
            "## Production endpoints",
            "",
            "| Endpoint | HTTP | Available | Response | TLS | Certificate days | API service | Version | Contract | Error |",
            "|---|---:|---:|---:|---|---:|---|---|---:|---|",
        ]
    )
    for item in results:
        lines.append(
            f"| {item.name} | {item.http_status or '—'} | {'YES' if item.available else 'NO'} | "
            f"{str(item.response_ms) + ' ms' if item.response_ms is not None else '—'} | "
            f"{item.tls_version or '—'} | {item.tls_days_remaining if item.tls_days_remaining is not None else '—'} | "
            f"{item.service or '—'} | {item.version or '—'} | "
            f"{'PASS' if item.contract_ok is True else ('FAIL' if item.contract_ok is False else 'N/A')} | "
            f"{item.error_type or '—'} |"
        )

    failures = [item for item in results if not item.available]
    lines.extend(["", "## Corrective actions", ""])
    if verdict == "MONITORING_RUNTIME_FAILURE":
        lines.append("- Repair or replace the monitoring runner. Do not change application DNS, TLS, GitHub Pages, or Workers based on this run.")
    elif failures:
        lines.append("- Investigate only the endpoints listed as failed; healthy applications must not be rolled back.")
        for item in failures:
            lines.append(f"- **{item.name}:** {item.error_type}: {item.error_message}")
    else:
        lines.append("- No corrective action required. Continue scheduled monitoring.")

    return "\n".join(lines) + "\n"


def main() -> int:
    output_dir = Path(os.environ.get("MONITOR_OUTPUT", "monitoring/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    controls = [probe({"name": name, "url": url, "kind": "website"}) for name, url in CONTROLS]
    controls_healthy = sum(1 for result in controls if result.available)

    if controls_healthy == 0:
        results: list[ProbeResult] = []
        verdict = "MONITORING_RUNTIME_FAILURE"
        exit_code = 2
    else:
        results = [probe(endpoint) for endpoint in ENDPOINTS]
        verdict = "HEALTHY" if all(result.available for result in results) else "PRODUCTION_FAILURE"
        exit_code = 0 if verdict == "HEALTHY" else 1

    payload = {
        "checkedAt": datetime.now(timezone.utc).isoformat(),
        "verdict": verdict,
        "controls": [asdict(item) for item in controls],
        "endpoints": [asdict(item) for item in results],
    }
    (output_dir / "production-report.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    report = markdown_report(verdict, controls, results)
    (output_dir / "production-report.md").write_text(report, encoding="utf-8")
    print(report)

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        Path(step_summary).write_text(report, encoding="utf-8")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
