def DeepFind(N,A,B,Ks,sum):
    if A < 1 or A > N:
        return -1
    if A == B :
        return sum
    if A > B:
        new_A = A - Ks[A - 1]
        if new_A >= 1:  # 确保不会跳到无效层
            result = DeepFind(N, new_A, B, Ks, sum + 1)
            if result != -1:
                return result
    else:
        new_A = A + Ks[A - 1]
        if new_A <= N:
            result = DeepFind(N, new_A, B, Ks, sum + 1)
            if result != -1:
                return result
    return -1

'''
N为总层数，A为起始层
B为终止层，Ks为每一层对应的数字
'''
N,A,B = map(int,input().split())
Ks = list(map(int, input().split()))
if len(Ks) != N:
    print("输入错误")
else:
    sum_end = DeepFind(N,A,B,Ks,0)
    print(sum_end)