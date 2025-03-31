#输入
N,K = map(int,input().split())
a = []
#生成矩阵
for _ in range(N):
        row = list(map(int,input().split()))
        a.append(row)

#控制步数
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

#总排序
total_list = []

#搜索
def dfs(x,y,list):
    #控制终止条件
    if x == N-1 and y == N-1:
        total_list.append(list)
        return
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        #控制递归语句
        if 1<= xx <= N and 1<= yy <=N and a[xx][yy] == a[x][y] +1:
            list.append(i)
            dfs(xx,yy,list)

s = []
dfs(0,0,s)
print(min(total_list))