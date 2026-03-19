# UNTP Publisher — Backend

FastAPI backend for the UNTP Publisher service. See the [repository README](../README.md) for overview and operational docs.

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

## Docker

From the repo root:

```bash
docker build -t untp-publisher-service -f backend/Dockerfile backend/
docker run -p 8000:8000 untp-publisher-service
```
