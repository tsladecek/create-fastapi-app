from app import models, schemas
from app.crud.base import CRUDBase


class CRUDItem(CRUDBase[models.Item, schemas.ItemCreate, schemas.ItemUpdate]):
    pass


crud_item = CRUDItem(models.Item)
