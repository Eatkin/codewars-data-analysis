# https://www.codewars.com/kata/56eb16655250549e4b0013f4
# 2023-06-05T07:36:24.251+0000
import datetime
def most_frequent_days(year):
    DAYS_DICT = {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0,
    }
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date = datetime.date(year, month, day)
                day_of_week = date.strftime('%A')
                DAYS_DICT[day_of_week] += 1
            except:
                continue
    
    # Iterate over the dictionary
    max_seen = 0
    most_frequent_days = []
    for key, value in DAYS_DICT.items():
        if value > max_seen:
            most_frequent_days = []
            most_frequent_days.append(key)
            max_seen = value
            continue
        if value == max_seen:
            most_frequent_days.append(key)
    
    return most_frequent_days