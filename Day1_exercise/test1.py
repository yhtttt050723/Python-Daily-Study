'''
1. 创建一个整数变量 `a`，赋值为 5。
2. 创建一个浮点数变量 `b`，赋值为 3.14。
3. 创建一个字符串变量 `c`，赋值为 "Hello, World!"。
4. 创建一个布尔变量 `d`，赋值为 True。
5. 将整数 `a` 转换为浮点数，并存储到新变量 `e` 中。
6. 将字符串 `c` 转换为全大写的字符串。
7. 使用类型检查函数（如 `type()`）打印每个变量的类型
'''
a=5
b=3.14
c="hello world{}"
d=True
e=float(a)
new_c=c.upper()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
num=1
sum=0
while num < 1001:
    if num%2 == 0:
        sum = sum + num
    num = num + 1
    continue