# 如果用户输入密码小于6位 提示错误信息
"""
1.定义一个异常类
2.使用这个异常类
"""

# 定义异常类
class PwdLength(Exception):
    # 出具异常信息给用户
    def __init__(self, length, minLen):
        self.length = length
        self.minLen = minLen

    # 存储的是将来的异常信息
    def __str__(self):
        return f'您输入的密码是{self.length}位，本系统要求密码至少{self.minLen}位'

try:
    pwd = input('请输入您的密码：')
    # 1. 抛出异常
    if len(pwd) < 6:
        # raise 异常对象
        raise PwdLength(len(pwd), 6)
except Exception as e:  # 2. 捕获异常
    print(e)
else:
    print('密码输入完成')

# if len(pwd) < 6:
#     print(f'您输入的密码是{len(pwd)}位，本系统要求密码至少6位')
# else:
#     print('密码输入完成')






