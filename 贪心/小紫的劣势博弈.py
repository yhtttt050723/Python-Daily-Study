n = int(input())
nums = list(map(int,input().split()))

def greedy(nums):
    s_nums = sorted(nums,reverse=True)
    total = 0
    for i in range(0,len(nums)):
        if i % 2 == 0:
            total += s_nums[i]
        else:
            total -= s_nums[i]
    return total

total = greedy(nums)
print(total)