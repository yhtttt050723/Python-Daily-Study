a,b,x,y = map(int,input().split())

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
    num_y = min(a,b) // y
    num_xa = (a - y * num_y) // x
    num_xb = (b - y * num_y) // x
    total = num_xa + num_xb + num_y

print(total)