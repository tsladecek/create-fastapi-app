from fastapi.testclient import TestClient

from app.core.config import settings


def test_runs_get(client: TestClient) -> None:
    """Test the get items endpoint"""
    r = client.get(f"{settings.API_VERSION}/item/")
    assert r.status_code == 200

    all_runs = r.json()
    assert len(all_runs) > 0
