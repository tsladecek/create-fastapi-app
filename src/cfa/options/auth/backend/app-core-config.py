from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    PORT: int = 8000
    APP_TITLE: str = 'FastAPI Backend'
    DESCRIPTION: str = 'FastAPI based Backend API communicating with SQL DB via SQLAlchemy'
    VERSION: str = '0.1.0'
    API_VERSION: str = '/api/v1'

    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///db.db'

    BACKEND_URL: str = ''

    class Config:
        env_file = '.env'


settings = Settings()
