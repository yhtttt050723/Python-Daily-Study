'''
第一次错误代码
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
'''
#输入控制
d1, p1, q1, d2, p2, q2 = map(int, input().split())

# 定义每个方向对应的轴向坐标变化 (dq, dr) 步数定义
directions = [
    (-1, 0),   # 方向0
    (0, -1),   # 方向1
    (1, -1),   # 方向2
    (1, 0),    # 方向3
    (0, 1),    # 方向4
    (-1, 1)    # 方向5
]

#由于一开始是从 d 位置走的 这个函数用来计算初识和终止坐标
def compute_coords(d, p, q):
    # 计算两个方向的总坐标变化
    dir1 = directions[d]
    dir2 = directions[(d + 2) % 6]
    q_total = p * dir1[0] + q * dir2[0]
    r_total = p * dir1[1] + q * dir2[1]
    return q_total, r_total

# 计算两个点的轴向坐标
q1_total, r1_total = compute_coords(d1, p1, q1)
q2_total, r2_total = compute_coords(d2, p2, q2)

'''
上面的思路很好想
下面这个转化坐标很经典
'''

# 转换为立方体坐标并计算曼哈顿距离
x1, y1, z1 = q1_total, r1_total, -q1_total - r1_total
x2, y2, z2 = q2_total, r2_total, -q2_total - r2_total

distance = (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) // 2
print(distance)