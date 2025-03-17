#确定哪些天必须用来做作业，哪些天可以选择不做作业以获得幸福值。

#控制输入
F1 = list(map(int,input().split()))
N = F1[0]#学期总天数
M = F1[1]#数学课节数，且一天只允许一节课，每次上完课都会布置作业
K = F1[2]#上交作业次数
happiness = list(map(int,input().split()))#每天对应的幸福值
upon = list(map(int,input().split()))#第几天上的课，并会在这一天布置作业
holdon = list(map(int,input().split()))#在第几天收作业

submit_day = 0

total = sum(happiness)

#找交作业的时间，确定交作业前共要写几次作业

for admission_index in range(M-1,-1,-1):
    for submit_index in range(0,K,1):
        if upon[admission_index] < holdon[submit_index]:
            submit_day = holdon[submit_index]
            break
    happiness_oneday = happiness[upon[admission_index]-1]
    admission_index_oneday = upon[admission_index]-1
    for day in range(upon[admission_index]-1,submit_day-1,1):
        if happiness_oneday > happiness[day]:
            happiness_oneday = happiness[day]
            admission_index_oneday = day
    happiness[admission_index_oneday] = 10000
    total = total - happiness_oneday

#测试

print(total)

