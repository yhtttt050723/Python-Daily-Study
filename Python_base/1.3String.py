#基本数据结构——字符串
'''
字符串定义时可以用单引号双引号三引号
但是定义后具有不可变性
'''
#索引与切片
text = "我太爱上学了,以致于我炸学校"
print(text[0])
print(text[-1])
print(text[1:])
print(text[0:7:2])#左闭右开的始末位置,末尾控制间隔数输出
print(text.find("我太爱",0,10))#找不到返回-1找到返回0
print(text.index("我太爱"))#找不到抛出错误
print(text.count("我"))
text2 = "I am a little boy"
text3 = "do not catch me"
print(text2.upper())
print(text2.lower())
print(text3.capitalize())
print(text3.title())
print(text3.rjust(20,"*"))
print(text3.center(20,"*"))
print(text3.split("o",1))#以o为界线 然后分隔 后面int型数据控制最大分隔次数
print(text3.isalnum())
print(text3.isdigit())
print(text3.isspace())
print(text3.startswith("d"))
print(text3.endswith("e"))