# AirTable Integration
Basic API with Python, FastAPI, MongoDB, and AirTable Integration with pyAirTable

## Clone
	git clone git@github.com:Kriz1618/fastapi-airtable-integration.git

## Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate
```
## Install
	pip install -r requirements.txt

## Start Database
	docker-compose up -d

## Start API
	`uvicorn main:app --reload`
	||
	python main.py

## Create the `.env` file
	
	DB_HOST = 'mongodb://localhost:27017'
	DB_USER = 'admin'
	DB_PASSWORD = 'admin'
	PORT = 8000
	ENV = 'local'
	CLUSTER = 'test-cluster'
	AIRTABLE_API_URL = 'https://api.airtable.com/v0'
	AIRTABLE_ACCESS_TOKEN = 'AIRTABLE_TOKEN'
	AIRTABLE_BASE_ID = 'DEFAULT_DB_ID'
	AIRTABLE_TABLE_NAME = 'TEST_TABLE'
	WEBHOOK_URL = 'https://0000-201-219-245-142.ngrok.io'
	

## See API documentation
open local [Link]('http://localhos:8000/docs')

## Serve localhost with ngrok
`ngrok http $PORT`

## Steps
* Install dependencies `pip install fastapi uvicorn pymongo`
* Generate requirements file `pip freeze > requirements.txt`

