'''
什么是引用？
1.对象引用
在python中所有数据都被视为对象，而变量是对这些对象的引用
实际上你将一个对象赋值给一个变量时
实际上创建了一个指向该对象的引用，而不是复制对象本身
'''
a = [1,2,3,4]
b = a
b.append(5)#这里b引用a 实际上是对a对象的引用，所以修改b,本身的a对象也会变
print(b)
print(a)
#如果只是赋值  可以使用copy函数
c = a.copy()
print(c)
c.append(6)
print(c)
print(a)#此时达到了C是C，A是A的目的

#导入
'''
from 1 import 2
'''