'''T = int(input())
l = []
for i in range(T):
    yeartime,daytime,offset = map(str,input().split())
    l.append([yeartime,daytime,offset])
print(l)
year = []
month = []
day = []
hour = []
minute = []
off = []

for i in range(T):
    year.append(l[i][0][0:4])
    month.append(l[i][0][5:7])
    day.append(l[i][0][8:10])
    hour.append(l[i][1][0:2])
    minute.append(l[i][1][3:5])
    off.append(l[i][2])
for i in range(T):
    y = 1970
    m0 = 1
    d = 1
    h = 0
    m = 0
    while y< int(year[i]):
        m+=int(offset)
        if m > 60:
            m-=60
            h+=1
        if h > 24:
            h-=24
            d+=1
        if d > 31:
            d-=31
            m0+=1
        if m0 > 12:
            m0-=12
            y+=1
    while m0 < int(month[i]):
        m+=int(offset)
        if m > 60:
            m-=60
            h+=1
        if h > 24:
            h-=24
            d+=1
        if d > 31:
            d-=31
            m0+=1
    while d < int(day[i]):
        m+=int(offset)
        if m > 60:
            m-=60
            h+=1
        if h > 24:
            h-=24
            d+=1
    while h < int(hour[i]):
        m+=int(offset)
        if m > 60:
            m-=60
            h+=1
    while m+int(offset) < int(minute[i]):
        m+=int(offset)
    if m > int(off[i]):
        m-=int(off[i])
        
    print(f'{y}-{m0:02d}-{d:02d} {h:02d}:{m:02d}:00')'''
#问题是还是需要用库函数，写的时候忘记库函数怎么写了，导致很烦
import datetime

T = int(input())
l = []
for i in range(T):
    # 保持输入处理方式
    parts = input().split()
    yeartime = parts[0]
    daytime = parts[1]
    offset = int(parts[2])
    l.append([yeartime, daytime, offset])

for case in l:
    # 合并日期时间字符串
    dt_str = f"{case[0]} {case[1]}"
    # 解析目标时间
    target_time = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    # 计算纪元时间
    epoch = datetime.datetime(1970, 1, 1)
    
    # 计算总秒数差
    delta = (target_time - epoch).total_seconds()
    total_minutes = int(delta // 60)
    
    # 计算最近的闹铃时间（保持offset变量名）
    x = case[2]
    remainder = total_minutes % x
    nearest_minutes = total_minutes - remainder
    
    # 转换回时间（保持变量名y,m0,d,h,m）
    nearest_time = epoch + datetime.timedelta(minutes=nearest_minutes)
    
    # 格式化输出（保持你的格式）
    print(nearest_time.strftime("%Y-%m-%d %H:%M:%S"))






    
