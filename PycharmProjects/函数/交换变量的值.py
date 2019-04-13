a = 1
b = 2
# 借助第三个变量，避免数据丢失
a, b = b, a         # python中独有的交换变量的值
print(a)
print(b)
