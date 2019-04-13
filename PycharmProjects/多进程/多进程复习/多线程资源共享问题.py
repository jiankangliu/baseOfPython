import threading
sum1 = 0
sum2 = 0


def add():
    global sum1
    for i in range(10):
        sum1 += i
    print(sum1)

thr1 = threading.Thread(target=add, name="thr1")
thr2 = threading.Thread(target=add, name="thr2")

if __name__ == '__main__':
    thr1.start()
    thr2.start()







