import os

BASE_ID = os.environ['AIRTABLE_BASE_ID']
TABLE_NAME = os.environ['AIRTABLE_TABLE_NAME']
AIRTABLE_API_URL = os.environ['AIRTABLE_API_URL']
ACCESS_TOKEN = os.environ['AIRTABLE_ACCESS_TOKEN']
BASEQL_ACCESS_TOKEN = os.environ['BASEQL_ACCESS_TOKEN']
WEBHOOK_URL = f"{os.environ['WEBHOOK_URL']}/api/airtable/webhook/payload"
BASEQL_URL = os.environ['BASEQL_URL']
USERS_KEY = os.environ['USERS_KEY']
BRANDS_KEY = os.environ['BRANDS_KEY']

HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

WISE_HEADERS = {
    'Authorization': f'Bearer {BASEQL_ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}
