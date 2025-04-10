from itertools import permutations,combinations
T = int(input())
ni = []
for i in range(T):
    n = int(input())
    ni.append(n)

l = []
for i in ni:
    flag = [-1,1] * i
    l = set(x for x in permutations(flag,i))
    ans = 0
    for j in l:
        for k in range(0,i):
            if j[k] == 1:
                if j[(k+1)%i]*j[(k+2)%i] > 0:
                    ans += 1
            if j[k] == -1:
                if j[(k+1)%i]*j[(k+2)%i] < 0:
                    ans += 1
    print(ans//2)
        
