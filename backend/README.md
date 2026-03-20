# Orgbook Publisher — Backend

FastAPI backend for the Orgbook Publisher service. See the [repository README](../README.md) for overview and operational docs.

## Setup

```bash
uv sync
```

## Run

```bash
uv run python main.py
# or
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## UNTP bundled artefacts (DCC)

Vendored JSON-LD contexts and v0.7.0 JSON Schemas live under **`untp/bundled/`** (`v{semver}/contexts/`, `v{semver}/schemas/`). The **`untp`** package exposes `releases` (canonical URL → paths), `cache.warm_cache()`, `get_context_document(url)`, and `get_schema(semver, name)` for offline use. Issuance is not wired to these yet; this change only ships the resources and loader.

## Docker

From the repo root:

```bash
docker build -t orgbook-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 orgbook-publisher-service
```
