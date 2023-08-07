from ast import List
from typing import Any

import jmespath
import requests
from src.schemas.user import serializeList

from src.config import airtable as config
from src.config import database
from src.models.airtable import WebhookBody


db = database.getCluster()
airtable_collection = db['airtable']


def list_records(base_id: str, table_name: str, page_size: int, fields: str, offset: str) -> dict:
    url = f'{config.AIRTABLE_API_URL}/{base_id}/{table_name}'
    params = {
        'pageSize': page_size,
        'fields': fields.split(','),
        'offset': offset
    }

    response = requests.get(url, headers=config.HEADERS, params=params)
    data = response.json()

    return data


def list_bases(offset: str) -> dict:
    url = f'{config.AIRTABLE_API_URL}/meta/bases/'
    params = {'offset': offset}
    response = requests.get(url, headers=config.HEADERS, params=params)
    data = response.json()

    return data


def list_base_tables(base_id: str) -> dict:
    url = f'{config.AIRTABLE_API_URL}/meta/bases/{base_id}/tables/'
    response = requests.get(url, headers=config.HEADERS)
    data = response.json()

    return data


def get_record(base_id: str, table_name: str, item_id: int) -> dict:
    url = f'{config.AIRTABLE_API_URL}/{base_id}/{table_name}/{item_id}'
    response = requests.get(url, headers=config.HEADERS)
    data = response.json()

    return data


def create_webhook(body: WebhookBody) -> dict:
    url = f'{config.AIRTABLE_API_URL}/bases/{body.base_id}/webhooks'
    data = {
        "notificationUrl": f"{config.WEBHOOK_URL}",
        "specification": {
            "options": {
                "filters": {
                    "dataTypes": [
                        "tableData"
                    ],
                    "recordChangeScope": body.table_id
                }
            }
        }
    }
    response = requests.post(url, headers=config.HEADERS, json=data)

    return response.json()


def delete_webhook(base_id: str, webhook_id: str) -> None:
    url = f'{config.AIRTABLE_API_URL}/bases/{base_id}/webhooks/{webhook_id}/'
    response = requests.delete(url, headers=config.HEADERS)

    return response.json()


def handle_webhook_event(data: dict) -> None:
    if 'base' in data and 'webhook' in data:
        base_id = jmespath.search('base.id', data)
        webhook_id = jmespath.search('webhook.id', data)
        cursor = get_webhook_cursor(base_id, webhook_id)
        webhook_payload = get_webhook_payloads(base_id, webhook_id, cursor)

        if webhook_payload:
            item_data = get_payload_data(base_id, webhook_payload)
            save_item(item_data)

    return True


def list_webhooks(base_id: str) -> dict:
    url = f'{config.AIRTABLE_API_URL}/bases/{base_id}/webhooks/'
    response = requests.get(url, headers=config.HEADERS)
    data = response.json()

    return data


def refresh_webhook(base_id: str, webhook_id: str) -> None:
    url = f'{config.AIRTABLE_API_URL}/bases/{base_id}/webhooks/{webhook_id}/refresh'
    response = requests.delete(url, headers=config.HEADERS)
    data = response.json()
    # Extends 7 days
    return data


def get_webhook_payloads(base_id: str, webhook_id: str, cursor: int = 0) -> None:
    url = f'{config.AIRTABLE_API_URL}/bases/{base_id}/webhooks/{webhook_id}/payloads/'
    params = {"limit": 1, "cursor": cursor}
    response = requests.get(url, headers=config.HEADERS, params=params)

    return response.json()


def get_webhook_cursor(base_id: str, webhook_id: str) -> int:
    response = list_webhooks(base_id=base_id)
    cursor = 0

    if response['webhooks'] and len(response['webhooks']):
        for item in response['webhooks']:
            if item['id'] == webhook_id:
                cursor = int(item['cursorForNextPayload'])
                break

    cursor = cursor - 1 if cursor else cursor
    return int(cursor)


def get_payload_data(base_id: str, payload: Any) -> dict:
    table_object = jmespath.search('payloads[0].changedTablesById', payload)
    record_id = None
    [table_id] = table_object.keys()
    payload_data = {'base_id': base_id, 'table_id': table_id}
    deleted_record = jmespath.search(
        f'{table_id}.destroyedRecordIds', table_object)

    if deleted_record:
        [record_id] = deleted_record
        payload_data = {
            **payload_data,
            "record_id": record_id,
            "is_deleted": True
        }
    else:
        [record_id] = jmespath.search(
            f'{table_id}.changedRecordsById', table_object)
        payload_data = {
            **payload_data,
            "record_id": record_id,
        }

    if record_id:
        current_item = get_record(base_id, table_id, record_id)
        payload_data['item'] = current_item

    return payload_data


def save_item(item_data: dict) -> None:
    result = airtable_collection.replace_one(
        {'_id': item_data['record_id']},
        item_data,
        True
    )

    return result.acknowledged


def list_items() -> List(dict):
    return serializeList(airtable_collection.find())


def update_webhook_status(base_id: str, webhook_id: str, enable: str) -> None:
    url = f'{config.AIRTABLE_API_URL}/bases/{base_id}/webhooks/{webhook_id}/enableNotifications/'
    response = requests.post(
        url,
        headers=config.HEADERS,
        json={'enable': enable}
    )

    return response.json()
