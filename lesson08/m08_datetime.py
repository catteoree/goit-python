from datetime import datetime, timedelta


# datetime

current_datetime = datetime.now()
print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.date())
print(current_datetime.time())

d1 = datetime(year=2012, month=1, day=7, hour=14, microsecond=123456)
print(d1)

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.weekday())

# timedelta

difference = seventh_day_2020 - seventh_day_2019
print(difference)
print(difference.total_seconds())

four_weeks_interval = timedelta(weeks=4)
foer_days_interval = timedelta(days=4)
print(seventh_day_2020 - foer_days_interval)
print(seventh_day_2020 + four_weeks_interval)
# print(help(timedelta))
delta = timedelta(
                  days = 50,
                  seconds = 27,
                  microseconds = 10,
                  milliseconds = 29000,
                  minutes = 5,
                  hours = 8,
                  weeks = 2
)
print(delta)

# timestamp 
# Почему в timestamp самая ранняя дата для нормальной работы 1970-01-02 02:00:00

second_hour_of_second_day_1970 = datetime(year=1970, month=1, day=2, hour=2, minute=0)
ts = second_hour_of_second_day_1970.timestamp()
print(second_hour_of_second_day_1970)
print(ts)

ts += 100000
print(datetime.fromtimestamp(ts))
# print(help(timedelta))
