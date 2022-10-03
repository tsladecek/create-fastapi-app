from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj = self.model(**obj_in.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def read(self, db: Session, *, item_id: int) -> ModelType:
        return db.query(self.model).get(item_id)

    def read_multi(self, db: Session, *, offset: int = 0, limit: Optional[int] = None) -> List[ModelType]:
        return db.query(self.model).offset(offset).limit(limit).all()

    def update(self, db: Session, *, item_id: int, obj_in: UpdateSchemaType) -> ModelType:
        obj = db.query(self.model).get(item_id)
        update_obj = obj_in.dict(exclude_unset=True)

        for column, value in update_obj.items():
            setattr(obj, column, value)

        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, *, item_id: int) -> ModelType:
        obj = db.query(self.model).get(item_id)
        db.delete(obj)
        db.commit()
        return obj
