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
    f.write('\n')
    f.write(str(personal_info))
    f.close()
    print('添加成功')


def del_info():
    global info_list
    name = input('请输入要删除的姓名：')
    for i in info_list:
        if i['name'] == name:
            index = info_list.index(i)
            del info_list[index]
            print('删除成功')
            return 0
    print('删除失败')
    return


def modify_info():
    global info_list
    name = input('请输入要修改学员的姓名：')
    for i in info_list:
        if i['name'] == name:
            name = input('请输入修改后的姓名：')
            phone = input('请输入修改后的手机号码：')
            qq = input('请输入修改后的qq：')
            i['name'] = name
            i['phone'] = phone
            i['qq'] = qq
            print('修改成功')
            return 0
    print('查无此人')


def search_all_info():
    for i in info_list:
        print(i)
    return 0


def search_info():
    name = input('请输入查找学生的姓名：')
    for i in info_list:
        if i['name'] == name:
            print('查找成功')
            print(i)
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

















