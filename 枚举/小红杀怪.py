'''a,b,x,y = map(int,input().split())

#单体x
#群体y

#单体伤害高于群体伤害时
if x > y:
    total = 0
    flag = False
    while a != 0 and b != 0:
        num_a = a // x
        num_b = b // x
        a = a - num_a * x
        b = b - num_b * x
        while a % y != 0:
            a = a + x
            num_a -= 1
        while b % y != 0:
            b = b + x
            num_b -= 1
        while a // y != b // y:
            if a //y >b//y:
                b = b + x
                num_b -= 1
            else:
                a = a + x
                num_a -=1
        if a//y == b//y:
            flag = True
        total = num_a +num_b+a//y
        if flag:
            break

elif x == y:
    num_y = min(a,b) // y
    num_xa = (a - y*num_y) // x
    num_xb = (b - y*num_y) // x
    total = num_xa+num_xb+num_y

else:
    total = 0
    flag = False
    num_a = 0
    num_b = 0
    while a != 0 and b != 0:
        num_y = min(a,b) // y
        a = a-num_y*y
        b = b-num_y*y
        while a % x != 0 or b % x != 0:
            a = a + y
            b = b + y
            num_y -= 1
        if a % x == 0 and b % x == 0:
            num_a = a // x
            num_b = b // x
            flag = True
        if flag:
            total = num_y + num_a + num_b
            break
print(total)'''

a,b,x,y = map(int,input().split())
min_total = float('inf')
max_k = max(a//y + 10,b//y + 10)

for k in range(0,max_k):
    rem_a = max(a - k * y, 0)
    rem_b = max(b - k * y, 0)

    f_a = (rem_a+x-1) // x if rem_a > 0 else 0
    f_b = (rem_b+x-1) // x if rem_b > 0 else 0

    total = k + f_a + f_b
    if total < min_total:
        min_total = total
print(min_total)