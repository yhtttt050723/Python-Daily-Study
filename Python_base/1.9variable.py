list1 = [2,3,1,5,3,2,1,6,7,4,3,9]
def compare(list):
    a=10
    list.append(a)
    list.sort()
    return list #a为函数内变量，为局部变量，函数外不可用，list1为全局变量，函数内外可用
endlist1 = compare(list1)
print(endlist1)