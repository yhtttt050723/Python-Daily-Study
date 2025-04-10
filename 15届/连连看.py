n,m = map(int,input().split())

l = []

for i in range(n):
    row = list(map(int,input().split()))
    l.append(row)
ans = 0
for row1 in range(n):
    for line1 in range(m):
        for row2 in range(n):
            for line2 in range(m):
                abs1 = abs(row1-row2)
                abs2 = abs(line1-line2)
                if abs1 == 0:
                    continue
                if abs2 == 0:
                    continue
                if l[row1][line1] == l[row2][line2]:
                    if abs1 == abs2:
                        ans+=1
print(ans)
