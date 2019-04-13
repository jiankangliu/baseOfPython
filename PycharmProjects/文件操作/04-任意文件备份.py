"""
1   用户输入要备份文件
2   得到用户输入文件名之后，构建新文件
3   保证新旧文件内容一致
    3.1  旧文件读取数据，写入新文件
"""
old_name = input('请输入要备份的文件名：')
# 构建新文件名
index = old_name.rfind('.')
new_name = old_name[:index] + '[备份]' + old_name[index:]
print(new_name)
f = open(old_name, 'w')
f.write('liujiankang')
f.close()
# 创建文件内容一致
"""
1    旧文件读方式打开， 新文件写方式打开
2    旧文件读，新文件写
3    关闭文件
"""
old_f = open(old_name, 'r')
new_f = open(new_name, 'w')
while True:         # 分步写入
    content = old_f.read(5)
    if len(content) == 0:
        break
    new_f.write(content)
old_f.close()
new_f.close()