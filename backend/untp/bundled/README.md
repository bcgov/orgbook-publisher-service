# Bundled UNTP artefacts

Vendored snapshots for offline use. **Canonical URLs** in issued credentials must match `untp/releases.py`.

Layout (repeat per semver patch line you support):

```text
v{semver}/
  contexts/   # JSON-LD @context document(s) for that release
  schemas/    # JSON Schemas when published for that release (optional)
```

| Semver | Context URL | Context bundle | Schemas |
|--------|-------------|----------------|---------|
| 0.5.0 | `https://test.uncefact.org/vocabulary/untp/dcc/0.5.0/` | `v0.5.0/contexts/dcc.jsonld` | _(none yet — `schemas/` reserved)_ |
| 0.7.0 | `https://vocabulary.uncefact.org/untp/0.7.0/context/` | `v0.7.0/contexts/untp.jsonld` | `v0.7.0/schemas/*.json` |

v0.7.0 schemas are from [UNTP Conformity Credential — v0.7.0 artefacts](https://untp.unece.org/docs/specification/ConformityCredential).

Add a new directory `v0.7.1/` (or patch) with the same `contexts/` + `schemas/` shape, then register the semver in `untp/releases.py`.
