total = 0
for n in range(1,2025):
    ans = 0
    i = n
    j = n
    i1 = n
    j1 = n
    while i >= 4:
        i //= 4
        ans += 1
    l = []
    for i in range(ans,-1,-1):
        s = j//(4**i)
        j = j - (4**i)*s
        l.append(s)
    ans1 = 0
    while i1 >= 2:
        i1 //= 2
        ans1 += 1
    l1 = []
    for i in range(ans1,-1,-1):
        s1 = j1//(2**i)
        j1 = j1 - (2**i)*s1
        l1.append(s1)
    if sum(l) == sum(l1):
        total+=1
print(total)


