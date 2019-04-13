# 输入某年某月某日，判断这一天是这一年的第几天？
sum = 0
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    list1 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while month - 1:
        sum += list1[month - 1]
        month -= 1
    sum += day
else:
    list1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while month - 1:
        sum += list1[month - 1]
        month -= 1
    sum += day
print(f'{year}年{month}月{day}日是{year}年第{sum}天')
