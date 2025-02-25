'''import random
#纸杯数
n = int(input())
#操作数
m = int(input())
#纸杯排序
nums = []
for i in range(0,n):
    num = int(input())
    nums.append(num)
'''
'''
#随机交换
flag1 = 0
flag2 = 0
for i in range(0,m+1):
    flag1 = random.randint(0,n - 1)
    flag2 = flag1
    while flag1 == flag2:
        flag2 = random.randint(0,n-1)
    if flag1 != flag2:
        nums[flag1],nums[flag2] = nums[flag2],nums[flag1]
        print(f'{nums[flag1]} {nums[flag2]}')
print(' '.join(map(str,nums)))
'''
n,m = map(int,input().split())
nums = list(map(int,input().split()))
for i in range (0,m):
    u,v = map(int,input().split())
    v = v-1
    u = u-1
    nums[u],nums[v] = nums[v],nums[u]
print(' '.join(map(str,nums)))