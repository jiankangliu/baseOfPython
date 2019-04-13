info_list = []


def info_print():
    print("""
        请选择不同的功能
        1--添加学员
        2--删除学员
        3--修改学员
        4--显示一个学员信息
        5--显示所有学员信息
        6--退出系统
    """)


def add_info():
    global info_list
    name = input('请输入姓名：')
    phone = input('请输入手机号：')
    qq = input('请输入QQ：')
    for i in info_list:
        if i['name'] == name:
            print('姓名重复，无法添加')
            return 0
    personal_info = {'name': name, 'phone': phone, 'qq': qq}
    info_list.append(personal_info)
    f = open('information.txt', 'a')
    f.write(personal_info['name'] + '\t\t' + personal_info['phone'] + '\t\t' + personal_info['qq'] + '\n')
    f.close()
    print('添加成功')


def del_info():
    global info_list
    flag = False
    name = input('请输入要删除的姓名：')
    f = open('information.txt', 'r')
    f1 = open('information.txt', 'w')
    lines = f.readlines()
    for line in lines:
        if line.startswith(name):
            flag = True
            print('删除成功')
            continue
        f1.writelines(line)
    f.close()
    f1.close()
    if flag:
        return 0
    print('删除失败')
    return


def modify_info():
    global info_list
    flag = False
    name = input('请输入要修改学员的姓名：')
    f = open('information.txt', 'r')
    f1 = open('information.txt', 'a')
    lines = f.readlines()
    for line in lines:
        if line.startswith(name):
            flag = True
            name = input('请输入修改后的姓名：')
            phone = input('请输入修改后的手机号码：')
            qq = input('请输入修改后的qq：')
            f.write(name + '\t\t' + phone + '\t\t' + qq + '\n')
            print('修改成功')
        f1.writelines(line)
    f.close()
    f1.close()
    if flag:
        return 0
    print('查无此人')
    return 0


def search_all_info():
    f = open('information.txt', 'r')
    for line in f.readlines():
        print(line)
    return 0


def search_info():
    name = input('请输入查找学生的姓名：')
    f = open('information.txt', 'r')
    lines = f.readlines()
    for line in lines:
        if line.startswith(name):
            print(line)
            print('查找成功')
            return 0
    print('查找失败')
    return 0


def main():
    while True:
        info_print()
        num1 = int(input())
        if num1 == 1:
            add_info()
        elif num1 == 2:
            del_info()
        elif num1 == 3:
            modify_info()
        elif num1 == 4:
            search_info()
        elif num1 == 5:
            search_all_info()
        elif num1 == 6:
            break
        else:
            print('输入错误')


main()

















