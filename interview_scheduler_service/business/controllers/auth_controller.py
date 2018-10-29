from flask_jwt_extended import create_access_token

from interview_scheduler_service.business.utils.hashing import hash_string
from interview_scheduler_service.business.utils.objects_validation import validate_user
from interview_scheduler_service.crud.user_operations import find_user


def users_auth(body):
    """
    Generates a Bearer token that the user will then send in the "Authorization" header in further requests
    :param body: User object containing the username and password
    :return:
    """
    # Authentication code here
    validate_user(body, enforce_type=False)
    # hashing the password
    user = find_user({"username": body['username'], "password": hash_string(body['password'])})
    if user is None:
        return "Bad username or password", 401
    # Identity can be any data that is json serializable
    access_token = create_access_token(identity={
        "username": user.get('username', None),
        "type": user['type']
    })
    return {"access_token": "Bearer {}".format(access_token)}, 200
