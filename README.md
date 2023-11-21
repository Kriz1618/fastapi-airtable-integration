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
open local [Link]('http://localhost:8000/docs')

## Serve localhost with ngrok
`ngrok http $PORT`

## Steps
* Create a local environment `python -m venv venv`
* Install dependencies `pip install fastapi uvicorn pymongo pipreqs`
* Generate requirements file `pipreqs`
* Generate AirTable AccessToken [Link](https://airtable.com/create/tokens)


## Configure GraphQL access
* Go to the [BaseQL page](https://app.baseql.com/)
* Add new data source (AirTable)
* Type a valid User Access Token
* In the playground click on Settings
* Enable Protected and Mutations options
* To update tables schemas, add the data source again



<p>
    <img src="https://freepngimg.com/thumb/python_logo/6-2-python-logo-free-png-image.png" width="100"  alt="Python" hspace="10" >
    <img src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" width="90" alt="FastAPI" hspace="10" >
    <img src="https://gcollazo.github.io/mongodbapp/assets/img/icon.png" width="90" alt="MongoDB" hspace="10" >
    <img src="https://i0.wp.com/alphalionlogistics.com/wp-content/uploads/2022/08/airtable-logo.png?fit=300%2C300&ssl=1" width="90" alt="Airtable" hspace="10" >
</p>
