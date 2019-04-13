year = int(input("请输入年份："))
moth = int(input("请输入月份："))
day = int(input("请输入日期："))
result = 0
while moth > 0:
    moth -= 1
    if moth == 1 or moth == 3 or moth == 5 or moth == 7 or moth == 8 or moth == 10 or moth == 12:
        result += 31
    if moth == 4 or moth == 6 or moth == 9 or moth == 11:
        result += 30
    if moth == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            result += 29
        else:
            result += 28
result += day
print(f"这一天是这一年的第{result}天")
