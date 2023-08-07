import os

BASE_ID = os.environ['AIRTABLE_BASE_ID']
TABLE_NAME = os.environ['AIRTABLE_TABLE_NAME']
AIRTABLE_API_URL = os.environ['AIRTABLE_API_URL']
ACCESS_TOKEN = os.environ['AIRTABLE_ACCESS_TOKEN']
WEBHOOK_URL = f"{os.environ['WEBHOOK_URL']}/api/airtable/webhook/payload"

HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}
