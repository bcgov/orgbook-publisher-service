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

Vendored JSON lives under **`untp/bundled/`** (snapshots from [UNTP `artefacts` on GitLab](https://opensource.unicc.org/un/unece/uncefact/spec-untp/-/tree/main/artefacts), keyed by [untp.unece.org](https://untp.unece.org) URLs). **`untp/releases.py`** defines **`BUNDLED_CONTEXTS`** and **`BUNDLED_SCHEMAS`** (DCC and [Digital Identity Anchor](https://untp.unece.org/docs/specification/DigitalIdentityAnchor) schemas). The DCC plugin uses **`dcc_context_url`** from **`untp`**; DIA schema URLs: **`dia_schema_artefact_url`**. Optional: **`untp.cache`** (`warm_cache`, `get_context_document`, `get_schema`, `get_dia_schema`).

## Docker

From the repo root:

```bash
docker build -t orgbook-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 orgbook-publisher-service
```
