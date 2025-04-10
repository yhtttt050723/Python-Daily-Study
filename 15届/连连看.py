'''n,m = map(int,input().split())

l = []

for i in range(n):
    row = list(map(int,input().split()))
    l.append(row)
ans = 0
for row1 in range(n):
    for line1 in range(m):
        for row2 in range(n):
            for line2 in range(m):
                abs1 = abs(row1-row2)
                abs2 = abs(line1-line2)
                if abs1 == 0:
                    continue
                if abs2 == 0:
                    continue
                if l[row1][line1] == l[row2][line2]:
                    if abs1 == abs2:
                        ans+=1
print(ans)'''
#这个遍历时间太长拿了7分，看了下题解，只能是对角线或者反对角线
#也就是说先判断是不是对角线 然后判断是不是相等
import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
l = []  # 保持你的二维数组名字

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    l.append(row)

ans = 0  # 保持结果变量名

# 改为统计法 (保留你的数据处理方式)
# 创建两种字典：主对角线(i-j)和反对角线(i+j)的数值出现计数
main_diag = defaultdict(lambda: defaultdict(int))  # {数值: {对角线编号: 个数}}
anti_diag = defaultdict(lambda: defaultdict(int))

for row in range(n):  # 保持你的行变量名
    for line in range(m):  # 保持你的列变量名
        val = l[row][line]
        main_key = row - line  # 主对角线特征
        anti_key = row + line  # 反对角线特征
        
        # 统计主对角线
        main_diag[val][main_key] += 1
        # 统计反对角线
        anti_diag[val][anti_key] += 1

# 计算对数 (保持你的ans变量名)
for val in main_diag:
    for cnt in main_diag[val].values():
        ans += cnt * (cnt - 1)

for val in anti_diag:
    for cnt in anti_diag[val].values():
        ans += cnt * (cnt - 1)

print(ans) 








