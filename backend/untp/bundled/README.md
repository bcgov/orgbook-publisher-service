# Bundled UNTP artefacts

Paths are registered in **`untp/releases.py`**:

- **`BUNDLED_CONTEXTS`** — JSON-LD `@context` URL → path under this directory (`.jsonld`)
- **`BUNDLED_SCHEMAS`** — published schema artefact URL → path (`.json`)
  - DCC: […/dcc/…](https://untp.unece.org/artefacts/schema/v0.7.0/dcc/ConformityCredential.json)
  - DIA: […/dia/…](https://untp.unece.org/docs/specification/DigitalIdentityAnchor) ([DigitalIdentityAnchor.json](https://untp.unece.org/artefacts/schema/v0.7.0/dia/DigitalIdentityAnchor.json), [RegisteredIdentity.json](https://untp.unece.org/artefacts/schema/v0.7.0/dia/RegisteredIdentity.json))

```text
v{semver}/
  contexts/
  schemas/
    dia/   # Digital Identity Anchor (optional)
```

Add files on disk, then add one line to the appropriate map.
