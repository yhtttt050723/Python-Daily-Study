'''
状态转移方程
dp[][][][] = max[][][][]
'''
N = int(input())
qt = [] #初始记录输入数据的一个列表
a,b,c = 1,1,1 #给a,b,c赋一个不全为零的初值方便后面控制输入输出
while a or b or c:#这一段只有在同时为零不进行循环
    a,b,c = map(int,input().split())#控制输入
    if a ==0 and b ==0 and c ==0:
        break
    d = [a,b,c] #用于暂存数据
    qt.append(d)
wz = [[0 for i in range(N+1)]for j in range(N+1)]#控制一个二维列表的生成
sd = [[[[0 for i in range(N+1)]for j in range(N+1)]for k in range(N+1)]for l in range(N+1)]
for i in qt:
    wz[i[0]][i[1]] = i[2]#在这里把上面数据输入到二维地图中
for i in range(1,N+1):
    for j in range(1, N + 1):
        for m in range(1, N + 1):
            for n in range(1, N + 1):
                sd[i][j][m][n] = max(sd[i-1][j][m-1][n],sd[i-1][j][m][n-1],sd[i][j-1][m-1][n],sd[i][j-1][m][n-1]) + wz[i][j] +wz[m][n]
                if i == m and j == n:#控制路径 不能让两次走同一条路
                    sd[i][j][m][n] -= wz[i][j]
print(sd[i][j][m][n])