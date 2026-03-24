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

## UNTP bundled artefacts (DCC + DIA)

Vendored JSON lives under **`untp/bundled/`** (snapshots from [UNTP `artefacts` on GitLab](https://opensource.unicc.org/un/unece/uncefact/spec-untp/-/tree/main/artefacts), keyed by [untp.unece.org](https://untp.unece.org) URLs). **`untp/releases.py`** defines **`CONTEXT_BUNDLE`** and **`SCHEMA_BUNDLE`** (with `path` + `digest` metadata) plus **`DEFAULT_DCC_CONTEXT_URL`** used by the DCC plugin. A future MongoDB layer can store resolved documents keyed by those canonical URLs.

## Docker

From the repo root:

```bash
docker build -t orgbook-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 orgbook-publisher-service
```
