'''sum = 0
x,y = map(int,input().split())
sum_x = []
sum_y = []
pairs = []
for i in (0,x):
    sum_x.append(i)
for i in (0,y):
    sum_y.append(i)
for i in sum_x:
    for j in sum_y:
        for m in sum_x:
            for n in sum_y:
                if i == m:
                    continue
                else:
                    k = (n-j)/(m-i)
                    b = (m*j - i*n)/(m-i)
                    new_pair = (k,b)
                    if new_pair not in pairs:
                        pairs.append(new_pair)
sum = len(new_pair) + y - 1
print(sum)'''
import math
m,n = map(int,input().split())
points = [(x,y) for x in range(m) for y in range(n)]
lines = set()
for i in range(len(points)):
    x1,y1 = points[i]
    for j in range(i+1,len(points)):
        x2,y2 = points[j]
        #现在点已经通过比上面更高效的方法提取出来了
        if x1 == x2 and y1 == y2:
            continue
        #如果确定两个点是相同的点跳过这个情况继续下面循环
        A = y2 - y1
        B = x1 - x2
        C = x2*y1 - x1*y2
        gcd_max = math.gcd(A,B,C)
        #这一步化简参数特别好，通过math库里面的内容对参数进行化简，这样就避免了很多重复情况的出现
        if gcd_max != 0:
            A //= gcd_max
            B //= gcd_max
            C //= gcd_max
            #接下来对每一个参数的符号进行限制 排除两个直线一样的情况
        if A < 0 or (A == 0 and B<0):
            A=-A
            B=-B
            C=-C
        lines.add((A,B,C))
print(len(lines))