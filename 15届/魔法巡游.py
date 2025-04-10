'''N =int(input())
si = list(map(int,input().split()))
ti = list(map(int,input().split()))
for i in range(N):
    s_i = str(si[i])
    if '0' in s_i:
        continue
    if '2' in s_i:
        continue
    if '4' in s_i:
        continue
    si[i] = -1

for i in range(N):
    t_i = str(ti[i])
    if '0' in t_i:
        continue
    if '2' in t_i:
        continue
    if '4' in t_i:
        continue
    ti[i] = -1
result = []
def dfs(si,ti,ans):
    if sum(si) == len(si)*(-1):
        result.append(ans)
        return
    if sum(ti) == len(ti)*(-1):
        result.append(ans)
        return
    for i in range(0,len(si)):
        if si[i] == -1:
            break
        for j in range(0,len(ti)):
            if ti[j] == -1:
                break
            if ti[j] > si[i]:
                si[i] = -1
                dfs(si,ti,ans+1)
            else:
                continue
print(result)'''
#动规题解不想看
import sys

def has_magic(num):
    s = str(num)
    return '0' in s or '2' in s or '4' in s

N = int(sys.stdin.readline())
si = list(map(int, sys.stdin.readline().split()))
ti = list(map(int, sys.stdin.readline().split()))

# 预处理有效标记（保持变量名si/ti）
valid_s = [has_magic(x) for x in si]
valid_t = [has_magic(x) for x in ti]

max_len = 0
# 动态规划变量（保持你的result命名思路）
dp_s = [0] * (N+1)  # 最后选的是小蓝
dp_t = [0] * (N+1)  # 最后选的是小桥

for i in range(N):
    # 处理小蓝的符文石
    if valid_s[i]:
        dp_s[i+1] = 1  #一个的情况
        # 找前面小桥的有效符文石
        for j in range(i):
            if valid_t[j] and j < i and (has_magic(si[i]) or has_magic(ti[j])):
                dp_s[i+1] = max(dp_s[i+1], dp_t[j+1] + 1)
        max_len = max(max_len, dp_s[i+1])
    
    # 处理小桥的符文石
    if valid_t[i]:
        dp_t[i+1] = 1  # 单独一个的情况
        # 找前面小蓝的有效符文石
        for j in range(i):
            if valid_s[j] and j < i and (has_magic(ti[i]) or has_magic(si[j])):
                dp_t[i+1] = max(dp_t[i+1], dp_s[j+1] + 1)
        max_len = max(max_len, dp_t[i+1])

print(max_len * 2 if max_len > 0 else 0)
        

