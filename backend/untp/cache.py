"""
In-memory cache of vendored UNTP JSON-LD contexts and JSON Schemas.

Wire-format @context remains a URL string; cache keys use that same canonical URL.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any

from untp import bundle_map
from untp import releases

_BUNDLE_ROOT = Path(__file__).resolve().parent / "bundled"
_LOCK = threading.Lock()
_LOADED: dict[str, Any] | None = None


def _bundle_path(relpath: str) -> Path:
    return _BUNDLE_ROOT / relpath


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_all() -> dict[str, Any]:
    """Load every bundled context and schema into memory (idempotent)."""
    global _LOADED
    with _LOCK:
        if _LOADED is not None:
            return _LOADED
        bundle_map.validate_bundle_map_file()
        contexts: dict[str, Any] = {}
        schemas: dict[tuple[str, str], Any] = {}
        for semver, meta in releases.DCC_BY_SEMVER.items():
            url = meta["context_canonical_url"]
            ctx_path = _bundle_path(meta["context_bundle_relpath"])
            if not ctx_path.is_file():
                raise FileNotFoundError(f"Missing bundled UNTP context: {ctx_path}")
            contexts[url] = _load_json(ctx_path)
            for name, rel in meta.get("schemas", {}).items():
                sp = _bundle_path(rel)
                if not sp.is_file():
                    raise FileNotFoundError(f"Missing bundled UNTP schema: {sp}")
                schemas[(semver, name)] = _load_json(sp)
        _LOADED = {"contexts": contexts, "schemas": schemas}
        return _LOADED


def get_context_document(canonical_url: str) -> Any:
    data = load_all()
    try:
        return data["contexts"][canonical_url]
    except KeyError as e:
        raise KeyError(f"No bundled context for URL {canonical_url!r}") from e


def get_schema(semver: str, name: str) -> Any:
    releases.require_dcc_semver(semver)
    data = load_all()
    try:
        return data["schemas"][(semver, name)]
    except KeyError as e:
        raise KeyError(f"No bundled schema {name!r} for UNTP {semver}") from e


def warm_cache() -> None:
    load_all()
