T = int(input())
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
        
    print(f'{y}-{m0:02d}-{d:02d} {h:02d}:{m:02d}:00')
