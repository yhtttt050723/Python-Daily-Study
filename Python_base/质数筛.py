n = 10000  # 代求的范围中的最大值
k = 0
s = [True for i in range(n)]  # 首先默认所有数都是质数
z = []
for i in range(2, n):
    if s[i]:  # 判断是否为质数，如果没有被标记过，就是质数
        k += 1
        z.append(i)  # 添加质数
        for j in range(i + i, n, i):  # 将是指数的倍数的数都改为False
            s[j] = False

print(k)  # 个数
print(z)  # 质数

n = 151
k = 0
z = []
for i in range(2, n):
    for j in range(2, int(i ** 0.5) + 1):  # 开方，减少循环的次数
        if i % j == 0:
            break
    else:
        k += 1
        z.append(i)
print(k)  # 个数
print(z)  # 质数
