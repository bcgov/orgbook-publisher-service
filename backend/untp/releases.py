"""
UNTP bundled artefacts: canonical URL -> local relative file path.

The files live under ``untp/bundled/`` and are addressed by their published
UNTP URLs (contexts and schema artefacts).
"""

from __future__ import annotations

CONTEXT_BUNDLE: dict[str, dict[str, str]] = {
    "https://vocabulary.uncefact.org/untp/0.7.0/context/": {
        "path": "v0.7.0/contexts/untp.jsonld",
        "digest": "sha256:e99627e9ddd159eb0d80c8bba9634ca9099597cc547a37246ad3a4ee6384687e",
    },
}

SCHEMA_BUNDLE: dict[str, dict[str, str]] = {
    "https://untp.unece.org/artefacts/schema/v0.7.0/dcc/ConformityAttestation.json": {
        "path": "v0.7.0/schemas/ConformityAttestation.json",
        "digest": "sha256:37e208da3b34a4c07c49776684ef079c5c8481541a9997afc3db9f4f874ccc2f",
    },
    "https://untp.unece.org/artefacts/schema/v0.7.0/dcc/ConformityCredential.json": {
        "path": "v0.7.0/schemas/ConformityCredential.json",
        "digest": "sha256:68e488ea1c2df8ff868ba63414a215087c2fb737b1b8f84909497ff32ee69f63",
    },
    "https://untp.unece.org/artefacts/schema/v0.7.0/dia/DigitalIdentityAnchor.json": {
        "path": "v0.7.0/schemas/dia/DigitalIdentityAnchor.json",
        "digest": "sha256:188358b324050f6d2b00378020e1f1cee0c87dc0462cb42d513dfc9685b7cc74",
    },
    "https://untp.unece.org/artefacts/schema/v0.7.0/dia/RegisteredIdentity.json": {
        "path": "v0.7.0/schemas/dia/RegisteredIdentity.json",
        "digest": "sha256:ce8120f1198ae405de08d69bc55d17d3f04d5c0bc5e3867deff33cf2ea040b75",
    },
}

# Current default UNTP DCC context URL used by the plugin.
DEFAULT_DCC_CONTEXT_URL = "https://vocabulary.uncefact.org/untp/0.7.0/context/"
