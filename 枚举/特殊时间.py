'''import datetime
starttime = datetime.datetime(1000,1,22,22,2)
endtime = datetime.datetime(9999,12,31,23,59)
sum = 0
while starttime!=endtime:
    #处理年份
    year = starttime.year
    list_year = []
    for i in str(year):
        list_year.append(i)
    #处理月份
    month = starttime.month
    list_month = []
    for i in str(month):
        list_month.append(i)
    if month < 10:
        list_month.append('0')
    day = starttime.day
    #处理日期
    list_day = []
    for i in str(day):
        list_day.append(i)
    if day < 10:
        list_day.append('0')
    #处理小时
    hour = starttime.hour
    list_hour = []
    for i in str(hour):
        list_hour.append(i)
    if hour < 10:
        list_hour.append('0')
    #处理分钟
    minute = starttime.minute
    list_minute = []
    for i in str(minute):
        list_minute.append(i)
    if hour < 10:
        list_minute.append('0')
    #判断
    for i in range(0,10):
        if list_year.count(str(i)) == list_month.count(str(i))+list_day.count(str(i)) and list_month.count(str(i))+list_day.count(str(i))==list_hour.count(str(i))+list_minute.count(str(i)):
            sum+=1
    starttime += datetime.timedelta(minutes=1)
print(sum - 1)
'''
#合法的日期（月日）取值仅有以下16种：
#0111,0222,1011,1211,1222,1101,1121,1110,1112,1113,1114,1115,1116,1117,1118,1119
#创建一个列表分别储存每个日期（月日）对应的合法时间个数：
time=[4,4,4,4,4,4,4,4,4,3,3,3,2,2,2,2]
#年份无限制，每个数乘4即可
year=[4*i for i in time]
print(sum(year))