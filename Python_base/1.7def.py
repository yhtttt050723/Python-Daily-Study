def liat_add(list):
    sum  = 0
    for i in list:
        sum = sum + i
    return sum

list1=[1,2,3,4,5,6]
list2=[7,6,45,3,2]
sum1 = liat_add(list1)
sum2 = liat_add(list2)
print(sum1)
print(sum2)

#定义参数默认值
def list_sum(list = [0]):
    sum2 = 0
    for i in list:
        sum2 = sum2 + i
    return sum2
print(list_sum()) #存在默认值时，不传递参数也可以运行

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Willie", animal_type="dog") #可以顺序不同，但是要写出参数名称

def add_many_list(*list): #注意此时是把list整个作为元素进行传递
    sum3 = 0
    for i in list:
        for j in i:
            sum3+=j
    return sum3
sum3_listall = add_many_list(list1,list2)
print(sum3_listall)