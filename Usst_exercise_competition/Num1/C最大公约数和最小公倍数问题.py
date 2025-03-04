'''

'''
x0,y0 = map(int,input().split())
if y0 % x0 != 0:
    print(1)
else:
    k = y0 // x0
    if k == 1:
        print(1)
    else:
        m = 0
        temp = k
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                m += 1
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            m += 1
        print(2 ** m)