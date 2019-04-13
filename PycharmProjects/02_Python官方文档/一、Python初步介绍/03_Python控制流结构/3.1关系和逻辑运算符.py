#3.1.1 ASCⅡ值
#chr(n)代表ASCⅡ值为n所对应的单个字符串
print(chr(65))
#ord(str)代表str这个字符的ASCⅡ值
print(ord('A'))

#3.1.2关系运算符
#字符，字符串的比较实际是比较ASCⅡ值的大小
#in  代表是字符字串
#not in 代表不是字符字串
print("a"in"absd")
print("a"in"dsg")
print("a"not in"dsgs")
print("a"not in"adsfs")

#不同类型的值不能进行比较。   例如，字符串不能与数字进行比较
#当in这种运算符用于一个列表或者元组时，这意味着包含关系
print('b'in['b','a','c'])

#3.1.3 列表元素的排序
#列表中的元素可以使用sort()方法进行比较和排序
list=[6,4,-5,3,5]
list.sort()
print(list)
list=["c","d","a","b","e"+chr(65),("g")]
list.sort()
print(list)

#3.1.4 逻辑运算符
#and , or , not。not cond1（当cond1为假时为真）
print(not(2>4))

#3.1.5 短路求值

#3.1.6布尔数据类型
#Ture对象和False对象属于布尔数据类型

#3.1.7三种返回布尔值的方法
str1="fantastic"
print(str1.startswith("Fant"))
print(str1.endswith("tic"))
print(isinstance(32,int))           #isinstance(字符m，类型n)方法判断字符m是否是类型n
print(str1.isdigit())           #判断str1是否所有字符都是数字
print(str1.isalpha())           #判断str1的所有字符都是字母目标上的字母
print(str1.isalnum())           #判断str1的所有字符都是字母表上的字母或数字
print(str1.islower())          #str1至少有一个字母字符，且所有字母字符都是小写
print(str1.isupper())             #str1至少有一个字母字符，且所有字母字符都是大写
print(str1.isspace())           #str1仅含有空白字符

#3.1.8简化条件
state="Md"
(state=="Md")or(state=="er")or(state=="li")
state in ["Md","er","li"]

x=6
(x>10)and(x<=20)
10<x<=20

(x<=10)or(x>20)
not(10<x<=20)

#3.4.3 for循环的嵌套
for m in range(1,6):
    for n in range(1,6):
        print(m,'*',n,'=',m*n,'\t',end='')
    print()











