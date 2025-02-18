#快速排序
def quick_sort(list,start = 0,end = None):
    #在定义函数参数时不可以使用可变对象的值作为参数值
    if end ==   None:
        end = len(list) - 1
    #终止条件判断
    if start >= end:
        return
    #基准选择
    mid_flag = int((start+end) / 2)
    flag = list[mid_flag]

    left,right = start,end

    #分区操作
    while left <= right:
        while list[left] < flag:
            left += 1
        while list[right] > flag:
            right -= 1
        if left <= right:
            list[left],list[right] = list[right],list[left]
            left += 1
            right -=1
            #为什么？这个递归会出现问题
        #正常情况下应该是开始到左，右到结束，这里为什么相反了？
    quick_sort(list,start,right)
    quick_sort(list,left,end)

list_test = [5,2,8,3,6,9,1]
quick_sort(list_test)
print(list_test)