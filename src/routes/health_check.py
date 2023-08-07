from fastapi import APIRouter


health_check_router = APIRouter()


@health_check_router.get('/', tags=["Health Check"])
async def api_status():
  return 'Api is running'
