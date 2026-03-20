"""
In-memory JSON cache for `BUNDLED_CONTEXTS` and `BUNDLED_SCHEMAS`.

Import explicitly when needed: ``from untp.cache import warm_cache``.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any

from untp.releases import (
    BUNDLED_CONTEXTS,
    BUNDLED_SCHEMAS,
    dcc_schema_artefact_url,
    dia_schema_artefact_url,
)

_BUNDLE_ROOT = Path(__file__).resolve().parent / "bundled"
_LOCK = threading.Lock()
_BY_URL: dict[str, Any] | None = None


def _bundle_path(relpath: str) -> Path:
    return _BUNDLE_ROOT / relpath


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _load_all() -> dict[str, Any]:
    global _BY_URL
    with _LOCK:
        if _BY_URL is not None:
            return _BY_URL
        by_url: dict[str, Any] = {}
        for mapping in (BUNDLED_CONTEXTS, BUNDLED_SCHEMAS):
            for url, relpath in mapping.items():
                p = _bundle_path(relpath)
                if not p.is_file():
                    raise FileNotFoundError(f"Missing bundled file for {url!r}: {p}")
                by_url[url] = _load_json(p)
        _BY_URL = by_url
        return _BY_URL


def get_context_document(canonical_url: str) -> Any:
    try:
        return _load_all()[canonical_url]
    except KeyError as e:
        raise KeyError(f"No bundled context for URL {canonical_url!r}") from e


def get_schema(semver: str, name: str) -> Any:
    url = dcc_schema_artefact_url(semver, name)
    try:
        return _load_all()[url]
    except KeyError as e:
        raise KeyError(f"No bundled schema {name!r} for UNTP {semver}") from e


def get_dia_schema(semver: str, name: str) -> Any:
    url = dia_schema_artefact_url(semver, name)
    try:
        return _load_all()[url]
    except KeyError as e:
        raise KeyError(f"No bundled DIA schema {name!r} for UNTP {semver}") from e


def warm_cache() -> None:
    _load_all()
