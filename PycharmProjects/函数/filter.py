my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def fun(x):
    return x % 2 == 1


result = filter(fun, my_list)
print(list(result))


