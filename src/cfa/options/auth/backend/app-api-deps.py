from typing import Generator

import httpx
from app.core.config import settings
from app.database.session import SessionLocal
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.API_VERSION}/auth/token')


def get_db() -> Generator:
    """Database Session generator"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_user_by_token_from_backend(token: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{settings.BACKEND_URL}/{settings.GET_USER_BY_TOKEN_ENDPOINT}/{token}')
        if r.status_code != 200:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail='Authentication failed. Invalid token.')
        return r.json()


async def get_user(token=Depends(oauth2_scheme)):
    user = await get_user_by_token_from_backend(token)
    return user
