from fastapi import APIRouter

from app.api.v1.endpoints import auth, item, user

router = APIRouter()

router.include_router(auth.router, prefix='/auth', tags=['Authorization'])
router.include_router(item.router, prefix='/item', tags=['Items'])
router.include_router(user.router, prefix='/user', tags=['User Management'])