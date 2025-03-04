'''
递归算法由一个基准条件和递归步骤组成
'''
def exchange(num,exchange_num,end_num = []):
    Big_num = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    if exchange_num > 16 or exchange_num < 2:
        return print('输入的转换进制错误')
    if num == 0:
        end_num.append(Big_num[num % exchange_num])
        return end_num
    else:
        end_num.append(Big_num[num % exchange_num])
        num = num // exchange_num
        return exchange(num,exchange_num,end_num)

n,m = map(int,input().split())
test = exchange(n,m,[])
test.reverse()
real_num = test[1:]
print(''.join(map(str,real_num)))