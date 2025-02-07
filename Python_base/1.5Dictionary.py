#字典
'''
是什么问题？
什么是字典？
一种用于存储键值对的数据结构
允许通过键查找对应的值
键必须是唯一的
而值可以是任意类型
'''
dictionary1={"a":1,"b":2}
print(dictionary1["a"])
#检查键是否在字典中：
if 'a' in dictionary1:
    print("存在")
#使用get()获取键对值 避免键不存在时报错
print(dictionary1.get("a","n")) #只返回了有的那个
#修改元素 通过直接赋值修改
dictionary1["a"] = 3
print(dictionary1["a"])
#update() 从其他字典更新原字典的值 如果存在相同则覆盖原值
dictionary2={"c":3,"d":4,"e":5,"a":1}
dictionary1.update(dictionary2)
print(dictionary1)
#pop 移除并返回指定键的值
num = dictionary1.pop("e")
print(num)
print(dictionary1)
#clear 清空字典
dictionary2.clear()
print(dictionary2)
#keys 返回一个包含所有键的视图对象
print(dictionary1.keys()) #返回所有键
#values 返回所有值
print(dictionary1.values()) #返回所有值
#items 返回所有键值对
print(dictionary1.items())
#遍历所有键 所有值
for key in dictionary1:
    print(key)
for item in dictionary1.values():
    print(item)
#同时遍历键和值
for key,item in dictionary1.items():
    print(f"{key} and {item}")
#字典推导式：
new_dictionary1 = {key : value**2 for key,value in dictionary1.items()}
print(new_dictionary1)#对原来键值对中所有值进行处理生成新的字典