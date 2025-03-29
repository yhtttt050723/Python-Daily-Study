'''
def jisuan(num,k = 0):
    list = []
    for char in str(num):
        list.append(int(char))
    k = sum(list)
    if k > 10:
        return jisuan(k,0)
    else:
        return k

num = int(input())
k = jisuan(num,0)
print(k)
'''
n = int(input())
print(n % 9 or 9)