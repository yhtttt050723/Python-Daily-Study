'''from itertools import combinations
N,M,L,R =map(int,input().split())
n = []
pay = []
for road in range(M):
    y = list(map(int,input().split()))
    n.append([y[0:2]])
    pay.append(y[2])
real = []
for i in range(M):
    if L<=pay[i]<=R:
        real.append(n[i])
nums = []
for i in real:
    for j in i:
        for k in j:
            nums.append(k)
s = set(nums)
if len(s) != 2*len(real):
    w = [p for p in combinations(list(s),2)]
print(len(w))
'''
import sys
from sys import stdin

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))  # 城市编号从1开始
        self.size = [1]*(size+1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            if self.size[fx] < self.size[fy]:
                fx, fy = fy, fx
            self.parent[fy] = fx
            self.size[fx] += self.size[fy]

N, M, L, R = map(int, stdin.readline().split())
edges = []
for _ in range(M):
    u, v, w = map(int, stdin.readline().split())
    edges.append((w, u, v))

# 按过路费升序排序
edges.sort()

uf = UnionFind(N)
total = 0
counted = 0

# 处理w < L的边，预计算连通块
pre_uf = UnionFind(N)
for w, u, v in edges:
    if w >= L:
        break
    pre_uf.union(u, v)

# 处理L <= w <= R的边
for w, u, v in edges:
    if w > R:
        break
    if w < L:
        continue
        
    root_u = uf.find(u)
    root_v = uf.find(v)
    if root_u != root_v:
        # 获取预处理阶段的连通块大小
        pre_root_u = pre_uf.find(u)
        pre_root_v = pre_uf.find(v)
        if pre_root_u == pre_root_v:
            total += uf.size[root_u] * uf.size[root_v]
        uf.union(u, v)

# 统计最终结果
print(total)
