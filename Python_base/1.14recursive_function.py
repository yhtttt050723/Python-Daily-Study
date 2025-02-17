#什么是递归函数
'''
直接或者间接调用自己
核心思想是将一个大问题分解成若干子问题

要素 ：
1. 基线条件  控制递归的终止防止无限循环
2。 递归条件 将问题分解为更小的子问题
'''

#示例 ： 阶乘计算
def function1(n):
    if n > 1:
        return n * function1(n-1)
    else :
        print("程序执行结束")
        return 1

print(function1(5))

def fibonacci(n):
    # 基线条件：前两项为1
    if n <= 1:
        return n
    # 递归条件：fib(n) = fib(n-1) + fib(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))  # 输出 5（第6项，索引从0开始）

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"将盘子从{source}-->{target}")
    else:
        hanoi(n-1,source,auxiliary,target)#将n-1个盘子移动到辅助盘子上
        print(f"将盘子从{source}-->{target}")
        hanoi(n-1,auxiliary,source,target)
        print(f"将盘子从{source}-->{target}")
    return None

hanoi(3,"A","C","B")

def resevere_string(s):
    if len(s)==1:
        return s
    return resevere_string(s[1:]) + s[0]

s = "awdiouhjawiuodjhaio"
re_s=resevere_string(s)
print(re_s)