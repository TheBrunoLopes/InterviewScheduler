from interview_scheduler.crud import mongo


def insert_or_update_one_slot(slot):
    return mongo.db.slots.update_one(slot, {'$set': slot}, upsert=True)


def find_slots(username):
    return list(mongo.db.slots.find({"username": username}, projection={
        '_id': False, 'username': False, "user_type": False}))


def delete_many_slots(start_date, end_date, username):
    _filter = {
        "dateTime": {
            "$lte": end_date,
            "$gte": start_date
        },
        "username": username
    }
    return mongo.db.slots.delete_many(_filter).deleted_count


def find_many_slots_matches(candidate, interviewers):
    candidate_slots_list = [slot['dateTime'] for slot in
                            mongo.db.slots.find({
                                "username": candidate,
                                "user_type": "candidate"
                            }, projection={'_id': False, 'username': False})]
    return list(mongo.db.slots.find({
        "username":     {"$in": interviewers},
        "dateTime":     {"$in": candidate_slots_list},
        "user_type":    "interviewer"
    }, projection={'_id': False}))
