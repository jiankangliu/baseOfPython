# print(num)  # NameError
# 捕获异常类型
# try:
#     print(num)
#     # print(1/0)
# # except ZeroDivisionError:
# except NameError as e:
#     print(e)

# try:
#     # print(num)
#     print(1/0)
# except ZeroDivisionError as e:
# # except NameError as e:
#     print(e)

try:
    print(1 / 0)
    print(num)

except Exception as e:
    print(e)
