"""
Flat map of canonical URIs / schema keys → paths under `untp/bundled/`.

`bundled/bundle-map.json` mirrors this structure for non-Python tooling; it must
stay in sync with `releases.DCC_BY_SEMVER` (validated in `warm_cache()`).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from untp.releases import DCC_BY_SEMVER

_BUNDLE_ROOT = Path(__file__).resolve().parent / "bundled"
BUNDLE_MAP_JSON = _BUNDLE_ROOT / "bundle-map.json"


def build_bundle_map() -> dict[str, Any]:
    """Canonical map derived from `releases.DCC_BY_SEMVER` (single source of truth)."""
    contexts: dict[str, str] = {}
    schemas: dict[str, str] = {}
    for semver, meta in DCC_BY_SEMVER.items():
        contexts[meta["context_canonical_url"]] = meta["context_bundle_relpath"]
        for name, rel in (meta.get("schemas") or {}).items():
            schemas[f"{semver}:{name}"] = rel
    return {
        "version": 1,
        "contexts": dict(sorted(contexts.items())),
        "schemas": dict(sorted(schemas.items())),
    }


def context_uri_to_bundle_relpath() -> dict[str, str]:
    """Map JSON-LD @context URL string → path relative to `untp/bundled/`."""
    return dict(build_bundle_map()["contexts"])


def schema_key_to_bundle_relpath() -> dict[str, str]:
    """Map `"{semver}:{schemaName}"` → path relative to `untp/bundled/`."""
    return dict(build_bundle_map()["schemas"])


def validate_bundle_map_file() -> None:
    """Ensure `bundled/bundle-map.json` matches `build_bundle_map()`."""
    if not BUNDLE_MAP_JSON.is_file():
        raise FileNotFoundError(f"Missing bundle map: {BUNDLE_MAP_JSON}")
    file_obj = json.loads(BUNDLE_MAP_JSON.read_text(encoding="utf-8"))
    expected = build_bundle_map()
    if file_obj.get("version") != expected["version"]:
        raise ValueError(
            f"bundle-map.json version {file_obj.get('version')!r} != expected {expected['version']!r}"
        )
    if file_obj.get("contexts") != expected["contexts"]:
        raise ValueError(
            "bundle-map.json `contexts` out of sync with untp/releases.py; regenerate from build_bundle_map()"
        )
    if file_obj.get("schemas") != expected["schemas"]:
        raise ValueError(
            "bundle-map.json `schemas` out of sync with untp/releases.py; regenerate from build_bundle_map()"
        )


def bundle_relpath_for_context_uri(uri: str) -> str:
    """Resolve a context URL to a bundle-relative path."""
    m = context_uri_to_bundle_relpath()
    try:
        return m[uri]
    except KeyError as e:
        raise KeyError(f"No bundle map entry for context URI {uri!r}") from e


def bundle_relpath_for_schema(semver: str, name: str) -> str:
    """Resolve a semver + schema logical name to a bundle-relative path."""
    key = f"{semver}:{name}"
    m = schema_key_to_bundle_relpath()
    try:
        return m[key]
    except KeyError as e:
        raise KeyError(f"No bundle map entry for schema key {key!r}") from e
