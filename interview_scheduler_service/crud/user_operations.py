from pymongo.errors import DuplicateKeyError

from interview_scheduler_service.crud import mongo
from interview_scheduler_service.crud.utils import bson_to_json


def insert_user(user):
    try:
        inserted_id = mongo.db.users.insert_one(user).inserted_id
    except DuplicateKeyError:
        raise ValueError(409, "Duplicate username")
    return str(inserted_id)


def find_users(user_type):
    return bson_to_json(mongo.db.users.find({'type': user_type}, projection={'password': False, '_id': False}))


def find_user(user):
    return bson_to_json(mongo.db.users.find_one(user))
