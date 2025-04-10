from itertools import combinations
N,M,L,R =map(int,input().split())
n = []
pay = []
for road in range(M):
    y = list(map(int,input().split()))
    n.append([y[0:2]])
    pay.append(y[2])
real = []
for i in range(M):
    if L<=pay[i]<=R:
        real.append(n[i])
nums = []
for i in real:
    for j in i:
        for k in j:
            nums.append(k)
s = set(nums)
if len(s) != 2*len(real):
    w = [p for p in combinations(list(s),2)]
print(len(w))
