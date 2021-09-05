from datetime import datetime, timedelta

input_datetime = input("Enter date and time in format: 'DD/MM/YYYY HH:MM': ")

first_datetime = datetime.strptime(input_datetime, "%d/%m/%Y %H:%M")
new_datetime = first_datetime
period = 114

print(f"Period: {period} hours")
for i in range(101):
    print("{}  {}".format(i, new_datetime))
    new_datetime += timedelta(hours=period)