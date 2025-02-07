#列表
'''
1.定义
直接使用[]定义一个列表
'''
list1=[1,2,3,4,5,6]
print(list1)#打印会带上方括号
#访问元素首索引为0
print(list1[0])
#支持负索引 从-1开始
print(list1[-1])
#切片操作 切片出来的也是一个列表左闭右开区间
print(list1[0:3])

#添加元素.append()方法 不返回任何值 只是在原来列表基础上添加东西 所以会返回none
list1.append(7)
print(list1)
#该方法支持添加不同类型数据
list1.append("数字")
print(list1)

#extend()方法 可将另一个可以迭代的对象的所有元素添加到列表末尾
list2=[21,122,342]
list1.extend(list2)
print(list1)
#其中list2 是可以迭代的对象

list1.append(list2)
print(list1)
'''
append与extend的区别是
append添加列表 输入到原列表是以列表形式
extend添加列表 输入的是该列表的元素形式
'''

#insert() 是在指定位置处插入一个元素,其他元素后移
list1.insert(0,999)
print(list1)

#remove() 移除指定值
list1.remove(1)
print(list1)
list1.append(2)
print(list1)
list1.remove(2) #移除只会移除第一个符合括号的元素，其余元素不变的
print(list1)

#pop() 移除并返回指定位置的元素,默认索引是-1
print(list1.pop(-1))
print(list1)

#index() 返回第一个匹配项的索引
print(list1.index(21))

#count() 计算某一个值出现的次数
list1.append(3)
print(list1.count(3))

#sort() 排序 对列表进行原地排序 可以接受一个关键字函数和布尔值reverse来控制排序规则 没有返回值
list_num=[2,1,32,4,6,2,65,6,5]
print(sorted(list_num)) #sorted 返回排序后的列表
list_num.sort()
print(list_num)#如果是纯数字 则默认从小到大对数字进行排列
list_num.sort(reverse=True)#降序排序
print(list_num)
#使用key参数自定义排序规则
list_string=["Banana","Apple","Orange","Watermelon"]
list_string.sort(key=len)
print(list_string)
list_string.sort(key=len,reverse=True)
print(list_string)

#reverse() 反转列表元素

#len() 返回列表长度
a = len(list1)
print(a)

#clear()清空列表
list1.clear()
print(list1)

#copy() 复制列表
list1=list2.copy()
print(list1)
