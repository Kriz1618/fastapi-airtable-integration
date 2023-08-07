from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter
from pymongo import ReturnDocument

from src.config import database
from src.models import User
from src.schemas.user import serializeDict, serializeList

user_router = APIRouter()
db = database.getCluster()
user_collection = db['user']


@user_router.get('/')
async def find_all_users():
    return serializeList(user_collection.find())


@user_router.post('/')
async def create_user(user: User):
    response = user_collection.insert_one(dict(user))
    return {"user_id": str(response.inserted_id)}


@user_router.put('/{id}')
async def update_user(id, user: User):
    updated_user = user_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user, updated_at=datetime.now())},
        return_document=ReturnDocument.AFTER
    )
    return serializeDict(updated_user)


@user_router.delete('/{id}')
async def delete_user(id):
    return serializeDict(user_collection.find_one_and_delete({"_id": ObjectId(id)}))
