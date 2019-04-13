import threading
import time
g_num = 0


def add1():
    global g_num
    for i in range(100000):
        with lock:
            g_num += 1
    print('add1:', g_num)


def add2():
    global g_num
    for i in range(100000):
        with lock:
            g_num += 1
    print('add2:', g_num)


if __name__ == '__main__':
    lock = threading.Lock()
    th1 = threading.Thread(target=add1)
    th1.start()
    th2 = threading.Thread(target=add2)
    th2.start()
    time.sleep(1)
    print("主进程g_sum:", g_num)
    pass




