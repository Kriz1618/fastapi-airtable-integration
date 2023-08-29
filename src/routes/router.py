from fastapi import APIRouter

from .users import user_router
from .airtable import airtable_router
from .baseql import baseql_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=['Users'])
router.include_router(airtable_router, prefix="/airtable", tags=['AirTable'])
router.include_router(baseql_router, prefix="/baseql_router", tags=['BaseQl'])
