n,S = map(int,input().split())

l = []
s = []
for _ in range(n):
    p,c = map(int,input().split())
    l.append(c)
    s.append(p)

total_S = []
while min(l) * sum(s) > min(l) * S:
    num_S = min(l)
    num_i = []
    for i in range(0,len(l)):
        if l[i] >= 0:
            l[i] = l[i] - num_S
        else:
            continue
    total_S.append(num_S)

pay_S = S *sum(total_S)

total_n = []
for i in range(0,len(l)):
    if l[i] ==0 :
        continue
    else:
        total_n.append(l[i]*s[i])

pay_n = sum(total_n)
print(pay_n+pay_S)