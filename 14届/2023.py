nums = [x for x in range(12345678,98765433)]
for i in (12345678,98765433):
    si = str(i)
    for j in range(0,5):
        if si[j] == '2':
            for k in range(j+1,6):
                if si[k] == '0':
                    for m in range(k + 1, 7):
                        if si[m] == '2':
                            for n in range(m+ 1, 8):
                                if si[n] == '3':
                                    if i in nums:
                                        nums.remove(i)

print(len(nums))