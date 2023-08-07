from fastapi import APIRouter

from .health_check import health_check_router
from .router import router

main_router = APIRouter()

main_router.include_router(health_check_router, prefix='/api/status')
main_router.include_router(router, prefix='/api')
