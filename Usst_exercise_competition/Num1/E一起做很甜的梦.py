n = int(input())
print("1 ", end = '')
a = range(2, n + 1)
a = a[::-1]
print(" ".join(map(str, a)))