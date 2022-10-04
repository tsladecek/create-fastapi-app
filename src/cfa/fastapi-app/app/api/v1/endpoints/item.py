from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.crud.crud_item import crud_item

router = APIRouter()


@router.get('/', response_model=List[schemas.Item])
def get_items(
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud_item.read_multi(db=db)
