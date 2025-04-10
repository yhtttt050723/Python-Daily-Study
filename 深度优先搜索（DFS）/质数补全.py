t = int(input())
nums = []
for _ in range(t):
    n = input()
    nums.append(n)
'''for 35
for i in range(0,t):
    int_i = int(nums[i])
    for j in range(2,int(int_i**0.5+1)):
        if int_i%j == 0 :
            nums[i] = -1
            break
for item in nums:
    print(item)
    '''
#for 100
nums_big = []
for i in range(0,t):
    b = []
    for x in range(0,10):
        b.append(nums[i].replace("*",str(x)))
    nums_big.append(b)

nums_small = [-1]*t
for i in range(0,t):
    for j in nums_big[i]:
        flag = True
        s_j = int(j)
        for k in range(2,int(s_j**0.5+1)):
            if s_j%k ==0:
                flag = False
                continue
        if flag:
            nums_small[i] = j
            break

for item in nums_small:
    print(item)