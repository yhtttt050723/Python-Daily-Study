#每一次消耗两个新硬币兑换一个旧硬币
#大的硬币肯定不行，因为没办法用小的硬币叠加，两个大硬币会浪费
#1到2023，猜测1012为最好的中间值，也就是说 两个1012，2024硬币为最多
#因为后面硬币比前面多 所以前面硬币直接累加就好
'''
total = 1012/2
for i in range(1,1012):
    total += i
print(total)
'''
#答案是错误的，那么我现在想写一段程序，可以算出n这个硬币能有多少个
'''n = 2024
total =0
for i in range(1,1012):
    total += i
print(total + 1012//2)'''
'''大概思路就是找起始位置终止位置，然后进行累加，如果是偶数再把最后那个两个能合成一个的加起来'''
'''首先可以确定一点，就是最后找的这个数字一定是比2023大的，也就是说在1到2023不会出现这个最大值'''
'''4000怎么算'''

'''
n = 4000
total = 0
start_position = n - 2023
end_position = n//2
print(end_position)
print(start_position)
for i in range(start_position,end_position):
    total += i
print(total)
if end_position%2 == 0:
    total = total + end_position//2
print(total)
'''
#那么具体就是以上步骤了，我现在只需要来一个列表，然后储存所有结果取最大值就行
total_list = []
for n in range(2024,4047):
    total = 0
    start_position = n - 2023
    end_position = n//2
    for i in range(start_position,end_position):
        total += i
    if end_position%2 ==0:
        total = total + end_position//2
    total_list.append(total)
print(max(total_list)+1)