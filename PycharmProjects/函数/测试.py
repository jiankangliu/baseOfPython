# list1 = [{'name': 'liu', 'age': 18}, {'name': 'li', 'age': 12}]
# def a():
#     for i in list1:
#         print(i['name'])
#         print(list1.index(i))
#         i['name'] = 'aaa'
#
#
# # f = open('info.txt', 'w')
# # f.write('liu Jiankang')
# # f.close()
# l = {'name': 'liu', 'age': 18}
# f = open('info1.txt', 'a')
# f.write('\n')
# f.write(str(l))
# f.close()
# f = open('info1.txt')
# content = f.readlines()
# print(str(content))
list1 = [{'name': 'liu', 'age': 18, 'gender': 'man'}, {'name': 'wang', 'age': 19, 'gender': 'woman'}]
f = open('1.txt', 'a')
f.writelines(list1[0]['name'] + '\n')
f.writelines(list1[1]['name'])
f.close()
f = open('1.txt', 'r')
content = f.read()
print(content)

