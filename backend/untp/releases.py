"""
UNTP Digital Conformity Credential (DCC) release metadata.

Canonical context URLs are the exact strings emitted in VC @context; bundled
files are vendored snapshots for offline cache (see cache.py).
"""

from __future__ import annotations

from typing import FrozenSet

# semver -> { context_canonical_url, context_bundle_relpath, optional schemas }
DCC_BY_SEMVER: dict[str, dict] = {
    "0.5.0": {
        "context_canonical_url": "https://test.uncefact.org/vocabulary/untp/dcc/0.5.0/",
        "context_bundle_relpath": "v0.5.0/contexts/dcc.jsonld",
    },
    "0.7.0": {
        "context_canonical_url": "https://vocabulary.uncefact.org/untp/0.7.0/context/",
        "context_bundle_relpath": "v0.7.0/contexts/untp.jsonld",
        "schemas": {
            "ConformityCredential": "v0.7.0/schemas/ConformityCredential.json",
            "ConformityAttestation": "v0.7.0/schemas/ConformityAttestation.json",
        },
    },
}


def normalize_semver(value: str) -> str:
    return value.strip()


def supported_dcc_semvers() -> FrozenSet[str]:
    return frozenset(DCC_BY_SEMVER.keys())


def require_dcc_semver(value: str) -> str:
    v = normalize_semver(value)
    if v not in DCC_BY_SEMVER:
        allowed = ", ".join(sorted(DCC_BY_SEMVER))
        raise ValueError(f"Unsupported UNTP DCC data model version {value!r}. Supported: {allowed}")
    return v


def dcc_context_url(semver: str) -> str:
    v = require_dcc_semver(semver)
    return DCC_BY_SEMVER[v]["context_canonical_url"]


def dcc_schema_paths(semver: str) -> dict[str, str]:
    v = require_dcc_semver(semver)
    return dict(DCC_BY_SEMVER[v].get("schemas") or {})
