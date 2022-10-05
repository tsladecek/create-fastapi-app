from typing import Generator, Dict

import pytest
from fastapi.testclient import TestClient

from app.database.session import SessionLocal
from app.core.config import settings
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    """Example Test"""
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Example Test"""
    with TestClient(app) as c:
        yield c


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.SUPERUSER_EMAIL,
        "password": settings.SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    """Super User Token Header"""
    return get_superuser_token_headers(client)

