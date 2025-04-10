#全排列数字生成
from itertools import permutations

nums = [1, 2, 3]
result = [list(p) for p in permutations(nums)]
print(result)
#组合数生成
from itertools import combinations
n = [1,2,3,4,5]
k = 3
l = list(x for x in combinations(n,k))
l1 = list(x for x in l)
print(l)
print(l1)