n = int(input())
l = [[0]*n for _ in range(n)]
solutions = []

def dfs(row = 0):
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if l[i][j] == 1:
                    solution.append(j+1)
        solutions.append(solution)
        return

    for col in range(n):
        safe = True
        for i in range(n):
            if l[i][col] == 1:
                safe = False
                break
        if safe:
            i,j = row-1,col-1
            while i >=0 and j >= 0:
                if l[i][j] == 1:
                    safe = False
                    break
                i-=1
                j-=1
        if safe:
            i,j = row-1,col+1
            while i >=0 and j < n:
                if l[i][j] == 1:
                    safe = False
                    break
                i-=1
                j+=1

        if safe:
            l[row][col] = 1
            dfs(row+1)
            l[row][col] = 0

dfs()
for item in solutions[0:3]:
    print(' '.join(map(str,item)))
print(len(solutions))

