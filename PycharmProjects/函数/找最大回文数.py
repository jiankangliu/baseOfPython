# def huiwen_string(s):
#     location = 0
#     le = len(s)
#     max1 = 1
#     for i in s:
#         m = 0
#         r = location
#         t = location + 1
#         while True:
#             if r < 0 or t > le - 1:
#                 break
#             if s[r] == s[t]:
#                 m += 2
#                 r -= 1
#                 t += 1
#                 continue
#             else:
#                 break
#         if m > max1:
#             max1 = m
#
#         m = 1
#         p = location - 1
#         q = location + 1
#         while True:
#             if p < 0 or q > le - 1:
#                 break
#             if s[p] == s[q]:
#                 m += 2
#                 p -= 1
#                 q += 1
#                 continue
#             else:
#                 break
#         if m > max1:
#             max1 = m
#         location += 1
#     print(max1)
# s = 'iiiiii'
# huiwen_string(s)


def find_max_huiwen_string(s):
    location = 0    # 定位初始化
    last_index = len(s) - 1     # 字符串最后一个字母的索引
    max = 0 # 记录最长回文子串的值，初始值为0
    for i in range(len(s)):
        # 情况一
        current_len = 0     # 假设回文字符串长度为偶数时，当前长度值为0
        r = location        # 对称中心为s[location]和s[location + 1]
        t = location + 1
        while True:
            if r < 0 or t > last_index:     # 如果r, t越界，则代表不是回文数，跳出循环
                break
            if s[r] == s[t]:
                # 若相等，则长度+2，r自减1，t自加一
                current_len += 2
                r -= 1
                t += 1
                continue
            else:
                # 若s[r] ！= s[t]，跳出循环
                break
        if current_len > max:
            # 当前回文串的长度大于，之前的长度，则更改max值
            max = current_len


        # 情况二：
        current_len = 1     # 回文子串长度为奇数时，当前长度为1
        p = location - 1
        q = location + 1
        while True:
            if p < 0 or q > last_index:
                break
            if s[p] == s[q]:
                current_len += 2
                p -= 1
                q += 1
                continue
            else:
                break
        if current_len > max:
            max = current_len


        location += 1
    print(max)


s = input('请输入要判断的字符串：')
find_max_huiwen_string(s)