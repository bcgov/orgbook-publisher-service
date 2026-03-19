"""Smoke tests for the UNTP Publisher API."""


def test_server_status_returns_ok(client):
    """GET /server/status returns 200 and status ok."""
    response = client.get("/server/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
