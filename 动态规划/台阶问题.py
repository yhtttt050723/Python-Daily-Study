'''
链接：https://www.luogu.com.cn/problem/P1192
题目描述
有 N 级台阶，你一开始在底部，每次可以向上迈 1∼K 级台阶，问到达第 N 级台阶有多少种不同方式。
输入格式
两个正整数 N,K。
输出格式
一个正整数 ans(mod100003)，为到达第 N 级台阶的不同方式数。
'''

#控制输入
N,K = map(int,input().split())

#初识dp数组
dp = [0] * 1000000
dp[0] = 1 #第零级只有一种方法走

#递推关系
'''
dp [5] = dp[3] + dp[2] 就是上三级的可能加上两级的可能
dp[n] = dp[i] + dp[n-i] #i 与n保持一致
'''
for i in range(1,N+1):
    #K是上台阶情况的遍历
    for j in range(1,K+1):
        if i - j >=0:
            dp[i] = (dp[i] + dp[i-j]) % 100003
print(dp[N])