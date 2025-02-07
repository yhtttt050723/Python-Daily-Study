from decimal import Decimal, getcontext

print("请输入控制的最大精度")
max_input = input()
try:
    max = int(max_input)
except ValueError:
    print("输入的不是有效整数")
    exit(1)
getcontext().prec = max
user_input = input("请输入一系列以逗号分隔的数值: ")
#控制用户输入
dynamic_server_util = [float(num.strip()) for num in user_input.split(',')]
#转换列表属性
dynamic_server_util_decimal = [Decimal(str(num)) for num in dynamic_server_util]
#求和
total_sum = sum(dynamic_server_util_decimal, Decimal('0'))

print(total_sum)