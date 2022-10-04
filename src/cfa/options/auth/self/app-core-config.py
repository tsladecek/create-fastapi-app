from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    PORT: int = 8000
    APP_TITLE: str = 'FastAPI Backend'
    DESCRIPTION: str = 'FastAPI based Backend API communicating with SQL DB via SQLAlchemy'
    VERSION: str = '0.1.0'

    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///db.db'

    JWT_SECRET_KEY: str = 'ad72bf68a0d760ece1d6aa924e2a3ba4a9db38b5663eb774e8f0389ab1cb5148'
    JWT_ALGORITHM: str = 'HS256'
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    SUPERUSER_NAME: str = 'admin'
    SUPERUSER_SURNAME: str = 'backend'
    SUPERUSER_EMAIL: EmailStr = EmailStr('admin@backend.com')
    SUPERUSER_PASSWORD: str = 'password'

    class Config:
        env_file = '.env'


settings = Settings()
