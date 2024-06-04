from check_up import CheckUp
from schedule import Schedule
import datetime as dt

def get_date() -> dt.date:
    date = input(f'Enter the first date (MM-DD-YYYY): ').split('-')
    try:
        assert int(date[0]) < 13 and int(date[0]) > 0
    except (AssertionError, ValueError):
        print(f'Invalid month, must be integer between 1 and 12')
        return
    try:
        assert int(date[1]) < 31 and int(date[1]) > 0
    except (AssertionError, ValueError):
        print(f'Invalid day, must be integer between 1 and 31')
        return
    try:
        assert int(date[2]) < 9999 and int(date[2]) > 2020
    except (AssertionError, ValueError):
        print(f'Invalid year, must be integer between 2020 and 9999')
        return
    date = dt.date(int(date[2]), int(date[0]), int(date[1]))
    return date

a = get_date()          
