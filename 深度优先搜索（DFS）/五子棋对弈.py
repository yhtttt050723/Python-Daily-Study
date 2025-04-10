from itertools import permutations
l = [[0]*5 for x in range(0,5)]
n = [0,1,2,3,4]

#统计
d = list(x for x in permutations(n,2))
for i in range(0,5):
    d.append((i,i))

ans = 0
total = 0
def dfs(l):
    global ans
    if 0 not in l:
        ans+=1
        return
    for i in range(len(d)):
        for j in range(len(d)):
            x = 0
            y = 0
            xx = x + d[i][j]
            yy = y + d[i][j]
            if l[xx][yy] == 0:
                if total%2==0:
                    l[xx][yy] = 1
                else:
                    l[xx][yy] = -1
            else:
                dfs(l)
print(ans)