n=100
result=0
while n:
    result+=n
    n-=1
print(result)

x=1
result2=0
while x<=100:
    if x%2==0:
        result2+=x
    x+=1
print(result2)

x2=0
result3=0;
while x2<=100:
    result3+=x2
    x2+=2
print(result3)

print("开始吃苹果：")
x3=0;
while x3<10:
    if x3==5:
        print("吃了五个吃饱了。")
        break
    print(f"我已经吃了{x3}个")
    x3+=1

# 输出1至4，输出6至10
x4=1
while x4<11:
    if x4==5:
        x4+=1
        continue
    print(x4)
    x4+=1