"""
打开open()
读写 read()   write()
关闭 close()
1.1read(num)    读取num个字符
1.2readlines()  按行读取所有数据，返回一个列表
"""

f = open('1.txt', 'w')
f.write('111\n222')
f.close()
f = open('1.txt', 'r')
content = f.read()
print(content)