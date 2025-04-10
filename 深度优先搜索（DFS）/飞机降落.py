'''
最早t
最晚t+d
降落需要时间l
'''
from itertools import permutations
def Paixu(N):
    l = [x for x in range(N)]
    result = [list(p) for p in permutations(l)]
    return result

def dfs(result,ti,di,li,N):
    for order in result:
        now = 0
        flag = True

        for plane in order:
            T = ti[plane]
            D = di[plane]
            L = li[plane]
            start = max(now,T)
            if start>D+T:
                flag = False
                break
            now = start+L
        if flag:
            return True
    return False

T = int(input())
end = []
for _ in range(T):
    N = int(input())
    ti = []
    di = []
    li = []
    for _ in range(N):
        t,d,l = map(int,input().split())
        ti.append(t)
        di.append(d)
        li.append(l)
    result = Paixu(N)
    if dfs(result,ti,di,li,N):
        end.append('YES')
    else:
        end.append('NO')
for item in end:
    print(item)