n = int(input())
ai = list(map(int,input().split()))

left = 0
right = n-1

total = []

for left in range(0,n):
    for right in range(n-1,0,-1):
        total.append([left+1,right+1,sum(ai[left:right+1])])
for i in range(0,n):
    total.append([i+1,i+1,ai[i]])

ns = []
for i in range(0,n):
    nums = []
    for j in total:
        if j[0] <= i+1 <=j[1]:
            nums.append(j[2])
    ns.append(max(nums))
for item in ns:
    print(item,end=' ')
