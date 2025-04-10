n = int(input())
l = []

for _ in range(n):
    s,b = map(int,input().split())
    l.append([s,b])

si = [x[0] for x in l]
bi = [x[1] for x in l]

total_s = []
index_s = []
for i in range(0,n):
    for j in range(n-1,i,-1):
        index_s.append([i,j])

for i in index_s:
    sm = 1
    for j in range(i[0],i[1]+1):
        sm *= si[j]
    total_s.append(sm)

for i in range(0,n):
    total_s.append(si[i])

total_b = []
index_b = []
for i in range(0,n):
    for j in range(n-1,i,-1):
        index_b.append([i,j])

for i in index_s:
    bm = 0
    for j in range(i[0],i[1]+1):
        bm += bi[j]
    total_b.append(bm)

for i in range(0,n):
    total_b.append(bi[i])

nums = []
for i in range(0,len(total_s)):
    nums.append(abs(total_s[i] - total_b[i]))
print(min(nums))