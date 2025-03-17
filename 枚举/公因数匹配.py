import math
# 读取输入的第一行，包含一个整数 n
n = int(input().strip())

# 读取输入的第二行，包含 n 个整数
input_nums = input().strip()

# 将读取到的字符串转换为整数列表
A = list(map(int, input_nums.split()))

digit = [(x,y) for x in A for y in A if x != y]

#把互为质数的去掉
for i in range(0,len(A)):
    for j in range(0,len(A)):
        if math.gcd(A[i],A[j]) == 1:
            digit.remove((A[i],A[j]))
'''
然后现在就都不是质数了，可以把重复去掉
'''

print(digit)