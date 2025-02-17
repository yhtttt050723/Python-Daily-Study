#元组的创建
'''
什么是元组？
一种不可变的有序集合
'''
tuple1=(1,)# 带了, 的数据类型才是元组
print(tuple1)
tuple2=(1) # 如果只有一个元素创建时没有带, 会被认为是整型
print(tuple2)
print(type(tuple2))
print(type(tuple1))

#索引
tuple3=(1,2,3)
print(tuple3[0])
#len()函数，返回元组长度
print(len(tuple3))
print(type(len(tuple3))) #返回长度为int类型
#max 与 min
print(max(tuple3))
#在元组内元素可以比较的情况下，返回最大值，最小值

#tuple.index() 返回第一个括号内元素的索引
print(tuple3.index(3)) #返回索引2

#tuple.count() 返回括号内元素的出现次数
tuple4=(1,1,1,2,1,3,4)
print(tuple4.count(1))

#示例
students_scores = (('Alice', 88), ('Bob', 95), ('Charlie', 70), ('David', 95))
student_name = tuple(name for name , _ in students_scores)
print(student_name)
student_score = tuple(score for _ , score in students_scores)
print(student_score)
print("####")
print(f"最高分的同学是{student_name[student_score.index(max(student_score))]}，他的成绩是{max(student_score)}")
