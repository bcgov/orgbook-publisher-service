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

Vendored JSON lives under **`untp/bundled/`** (snapshots from [UNTP `artefacts` on GitLab](https://opensource.unicc.org/un/unece/uncefact/spec-untp/-/tree/main/artefacts)). **`untp/releases.py`** maps each **canonical published URL** (vocabulary context URL plus [untp.unece.org](https://untp.unece.org) schema URLs) to **`path`** and **`sha256` digest** via **`CONTEXT_BUNDLE`** and **`SCHEMA_BUNDLE`**. **`DEFAULT_DCC_CONTEXT_URL`** is the default `@context` for the DCC plugin. See **`untp/bundled/README.md`** for layout and how to add artefacts. A future MongoDB layer can store resolved documents keyed by those URLs.

## Docker

From the repo root:

```bash
docker build -t orgbook-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 orgbook-publisher-service
```
