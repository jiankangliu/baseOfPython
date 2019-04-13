s = input("请输入母串：")
p = input("请输入要查询的子串：")
plen = p.__len__()
next = [0] * plen
next[0] = -1
i = 1
while i < plen:
    if p[i - 1] == p[next[i - 1]]:
        next[i] = next[i - 1] + 1
    i += 1
print(next)


