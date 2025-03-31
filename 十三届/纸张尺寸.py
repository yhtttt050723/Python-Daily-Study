flag = input()

A0 = [1189,841]
A1 = [A0[1],A0[0]//2]
A2 = [A1[1],A1[0]//2]
A3 = [A2[1],A2[0]//2]
A4 = [A3[1],A3[0]//2]
A5 = [A4[1],A4[0]//2]
A6 = [A5[1],A5[0]//2]
A7 = [A6[1],A6[0]//2]
A8 = [A7[1],A7[0]//2]
A9 = [A8[1],A8[0]//2]

totalname = ['A0','A1','A2','A3','A4','A5','A6','A7','A8','A9']
total = [A0,A1,A2,A3,A4,A5,A6,A7,A8,A9]

for i in range(0,len(totalname)):
    if flag == totalname[i]:
        print(total[i][0])
        print(total[i][1])