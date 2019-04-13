#两种类型函数。1、设计成返回值。 2、仅执行代码而不返回值
#4.1.1 内建函数

#4.1.2 用户自定义函数
#定义形式
#def functionName(part1,part2,...):
#   indented block of statements
#   return expression

#4.1.3 具有一个参数的函数
def fahrenheitToCelsius(t):
    convertedTenperature=(5/9)*(t-32)
    return convertedTenperature

def firstName(fullName):
    firstSpace=fullName.index(' ')
    return fullName[:firstSpace]

fahrenheitTemp=eval(input("Enter a temperature indegree Fahrenheit: "))
celsiusTemp=fahrenheitToCelsius(fahrenheitTemp)
print("Celsius equivalent:",celsiusTemp,"degrees.")

fullName=input("Enter a person's full name: ")
print(firstName(fullName))

#4.1.4 向函数传值
#如果对象是不可变的且函数改变了形式参数变量的值，实际参数所指对象的值不会发生任何变化，即使两个变量有相同的名字。
#因此，当实际参数指向数值、字符串或元组对象时，不管怎样通过函数调用改变实际参数的知名，这都是不可能的。
num=2
def triple(num):
    num*=3
    return num
print(triple(num))      #输出6
print(num)              #输出2

#4.1.5 具有多个参数的函数

#4.1.6 返回布尔型或列表型的函数
#例6 元音单词，包含全部的五个元音字母
def isVowelWord(word):
    word=word.upper()
    vowels=['A','E','I','O','U']
    for vowel in vowels:
        if vowel not in word:
            return False
    return True
word=input("Enter a word: ")
if isVowelWord(word):
    print(word,"contain rvery vowel.")
else:
    print(word,"doesn't contain every vowel.")

#例7 包含元音的字母
def occurringVowels(word):
    word=word.upper()
    vowels=['A','E','I','O','U']
    for vowel in vowels:
        if vowel in word:
            return True
    return False

word=input("Enter a word: ")
if occurringVowels(word):
    print(word,"contains vowel.")
else:
    print(word,"not contains vowel.")

#4.1.7 无返回值的函数
#无返回值的函数不包含任何return语句。可能或者没有任何参数

#4.1.8 无参数的函数

#4.1.9 变量的作用域
#在函数内部创建的变量只能被同一函数内部的语句访问，并且当函数推出后变量就不存在了。这样的变量对于函数来说是局部的。
#或者说有局部作用域

#例10 变量作用域
def main():
    x=2
    print(str(x)+":function main")
    trivial()
    print(str(x)+":function main")
def trivial():
    x=3
    print(str(x)+":function trivial")
main()

#例11 局部变量
def main():
    trivial()
def trivial():
    x=5
    print(x)
main()

#例12 全局变量

#4.1.10 命名常量
#多次使用到的特殊变量，它的名字使用大写字母的单词，并且单词间用下划线分隔。并赋给一个常量

#4.1.11 库模块
#Python通过库模块的文件支持函数的重用。库模块是一个扩展名为.py的文件。
#包含了可能被其他任何程序使用的函数和变量。