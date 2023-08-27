"""  
你会不会有些好奇Python为什么可以直接使用一些内建函数，而不用显式的导入它们？
比如 str()、int()、dir()、id()、type()，max()，min()，len()等，许多许多非常好用，快捷方便的函数。

因为这些函数都是一个叫做builtins模块中定义的函数，而builtins模块默认在Python环境启动的时候就自动导入，所以你可以直接使用这些函数。

Python通过这个近80个内置函数，为我们提供了丰富、强大、高效、快速的解决方案，大多数时候，我们根本不需要导入第三方库，甚至标准库都不需要。
"""
print("\n")
# globals()函数可以查看当前状态下，全局变量有哪些
g = globals()
print(g)

print("\n")
# dir()函数查看它的成员属性
p = dir(__builtins__)
print(p)

print("\n")
for x in p:
    print(x)
print("\n")

# 注意
# 同样也可以将其他对象赋值给内置函数，这时就完全变了。
# 所以，内置函数不是Python关键字，要注意对它们的保护，不要使用和内置函数重名的变量名，这会让代码混乱，容易发生难以排查的错误。

# 绝对值函数
# abs() 

# 接收一个可迭代对象，如果对象里的所有元素的bool运算值都是True，那么返回True，否则False。不要小瞧了这个函数，如果all函数中的可迭代对象是空的，直接返回True。
# all() 

# 接收一个可迭代对象，如果迭代对象里有一个元素的bool运算值是True，那么返回True，否则False。与all()是一对兄弟。
# any()

print(all([])) # True
print(any([])) # False

# 调用对象的__repr__()方法，获得该方法的返回值。__repr__()方法是由对象所属类型实现的方法。不可以简单地理解为print或echo。
# 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符
# ascii()
s = [1,2,3]
print(ascii(all)) # <built-in function all>

# bin()、oct()、hex()
# 三个函数是将十进制数分别转换为2/8/16进制。
i = 10
print(bin(i)) # 0b1010
print(oct(i)) # 0o12
print(hex(i)) # 0xa

# 测试一个对象或表达式的执行结果是True还是False。
bool(1==3)

# 实例化一个bytearray类型的对象。参数可以是字符串、整数或者可迭代对象。返回一个新的字节数组
aa = bytearray("张三",encoding='utf-8')
print(aa) #bytearray(b'\xe5\xbc\xa0\xe4\xb8\x89')

# 将对象转换成字节类型。例如：s = '张三';m = bytes(s,encoding='utf-8')
aa1 = bytes('张三',encoding='utf-8')
print(aa1) # b'\xe5\xbc\xa0\xe4\xb8\x89'


# 将对象转换成字符串类型，同样也可以指定编码方式。例如：str(bytes对象，encoding='utf-8')
print(str(23))        # '23'
print(str([1,2,3]))   # '[1, 2, 3]'

# 判断对象是否可以被调用。如果某个对象具有__call__方法，那它就能被调用。 例如，def f1(): pass,那么callable(f1)返回True。
def ff():pass
ff1 = "abc"
print(callable(ff1))  # False
print(callable(ff))   # True

# 返回某个十进制数对应的ASCII字符
# chr() 例如：chr(99) = ''

# 与chr()相反，返回某个ASCII字符对应的十进制数 例如，ord('A') = 65
# ord()

# classmethod()、staticmethod()和property()
# 类机制中，用于生成类方法、静态方法和属性的函数。在面向对象章节会有详细介绍。

# 将字符串编译成Python能识别或执行的代码。 也可以将文件读成字符串再编译。
# compile()
s  = "print('helloworld')"
r = compile(s,"<string>","exec")
# r()
exec(r)  # helloworld

# 通过数字或字符串生成复数类型对象。
# complex()

# 类机制中，分别用来删除、设置、获取和判断属性。后面会有详解
# delattr()、setattr()、getattr()、hasattr()

# 显示对象所有的属性和方法。最棒的辅助函数之一！
dir()


# 与bool()、str()、bytes()一样，它们都是实例化对应数据类型的类。
# int()、float()、list()、dict()、set()、tuple()


# divmod 除法，同时返回商和余数的元组。
divmod(10,3) # (3,1)

# 枚举函数，在迭代对象的时候，额外提供一个序列号的输出。
# enumerate(li,1)中的1表示从1开始序号，默认从0开始。注意，第二个参数才是你想要的序号开始，不是第一个参数
lis = {"a":9,"b":8,"c":7}
enumerate(lis,1)

for i, key in enumerate(lis, 5):
    print(i,"\t",key)

# 将字符串直接解读并执行。例如：s = "6*8"，s是一个字符串，d = eval(s)， d的结果是48。
# eval()

# 执行字符串或compile方法编译过的字符串，没有返回值。 
# exec()

# 执行format()，其实就是调用该对象所属类的__format__方法。类似print功能。
# format()

# 返回一个不能增加和修改的集合类型对象。
# a = frozenset(range(10))


# 为不可变对象，例如字符串生成哈希值的函数！
# hash()
hash("hello py") #5094071384489611808


# 返回对象的帮助文档。谁用谁知道！
# lis = [1,2]
# help(lis)


# 返回对象的内存地址,常用来查看变量引用的变化，对象是否相同等。常用功能之一！
# id()

# 接收用户输入，返回一个输入的字符串。
# input()

# 判断一个对象是否是某个类的实例。比type()方法适用面更广。
# isinstance("haha", str)

# issubclass(a，b),判断a是否是b的子类。
# issubclass()


# 制造一个迭代器，使其具备next()能力。
# lis = [1, 2, 3]
# i = iter(lis)

# 返回对象的长度。不能再常用的函数之一了。
# len()


# 返回当前可用的局部变量。
# locals()


# 返回给定集合里的最大或者最小的元素。可以指定排序的方法！
# max()/min():


# 返回obj的内存视图对象。obj只能是bytes或bytesarray类型。memoryview对象的使用方法如下：
v = memoryview(b'abcefg')
print(v[0]) #97


# 通过调用迭代器的__next__()方法，获取下一个元素。
# next()


# 该方法不接收任何参数，返回一个没有任何功能的对象。object是Python所有类的基类。
# object()

# 打开文件的方法。在Python2里，还有一个file()方法，Python3中被废弃了。后面章节会详细介绍open()的用法。
# open()

# 幂函数。
pow(3, 2) #9


# 调用对象所属类的__repr__方法，与print功能类似。
# repr()

# 反转，逆序对象
a = reversed([1,2,3,4,5])
list(a) # 使用list方法将它转换为一个列表   [5, 4, 3, 2, 1]


# 四舍五入
# round()


# 返回一个切片类型的对象。slice是一个类，一种Python的数据类型。Python将对列表等序列数据类型的切片功能单独拿出来设计了一个slice类，可在某些场合下使用。
s = slice(1, 10, 2)
type(s)
lis2 = [i for i in range(10)]
lis2[s]  # lis[s]

# 求和．
# sum()

# 调用父类。面向对象中类的机制相关。后面介绍。
# super()


# 显示对象所属的数据类型。常用方法！前面已经展示过。
# type()


# 与dir()方法类似，不过dir()方法返回的是key，vars()方法返回key的同时还把value一起打印了。
# vars()

# 映射函数。使用指定的函数，处理可迭代对象，并将结果保存在一个map对象中，本质上和大数据的mapreduce中的map差不多。
# map()
li = [1,2,3]
data = map(lambda x :x*100,li)  # 这里直接使用了一个匿名函数
print(list(data)) #[100, 200, 300]      # 返回值是一个map对象，它是个迭代器。


# 过滤器，用法和map类似。在函数中设定过滤的条件，逐一循环对象中的元素，将返回值为True时的元素留下（注意，不是留下返回值！），形成一个filter类型的迭代器
# filter()
def f11(x):
    if x > 3:
        return True
    else:
        return False
li11 = [1,2,3,4,5]
data11 = filter(f11,li11)
print(list(data11)) # [4,5]


# 组合对象。将对象逐一配对。那么如果对象的长度不一致呢？多余的会被抛弃！以最短的为基础！
# zip()
list_1 = [1,2,3]
list_2 = ['a','b','c']
s = zip(list_1,list_2)
print(list(s)) # [(1, 'a'), (2, 'b'), (3, 'c')]


# sorted() 排序 有key和reverse两个重要参数。 有key和reverse两个重要参数。
sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]
# 指定排序的关键字。关键字必须是一个可调用的对象。例如下面的例子，规则是谁的绝对值大，谁就排在后面
sorted([36, 5, -12, 9, -21], key=abs) #[5, 9, -12, -21, 36]

# 指定按反序排列。下面的例子，首先按忽略大小写的字母顺序排序，然后倒序排列。
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True) #['Zoo', 'Credit', 'bob', 'about']


# 这个方法为我们提供了一种通过字符串反射包、库或模块的手段。其中的name是你想要导入的库的名称的字符串。
# __import__(name)

t = __import__("time")
print(t.time()) # 时间戳 多少秒 1693123472.2509053

# 利用字符串“time”，导入了实际的time库，并赋值给t变量。这个变量实际就相当于import time的结果。然后使用t.time()进行调用。





