s = input()
l = list(s)
l2 = []
d = 'abcdefghijklmnopqrstuvwxyz'
for i in d:
    l2.append(l.count(i))
l2.sort(reverse = True)
for i in d:
    if l.count(i) == l2[0]:
        print(i)
        print(l2[0])
        break