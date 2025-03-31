import math
d1,p1,q1,d2,p2,q2 = map(int,input().split())

#常数定义
g3 = pow(3,1/2)

#步数定义
dx = [-1,g3/2,g3/2,1,-g3,-g3]
dy = [0,-0.5,0.5,0,0.5,-0.5]

#初识位置定义 和 结束位置的二维平面定义
sx = dx[d1] * p1 + dx[(d1+2)%6] * q1
sy = dy[d1] * p1 + dy[(d1+2)%6] * q1

fx = dx[d2] * p2 + dx[(d2+2)%6] * q2
fy = dx[d2] * p2 + dx[(d2+2)%6] * q2

def dfs(x,y,step):
    if x == fx and y == fy:
        return step

    for i in range(len(dx)):
        xx = x + dx[i]
        yy = y + dy[i]
        if (xx != fx):
            dfs(xx,yy,step+1)

total = dfs(sx,sy,0)
print(total)