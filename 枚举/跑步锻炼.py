import datetime

start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 10, 1)
total = 0

current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 0 or current_date.day == 1:
        total += 2
    else:
        total += 1
    current_date += datetime.timedelta(days=1)

print(total)