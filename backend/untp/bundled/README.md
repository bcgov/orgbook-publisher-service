# Bundled UNTP artefacts

**Upstream source:** artefacts are maintained in the UNCEFACT UNTP spec repo — [`spec-untp` → `artefacts/`](https://opensource.unicc.org/un/unece/uncefact/spec-untp/-/tree/main/artefacts) on GitLab ([opensource.unicc.org](https://opensource.unicc.org/un/unece/uncefact/spec-untp/-/tree/main/artefacts)).

**Published mirrors:** we register the same files under the canonical URLs served with the public spec (e.g. [untp.unece.org artefacts](https://untp.unece.org/artefacts/schema/v0.7.0/dcc/ConformityCredential.json)) so wire-format `@context` / `$ref` strings stay stable.

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
