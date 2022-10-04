from sqlalchemy.orm import Session

from app import schemas
from app.crud.crud_item import crud_item
from app.database.base import Base
from app.database.session import SessionLocal, engine


def initialize(db: Session):
    Base.metadata.create_all(bind=engine)

    create_items(db)


def create_items(db: Session):
    for name, brand in [('laptop', 'apple'), ('phone', 'samsung'), ('tv', 'sony')]:
        crud_item.create(db=db, obj_in=schemas.ItemCreate(name=name, brand=brand))


if __name__ == '__main__':
    database = SessionLocal()
    initialize(database)
