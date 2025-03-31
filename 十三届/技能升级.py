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