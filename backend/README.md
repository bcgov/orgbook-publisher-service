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
uv run uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Test suite mode (`TEST_SUITE`)

Set **`TEST_SUITE=true`** in the environment to run a **minimal** app: only **`GET /server/status`** and **`POST /test-suite/validate`**. The publisher API (auth, registrations, credentials, static) is **not** registered. Use this for isolated UNTP validation in CI or harnesses.

- **`POST /test-suite/validate`** — JSON body is the UNTP document; optional query **`kind`** (`dcc_credential` or `dcc_attestation`) skips automatic `type` detection.
- Response: **`success`**, **`validation_checks`** (same structure as the validator’s per-check report), **`artefact_kind`**, and **`error`** when validation fails.

When **`TEST_SUITE`** is unset or false, **`/test-suite/*`** routes are omitted entirely.

## UNTP bundled artefacts (DCC + DIA)

Vendored JSON lives under **`untp/bundled/`** (snapshots from [UNTP `artefacts` on GitLab](https://opensource.unicc.org/un/unece/uncefact/spec-untp/-/tree/main/artefacts)). **`untp/releases.py`** maps each **canonical published URL** (vocabulary context URL plus [untp.unece.org](https://untp.unece.org) schema URLs) to **`path`** and **`sha256` digest** via **`CONTEXT_BUNDLE`** and **`SCHEMA_BUNDLE`**. **`DEFAULT_DCC_CONTEXT_URL`** is the default `@context` for the DCC plugin. See **`untp/bundled/README.md`** for layout and how to add artefacts. A future MongoDB layer can store resolved documents keyed by those URLs.

## Docker

From the repo root:

```bash
docker build -t orgbook-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 orgbook-publisher-service
```
