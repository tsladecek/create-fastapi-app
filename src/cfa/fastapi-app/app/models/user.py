from sqlalchemy import Column, Integer, String

from app.database.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)

    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(511), nullable=False)
