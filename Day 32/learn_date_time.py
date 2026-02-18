import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.day

date_of_birth = dt.datetime(year=2002, month=2, day=24, hour=19, minute=30)
print(date_of_birth)
