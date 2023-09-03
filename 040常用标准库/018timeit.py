"""  
前面我们介绍过，time.time()和time.clock()方法可以用来计算程序执行时间及cpu时间。
但是，很多时候我们只想对某些代码片段或者算法进行执行时间的统计，这时候，使用timeit模块就比较方便。
timeit模块是Python内置的用于统计小段代码执行时间的模块，它同时提供命令行调用接口。


注意:在windows命令行中执行时，最外围要用双引号

timeit.timeit(stmt='pass', setup='pass', timer=, number=1000000, globals=None)


"""
import timeit
st = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(st) #0.09063749999768334
# 执行第一个参数的代码，返回执行的时间

st2 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# "-".join(str(n) for n in range(100))
"""  
stmt是要执行的代码，字符串形式，多行就多个字符串。setup是执行前的环境配置，
比如import语句。timer是使用的计时器。number是执行的次数。globals是执行的命名空间。


timeit.repeat(stmt='pass', setup='pass', timer=, repeat=3, number=1000000, globals=None)
指定重复次数的执行timeit方法，返回一个结果列表。

timeit.default_timer()
默认的计时器，也就是time.perf_counter()

class timeit.Timer(stmt='pass', setup='pass', timer=, globals=None)
用于进行代码执行速度测试的计时类。该类有四个方法：
    timeit(number=1000000)
    autorange(callback=None)
    repeat(repeat=3, number=1000000)
    print_exc(file=None)


"""