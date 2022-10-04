from sqlalchemy.orm import Session

from app import models, schemas
from app.crud.base import CRUDBase
from app.utils import get_password_hash


class CRUDUser(CRUDBase[models.User, schemas.UserCreate, schemas.UserUpdate]):
    @staticmethod
    def get_by_email(db: Session, *, user_email) -> models.User:
        return db.query(models.User).filter_by(email=user_email).one_or_none()

    def create(self, db: Session, *, obj_in: schemas.UserRegister) -> models.User:
        user_create = schemas.UserCreate(
            name=obj_in.name,
            surname=obj_in.surname,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password)
        )
        return super().create(db, obj_in=user_create)


crud_user = CRUDUser(models.User)
