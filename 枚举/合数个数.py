total_list = [x for x in range(1,2021)]
for i in total_list:
    if (i-2) >= 0 and (i-2)%2 == 0:
        total_list.remove(i)
total_list.append(2)
total_list.sort()
for i in range (2,len(total_list)-1):
    if total_list[i] != -1:
        for j in range(i + 1,len(total_list)):
            if total_list[j] % total_list[i] == 0:
                total_list[j] = -1
total_list = [x for x in total_list if x != -1]
print(2020 - len(total_list))