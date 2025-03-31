n = int(input())
m = int(input())

nums = [str(i) for i in range(1,n+1)]
sorted_num = sorted(nums,key = lambda x:(sum(int(i) for i in x),int(x)))

print(sorted_num[m - 1])