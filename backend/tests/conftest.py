"""Pytest fixtures for UNTP Publisher backend tests."""
import os

# Set minimal env so Settings validates when app is imported (no .env in CI)
for key in (
    "DOMAIN", "TRACTION_API_URL", "TRACTION_API_KEY", "TRACTION_TENANT_ID",
    "DID_WEB_SERVER_URL", "PUBLISHER_MULTIKEY", "ISSUER_REGISTRY_URL",
    "MONGO_HOST", "MONGO_PORT", "MONGO_USER", "MONGO_PASSWORD", "MONGO_DB",
):
    os.environ.setdefault(key, "test-value")

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client() -> TestClient:
    """FastAPI test client."""
    return TestClient(app)
