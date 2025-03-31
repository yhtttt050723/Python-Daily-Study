#输入
N = int(input())
tri = []
for i in range (N):
    tri.append(list(map(int,input().split())))

#总和定义
total_list = []

#步定义
dy = [0,1]

#搜索
def dfs(x = 0,y = 0,total = tri[0][0]):
    if (x == N-1):
        total_list.append(total)
        return
    for i in range(2):
        xx = x + 1
        yy = y + dy[i]
        if ( xx <= N and 0 <= yy <= xx):
            dfs(xx,yy,total+tri[xx][yy])

dfs(0,0)

print(max(total_list))
