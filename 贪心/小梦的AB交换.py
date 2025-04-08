def greedy(n,s):
    flag1 = []
    flag2 = []

    for i in range(0,2*n):
        if i % 2 == 0:
            flag1.append('A')
            flag2.append('B')
        else:
            flag1.append('B')
            flag2.append('A')

    str1 = 0
    str2 = 0

    for i in range(0,len(s)):
        if flag1[i] == s[i]:
            str1 += 1
        if flag2[i] == s[i]:
            str2 += 1

    total = min(str1,str2)
    print('')
    return total

T = int(input())

for _ in range(T):
    n = int(input())
    s = input()
    total = greedy(n,s)
    if len(s) != n*2:
        continue
    print(total//2)