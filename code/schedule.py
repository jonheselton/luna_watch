import datetime as dt

class Schedule:
    def __init__(self) -> None:
        self.tz = dt.timezone
        self.days = int
        self.start_date = dt.date
        self.end_date = dt.date
        self.visits_per_day = int
        self.visit_times = list[dt.time]


a = Schedule()