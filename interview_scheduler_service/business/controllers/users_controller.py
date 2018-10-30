from interview_scheduler_service.business.utils.hashing import hash_string
from interview_scheduler_service.business.utils.objects_validation import validate_user
from interview_scheduler_service.crud.user_operations import insert_user, find_users


def post_users(body):
    """
    Inserts a user in the database
    :param body: user object
    :return:
    """
    validate_user(body)
    body['password'] = hash_string(body['password'])
    try:
        insert_user(body)
    except ValueError:
        return "Username already exists", 400
    return None, 201


def get_users(user_type):
    """
    Retrieves a list of users of a certain type (candidate / interviewer)
    :param user_type:
    :return:
    """
    return find_users(user_type), 200
