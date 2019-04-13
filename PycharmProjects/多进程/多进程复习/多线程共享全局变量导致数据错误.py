import threading
import time
sum = 0
def add():
    global sum
    for i in range(1000000):
        sum += 1
thr1 = threading.Thread(target=add)
thr2 = threading.Thread(target=add)
if __name__ == '__main__':
    thr1.start()
    time.sleep(2)
    thr2.start()
    time.sleep(2)
    print(sum)




