import datetime

def holiday_check (day):
    dt = datetime.datetime.now()
    return datetime.date(dt.year, dt.month, day).weekday() == 5 or datetime.date(dt.year, dt.month, day).weekday() == 6