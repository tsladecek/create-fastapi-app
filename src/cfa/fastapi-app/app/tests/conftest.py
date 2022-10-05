from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.database.session import SessionLocal
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
