"""
UNTP vendored JSON: two URL → path maps under `untp/bundled/`.

- `BUNDLED_CONTEXTS`: JSON-LD @context URL → relative path (.jsonld)
- `BUNDLED_SCHEMAS`: published JSON Schema artefact URL → relative path (.json)
  (DCC under ``…/dcc/…``, DIA under ``…/dia/…`` per untp.unece.org).
"""

from __future__ import annotations

BUNDLED_CONTEXTS: dict[str, str] = {
    "https://vocabulary.uncefact.org/untp/0.7.0/context/": "v0.7.0/contexts/untp.jsonld",
}

BUNDLED_SCHEMAS: dict[str, str] = {
    "https://untp.unece.org/artefacts/schema/v0.7.0/dcc/ConformityAttestation.json": "v0.7.0/schemas/ConformityAttestation.json",
    "https://untp.unece.org/artefacts/schema/v0.7.0/dcc/ConformityCredential.json": "v0.7.0/schemas/ConformityCredential.json",
    "https://untp.unece.org/artefacts/schema/v0.7.0/dia/DigitalIdentityAnchor.json": "v0.7.0/schemas/dia/DigitalIdentityAnchor.json",
    "https://untp.unece.org/artefacts/schema/v0.7.0/dia/RegisteredIdentity.json": "v0.7.0/schemas/dia/RegisteredIdentity.json",
}

_DCC_SCHEMA_ARTEFACT = "https://untp.unece.org/artefacts/schema/v{semver}/dcc/{name}.json"
_DIA_SCHEMA_ARTEFACT = "https://untp.unece.org/artefacts/schema/v{semver}/dia/{name}.json"


def _context_url_by_semver() -> dict[str, str]:
    """Map DCC semver → JSON-LD @context URL (semver taken from `v{semver}/…` bundle path)."""
    out: dict[str, str] = {}
    for url, relpath in BUNDLED_CONTEXTS.items():
        prefix = relpath.split("/")[0]
        if not prefix.startswith("v") or "." not in prefix[1:]:
            raise ValueError(f"Expected v{{semver}}/… in bundle path, got {relpath!r}")
        semver = prefix[1:]
        if semver in out:
            raise ValueError(f"Multiple bundled contexts for semver {semver!r}")
        out[semver] = url
    return out


_CONTEXT_URL_BY_SEMVER: dict[str, str] = _context_url_by_semver()


def _require_semver(value: str) -> str:
    v = value.strip()
    if v not in _CONTEXT_URL_BY_SEMVER:
        allowed = ", ".join(sorted(_CONTEXT_URL_BY_SEMVER))
        raise ValueError(f"Unsupported UNTP DCC data model version {value!r}. Supported: {allowed}")
    return v


def dcc_context_url(semver: str) -> str:
    return _CONTEXT_URL_BY_SEMVER[_require_semver(semver)]


def dcc_schema_artefact_url(semver: str, name: str) -> str:
    v = _require_semver(semver)
    url = _DCC_SCHEMA_ARTEFACT.format(semver=v, name=name)
    if url not in BUNDLED_SCHEMAS:
        raise KeyError(f"No DCC schema {name!r} for UNTP {v!r}")
    return url


def dia_schema_artefact_url(semver: str, name: str) -> str:
    """Published URL for a Digital Identity Anchor JSON Schema (``…/dia/{name}.json``)."""
    v = _require_semver(semver)
    url = _DIA_SCHEMA_ARTEFACT.format(semver=v, name=name)
    if url not in BUNDLED_SCHEMAS:
        raise KeyError(f"No DIA schema {name!r} for UNTP {v!r}")
    return url
