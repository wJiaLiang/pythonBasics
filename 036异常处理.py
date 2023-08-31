"""  
在程序运行过程中，总会遇到各种各样的问题和错误。有些错误是我们编写代码时自己造成的，比如语法错误、调用错误，甚至逻辑错误。
还有一些错误，则是不可预料的错误，但是完全有可能发生的，比如文件不存在、磁盘空间不足、网络堵塞、系统错误等等。
这些导致程序在运行过程中出现异常中断和退出的错误，我们统称为异常。

大多数的异常都不会被程序处理，而是以错误信息的形式展现出来。

异常有很多种类型，Python内置了几十种常见的异常，就在builtins模块内，无需特别导入，直接就可使用。
需要注意的是，所有的异常都是异常类，首字母是大写的！

"""

# 我们应当尽量考虑全面，将可能出现的异常进行处理，而不是留在那里，任由其发生。
# Python内置了一套try...except...finally（else）...的异常处理机制，来帮助我们进行异常处理。其基本语法是：
"""  
try:
    pass
except Exception as ex:
    pass
"""

# Python的异常机制具有嵌套处理的能力，比如下面的函数f3()调用f2()，f2()调用f1()，虽然是在f1()出错了，
# 但只需要在f3()进行异常捕获，不需要每一层都捕获异常。

def f1():
    return 10/0
def f2():
    f1()
def f3():
    f2()
try:
    f3()
except ZeroDivisionError as e:
    print(e) # division by zero



# try…except…语句处理异常的工作机制如下：
# 1、首先，执行try子句（在关键字try和关键字except之间的语句）
# 2、如果没有异常发生，忽略 except 子句，try子句执行后结束。
# 3、如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。

try:
    print("发生异常之前的语句正常执行")
    print(1/0)
    print("发生异常之后的语句不会被执行")
except ZeroDivisionError as e:
    print(e)

# 如果程序发生的异常不在你的捕获列表中，那么依然会抛出别的异常。

# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
# 也就是前面说的嵌套处理能力。直到程序最顶端如果还没有被捕获，那么将弹出异常。
try:
    try:
        print("发生异常之前的语句正常执行")
        print(1/0)
        print("发生异常之后的语句不会被执行")
    except ValueError as e:
        print(e)

except ZeroDivisionError as e:
    print("里层没有抓好，只能辛苦我外层了")


# 可能包含多个except子句，分别来处理不同的特定的异常。但最多只有一个分支会被执行。
# 所以except子句有排序先后问题，进了一条巷子就不会进别的巷子

# 处理程序将只针对对应的try子句中的异常进行处理，不会处理其他try语句中的异常。
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组。
try:
    print("发生异常之前的语句正常执行")
    print(1/0)
    print("发生异常之后的语句不会被执行")
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print("我是第一个抓取到除零异常的")
except (ValueError,ZeroDivisionError) as e:
    print("我是备胎")



# 通用异常：Exception
# 在Python的异常中，有一个通用异常：Exception，它可以捕获任意异常。

s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print('错误')

"""  
那么既然有这个什么都能管的异常，其他诸如OSError、ValueError的异常是不是就可以不需要了？当然不是！
很多时候程序只会弹出那么几个异常，没有必要针对所有的异常进行捕获，那样的效率会很低。
另外，根据不同的异常种类，制定不同的处理措施，用于准确判断错误类型，存储错误日志，都是非常有必要甚至强制的。

"""




# finally和else子句

# try except语法还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
# 这个子句将在try子句没有发生任何异常的时候执行。
"""  
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
"""

# 同样的，还有一个可选的finally子句。无论try执行情况和except异常触发情况，finally 子句都会被执行！
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
finally:
    print('finally...')
print('END')


# 也可以else和finally同时存在时：
try:
    pass
except:
    pass
else:
    print("else")
finally:
    print("finally")



# 主动抛出异常： raise
# 很多时候，我们需要主动抛出一个异常。Python内置了一个关键字raise，可以主动触发异常。
# raise唯一的一个参数指定了要被抛出的异常的实例，如果什么参数都不给，那么会默认抛出当前异常。
# 为什么要自己主动抛出异常？不嫌多事么？因为有的时候，你需要记录错误信息，然后将异常继续往上层传递，让上层去处理异常
# 有时候，你需要主动弹出异常，作为警告或特殊处理：
sex = int(input("Please input a number: "))
try:
    if sex == 1:
        print("这是个男人！")
    elif sex == 0:
        print("这是个女人！")
    else:
        print("好像有什么不符合常理的事情发生了！！")
        raise ValueError("非法的输入")
except ValueError:
    print("这是个人妖！")


# 自定义异常
# Python内置了很多的异常类，并且这些类都是从 BaseException 类 派生的。
# 下面是一些常见异常类，请把它们记下来！这样你在见到大多数异常的时候都能快速准确的判断异常类型。

"""  
异常名	            解释
AttributeError	    试图访问一个对象没有的属性
IOError	            输入/输出异常
ImportError	        无法引入模块或包；多是路径问题或名称错误
IndentationError	缩进错误
IndexError	        下标索引错误
KeyError	        试图访问不存在的键
KeyboardInterrupt	Ctrl+C被按下，键盘终止输入
NameError	        使用未定义的变量
SyntaxError	        语法错误
TypeError	        传入对象的类型与要求的不符合
UnboundLocalError	试图访问一个还未被设置的局部变量
ValueError	        传入一个调用者不期望的值，即使值的类型是正确的
OSError	            操作系统执行错误

大多数情况下，上面的内置异常已经够用了，但是有时候你还是需要自定义一些异常。
自定义异常应该继承Exception类，直接继承或者间接继承都可以，例如:
"""
class MyExcept(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise MyExcept('我的异常!')
except MyExcept as ex:
    print(ex) #我的异常

# 异常的名字都以Error结尾，我们在为自定义异常命名的时候也需要遵守这一规范，就跟标准的异常命名一样。


