from datetime import datetime, timedelta

# input_datetime2 = input("Enter date and time in format: 'DD/MM/YYYY HH:MM': ")
first_datetime = datetime.now()
second_datetime = datetime.strptime("24/08/2021 00:00", "%d/%m/%Y %H:%M")
new_datetime = second_datetime - first_datetime
print(new_datetime)
datetime_2m = datetime.strptime("19/08/2021 06:00", "%d/%m/%Y %H:%M")
datetime_3m = datetime.strptime("20/08/2021 00:30", "%d/%m/%Y %H:%M")
datetime_4m = datetime.strptime("20/08/2021 08:00", "%d/%m/%Y %H:%M")
datetime_5m = datetime.strptime("20/08/2021 18:00", "%d/%m/%Y %H:%M")
datetime_6m = datetime.strptime("21/08/2021 06:00", "%d/%m/%Y %H:%M")
datetime_7m = datetime.strptime("21/08/2021 18:00", "%d/%m/%Y %H:%M")
datetime_8m = datetime.strptime("22/08/2021 06:00", "%d/%m/%Y %H:%M")
datetime_9m = datetime.strptime("22/08/2021 18:00", "%d/%m/%Y %H:%M")
datetime_10m = datetime.strptime("23/08/2021 06:00", "%d/%m/%Y %H:%M")
datetime_11m = datetime.strptime("23/08/2021 18:00", "%d/%m/%Y %H:%M")
datetime_12m = datetime.strptime("24/08/2021 00:00", "%d/%m/%Y %H:%M")

new_datetime_2m = datetime_2m - first_datetime
new_datetime_3m = datetime_3m - first_datetime
new_datetime_4m = datetime_4m - first_datetime
new_datetime_5m = datetime_5m - first_datetime
new_datetime_6m = datetime_6m - first_datetime
new_datetime_7m = datetime_7m - first_datetime
new_datetime_8m = datetime_8m - first_datetime
new_datetime_9m = datetime_9m - first_datetime
new_datetime_10m = datetime_10m - first_datetime
new_datetime_11m = datetime_11m - first_datetime
new_datetime_12m = datetime_12m - first_datetime

hours = new_datetime.days * 24 + new_datetime.seconds / 60 / 60
hours_2m = new_datetime_2m.days * 24 + new_datetime_2m.seconds / 3600
hours_3m = new_datetime_3m.days * 24 + new_datetime_3m.seconds / 3600
hours_4m = new_datetime_4m.days * 24 + new_datetime_4m.seconds / 3600
hours_5m = new_datetime_5m.days * 24 + new_datetime_5m.seconds / 3600
hours_6m = new_datetime_6m.days * 24 + new_datetime_6m.seconds / 3600
hours_7m = new_datetime_7m.days * 24 + new_datetime_7m.seconds / 3600
hours_8m = new_datetime_8m.days * 24 + new_datetime_8m.seconds / 3600
hours_9m = new_datetime_9m.days * 24 + new_datetime_9m.seconds / 3600
hours_10m = new_datetime_10m.days * 24 + new_datetime_10m.seconds / 3600
hours_11m = new_datetime_11m.days * 24 + new_datetime_11m.seconds / 3600
hours_12m = new_datetime_12m.days * 24 + new_datetime_12m.seconds / 3600
print(round(hours, 3))


print(f"Deadline for 2 module completed on {datetime_2m}.")
print(f"Deadline for 3 module completed on {hours_3m}.")
print(f"Deadline for 4 module in {hours_4m}.")
print(f"Deadline for 5 module in {hours_5m}.")
print(f"Deadline for 6 module in {hours_6m}.")
print(f"Deadline for 7 module in {hours_7m}.")
print(f"Deadline for 8 module in {hours_8m}.")
print(f"Deadline for 9 module in {hours_9m}.")
print(f"Deadline for 10 module in {hours_10m}.")
print(f"Deadline for 11 module in {hours_11m}.")
print(f"Deadline for 12 module in {hours_12m}.")
