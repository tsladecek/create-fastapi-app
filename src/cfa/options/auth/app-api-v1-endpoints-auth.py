from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.api.deps import create_access_token
from app.crud.crud_user import crud_user

router = APIRouter()


@router.post('/token', response_model=schemas.Token)
def get_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(deps.get_db)
) -> Any:
    user = crud_user.get_by_email(db, user_email=form_data.username)
    return schemas.Token(access_token=create_access_token(user, form_data.password))
