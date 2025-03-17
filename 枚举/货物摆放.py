N = 2021041820210418
list_N = [1,N]
t = int(N ** 0.5) + 1
for i in range(2,t):
    fn,sn = divmod(N,i)
    if sn == 0:
        list_N.append(i)
        list_N.append(fn)
res_s = set()
for i in list_N:
    for j in list_N:
        temp = i * j
        fn2,sn2 = divmod(N,temp)
        if sn2 == 0:
            res_s.add((i,j,fn2))
print(len(res_s))