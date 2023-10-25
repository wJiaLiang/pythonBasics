import threading
import time

number = 0


def plus():
    global number       # global声明此处的number是外面的全局变量number
    for _ in range(100000):    # 进行一个大数级别的循环加一运算
        number += 1
        print("==>n", number)
    print("子线程%s运算结束后，number = %s" %
          (threading.current_thread().name, number))


for i in range(2):      # 用2个子线程，就可以观察到脏数据
    t = threading.Thread(target=plus)
    t.start()


time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
print("主线程执行完毕后，number = ", number)
