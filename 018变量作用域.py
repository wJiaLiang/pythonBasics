# 一、 作用域指的是变量的有效范围。变量并不是在哪个位置都可以访问的，访问权限取决于这个变量是在哪里赋值的，也就是在哪个作用域内的。

"""  
在编程语言中，变量的作用域从代码结构形式来看，有块级、函数、类、模块、包等由小到大的级别。但是在Python中，
没有块级作用域，也就是类似if语句块、for语句块、with上下文管理器等等是不存在作用域概念的，他们等同于普通的语句。

if True:
    a = 1
print(a) #1

def name():
    b = 2
    pass
print(b) # 报错
就是内部代码可以访问外部变量，而外部代码通常无法访问内部变量。
"""

# 二、 Python的作用域一共有4层，分别是：
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域

"""  
Python以L –> E –> G –>B的规则查找变量，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，最后去内建中找。
如果这样还找不到，那就提示变量不存在的错误。
"""

# 三、 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，被叫做局部变量，定义在函数外的拥有全局作用域的变量，被称为全局变量。（类、模块等同理）
# 所谓的局部变量是相对的。局部变量也有可能是更小范围内的变量的外部变量。


# 四、 global和 nonlocal 关键字

total = 0                        # total是一个全局变量

def plus( arg1, arg2 ):
    global total                 # 使用global关键字申明此处的total引用外部的total
    total = arg1 + arg2          # 如果没有上面这一行， total在这里是局部变量
    
    print("函数内局部变量total=  ", total)
    print("函数内的total的内存地址是: ", id(total))
    return total

plus(10, 20)
print("函数外部全局变量total= ", total)
print("函数外的total的内存地址是: ", id(total))

"""  
函数plus内部通过total = arg1 + arg2语句，新建了一个局部变量total，它和外面的全局变量total是两码事。
而如果我们，想要在函数内部修改外面的全局变量total呢？使用global关键字！
"""

# 如果，inner内部想使用outer里面的那个a，而不是全局变量的那个a，怎么办？
a = 1
print("函数outer调用之前全局变量a的内存地址： ", id(a))
def outer():
    a = 2
    print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
    def inner():
        # global a # 这里的a 引用的是全局作用域的a
        nonlocal a # 引用的a 就是 outer 函数中的a
        a = 3
        print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
    inner()
    print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
outer()
print("函数outer执行完毕，全局变量a的内存地址： ", id(a))

