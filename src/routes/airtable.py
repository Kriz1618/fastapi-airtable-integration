from fastapi import APIRouter, Request

from src.config import airtable as config
from src.models.airtable import WebhookBody
from src.services import airtable as service

airtable_router = APIRouter()
FIELDS = "Name,Status,Type,Email Address"


@airtable_router.get('/bases')
async def list_bases_info(offset: str = None):
    return service.list_bases(offset)


@airtable_router.get('/bases/{id}')
async def list_base_tables(id: str):
    return service.list_base_tables(id)


@airtable_router.get('/saved_items')
async def list_syncronized_items():
    return service.list_items()


@airtable_router.get('/list')
async def list_table_items(
    base_id: str = config.BASE_ID,
    table: str = config.TABLE_NAME,
    size: int = 10,
    fields: str = FIELDS,
    offset: str = None
):
    return service.list_records(base_id=base_id, table_name=table, page_size=size, fields=fields, offset=offset)


@airtable_router.get('/record/{id}')
async def get_record_by_id(
    base_id: str = config.BASE_ID,
    table: str = config.TABLE_NAME,
    id: str = None
):
    return service.get_record(base_id=base_id, table_name=table, item_id=id)


@airtable_router.get('/webhooks')
async def list_webhooks(base_id: str = config.BASE_ID):
    return service.list_webhooks(base_id=base_id)


@airtable_router.get('/webhook/{id}/payloads')
async def list_webhook_payloads(base_id: str, id: str):
    return service.get_webhook_payloads(base_id, id)


@airtable_router.post('/webhook')
async def create_webhook(body: WebhookBody):
    return service.create_webhook(body)


@airtable_router.post('/webhook/payload')
async def receive_webhook_payload(request: Request):
    data = await request.json()
    return service.handle_webhook_event(data)


@airtable_router.post('/webhook/{id}')
async def enable_webhook(base_id: str, id: str, enable: bool):
    return service.update_webhook_status(base_id, id, enable)


@airtable_router.delete('/webhook/{id}')
async def create_webhook(base_id: str, id: str):
    return service.delete_webhook(base_id=base_id, webhook_id=id)
