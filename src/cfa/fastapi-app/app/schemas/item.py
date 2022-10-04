from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    brand: str


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemCreate):
    pass


class ItemInDB(ItemBase):
    id: int

    class Config:
        orm_mode = True


class Item(ItemInDB):
    pass
