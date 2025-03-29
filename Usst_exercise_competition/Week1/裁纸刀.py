#T3 裁纸刀
'''问题描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

小蓝有一个裁纸刀，每次可以将一张纸沿一条直线裁成两半。

小蓝用一张纸打印出两行三列共 6 个二维码，至少使用九次裁出来，下图给出了一种裁法。

图片描述

在上面的例子中，小蓝的打印机没办法打印到边缘，所以边缘至少要裁 4 次。另外，小蓝每次只能裁一张纸，不能重叠或者拼起来裁。

如果小蓝要用一张纸打印出 20 行 22 列共 440 个二维码，他至少需要裁多少次？

运行限制
最大运行时间：1s
最大运行内存: 256M
'''
#print(24-3-3-2-2 -4-4-2-2-2)
'''total_num = 4 * 440
line = 22
width = 20
beside_total_num = total_num - (width+line) * 2
num=[4]
sum = 0
#先对列进行裁剪
for i in range(0,line):
    total_num = total_num - 2 * width
    num.append(1)
#print(total_num)
#print(num)
#对行进行裁剪
for i in range(0,width):
    total_num = total_num -2 * line
    num.append(1)
#print(total_num)
#print(num)

for i in range(0,len(num)):
    sum += num[i]
print(sum)'''
# 计算行和列的分割次数
rows = 20
cols = 22

# 边缘裁剪次数
edge_cuts = 4

# 行分割次数（每次将纸张分成更多的行）
row_cuts = rows - 1

# 列分割次数（每行需要分割cols-1次，总共有rows行）
col_cuts = (cols - 1) * rows

# 总裁剪次数
total_cuts = edge_cuts + row_cuts + col_cuts

print(total_cuts)