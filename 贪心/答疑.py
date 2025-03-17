'''
students = int(input())

students_message = []
for i in range(students):
    message = list(map(int,input().split()))
    students_message.append(message)

first_two = []
#print(students_message)

for i in students_message:
    two = i[0] + i[1]
    first_two.append([two,i[2]])

first_two.sort()

#print(first_two)

total =0
for i in range(0,students):
        total += first_two[i][0]*(students-i) + first_two[i][1]*(students-i-1)

print(total)
'''

n = int(input())
students = []
for _ in range(n):
    s,a,e = map(int,input().split())
    students.append((s,a,e))
students.sort(key=lambda x:(x[0]+x[1]+x[2]))

total = 0
for i in range(n):
    s,a,e = students[i]
    total += (s+a)*(n-i)
    total += e*(n-1-i)
print(total)