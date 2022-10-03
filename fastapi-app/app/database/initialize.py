from sqlalchemy.orm import Session

from app import models, schemas
from app.core.config import settings
from app.crud.crud_user import crud_user
from app.database.base import Base
from app.database.session import SessionLocal, engine


def initialize(db: Session):
    Base.metadata.create_all(bind=engine)

    create_users(db)


def create_users(db: Session):
    if not db.query(models.User).filter_by(email=settings.SUPERUSER_EMAIL).first():
        crud_user.create(db=db, obj_in=schemas.UserRegister(
            name=settings.SUPERUSER_NAME,
            surname=settings.SUPERUSER_SURNAME,
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD
        ))


if __name__ == '__main__':
    database = SessionLocal()
    initialize(database)
