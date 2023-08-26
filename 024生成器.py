"""  
有时候，序列或集合内的元素的个数非常巨大，如果全制造出来并放入内存，对计算机的压力是非常大的。
比如，假设需要获取一个10**20次方如此巨大的数据序列，把每一个数都生成出来，并放在一个内存的列表内，这是粗暴的方式，
有如此大的内存么？如果元素可以按照某种算法推算出来，需要就计算到哪个，
就可以在循环的过程中不断推算出后续的元素，而不必创建完整的元素集合，从而节省大量的空间。
在Python中，这种一边循环一边计算出元素的机制，称为生成器：generator。

"""
g = (x * x for x in range(1, 4))
print(g) # <generator object <genexpr> at 0x000001E01A948430>

# 可以通过next()函数获得generator的下一个返回值，这点和迭代器非常相似：
print(next(g)) #1
print(next(g)) #4
print(next(g)) #9
# 但更多情况下，我们使用for循环。
for i in g:
    print(i)

# 除了使用生成器推导式，我们还可以使用yield关键字。

"""  
在 Python中，使用yield返回的函数会变成一个生成器（generator）。 
在调用生成器的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值。
并在下一次执行next()方法时从当前位置继续运行。
"""
print("=======================================")
# 斐波那契函数
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a             # yield让该函数变成一个生成器 返回循环直到 推出循环
        a, b = b, a + b
        print("+++",a,"++++")
        counter += 1
print("---------------------------------------")
fib = fibonacci(10)           # fib是一个生成器
# print(next(fib))
# print(next(fib))
# print(next(fib))
print(type(fib)) #<class 'generator'>
for i in fib:
    print(i, end=",") #0 1 1 2 3 5 8 13 21 34 55

"""  
当生成器函数再次被调用时则直接从上次暂停的yield表达式处接着运行，直到遇到下一个yield语句，或者没有遇到yield语句则运行结束。
需要说明的是，在函数重新运行时，其实上次暂停处的yield表达式会先接收一个值作为结果，然后才接着运行直到碰到下一个yield表达式。
"""
print('\n',"===============")
def wine():
    print('first yield...')
    yield 1
    print('second yield...')
    yield 2
    print('第三个')

ww = wine()
print(next(ww)) # 1
print(next(ww)) # 2
# 一次返回下面结果
# first yield...
# 1
# second yield...
# 2