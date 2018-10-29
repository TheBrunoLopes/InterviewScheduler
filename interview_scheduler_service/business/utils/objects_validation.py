from interview_scheduler_service.business.utils.date_time import create_date_object


def validate_user(user: dict, enforce_type=True):
    """
    Validates if the user dict has all the appropriate fields
    :param user:
    :param enforce_type: if the user dict needs to have the type field
    :return:
    """
    if user.get('username', None) is None:
        raise ValueError("Missing username attribute")
    if user.get('password', None) is None:
        raise ValueError("Missing password attribute")
    if enforce_type is True and user.get('type', None) is None:
        raise ValueError("Missing type attribute")


def validate_date_interval(start_date: str, end_date: str) -> tuple:
    """
    Validates that end_date >= start_date and returns the start_date and end_date datetime objects.
    Raises ValueError otherwise
    :param start_date:
    :param end_date:
    :return: start_date and end_date datetime objects
    """
    start_date = create_date_object(start_date)
    end_date = create_date_object(end_date)
    # Check if endDate comes after startDate
    if end_date < start_date:
        raise ValueError("endDate must be greater than startDate")
    return start_date, end_date
