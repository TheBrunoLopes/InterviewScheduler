from interview_scheduler.business.utils.date_time import create_date_object


def validate_user(user, enforce_type=True):
    if user.get('username', None) is None:
        raise ValueError("Missing username attribute")
    if user.get('password', None) is None:
        raise ValueError("Missing password attribute")
    if enforce_type is True and user.get('type', None) is None:
        raise ValueError("Missing type attribute")


def validate_date_interval(start_date: str, end_date: str) -> tuple:
    start_date = create_date_object(start_date)
    end_date = create_date_object(end_date)
    # Check if endDate comes after startDate
    if end_date < start_date:
        raise ValueError("endDate must be greater than startDate")
    return start_date, end_date
