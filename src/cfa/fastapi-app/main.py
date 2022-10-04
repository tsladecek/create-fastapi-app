import uvicorn
from fastapi import FastAPI

from app.api.v1 import router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.include_router(router, prefix=settings.API_VERSION)

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT, reload=True)
