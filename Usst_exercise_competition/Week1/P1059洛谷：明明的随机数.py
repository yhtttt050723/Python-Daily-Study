'''
题目描述
明明想在学校中请一些同学一起做一项问卷调查，
为了实验的客观性，
他先用计算机生成了 N 个 1 到 1000 之间的随机整数 (N≤100)，
对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请
你协助明明完成“去重”与“排序”的工作。
输入格式
输入有两行，第 1 行为 1 个正整数，表示所生成的随机数的个数 N。
第 2 行有 N 个用空格隔开的正整数，为所产生的随机数。
输出格式
输出也是两行，第 1 行为 1 个正整数 M，表示不相同的随机数的个数。
第 2 行为 M 个用空格隔开的正整数，为从小到大排好序的不相同的随机数。
'''
import random
num = int(input())
number = []
for i in range(num):
    number.append(random.randint(1,1000))
set_num = set(number)
while len(set_num) != num:
    set_num.add(random.randint(1,1000))
n = sorted(set_num)
print(num)
print(' '.join(map(str,n)))