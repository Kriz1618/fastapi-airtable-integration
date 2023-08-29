from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.schemas.campaign import CampaignInput, EventInput

from src.services import baseql as service

baseql_router = APIRouter()


@baseql_router.get('/users')
async def list_users(page_size: int, page: int = 1):
    return service.users_query(page=page, page_size=page_size)


@baseql_router.get('/locations/:brand_id')
async def list_locations(brand_id: str, page_size: int = 10, page: int = 1):
    return service.get_brand_locations(brand_id=brand_id, page=page, page_size=page_size)


@baseql_router.post('/campaign')
async def create_campign(campign_input: CampaignInput):
    json_data = jsonable_encoder(campign_input)
    return service.create_campaign(json_data)


@baseql_router.get('/events')
async def list_events(page_size: int, page: int = 1):
    return service.event_query(page=page, page_size=page_size)


@baseql_router.post('/event')
async def create_event(event_input: EventInput):
    json_data = jsonable_encoder(event_input)
    return service.create_event(json_data)


@baseql_router.patch('/event/{id}')
async def update_event(id: str, event_input: EventInput):
    json_data = jsonable_encoder(event_input)
    return service.update_event(id, json_data)


@baseql_router.delete('/event/{id}')
async def delete_event(id: str, ):
    return service.delete_event(id)
