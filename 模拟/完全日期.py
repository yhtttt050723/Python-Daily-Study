import datetime
start_time = datetime.date(2001,1,1)
end_time = datetime.date(2021,12,31)

total = 0

while start_time <= end_time:
    year = 0
    month = 0
    day = 0
    for i in str(start_time.year):
        year += int(i)
    for i in str(start_time.month):
        month += int(i)
    for i in str(start_time.day):
        day += int(i)
    if year+month+day == 9 or year+month+day == 16 or year+month+day == 25:
        total+=1
    start_time += datetime.timedelta(days=1)
print(total)