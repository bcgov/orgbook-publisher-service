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

Vendored JSON-LD contexts for **0.6.0**, **0.6.1**, and **0.7.0** (plus v0.7.0 JSON Schemas) live under **`untp/bundled/`** (`v{semver}/contexts/`, `v{semver}/schemas/`). The **`untp`** package exposes `releases`, `cache.warm_cache()`, `get_context_document(url)`, and `get_schema(semver, name)`. The DCC plugin currently defaults the emitted context URL to **0.7.0** via `dcc_context_url("0.7.0")`.

## Docker

From the repo root:

```bash
docker build -t orgbook-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 orgbook-publisher-service
```
