from interview_scheduler_service.business.utils.hashing import hash_string
from interview_scheduler_service.business.utils.objects_validation import validate_user
from interview_scheduler_service.crud.user_operations import insert_user, find_users


def post_users(body):
    validate_user(body)
    body['password'] = hash_string(body['password'])
    try:
        insert_user(body)
    except ValueError:
        return "Username already exists", 400
    return None, 201


def get_users(user_type):
    return find_users(user_type), 200
