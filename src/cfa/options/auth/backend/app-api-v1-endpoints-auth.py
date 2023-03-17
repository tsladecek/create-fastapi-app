from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import backend_login

router = APIRouter()


@router.post('/token')
async def login_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    token = await backend_login(username=form_data.username,
                                password=form_data.password)

    return token
