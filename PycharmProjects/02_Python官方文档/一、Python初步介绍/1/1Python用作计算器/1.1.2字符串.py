print('spam eggs')
print("'spam eggs'")
print('"spam eggs"')
print('\'sqam eggs"')
print('"Isn\'t,"she said.')
print("""""")
""""
起始和末尾的引号必须一致（要么都是双引号，要么都是单引号）。
双引号中可以直接出现单引号，单引号中可以直接出现双引号。
双引号中出现双引号必须用转义字符。单引号同理。
"""
str="spam & eggs"   #str的索引和切片。第一个字符对应索引为0
print(str[0])   #输出s
print(str[1])   #输出p
print(str[0:6]) #输出str中0到6以前的字符
print("Python")
print("Python"[1],"Python"[5])
print(str.find('s'))    #输出s的第一个索引。   如果找不到则输出-1
print(str[0:11])

#反向索引，最右端的索引值为-1，它左边的为-2，从右向左依次类推
print(str[-2])      #输出g
print(str[0:-1])    #输出spam & egg
print(str[:4])      #str[m:n]，m的值默认为0。n默认为最后一个索引值加1
print(str[1:])
print(str[:])       #输出整个字符串
                    #右边不包括左包括