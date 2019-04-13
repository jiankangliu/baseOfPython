# print(num)  # NameError
# 捕获异常类型
try:
    print(num)
    print(1/0)
# except ZeroDivisionError:
except (ZeroDivisionError, NameError):
    print('有错误')




