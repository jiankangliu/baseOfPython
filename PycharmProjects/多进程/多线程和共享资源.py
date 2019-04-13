import threading
import time
sum1 = 0


def add():
    global sum1
    for i in range(10):
        sum += i
    print(sum)


def main():
    thd = threading.Thread(target=add)
    thd.start()
    thd.join()
    print('这是主线程的sum：', sum1)
    pass


if __name__ == '__main__':
    main()


