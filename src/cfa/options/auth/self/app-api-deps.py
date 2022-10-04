from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app import models, schemas
from app.core.config import settings
from app.crud.crud_user import crud_user
from app.database.session import SessionLocal
from app.utils import verify_password


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.API_VERSION}/auth/token')


def get_user(db: Session = Depends(get_db),
             token: str = Depends(oauth2_scheme)) -> models.User:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY,
                             algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload['sub'])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate credentials.')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid token. Token must contain sub field')
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid token. Token sub field must be an integer')
    else:
        user = crud_user.read(db, item_id=user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
        return user


def create_access_token(user: models.User, password: str) -> str:
    # 1. Verify that hashed password from db matches the password
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect password')

    token = schemas.TokenContent(sub=str(user.id))
    jwt_token = jwt.encode(
        token.__dict__, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return jwt_token
