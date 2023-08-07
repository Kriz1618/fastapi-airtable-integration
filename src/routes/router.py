from fastapi import APIRouter

from .users import user_router
from .airtable import airtable_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=['Users'])
router.include_router(airtable_router, prefix="/airtable", tags=['AirTable'])
