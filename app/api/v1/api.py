from fastapi import APIRouter

from app.api.v1.endpoints import login, users


api_router = APIRouter(prefix="/api/v1")
api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
