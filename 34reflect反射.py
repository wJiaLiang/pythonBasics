# 在前面的章节，我们遗留了hasattr()、getattr()、setattr()和delattr()的相关内容，它们在这里。

# 对编程语言比较熟悉的同学，应该听说过“反射”这个机制。Python作为一门动态语言，当然不会缺少这一重要功能。
# 下面结合一个web路由的实例来阐述Python反射机制的使用场景和核心本质。

# 首先，我们要区分两个概念——“标识名”和看起来相同的“字符串”。两者字面上看起来一样，却是两种东西，比如下面的func函数和字符串“func”：

def func():
    print("func是这个函数的名字！")

s = "func"
print("%s是个字符串" % s) # func是个字符串

# 前者是函数func的函数名，后者只是一个叫“func”的字符串，两者是不同的事物。
# 我们可以用func()的方式调用函数func，但我们不能用"func"()的方式调用函数。说白了就是，不能通过字符串来调用名字看起来相同的函数！
# Python提供了反射机制，帮助我们实现这一想法，其主要就表现在getattr()等几个内置函数上!


