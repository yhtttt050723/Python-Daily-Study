#文件输入输出
'''with open('FileOne.txt','r') as f:
    content = f.read()#会移动文件指针，导致指针已经达到文件末尾，所以下面的readline读不出东西
    f.seek(0)
    Linecontent = f.readline()#按行读，逐行读出并且没有换行符,读到换行符为止,同样会移动文件指针，如果需要重新开始需要调整文件指针
    f.seek(0)
    Linescontent = f.readlines()
print(content)
print("**********")
print(type(Linecontent))
print(Linecontent)
print("**********")
print(type(Linescontent))
print(Linescontent)
for i in Linescontent:
    print(i)#逐行打印'''
with open('FileOne.txt','w') as flag:
    flag.write("Hello!!!\n")#覆盖文本所有内容，写入新的东西
with open('FileOne.txt','a') as flag:
    flag.write("Add?\n")#追加写入，不覆盖原来文本内容
with open('FileOne.txt','r') as flag:
    content = flag.read()
print(content)
