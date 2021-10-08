from datetime import datetime, timedelta


# input_datetime2 = input("Enter date and time in format: 'DD/MM/YYYY HH:MM': ")
first_datetime = datetime.now()
second_datetime = datetime.strptime("30/08/2021 00:00", "%d/%m/%Y %H:%M")
new_datetime = second_datetime - first_datetime

datetime_2m = datetime.strptime("19/08/2021 06:00", "%d/%m/%Y %H:%M")
datetime_3m = datetime.strptime("20/08/2021 02:00", "%d/%m/%Y %H:%M")
datetime_4m = datetime.strptime("21/08/2021 14:00", "%d/%m/%Y %H:%M")
datetime_5m = datetime.strptime("30/09/2021 21:00", "%d/%m/%Y %H:%M")
datetime_6m = datetime.strptime("10/10/2021 18:00", "%d/%m/%Y %H:%M")
datetime_7m = datetime.strptime("16/10/2021 18:00", "%d/%m/%Y %H:%M")
datetime_8m = datetime.strptime("22/10/2021 18:00", "%d/%m/%Y %H:%M")
datetime_9m = datetime.strptime("29/10/2021 18:00", "%d/%m/%Y %H:%M")
datetime_10m = datetime.strptime("05/11/2021 18:00", "%d/%m/%Y %H:%M")
datetime_11m = datetime.strptime("12/11/2021 18:00", "%d/%m/%Y %H:%M")
datetime_12m = datetime.strptime("19/11/2021 18:00", "%d/%m/%Y %H:%M")

writer_deadline_book001 = datetime.strptime("10/10/2021 18:00", "%d/%m/%Y %H:%M")
writer_deadline_book002 = datetime.strptime("14/10/2021 18:00", "%d/%m/%Y %H:%M")
writer_deadline_book01 = datetime.strptime("19/10/2021 18:00", "%d/%m/%Y %H:%M")
writer_deadline_book02 = datetime.strptime("29/10/2021 18:00", "%d/%m/%Y %H:%M")
writer_deadline_book03 = datetime.strptime("09/11/2021 18:00", "%d/%m/%Y %H:%M")
writer_deadline_book04 = datetime.strptime("19/11/2021 18:00", "%d/%m/%Y %H:%M")

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

new_writer_deadline_book001 = writer_deadline_book001 - first_datetime
new_writer_deadline_book002 = writer_deadline_book002 - first_datetime
new_writer_deadline_book01 = writer_deadline_book01 - first_datetime
new_writer_deadline_book02 = writer_deadline_book02 - first_datetime
new_writer_deadline_book03 = writer_deadline_book03 - first_datetime
new_writer_deadline_book04 = writer_deadline_book04 - first_datetime

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

hours_writer_deadline_book001 = new_writer_deadline_book001.days * 24 + new_writer_deadline_book001.seconds / 3600
hours_writer_deadline_book002 = new_writer_deadline_book002.days * 24 + new_writer_deadline_book002.seconds / 3600
hours_writer_deadline_book01 = new_writer_deadline_book01.days * 24 + new_writer_deadline_book01.seconds / 3600
hours_writer_deadline_book02 = new_writer_deadline_book02.days * 24 + new_writer_deadline_book02.seconds / 3600
hours_writer_deadline_book03 = new_writer_deadline_book03.days * 24 + new_writer_deadline_book03.seconds / 3600
hours_writer_deadline_book04 = new_writer_deadline_book04.days * 24 + new_writer_deadline_book04.seconds / 3600

print(f"Deadline for 2 module completed on {datetime_2m}.")
print(f"Deadline for 3 module completed on {datetime_3m}.")
print(f"Deadline for 4 module completed on {datetime_4m}.")
print(f"Deadline for 5 module completed on {datetime_5m}.")
print(f"Deadline for 6 module in {hours_6m} ({new_datetime_6m}).")
print(f"Deadline for 7 module in {hours_7m} ({new_datetime_7m}).")
print(f"Deadline for 8 module in {hours_8m} ({new_datetime_8m}).")
print(f"Deadline for 9 module in {hours_9m} ({new_datetime_9m}).")
print(f"Deadline for 10 module in {hours_10m} ({new_datetime_10m}).")
print(f"Deadline for 11 module in {hours_11m} ({new_datetime_11m}).")
print(f"Deadline for 12 module in {hours_12m} ({new_datetime_12m}).")

print(f"Deadline for novel 'Children of Five Stars' in {hours_writer_deadline_book001} ({new_writer_deadline_book001}).")
print(f"Deadline for novel 'Lirika CatTeoRee' in {hours_writer_deadline_book002} ({new_writer_deadline_book002}).")
print(f"Deadline for big novel 'Aezerlit' in {hours_writer_deadline_book01} ({new_writer_deadline_book01}).")
print(f"Deadline for big novel 'Yul and Ursa' in {hours_writer_deadline_book02} ({new_writer_deadline_book02}).")
print(f"Deadline for big novel 'Legend about Siyazeer' in {hours_writer_deadline_book03} ({new_writer_deadline_book03}).")
print(f"Deadline for big novel 'Legend about White Nunda' in {hours_writer_deadline_book04} ({new_writer_deadline_book04}).")
