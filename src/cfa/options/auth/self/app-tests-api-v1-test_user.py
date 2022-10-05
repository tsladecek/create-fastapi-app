import random
from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings
from app.crud.crud_user import crud_user


def test_users_get_by_id(
        client: TestClient, superuser_token_headers: Dict,
        db: Session
) -> None:
    """Retrieve user by user id"""
    users = crud_user.get_multi(db)
    user_id = random.choice([u.id for u in users])
    r = client.get(f"{settings.API_V1_STR}/user/{user_id}", headers=superuser_token_headers)
    assert r.status_code == 200
    response = r.json()
    assert response["id"] == user_id

