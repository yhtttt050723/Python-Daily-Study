'''from itertools import permutations,combinations
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
   '''
#错的，看了题解
#问题是用户的原始代码尝试生成所有可能的排列，并检查每个排列是否满足条件，
#然后统计说谎者的数量。
#这种方法在小n时可行，但当n很大时，时间复杂度会爆炸，无法处理。
T = int(input())
ni = []
for _ in range(T):
    n = int(input())
    ni.append(n)

for i in ni:
    if i % 3 == 0:
        print(2 * i)
    else:
        print(i)
