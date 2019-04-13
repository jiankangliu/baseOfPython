#3.2.1 if-else语句
#例1 求较大值
num1=eval(input("Enter the first number: "))
num2=eval(input("Enter the second number: "))
if num1>num2:
    print("The larger number is:",num1)
else:
    print("The larger number is: ",num2)

#3.2.2 if语句
firstNumber=eval(input("Enter the first number: "))
secondNumber=eval(input("Enter the second number: "))
thirdNumber=eval(input("Enter the third number: "))
max=firstNumber
if secondNumber>firstNumber:
    max=secondNumber
if thirdNumber>max:
    max=thirdNumber
print("The largest number is: ",max)

#3.2.3 嵌套的if-else语句
#例4 灯标的意义
color=input("Enter a color (BLUE or RED): ")
mode=input("Enter a mode (STEADY or FLASHING): ")
result=""
color=color.upper()
mode=mode.upper()
if color=="BLUE":
    if mode=="STEADY":
        result="Clear View"
    else:
        result="Clouds Due"
else:
    if mode=="STEADY":
        result="Rain Ahead"
    else:
        result="Snow Ahead"
print("The weather forecast is",result)


