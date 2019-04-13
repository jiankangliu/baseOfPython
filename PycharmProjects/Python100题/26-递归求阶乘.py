# 题目：利用递归方法求5!
def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)


print(recursion(5))
