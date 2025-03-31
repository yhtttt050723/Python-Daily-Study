'''
11 和 17 的倍数
'''
N = 11 * 17
q = 0
nums = []
listnum = []
for q in range(10**9 + 10**8,10**9 + 10**9):#9 10
    if q % 2 ==0:
        continue
    if q %(11*17)!= 0:
        continue
    if q %5 == 0:
        continue
    if q % 7 == 0:
        continue
    if (q +5) % 47 != 0:
        continue
    if (q +22) % 37 != 0:
        continue
    if (q +18) % 19 != 0:
        continue
    if (q +11) % 43 != 0:
        continue
    if (q + 10) % 13 != 0:
        continue
    nums.append(q)

#[10002817, 22360151, 47074819, 59432153, 84146821] 78
#[356008169, 887373531]89
#17

print(nums)
