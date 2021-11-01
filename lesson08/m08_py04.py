from sys import executable
from datetime import datetime, timedelta
import pytz
import money

# print(executable)
time_utc = datetime.now(tz=pytz.timezone('UTC'))    # Coordinated Universal Time
str_time_utc = time_utc.strftime('%Y/%m/%d %H:%M:%S %Z %z')
delta = timedelta(hours=2)

str_time_delta = time_utc + delta
str_time_delta = str_time_delta.strftime('%Y/%m/%d %H:%M:%S %Z %z')

print(time_utc)
print(str_time_utc)
print(str_time_delta)

print(help(money))
