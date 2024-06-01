import datetime as dt

class Schedule:
    def __init__(self, tz: dt.timezone = None, days: int = 0, start_date: dt.date = None, end_date:dt.date = None, visits_per_day: int = 3, visit_times: list[dt.time] = None) -> None:
        self.tz = tz
        self.days = days
        self.start_date = start_date
        self.end_date = end_date
        self.visits_per_day = visits_per_day
        self.visit_times = visit_times

class Visit:
    def __init__(self) -> None:
        self.datetime = dt.datetime
        self.person = str
        self.feeding = bool
