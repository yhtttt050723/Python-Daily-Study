N = int(input())
score_list = []
perfectnum = 0
passnum = 0
for i in range(N):
    score = int(input())
    if score < 0 or score > 100:
        score = int(input())
    score_list.append(score)

for i in score_list:
    if i >= 85:
        perfectnum += 1
    elif i >= 60 and i < 85:
        passnum += 1
persent_per = round(perfectnum / N * 100)
persent_pass = round((perfectnum+passnum) / N * 100)

n1 = float(persent_per)
n2 = float(persent_pass)

print(f'{int(n2)}'+'%')
print(f'{int(n1)}'+'%')