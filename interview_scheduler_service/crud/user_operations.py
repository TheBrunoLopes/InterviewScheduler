from pymongo.errors import DuplicateKeyError

from interview_scheduler_service.crud import mongo
from interview_scheduler_service.crud.utils import bson_to_json


def insert_user(user):
    """
    Inserts a user in the database
    :param user:
    :return:
    """
    # We copy the user object so that we do not change it
    user = user.copy()
    try:
        inserted_id = mongo.db.users.insert_one(user).inserted_id
    except DuplicateKeyError:
        raise ValueError(409, "Duplicate username")
    return str(inserted_id)


def find_users(user_type):
    """
    Retrieves all users of a certain user_type
    :param user_type:
    :return:
    """
    return bson_to_json(mongo.db.users.find({'type': user_type}, projection={'password': False, '_id': False}))


def find_user(user):
    return bson_to_json(mongo.db.users.find_one(user))
