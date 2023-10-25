import time
import threading
for i in range(3):
    print(i)
# 我们还可以使用setDaemon(True)把所有的子线程都变成主线程的守护线程，当主线程结束后，守护子线程也会随之结束，整个程序也跟着退出。


def run():
    print(threading.current_thread().name, "开始工作")
    time.sleep(2)       # 子线程停2s
    print("子线程工作完毕")


for i in range(3):
    t = threading.Thread(target=run,)
    # t.setDaemon(True)   # 把子线程设置为守护线程，必须在start()之前设置
    t.daemon = True
    t.start()

time.sleep(1)     # 主线程停1秒
print("主线程结束了！")
print(threading.active_count())  # 输出活跃的线程数
