import multiprocessing
from multiprocessing import cpu_count
from time import sleep

print(multiprocessing.cpu_count())
print(cpu_count())


num = 0
while  True:
    sleep(1)
    num+=1
    m = num // 60
    s = num % 60
    ms = ((str(m)+"分") + (str(s) +"秒")) if m > 0 else str(s)+"秒" 
    print('\r', str(ms).ljust(10),end='',flush=True)
