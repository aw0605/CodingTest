import datetime

def solution(date1, date2):
    datetime1 = datetime.datetime(date1[0], date1[1], date1[2])
    datetime2 = datetime.datetime(date2[0], date2[1], date2[2])
    return 1 if datetime1 < datetime2 else 0