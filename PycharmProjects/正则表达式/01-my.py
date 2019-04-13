import re
res = re.match(r'liu', 'liujiankang')
res = re.match(r'itcas\w', 'itcast')
res = re.match(r'itcas\w', 'itcas刘', re.A)
res = re.match(r'itcas\d', 'itcas7', re.A)
res = re.match(r'itcas\D', 'itcas7', re.A)
res = re.match(r'itcas\s', 'itcas 7')
res = re.match(r'itcas\s', 'itcas\f')
res = re.match(r'itcas\S', 'itcast')
res = re.match(r'itcas[^1-9]', '-itcas1')
res = re.match(r'itcas[1-9][a-z]', 'itcas1d')
res = re.match(r'python\d?', 'python99')
res = re.match(r'python\d*', 'python')
res = re.match(r'python\d+', 'python2')
res = re.match(r'python\d{1, }', 'python2')
res = re.match(r'python\d{,5}', 'python2')
res = re.match(r'[a-zA-B_]\w*[a-z0-9A-Z_]$', 'liu')
res = re.match(r'[0-9]?', '000')

if res:
    print('匹配成功', res.group())
else:
    print('匹配失败')



