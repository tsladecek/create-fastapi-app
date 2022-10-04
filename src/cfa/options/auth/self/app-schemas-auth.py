import datetime

from pydantic import BaseModel

from app.core.config import settings


class TokenContent(BaseModel):
    sub: str
    exp: datetime.datetime = datetime.datetime.utcnow(
    ) + datetime.timedelta(settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
