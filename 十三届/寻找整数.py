'''
11 和 17 的倍数
'''
#N = 11 * 17
nums = []
listnum = []
more_nums = [0,1,2,1,4,5,4,1,2,9,0,5,10,11,14,9,0,11,18,9,11,11,15,17,9,23,20,25,16,29,27,25,11,17,4,29,22,37,23,9,1,11,11,33,29,15,5,41,46]
'''
for i in range(304991798969,10**17,N*2):#判断函数
    v = True
    for j in range(0, len(more_nums)):
        if i % (j + 1) != more_nums[j]:
            v = False
            break
    if v:
        nums.append(i)
print(nums)
'''

N = 1467466423049 - 1460334676889
for i in range(1460334676889,10**17,N):
    if i%44==33 and i%45==29 and i%46==15 and i%47==5 and i%48==41 and i%49==46:
        listnum.append(i)

for i in listnum:#判断函数
    v = True
    for j in range(0, len(more_nums)):
        if i % (j + 1) != more_nums[j]:
            v = False
            break
    if v:
        nums.append(i)
print(nums)

#1467466423049,1460334676889这个数字是通过暴力找出来的,前面的数字认证过是不符合的
#步长优化 是通过两个相邻的数字相减去得到的
#步长优化过后会导致遍历次数大大减少
