import hashlib
import random

from interview_scheduler_service.business.utils.date_time import generate_interview_slots
from interview_scheduler_service.business.utils.objects_validation import validate_date_interval
from interview_scheduler_service.crud import mongo
from interview_scheduler_service.crud.slot_operations import insert_or_update_one_slot
from interview_scheduler_service.crud.user_operations import insert_user


def users_init():
    """
    Populates the database with candidates carlos and arturito, and with interviewers ines and ingrid.
    :return: None
    """
    mongo.db.users.drop()
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


def slots_init():
    """
    Initializes many random interview slots during December
    :return: None
    """
    mongo.db.slots.drop()
    start_date, end_date = validate_date_interval("2018-12-01 0", "2019-1-01 0")
    users = [{"username": "carlos", "user_type": "candidate"},
             {"username": "arturito", "user_type": "candidate"},
             {"username": "ines", "user_type": "interviewer"},
             {"username": "ingrid", "user_type": "interviewer"}]
    for interview_slot in generate_interview_slots(start_date, end_date):
        # Add a few users to this time slot
        for i in range(random.randint(0, 3)):
            insert_or_update_one_slot({"username": users[random.randint(0, len(users) - 1)]['username'],
                                       "dateTime": interview_slot,
                                       "user_type": users[random.randint(0, len(users) - 1)]['user_type']
                                       })


if __name__ == '__main__':
    users_init()
    slots_init()
