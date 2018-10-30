from interview_scheduler_service.business.utils.date_time import create_date_object, generate_interview_slots
from interview_scheduler_service.business.utils.objects_validation import validate_date_interval


def test_simple_date():
    """
    Tests if create_date_object(..) can create a simple datetime object from a string
    :return:
    """
    test_date = create_date_object("2018-12-01 06")
    assert test_date.hour == 6
    assert test_date.day == 1
    assert test_date.month == 12
    assert test_date.year == 2018


def test_incorrect_date():
    """
    Tests if a ValueError exception is raised when we pass incorrect date formats to create_date_object(..)
    :return:
    """
    try:
        create_date_object("2018-12-01 06s")
        create_date_object("12-01 06")
        create_date_object("ff-01 06")
    except ValueError:
        pass
    else:
        # If the valueError was not raised it means the test failed
        assert 0


def test_interview_slots():
    """
    Test if the interview slots are being generated with an one hour interval
    :return:
    """
    start_date, end_date = validate_date_interval("2018-12-01 0", "2018-12-02 12")
    slot_list = list(generate_interview_slots(start_date, end_date, slot_hours_duration=1))
    for i in range(len(slot_list)):
        # We count the hours within the day
        assert slot_list[i].hour == i % 24
