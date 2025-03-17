#选质数代码
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

total_list = []
#只能是这几个数字组成的数字并且是质数才能是纯质数
digit = ['2','3','5','7']
for i in range(1,20210606):#20210606
    str_i = str(i)
    if all(num in digit for num in str_i):
        if is_prime(i):
            total_list.append(i)

print(total_list)
print(len(total_list))