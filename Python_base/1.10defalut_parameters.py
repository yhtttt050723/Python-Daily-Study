#缺省函数 为函数传递元素值添加默认值，提高可读性避免错误
def greet(name="name",message="你好"):
    print(f"{name},{message}")
    return None
greet("王伟")

def add_list1(value,list=[]):
    list.append(value)
    return list
print(add_list1(1))
print(add_list1(2)) #会重复函数内容，即保存上面添加1 的内容添加2

def add_list2(value,list=None):
    if list is None:
        list = []
    list.append(value)
    return list
print(add_list2(1))
print(add_list2(2))#此时就不会保存，但是如果默认值为None 就会导致需要在函数重新申明这个元素的内容
