year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
dayth = 0
m = 0
# 闰年的情况下
if (year % 4 == 0 and year % 100 != 00) or year % 400 == 0:
    Month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while m < month:
        dayth += Month[m]
        m += 1
    dayth += day
    print(f"{year}年{month}月{day}是{year}年第{dayth}天。")

# 非闰年
else:
    Month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while m < month:
        dayth += Month[m]
        m += 1
    dayth += day
    print(f"{year}年{month}月{day}是{year}年第{dayth}天。")
