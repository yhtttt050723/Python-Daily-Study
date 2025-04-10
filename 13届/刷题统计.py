a,b,n = map(int,input().split())

week = n//(5*a + 2*b)
nums = [a,a,a,a,a,b,b]
num_week = week * sum(nums)
total = n - num_week

num_day = 0
for i in nums:
    total -= i
    num_day += 1
    if total <= 0:
        break
print(num_day+week*7)