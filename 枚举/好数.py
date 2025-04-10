n = int(input())
list0 = []
for i in range(0,n+1):
    s_i = list(str(i))[::-1]
    #标志变量
    flag = False
    for i in range(0,len(s_i),2):
        if int(s_i[i]) % 2 != 1:
            flag = True
            continue
    if flag:
        continue
    for i in range(1,len(s_i),2):
        if int(s_i[i]) % 2 != 0:
            flag = True
            continue
    if flag:
        continue

    list0.append(i)
print(len(list0))
'''
遍历效率低下
应该在范围内直接构造好数
'''