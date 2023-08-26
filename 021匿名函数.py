"""  
有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
这省去了我们挖空心思为函数命名的麻烦，也能少写不少代码，很多编程语言都提供这一特性。
匿名函数用好了，会有画龙点睛的效果，没用好，就容易“画虎不成反类犬”，

"""
# Python语言使用lambda关键字来创建匿名函数。
# 所谓匿名，即不再使用def语句这样标准的形式定义一个函数。
    #1、 lambda只是一个表达式,而不是一个代码块，函数体比def简单很多。
    #2、 仅仅能在lambda表达式中封装有限的逻辑。
    #3、 lambda 函数拥有自己的命名空间。

# 其形式通常是这样的：lambda 参数: 表达式。
# 例如：lambda x: x * x。它相当于下面的函数：
def f(x):
    return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数，x*x是执行代码。

"""  
匿名函数只能有一个表达式，不用也不能写return语句，表达式的结果就是其返回值。 
匿名函数没有函数名字，不必担心函数名冲突，节省字义空间。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

# 也可以把匿名函数作为别的函数的返回值返回。
def add(string, i):
    return lambda: int(string) + i
"""


print((lambda x: x * x)(5)) #25