f = open('test.txt', 'w')
f.write('Hello world, I am here.')
f.close()
f = open('test.txt', 'w')               # 如果文件不存在则先创建，如果存在就先清空，然后写入
f.write('一壶离愁漂泊天涯难入喉，\n你走之后酒暖回忆思念瘦。')
f.close()

f = open('test.txt', 'r')               # f = open('test.txt')          默认‘r’
content = f.read()                      # content接收内容
f.close()
print(content)

f = open('test.txt')
content = f.readlines()                 # readlines()可以按照行的方式把文件进行一次性读取，并且返回一个列表，每行为一个列表元素
print(type(content))                    # 为列表类型
print(content)

f = open('test1.txt', 'w')
f.write('hello world, i am mis liu.\n u are my world')
f = open('test1.txt')
content = f.readline()                  # readline() 读取第一行
f.close()
print(content)






