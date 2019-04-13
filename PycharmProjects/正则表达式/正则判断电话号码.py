import re
phone = input("请输入电话号码：")
rephone = input("请再次输入电话号码：")
res = re.match(r"(?P<area>\d{3,4})-(?P<phone>\d{6,8})(?P=area)-(?P=phone)", phone + rephone)
if res:
    print('匹配成功', res.group('phone'))
else:
    print('匹配失败')


