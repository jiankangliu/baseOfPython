# for循环实现乘法口诀
print("hello\tworld")
str1="liujiankang"
for i in str1:
    print(i)
    print(type(i))
for i in str1:
    if i=='a':
        print("不打印a")
        continue
    print(i)

for i in range(9):
    for j in range(i+1):
        print(f"{j+1}*{i+1}={(j+1)*(i+1)}",end="\t")
    print()

result=1
for i in range(9):
    result*=(i+1)
print(result)

