a,b,c = map(int,input().split())
'''
就是说找abc三个数的最小公倍数
'''
num = 1
while True:
    if num % a == 0 and num % b == 0 and num % c == 0:
        print(num)
        break
    else:
        num += 1
