import multiprocessing
from multiprocessing import cpu_count
from time import sleep

print(multiprocessing.cpu_count())
print(cpu_count())

print("itme",end='',flush=True)
sleep(3)
print("\r","xxxx",end='',flush=True)