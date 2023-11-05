# 一、概述

"""  
其实对于IO密集型任务我们还有一种选择就是协程。协程，又称微线程，英文名Coroutine，是运行在单线程中的“并发”，
协程相比多线程的一大优势就是省去了多线程之间的切换开销，获得了更高的运行效率。
Python中的异步IO模块asyncio就是基本的协程模块。

Python中的协程经历了很长的一段发展历程。最初的生成器yield和send()语法，
然后在Python3.4中加入了asyncio模块，引入@asyncio.coroutine装饰器和yield from语法，
在Python3.5上又提供了async/await语法，目前正式发布的Python3.6中asynico也由临时版改为了稳定版。

"""

# 二、 协程：

"""  
协程的切换不同于线程切换，是由程序自身控制的，没有切换的开销。
协程不需要多线程的锁机制，因为都是在同一个线程中运行，所以没有同时访问数据的问题，执行效率比多线程高很多。

因为协程是单线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

进程/线程：  操作系统提供的一种并发处理任务的能力。
协程：       程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧。

"""

# 三、 yield
""" 
最早的时候，Python提供了yield关键字，用于制造生成器。也就是说，包含有yield的函数，都是一个生成器！
yield的语法规则是：在yield这里暂停函数的执行，并返回yield后面表达式的值（默认为None），
直到被next()方法再次调用时，从上次暂停的yield代码处继续往下执行。
当没有可以继续next()的时候，抛出异常，该异常可被for循环处理。

def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b = b, a+b
        i += 1
f = fib(5)
next(f)
"""

# 下面是通过for循环不断地使fib生成下一个数，实际上就是不断地调用next()方法。


def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b = b, a+b
        i += 1


if __name__ == '__main__':
    f = fib(10)
    for item in f:
        print(item)

# 四、send()
"""  
最初的yield只能返回并暂停函数，并不能实现协程的功能。后来，Python为它定义了新的功能——接收外部发来的值，这样一个生成器就变成了协程。

每个生成器都可以执行send()方法，为生成器内部的yield语句发送数据。
此时yield语句不再只是yield xxxx的形式，还可以是var = yield xxxx的赋值形式。
它同时具备两个功能，一是暂停并返回函数，二是接收外部send()方法发送过来的值，重新激活函数，并将这个值赋值给var变量！

def simple_coroutine():
    print('-> 启动协程')
    y = 10
    x = yield y
    print('-> 协程接收到了x的值:', x)

my_coro = simple_coroutine()
ret = next(my_coro)
print(ret)
my_coro.send(10)

"""

# 五、 @asyncio.coroutine与yield from
""" 
    省略
"""

# 六、async和await
"""  
async和await 将代替上面其他写法

Python3.5中对协程提供了更直接的支持，引入了async/await关键字。
上面的代码可以这样改写：使用async代替@asyncio.coroutine，使用await代替yield from，代码变得更加简洁可读。
从Python设计的角度来说，async/await让协程独立于生成器而存在，不再使用yield语法。
看  example_002.py

"""

# 七、 asyncio模块 的使用

"""  
asyncio的使用可分三步走：
1、创建事件循环
2、指定循环模式并运行
3、关闭循环

通常我们使用asyncio.get_event_loop()方法创建一个循环。
运行循环有两种方法：一是调用run_until_complete()方法，二是调用run_forever()方法。
run_until_complete()内置add_done_callback回调函数，
run_forever()则可以自定义add_done_callback()，具体差异请看下面两个例子。

example_003.py  和 example_004.py


asyncio中几个重要概念
1.事件循环
管理所有的事件，在整个程序运行过程中不断循环执行并追踪事件发生的顺序将它们放在队列中，空闲时调用相应的事件处理者来处理这些事件。

2.Future
Future对象表示尚未完成的计算，还未完成的结果

3.Task
是Future的子类，作用是在运行某个任务的同时可以并发的运行多个任务。
asyncio.Task用于实现协作式多任务的库，且Task对象不能用户手动实例化，通过下面2个函数创建：
asyncio.async()
loop.create_task() 或 asyncio.ensure_future()


https://www.cnblogs.com/xyztank/articles/17571804.html



"""
