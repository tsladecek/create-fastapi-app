from fastapi import APIRouter

from app.api.v1.endpoints import auth, item

router = APIRouter()

router.include_router(auth.router, prefix='/auth', tags=['Authorization'])
router.include_router(item.router, prefix='/item', tags=['Items'])
