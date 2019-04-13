# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
num = int(input('请输入一个五位数：'))
ge_num = num % 10
shi_num = int((num % 100) / 10)
qian_num = int((num % 10000) / 1000)
wan_num = int(num / 10000)
if ge_num == wan_num and shi_num == qian_num:
    print(f'{num}是回文数字。')
else:
    print(f'{num}不是回文数字。')




