#精度问题导致这个方法不可行
'''
num = int(input())
sum = int(num*(num+1)*(2*num+1)/6)
print(sum % 1000000007)
'''
#另一种方法
'''
费马小定理：
一个任意整数a 一个素数p
a的p-1次方模p为一
math.pow(a,p-1)%p = 1
'''
#快速幂策略 用于高效计算a的b次方模m的问题
num = int(input())
mod = 1000000007
a = num % mod
b = (num+1) % mod
c = (2*num+1) % mod
inv_6 = pow(6,mod-2,mod)
product1 = a * b % mod
product2 = product1 * c % mod
result = product2 * inv_6 % mod
print(result)