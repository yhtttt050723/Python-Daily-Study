def D(n):
    if n <= 1:
        return n
    i = 2
    while i*i <= n:
        if n%i == 0:
            return i
        i += 1
    return n

print(D(9))#寻找最小因数

#存因数
def E(n):
    nums = []
    if n <= 1:
        nums.append(n)
        return nums
    i = 2
    while i*i <= n:
        if n%i == 0:
            nums.append(i)
        i += 1
    return nums

n = E(100)
print(n)