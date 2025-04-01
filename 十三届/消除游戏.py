s = list(input())
changed = True

while changed:
    n = len(s)
    if n == 0:
        break
    marked = [False] * n
    changed = False

    # 遍历每个可能的中间位置i
    for i in range(1, n - 1):
        # 情况1：s[i]等于前一个且不等于后一个
        if s[i] == s[i-1] and s[i] != s[i+1]:
            marked[i] = True
            marked[i+1] = True
        # 情况2：s[i]不等于前一个但等于后一个
        elif s[i] != s[i-1] and s[i] == s[i+1]:
            marked[i-1] = True
            marked[i] = True

    # 构建新字符串并检查是否发生变化
    new_s = [s[i] for i in range(n) if not marked[i]]
    if len(new_s) != len(s):
        changed = True
    s = new_s

print(''.join(s) if s else 'EMPTY')