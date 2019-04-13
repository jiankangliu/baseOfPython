
import multiprocessing
import time


def add_list(l):
    for i in range(5):
        l.append(i)
    print(l)


def read_list(l):
    print(l)


def main():
    l = list()
    pro1 = multiprocessing.Process(target=add_list, args=(l,))
    pro1.start()
    pro2 = multiprocessing.Process(target=read_list, args=(l,))
    pro2.start()
    time.sleep(1)
    print(l)


if __name__ == '__main__':
    main()


