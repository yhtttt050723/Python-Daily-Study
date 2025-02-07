'''
python 基础概念
python 面向对象的解释型高级编程语言
源代码->解释器->输出
'''
#数据类型
int_a = 1
boolean_b = True # 首字母需要大写
string_c = "你好" #这里使用python3.9
list_d = ["a","b","c","d",int_a,boolean_b]
list_e = ["a","b","c","d",int_a,boolean_b,list_d]
print(list_d)
print(list_e)#列表中什么都可以放进去而且可以嵌套
dictionary_f = {"list1":list_e,"list2":list_d}
print(dictionary_f)
dictionary_g = {"list1":list_e,"list2":list_d,"list3":dictionary_f}
print(dictionary_g)#同样可以进行嵌套
print("你" in string_c)
print("你好" == string_c)
'''
输入输出
'''
