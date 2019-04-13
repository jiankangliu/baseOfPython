import multiprocessing
sum = 0
def add():
    global sum
    for i in range(10):
        sum += i
    print(sum)
pro1 = multiprocessing.Process(target=add)
pro2 = multiprocessing.Process(target=add)
if __name__ == '__main__':
    pro1.start()
    pro2.start()







