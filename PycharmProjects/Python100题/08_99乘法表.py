i = 0
j = 0
while i < 9:        # 外层循环9行
    j = 0
    while j <= i:           # 每一行的循环
        print(f'{i + 1}*{j + 1}={(i + 1) * (j + 1)}', end='\t')
        j += 1
    print()
    i += 1
