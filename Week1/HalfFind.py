#二分查找
def HalfFind(list,target = 0):
    list.sort()
    left = 0
    right = len(list) - 1
    while left<right:
        mid = (left+right) // 2
        if target == list[mid]:
            return mid
            break
        else:
            if list[mid] > target:
                right = mid - 1
            elif list[mid] < target:
                left = mid + 1
            else:
                return mid

list = [2,1,4,3,6,8,7,11,45,12]
num = HalfFind(list,6)
print(f'{num},{list[num]}')