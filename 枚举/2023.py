k = 0
for num in range(12345678, 98765433):
    str1 = ["2", "0", "2", "3"]
    for x in str(num):
        if x in str1:
            if str1[0] == x:
                str1.pop(0)
            if len(str1) != 0:
                k += 1
print(k)