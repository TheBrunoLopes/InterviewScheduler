import hashlib

from interview_scheduler_service.crud import mongo
from interview_scheduler_service.crud.user_operations import insert_user


def users_init():
    mongo.db.users.create_index("username", unique=True)
    user = {"username": "carlos",
            "password": hashlib.sha256("not 1234".encode('utf-8')).hexdigest(),
            "type": "candidate"
            }
    insert_user(user)
    user["username"] = "arturito"
    insert_user(user)
    user["type"] = "interviewer"
    user["username"] = "ines"
    insert_user(user)
    user["username"] = "ingrid"
    insert_user(user)


if __name__ == '__main__':
    users_init()
