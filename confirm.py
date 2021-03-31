import calendar
import datetime

def holiday_check(day):
    dt = datetime.datetime.now()
    return datetime.date(dt.year, dt.month, day).weekday() == 5 or datetime.date(dt.year, dt.month, day).weekday() == 6

def lastday_check(day):
    dt = datetime.datetime.now()
    return int(calendar.monthrange(dt.year,dt.month)[1]) == int(day) #리턴갑이 F면 정상 T면 다음달1일로 넘어감