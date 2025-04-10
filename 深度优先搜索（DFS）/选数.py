from itertools import combinations
n,k = map(int,input().split())
xi = list(map(int,input().split()))

l = list(combinations(xi,k))
nums = list(sum(x) for x in l)
result = 0

for i in nums:
    if i < 2:
        continue
    else:
        flag = True
        for j in range(2,int(i**0.5+1)):
            if i%j ==0:
                flag =False
                break
        if flag:
            result+=1
print(result)