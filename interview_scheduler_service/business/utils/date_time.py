from datetime import datetime, timedelta

date_format = "%Y-%m-%d %H"


def create_date_object(date_string):
    return datetime.strptime(date_string, date_format)


def date_object_to_string(date):
    return date.strftime(date_format)


def generate_interview_slots(start_date, end_date, slot_hours_duration=1):
    iterator_date = timedelta(0)
    while start_date + iterator_date < end_date:
        yield start_date + iterator_date
        iterator_date += timedelta(hours=slot_hours_duration)
