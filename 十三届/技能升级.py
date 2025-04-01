'''
第一次代码
N,M = map(int,input().split())
nums = []
total_list = []

for _ in range(N):
    row = list(map(int,input().split()))
    nums.append(row)
total = 0
def a(x = 0):
    global total
    for i in range(N):
        for j in range(M):
            ans = nums[i][0] // (nums[i][1]**M)
            total += ans
        total_list.append(total)
    return
a()

print(max(total_list)-1)
'''
import heapq

N, M = map(int, input().split())
heap = []

# 初始化最大堆，存储当前每个技能可提供的攻击力
for _ in range(N):
    A, B = map(int, input().split())
    if A > 0:
        heapq.heappush(heap, (-A, A, B))  # 用负数模拟最大堆

total = 0
count = 0

# 每次取出当前最大收益
while heap and count < M:
    current = heapq.heappop(heap)
    val = current[1]
    total += val

    # 计算下一次的收益
    next_val = val - current[2]
    if next_val > 0:
        heapq.heappush(heap, (-next_val, next_val, current[2]))

    count += 1

print(total)