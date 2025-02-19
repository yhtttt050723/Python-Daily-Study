#插入排序
def Insert(list,start = 0,end = None):
    new_list = list.copy()
    if end == None:
        end = len(list)
    for i in range(start + 1,end):
        key = new_list[i]
        j = i - 1
        while j >= start and key < new_list[j]:
            new_list[j+1] = new_list[j]
            j -= 1
        new_list[j+1] = key
    return new_list

list_test = [3,1,5,6,2,0]
test = Insert(list_test)
print(test)