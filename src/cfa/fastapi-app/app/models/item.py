from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=False)
