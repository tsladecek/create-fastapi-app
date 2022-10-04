from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, models
from app.api import deps
from app.crud.crud_user import crud_user

router = APIRouter()


@router.get('/', response_model=schemas.User)
def get_user(
        user_id: int,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_user)
) -> Any:
    return crud_user.read(db, item_id=user_id)
