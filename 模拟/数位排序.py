N = int(input())
position = int(input())
nums = [i for i in range(1,N+1)]
for i in (0,len(nums)-2):
    for j in (i+1,len(nums)-1):
        list_i = [int(i) for i in str(nums[i])]
        list_j = [int(j) for j in str(nums[j])]
        if sum(list_i) > sum(list_j):
            nums[i],nums[j] = nums[j],nums[i]
print(nums)