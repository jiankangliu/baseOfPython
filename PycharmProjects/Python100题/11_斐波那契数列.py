sum = 1
month = 3
print(1, '\n',1)
a = b = 1
while month < 20:
    print(a + b)
    c = a
    a = b
    b = c + a
    month += 1
