#记录步数情况
dx = [0,0,1,-1]
dy = [-1,1,0,0]
#总数
ans = 0

#搜索
def dfs(x,y,step,grid):
    global ans
    if step == 16:
        ans += 1
        return
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < 4 and 0 <= yy <4:
            if grid[xx][yy] == 0:
                new_grid = [row[:] for row in grid]
                new_grid[xx][yy] = step + 1
                dfs(xx,yy,step +1,new_grid)

for i in range(4):
    for j in range(4):
        grid = [[0]*4 for _ in range(4)]
        grid[i][j] = 1
        dfs(i,j,1,grid)

print(ans)