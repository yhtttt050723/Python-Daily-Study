#冒泡排序
def Paixu(list1):
    num_len = len(list1)
    for i in range(num_len):
        for j in range(num_len - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1
list2 = [4,3,5,1,8,6,9]
print(Paixu(list2))
'''
为什么刚刚调试会出错？
在于外层循环并不会继续进行
所以只会比较在当前位置到最后位置的比较次数
即每次排序并不会比较这个位置数字之前的数字
所以会导致出错
'''