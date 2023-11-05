def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b = b, a+b
        i += 1


f = fib(5)
print(next(f))  # 1
for item in f:
    print(item)

print("-----------------------------------")


def simple_coroutine():
    print('-> 启动协程')
    y = 10
    x = yield y
    print('-> 协程接收到了x的值:', x)


my_coro = simple_coroutine()
ret = next(my_coro)
print(ret)
my_coro.send(10)
