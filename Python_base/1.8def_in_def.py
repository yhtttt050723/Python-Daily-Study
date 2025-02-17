def outer_def(name = "name"):
    '''
    函数内嵌套函数要注意返回值
    首先外部函数处理值，内部函数使用外部函数处理过的值
    然后在外部去返回内部函数，进而达到内部函数的同时使用
    :param name:
    :return:
    '''
    print("这是外层函数")
    def inner_def(name="name"):
        print(f"{name}你好")
        return None
    return inner_def(name)

outer_def("Slice")