name="Tom"
age=18
studentId=1
weight=60.6
print("我的名字是%s，我今年%d岁，体重%.2f千克，学号是%04d" % (name,age,weight,studentId))
print(f"我的名字是{name}，我今年{age}岁，体重%.2f千克，学号是%04d" % (weight,studentId))
print("%05d" % age)
'''
    %s-字符串
    %f-浮点型
    %d-整型
    f格式化输出
    %.2f-输出两位小数的浮点型
    %05d-输出五位的整型，不足位的用0补充，超过或者等于五位的按原型输出
    \n换行符   \t下一个制表符
    print()函数默认的结束符是\n
'''

