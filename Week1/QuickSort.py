#快速排序
def partition(arr,low=0,high=None):
    #参数值处理
    i = low-1
    if high ==  None:
        high = len(arr) - 1
    pivot = arr[high]#基准值取列表最后一个
    # 在j<=基准值时，把小的放前面，然后大于基准值放后面
    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    #取i+1这个位置，刚好时插入基准值可以分隔列表的位置
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def QuickSort(arr,low=0,high=None):
    flag = 0
    if high == None:
        high = len(arr) - 1
        #两次递归更新左右区间
    if low < high:
        flag = partition(arr,low,high)
        QuickSort(arr,low,flag-1)
        QuickSort(arr,flag+1,high)
    return arr

list = [2,1,4,3,6,8,7,11,45,12]
endlist = QuickSort(list)
print(endlist)