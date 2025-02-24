'''
数列求值
题目描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
给定数列 1,1,1,3,5,9,17,⋯从第4项开始，每项都是前3项的和。
求第 20190324 项的最后4位数字。
运行限制
最大运行时间：1s
最大运行内存: 128M
'''
list = []

def FeiBoplus(list,N):
    a,b,c = 1,1,1
    list.append(1)
    for i in range(N):
        n = a
        if a > 10000:
            str_a = str(a)
            mid = str_a[-4:]
            n = int(mid)
            n,b,c = b,c,n+b+c
            list.append(n)
        else:
            a, b, c = b, c, a + b + c
            list.append(a)
    return list

endlist = FeiBoplus(list,50)
print(endlist)