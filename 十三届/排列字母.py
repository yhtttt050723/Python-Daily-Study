'''
排列字母
问题描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
小蓝要把一个字符串中的字母按其在字母表中的顺序排列。
例如，LANQIAO 排列后为 AAILNOQ。
又如，GOODGOODSTUDYDAYDAYUP 排列后为 AADDDDDGGOOOOPSTUUYYY。
请问对于以下字符串，排列之后字符串是什么？
WHERETHEREISAWILLTHEREISAWAY
'''
target = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

s = input()
s_list = []

for i in s:
    for j in range(0,len(target)-1):
        if i == target[j]:
            s_list.append(j)

right_list = sorted(s_list)
end = []

for i in right_list:
    end.append(target[i])

print(''.join(end))