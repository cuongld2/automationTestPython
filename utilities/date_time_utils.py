import dateutil.parser
import datetime


def parse_string_to_date(string_datetime):
    your_date = dateutil.parser.parse(string_datetime)
    return your_date.date()


def how_many_days_til_now(datetime_value):
    number_of_days = None
    if type(datetime_value) == str:
        number_of_days = datetime.date.today() - parse_string_to_date(datetime_value)
    elif type(datetime_value) == datetime.datetime:
        number_of_days = datetime.date.today() - datetime_value.date()
    return number_of_days.days


def how_many_seconds_between_times(previous_time, later_time):
    return later_time.time().second - previous_time.time().second






