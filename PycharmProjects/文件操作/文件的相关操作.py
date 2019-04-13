import os
f = open('te.txt', 'w')
f.write('hello world, i am liu')
f.close()
os.rename('te.txt', 'te1.txt')


