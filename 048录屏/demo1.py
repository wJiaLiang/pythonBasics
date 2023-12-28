import multiprocessing
from multiprocessing import cpu_count
from time import sleep

print(multiprocessing.cpu_count())
print(cpu_count())


num = 0
while  True:
    sleep(1)
    num+=1
    print('\r',num,end='',flush=True)