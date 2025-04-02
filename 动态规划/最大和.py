'''
链接：https://www.lanqiao.cn/problems/2385/learning/?page=1&first_category_id=1&second_category_id=3&tag_relation=intersection&sort=difficulty&asc=1&tags=2022,%E7%9C%81%E8%B5%9B,%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92

'''
#输入
n = int(input())

values = list(map(int,input().split()))

'''
想着是记录所有可能然后直接max最大值
dfs?
'''

'''
def isPrim(n):
    if n <= 1: 
    return n
    i = 2
    while i*i < n:
        if n%i == 0: 
        list.append(i)
    return min(list)

'''
def D(n):
    nums = []
    if n <= 1:
        return n
    i = 2
    while i*i <= n:
        if n%i == 0:
            return i
        i += 1
    return n
#初始值规划
dp = [0] * (n+5)
dp[1] = values[0]

#状态转移方程
'''
dp[i] = dp[j] + values[i] j = p + 1 or j = p + D(n - p) 
'''

for i in range(2,n+1):
    limit = D(n - i + 1)
    #两种状态是 i + 1 or i + D (n - i)
    for j in range(max(1,limit),i):
        if dp[j] + values[i-1] >dp[i]:
            dp[i] = dp[j] + values[i-1]
print(dp[n])
