#基于位置的不定长参数和基于关键字的不定长参数
'''def greet(*names):
    for name in names:
        print(f"{name},你好！")
    return None
greet("张三","李四")
#这里一个星号在函数中跑出来的是一个元组
#两个星号是一个字典
'''
def introduce(**info):
    for key,value in info.items():
        print(f"{key},{value}")
        print(f"{key}")
        print(f"{value}")
introduce(name = "张三",age = 25,sex = "男")
#上面每一个都是一个键值对，前面为key值后面为value值