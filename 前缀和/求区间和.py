n = int(input())
ai = list(map(int,input().split()))
m = int(input())
left = []
right = []
for _ in range(m):
    a,b = map(int,input().split())
    left.append(a)
    right.append(b)

for i in range(0,m):
    print(sum(ai[left[i]-1:right[i]]))
#洛谷时间限制超出，蓝桥杯不会，这里不进行修改了