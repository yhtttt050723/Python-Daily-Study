'''
回溯算法
'''
def Meiju(n,k,path,used,result):
    if len(path) == k:
        result.append(path[:])
        return
    for i in range(1,n+1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        Meiju(n,k,path,used,result)
        path.pop()
        used[i] = False

n,k = map(int,input().split())
path = []
result = []
used = [False]*(n+1)
Meiju(n,k,path,used,result)
for p in result:
    print(' '.join(map(str,p)))