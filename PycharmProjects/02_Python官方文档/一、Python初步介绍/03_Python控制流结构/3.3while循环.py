#当特定的条件满足时，while循环重复执行一个缩进的语句块
print("This program displays a fanous movie quotation.")
responses=('1','2','3')
response='0'
while response not in responses:
    response=input("Enter 1, 2, or 3:")
    if response=='1':
        print("Plastics.")
    elif response=='2':
        print("Rosebud.")
    elif response=='3':
        print("That's all folks.")

#3.3.2 break语句

#3.3.3 continue语句

#3.3.4 创建菜单
#例8 美国的情况
print("Enter a number from the menu to obtain fact")
print("about the United States or to exit the program.\n")
print("1. Capital")
print("2. National Bird")
print("3. National flower")
print("4. Quit\n")
while True:
    num=eval(input("Make a delection from the menu: "))
    if num==1:
        print("Washington")
    elif num==2:
        print("Bald Eagle")
    elif num==3:
        print("Rose")
    elif num==4:
        break
