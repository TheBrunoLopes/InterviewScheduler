from flask_jwt_extended import jwt_required, get_jwt_identity

from interview_scheduler_service.business.utils.date_time import generate_interview_slots, \
    date_object_to_string
from interview_scheduler_service.business.utils.objects_validation import validate_date_interval
from interview_scheduler_service.crud.slot_operations import insert_or_update_one_slot, find_slots, delete_many_slots, \
    find_many_slots_matches


@jwt_required
def get_slots():
    slots_list = find_slots(get_jwt_identity()['username'])
    for slot in slots_list:
        slot["dateTime"] = date_object_to_string(slot["dateTime"])
    return slots_list, 200


@jwt_required
def post_slots(body):
    try:
        start_date, end_date = validate_date_interval(body['startDate'], body['endDate'])
    except ValueError as er:
        return er.args[0], 400
    for interview_slot in generate_interview_slots(start_date, end_date):
        insert_or_update_one_slot({"username": get_jwt_identity()['username'],
                                   "dateTime": interview_slot,
                                   "user_type": get_jwt_identity()['type']
                                   })
    return None, 201


@jwt_required
def delete_slots(body):
    try:
        start_date, end_date = validate_date_interval(body['startDate'], body['endDate'])
    except ValueError as er:
        return er.args[0], 400
    return delete_many_slots(start_date, end_date, get_jwt_identity()['username']), 200


def get_slots_matches(candidate, interviewers):
    slots_list = find_many_slots_matches(candidate, interviewers)
    # This for loop, puts the dateTime in the correct format
    # and collapses slots with the same dateTime that have different interviewers
    # The username field of a slot will be an array with the usernames of the interviewers
    # available for that slot
    slots_dict = {}
    for slot in slots_list:
        slot["dateTime"] = date_object_to_string(slot["dateTime"])
        slots_dict.update({slot["dateTime"]: {**slots_dict.get(slot["dateTime"], {}), **{
            "dateTime": slot["dateTime"]
        }}})
        if slots_dict[slot["dateTime"]].get("username", None) is not None:
            slots_dict[slot["dateTime"]]['username'].append(slot['username'])
        else:
            slots_dict[slot["dateTime"]]['username'] = [slot['username']]
    return list(slots_dict.values()), 200
