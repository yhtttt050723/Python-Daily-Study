def greedy(n,a,s):
    count = 0
    for i in range(0,n):
        if s[i] == ('>'):
            if a[i] <= 0:
                count += 1
                a[i] = 1
        elif s[i] == ('<'):
            if a[i] >= 0:
                count += 1
                a[i] = -1
        elif s[i] == ('Z'):
            if i > 0:
                if a[i] * a[i-1]<=0:
                    count+=1
                    if a[i-1]>0:
                        a[i] = 1
                    elif a[i-1]<0:
                        a[i] = -1
                    else:
                        a[i] = 1
            else:
                pass
    return count

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    count = greedy(n,a,s)
    print(count)

