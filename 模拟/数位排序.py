'''
N = int(input())
position = int(input())
nums = [str(i) for i in range(1,N+1)]

sumlist = []

for i in range(0,len(nums)):
    s = 0
    for j in nums[i]:
        s += int(j)
    sumlist.append((i+1,s))

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
            if sumlist[i][1] > sumlist[j][1]:
                nums[i],nums[j] = nums[j],nums[i]
                sumlist[i],sumlist[j] = sumlist[j],sumlist[i]

print(int(nums[position-1]))
'''
N = int(input())
position = int(input())

nums = [str(x) for x in range(1,N+1)]

sort_nums = sorted(nums,key=lambda x:(sum(int(i) for i in x),int(x)))

print(sort_nums[position-1])