# 回文字符串：对称的字符串为回文字符串。如abcba，abccba
#
# 判断回文字符串时有两种情况：
#
# 情况一：回文字符串长度为偶数。　　判断方式：以相邻的两个字符为中心，先比较这两个字符，再比较两边的字符。初始长度为0，每比较成功一次长度 + 2
#
# 情况一：回文字串长度为奇数。　　判断方式：以一个字符为中心，分别比较这个字符两边的字符。长度初始值为1，每比较成功一次长度 + 2


def find_max_huiwen_string(s):
    location = 0  # 定位初始化
    last_index = len(s) - 1  # 字符串最后一个字母的索引
    max = 0  # 记录最长回文子串的值，初始值为0
    for i in range(len(s)):
        # 情况一
        current_len = 0  # 假设回文字符串长度为偶数时，当前长度值为0
        r = location  # 对称中心为s[location]和s[location + 1]
        t = location + 1
        while True:
            if r < 0 or t > last_index:  # 如果r, t越界，则代表不是回文数，跳出循环
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
        current_len = 1  # 回文子串长度为奇数时，当前长度为1
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