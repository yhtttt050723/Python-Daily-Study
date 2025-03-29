'''
奇怪的捐赠
题目描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

地产大亨 Q 先生临终的遗愿是：拿出100万元给 X 社区的居民抽奖，以稍慰藉心中愧疚。
麻烦的是，他有个很奇怪的要求：
100 万元必须被正好分成若干份（不能剩余）。每份必须是
7 的若干次方元。比如：
1 元,
7 元，
49 元，
343 元，...
相同金额的份数不能超过5份。

在满足上述要求的情况下，分成的份数越多越好！
请你帮忙计算一下，最多可以分为多少份？
运行限制
最大运行时间：1s
最大运行内存: 128M
'''
import math

total = 1000000
num = 0
list = []
'''while total!=0:
    for i in range(0,7):
        if total == 0:
            break
        for j in range(1,5):
            total = total - math.pow(7,i)*j
            if total <= 0:
                break
            num += j'''
for i in range(0,8):
    list.append(int(math.pow(7,i)))
'''for i in list:
    for j in range(0,6):
        if total == 0:
            break
        else:
            total = total - i*j
            num += j
print(num)'''
print(list)
total_1 = total - list[7]-list[6]
print(total_1)
total_2 = total_1 -3*list[5]
print(total_2)
total_3 = total_2 - 3*list[4]
print(total_3)
total_4 = total_3 - 3*list[3]
print(total_4)
total_5 =total_4 - 3*list[2]
print(total_5)