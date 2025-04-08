# 给定数组，选择若干个数字做 and 运算，最小化结果
nums = [7, 5, 3, 1]
result = nums[0]
for num in nums[1:]:
    result &= num
print(result)