N =int(input())
si = list(map(int,input().split()))
ti = list(map(int,input().split()))
for i in range(N):
    s_i = str(si[i])
    if '0' in s_i:
        continue
    if '2' in s_i:
        continue
    if '4' in s_i:
        continue
    si[i] = -1

for i in range(N):
    t_i = str(ti[i])
    if '0' in t_i:
        continue
    if '2' in t_i:
        continue
    if '4' in t_i:
        continue
    ti[i] = -1
result = []
def dfs(si,ti,ans):
    if sum(si) == len(si)*(-1):
        result.append(ans)
        return
    if sum(ti) == len(ti)*(-1):
        result.append(ans)
        return
    for i in range(0,len(si)):
        if si[i] == -1:
            break
        for j in range(0,len(ti)):
            if ti[j] == -1:
                break
            if ti[j] > si[i]:
                si[i] = -1
                dfs(si,ti,ans+1)
            else:
                continue
print(result)
        

