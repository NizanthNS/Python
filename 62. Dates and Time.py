import datetime

date = datetime.date(2025, 10, 26)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y")

# print(date)
# print(today)
# print(time)
# print(now)

target_date = datetime.datetime(2020, 1, 2, 12, 30, 2)
current_time = datetime.datetime.now()

if target_date < current_time:
    print("Target date has passed")
else:
    print("Target date is not passed")