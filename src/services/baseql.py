import json
from typing import List, Optional
import requests
from src.schemas.campaign import CampaignInput, EventInput, Event

from src.config import airtable as config


def exec_query(base_key: str, query: str, variables: Optional[str] = None, wise_headers: bool = True) -> dict:
    url = f'{config.BASEQL_URL}{base_key}'
    headers = config.WISE_HEADERS if wise_headers else config.HEADERS

    data = {"query": query}
    if variables:
        data["variables"] = variables
    response = requests.post(url, json=data, headers=headers)

    return response.json()


def users_query(page: int, page_size: int = 5) -> dict:
    variables = {
        "page": page,
        "page_size": page_size
    }
    query = '''
        query UsersQuery($page: JSON, $page_size: JSON) {
            users(_page: $page, _page_size: $page_size) {
                description
                name
                status
                tasks {
                    task
                    id
                }
            }
        }
    '''

    data = exec_query(base_key=config.USERS_KEY, query=query, variables=json.dumps(
        variables), wise_headers=False)
    if 'data' not in data:
        return data

    return data['data']


def get_brand_locations(brand_id: str, page: int, page_size: int = 5) -> dict:
    variables = {
        "page": page,
        "page_size": page_size,
        "brand_id": brand_id
    }
    query = '''
        query GetLocationsByBrandId($brand_id: String, $page: JSON, $page_size: JSON) {
            brands(_page: $page, _page_size: $page_size, id: $brand_id) {
                id
                name
            }
            locations(_page: $page, _page_size: $page_size, _filter: {
                brandId: $brand_id,
            }, _order_by: "title") {
                id
                locationName
                fullAddress
                title
            }
        }
    '''

    data = exec_query(base_key=config.BRANDS_KEY, query=query,
                      variables=json.dumps(variables))
    if 'data' not in data:
        return data

    return data['data']


def create_campaign(campaign_input: CampaignInput) -> str:
    variables = campaign_input
    query = '''
        mutation InsertCampaign(
            $title: String
            $brand: [String]
            $locations: [String]
            $whatYouRecieve: String
            $description: String
            $brandStory: String
            $retailValue: Float
            $startDate: String
            $endDate: String
            $targetCreatorSize: [String]
            $lowAge: Float
            $highAge: Float
            $niche: [String]
            $content: [String]
            $visualsTheme: String
            $caption: String
            $hashtagsMentions: String
            $inspiration: String
            $schedulingRequirements: String
            $campaignImage: [JSON]
            $campaignCity: String
            $neighborhood: [String]
            $status: String
            $goal: String
            $count: String
        )   {
            insert_campaigns(
                fixedLocation: "true"
                title: $title
                brand: $brand
                locations: $locations
                whatYouRecieve: $whatYouRecieve
                description: $description
                brandStory: $brandStory
                retailValue: $retailValue
                startDate: $startDate
                endDate: $endDate
                targetCreatorSize: $targetCreatorSize
                lowAge: $lowAge
                highAge: $highAge
                niche: $niche
                content: $content
                visualsTheme: $visualsTheme
                caption: $caption
                hashtagsMentions: $hashtagsMentions
                inspiration: $inspiration
                schedulingRequirements: $schedulingRequirements
                campaignImage: $campaignImage
                neighborhood: $neighborhood
                status: $status
                goal: $goal
                count: $count
                campaignCity: $campaignCity
		    ) {
			    id
		    }
        }
    '''
    data = exec_query(base_key=config.USERS_KEY, query=query, variables=json.dumps(
        variables), wise_headers=True)
    if 'data' not in data:
        return data

    return data['data']


def create_event(event_input: EventInput) -> str:
    variables = event_input
    mutation = '''
        mutation InsertEvent(
            $title: String
            $description: String
            $email: String
            $status: String
            $creators: Float
        ) {
            insert_event(
                title: $title
                description: $description
                email: $email
                status: $status
                creators: $creators
            ) {
                id
            }
        }
    '''

    data = exec_query(base_key=config.USERS_KEY, query=mutation,
                      variables=json.dumps(variables), wise_headers=False)
    if 'data' not in data:
        return data

    return data['data']


def event_query(page: int, page_size: int = 5) -> List[Event]:
    variables = {
        "page": page,
        "page_size": page_size
    }
    query = '''
        query EventsQuery($page: JSON, $page_size: JSON) {
            events(_page: $page, _page_size: $page_size) {
                id
                title
                description
                status
                email
                creators
            }
        }
    '''

    data = exec_query(base_key=config.USERS_KEY, query=query,
                      variables=json.dumps(variables), wise_headers=False)
    if 'data' not in data:
        return data

    return data['data']


def create_event(event_input: EventInput) -> str:
    variables = event_input
    mutation = '''
        mutation InsertEvents(
            $title: String
            $description: String
            $email: String
            $status: String
            $creators: Float
        ) {
            insert_events(
                title: $title
                description: $description
                email: $email
                status: $status
                creators: $creators
            ) {
                id
            }
        }
    '''

    data = exec_query(base_key=config.USERS_KEY, query=mutation,
                      variables=json.dumps(variables), wise_headers=False)
    if 'data' not in data:
        return data

    return data['data']['insert_events'][0]['id']


def update_event(id: str, event_input: EventInput) -> Event:
    variables = event_input
    variables['id'] = id
    mutation = '''
        mutation InsertEvents(
            $id: String
            $title: String
            $description: String
            $email: String
            $status: String
            $creators: Float
        ) {
            update_events(
                id: $id
                title: $title
                description: $description
                email: $email
                status: $status
                creators: $creators
            ) {
                id
                title
                description
                email
                status
                creators
            }
        }
    '''

    data = exec_query(base_key=config.USERS_KEY, query=mutation,
                      variables=json.dumps(variables), wise_headers=False)
    if 'data' not in data:
        return data

    return data['data']['update_events']


def delete_event(id: str) -> str:
    variables = {'id': id}
    mutation = '''
        mutation DeleteEvents($id: String) {
            delete_events(id: $id) {
                id
            }
        }
    '''

    data = exec_query(base_key=config.USERS_KEY, query=mutation,
                      variables=json.dumps(variables), wise_headers=False)
    if 'data' not in data:
        return data

    return data['data']['delete_events'][0]['id']
