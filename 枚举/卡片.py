'''total = [2021] * 10
num =1
while True:
    str_num = str(num)
    for digit in str_num:
        if total[int(digit)] == 0:
            print(num)
            exit()
        total[int(digit)] -= 1
    num += 1'''
#测试检验
nums = []
for i in range(1,3182):
    for j in str(i):
        nums.append(str(j))
for i in range(0,10):
    print(nums.count(str(i)))