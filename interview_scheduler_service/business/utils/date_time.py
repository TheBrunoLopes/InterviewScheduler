from datetime import datetime, timedelta

date_format = "%Y-%m-%d %H"


def create_date_object(date_string: str) -> datetime:
    """
    Receives a dateTime string and returns a datetime object
    :param date_string:
    :return:
    """
    return datetime.strptime(date_string, date_format)


def date_object_to_string(date: datetime):
    """
    Returns the string representation of a datetime object
    :param date:
    :return: str
    """
    return date.strftime(date_format)


def generate_interview_slots(start_date: datetime, end_date: datetime, slot_hours_duration=1):
    """
    Calculates a list of interview slots based on the start_date and end_date.
    :param start_date:
    :param end_date:
    :param slot_hours_duration: specifies the duration of the slots
    :return: Generator
    """
    iterator_date = timedelta(0)
    while start_date + iterator_date < end_date:
        yield start_date + iterator_date
        iterator_date += timedelta(hours=slot_hours_duration)
