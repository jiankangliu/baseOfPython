# 题目：求1+2!+3!+...+20!的和
sum = 1
num = 1
for i in range(10):
    num = 1
    while i + 1 > 0:
        num *= (i + 1)
        i -= 1
    sum *= num
print(sum)



