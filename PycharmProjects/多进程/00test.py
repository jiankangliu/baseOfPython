import threading, time


def work(arg):
    print('参数是：', arg)
    time.sleep(1)
    print(threading.current_thread())
    print(threading.current_thread().name)


if __name__ == '__main__':
    thd1 = threading.Thread(target=work, args=('liu',), name='线程1')
    thd1.setDaemon(True)
    thd1.start()





