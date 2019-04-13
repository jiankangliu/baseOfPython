import threading
import time
g_num = 0


def add1(lock):
    global g_num
    for i in range(100000):
        lock.acquire()
        g_num += 1
        lock.release()
    print('add1_g_num', g_num)


def add2(lock):
    global g_num
    for i in range(100000):
        lock.acquire()
        g_num += 1
        lock.release()
    print('add2_g_num:', g_num)


def main():
    lock = threading.Lock()
    thd = threading.Thread(target=add1, args=(lock,))
    # thd.daemon = True
    thd2 = threading.Thread(target=add2, args=(lock,))
    # thd2.daemon = True
    thd.start()
    thd2.start()
    # time.sleep(1)
    print(f'主线程获取全局变量：{g_num}')
    pass


if __name__ == '__main__':
    main()





