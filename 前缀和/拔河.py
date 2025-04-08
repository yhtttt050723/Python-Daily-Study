n = int(input())
ai = list(map(int,input().split()))

left = 0
right = n-1
total = []
while left != n:
    listleft = ai[0:left]
    listright = ai[left:]
    total.append(abs(sum(listleft) - sum(listright)))
    left+=1
print(min(total))