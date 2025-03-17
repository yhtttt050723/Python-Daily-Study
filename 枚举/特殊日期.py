import datetime
start_date = datetime.date(1900, 1, 1)
end_date = datetime.date(9999, 12, 31)
sum = 0
while start_date!=end_date:
    day = start_date.day
    month = start_date.month
    year = start_date.year
    total_day=0
    total_month=0
    total_year=0
    for i in str(day):
        total_day += int(i)
    for i in str(month):
        total_month += int(i)
    for i in str(year):
        total_year += int(i)
    if total_day+total_month == total_year:
        sum += 1
    start_date += datetime.timedelta(days = 1)
print(sum)