# 一、概念
"""  
装饰器（Decorator）：从字面上理解，就是装饰对象的器件。可以在不修改原有代码的情况下，为被装饰的对象增加新的功能或者附加限制条件或者帮助输出。
装饰器有很多种，有函数的装饰器，也有类的装饰器。装饰器在很多语言中的名字也不尽相同，它体现的是设计模式中的装饰模式，强调的是开放封闭原则。
装饰器的语法是将@装饰器名，放在被装饰对象上面。

@dec
def func():
    pass

由于顺序执行的原因，如果你真的对同一个函数定义了两次，那么，后面的定义会覆盖前面的定义。
因此，在Python中代码的放置位置是有区别的，不能随意摆放，通常函数体要放在调用的语句之前

"""


def outer(func):
    def inner():
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return result
    return inner


@outer
def f1():
    print("业务部门1数据接口......")


f1()

# 二、 执行过程
"""  
1、程序开始运行，从上往下解释，读到def outer(func):的时候，发现这是个“一等公民”函数，于是把函数体加载到内存里，然后过。

2、读到@outer的时候，程序被@这个语法糖吸引住了，知道这是个装饰器，按规矩要立即执行的，于是程序开始运行@后面那个名字outer所定义的函数。

3、程序返回到outer函数，开始执行装饰器的语法规则。规则是：被装饰的函数的名字会被当作参数传递给装饰函数。
    装饰函数执行它自己内部的代码后，会将它的返回值赋值给被装饰的函数。原来的f1函数被当做参数传递给了func，而f1这个函数名之后会指向inner函数。
注意：@outer和@outer()有区别，没有括号时，outer函数依然会被执行

4.程序开始执行outer函数内部的内容，一开始它又碰到了一个函数inner，inner函数定义块被程序观察到后不会立刻执行，而是读入内存中（这是默认规则）。

5.再往下，碰到return inner，返回值是个函数名，并且这个函数名会被赋值给f1这个被装饰的函数，
  也就是f1 = inner。根据前面的知识，
  此时f1函数被新的函数inner覆盖了（实际上是f1这个函数名更改成指向inner这个函数名指向的函数体内存地址，f1不再指向它原来的函数体的内存地址），
  再往后调用f1的时候将执行inner函数内的代码，而不是先前的函数体。
  那么先前的函数体去哪了？还记得我们将f1当做参数传递给func这个形参么？func这个变量保存了老的函数在内存中的地址，
  通过它就可以执行老的函数体，你能在inner函数里看到result = func()这句代码，它就是这么干的！

6、依然通过f1()的方式调用f1函数时，执行的就不再是旧的f1函数的代码，而是inner函数的代码。

7、请注意，@outer这句代码在程序执行到这里的时候就会自动执行outer函数内部的代码，如果不封装一下，在业务部门还未进行调用的时候，就执行了

"""

print("1111111111111111111111111111111111111111111111111111")
def outer(func):
    def inner(username):
        print("认证成功！")
        result = func(username)
        print("日志添加成功")
        return result
    return inner


@outer
def f1(name):
    print("%s 正在连接业务部门1数据接口......" % name)


f1("jack")  # 传递参数

print("222222222222222222222222222222222222222222222222222222")

# 三、 接受不确定参数个数


def outer(func):
    def inner(*args, **kwargs):
        print("认证成功！")
        result = func(*args, **kwargs)
        print("日志添加成功")
        return result
    return inner


@outer
def f1(name, age):
    print("%s 正在连接业务部门1数据接口......" % name)


f1("jack", 18)

print('-----------------------------------------------------------')

# 四、 一个函数可以被多个函数装饰吗？可以的！
# 多个装饰器的时候 离函数近的先执行 这里也就是 outer2 先执行 
def outer1(func):
    # print("我是outer1")
    def inner(*args, **kwargs):
        print("认证成功！")
        result = func(*args, **kwargs)
        print("日志添加成功")
        return result
    return inner


def outer2(func):
    # print("我是outer2")
    def inner2(*args, **kwargs):
        print("一条欢迎信息。。。")
        result = func(*args, **kwargs)
        print("二条欢送信息。。。")
        return result
    return inner2


@outer1
@outer2
def f2(name, age):
    print("%s 正在连接业务部门1数据接口......" % name)

f2("jack", 18)

# 执行结果
# 认证成功！
# 一条欢迎信息。。。
# jack 正在连接业务部门1数据接口......
# 二条欢送信息。。。
# 日志添加成功

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 五、 装饰器自己可以有参数吗？可以的！
# 认证函数
def auth(request, kargs):
    print("认证成功！")

# 日志函数
def log(request, kargs):
    print("日志添加成功")

# 装饰器函数。接收两个参数，这两个参数应该是某个函数的名字。
def Filter(auth_func, log_func):
    # 第一层封装，f1函数实际上被传递给了main_fuc这个参数
    def outer(main_func):
        # 第二层封装，auth和log函数的参数值被传递到了这里
        def wrapper(request, kargs):
            # 下面代码的判断逻辑不重要，重要的是参数的引用和返回值
            before_result = auth(request, kargs)
            if (before_result != None):
                return before_result

            main_result = main_func(request, kargs)
            if (main_result != None):
                return main_result

            after_result = log(request, kargs)
            if (after_result != None):
                return after_result

        return wrapper
    return outer
# 注意了，这里的装饰器函数有参数哦，它的意思是先执行filter函数
# 然后将filter函数的返回值作为装饰器函数的名字返回到这里，所以，
# 其实这里，Filter(auth,log) = outer , @Filter(auth,log) =  @outer
@Filter(auth, log)
def f12(name, age):

    print("%s 正在连接业务部门1数据接口......" % name)

f12("jack", 18)
