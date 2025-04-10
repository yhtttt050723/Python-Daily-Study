T = int(input())
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

    c1 = 0
    c2 = 0

    for i in range(0,len(s)):
        if flag1[i] == s[i]:
            c1 += 1
        if flag2[i] == s[i]:
            c2 += 1

    total = min(c1,c2)
    return total

for _ in range(T):
    n = int(input())
    s = input().strip()
    total = greedy(n,s)
    print(total//2)