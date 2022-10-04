from typing import Any, List

from app import schemas
from app.api import deps
from app.crud.crud_item import crud_item
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/', response_model=List[schemas.Item])
def get_items(
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud_item.read_multi(db=db)


@router.post('/', response_model=schemas.Item)
def create_item(
        obj_in: schemas.ItemCreate,
        db: Session = Depends(deps.get_db),
        current_user=Depends(deps.get_user)
) -> Any:
    return crud_item.create(db=db, obj_in=obj_in)
