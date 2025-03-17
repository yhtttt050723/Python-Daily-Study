#T1 奇怪的捐赠
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
n = 0
i = 0
sum = 0
flag_list = []
num_list = []
count_list = []
#通过判断去找最高次幂
while int(math.pow(7,n))<1000000:
    n += 1
for i in range(0,n):
    flag_list.append(int(math.pow(7,i)))
#print(flag_list)

for i in range (0,n):
    num_list.append(5)
#print(num_list)
def Greedy(list,list_num,list_count,total_num):
    list.sort(reverse = True)
    if total_num > 0:
        for i in range(0,len(num_list)):
            list_count.append(min(list_num[i],total_num//list[i]))
            total_num = total_num - list_count[i]*list[i]
    return list_count

end_list = Greedy(flag_list,num_list,count_list,1000000)
#print(end_list)
for i in range(0,len(end_list)):
    sum = sum + end_list[i]
print(sum)