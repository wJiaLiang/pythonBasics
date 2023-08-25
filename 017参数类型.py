# 参数类型
x, y, z = 1, 2, 3
def add(a, b, c):
    return a+b+c
add(x, y, x)        # 使用变量，传递参数
add(4, 5, 6)        # 直接传递值也是可以的。
# a，b，c叫做形式参数，简称形参。而x，y，z和4，5，6叫做实际参数，简称实参，也就是实际要传递的值。而我们通常讨论的参数，指的都是形参。
# python函数的参数定义灵活度非常大。除了正常定义的位置参数外，还可以使用默认参数、动态参数和关键字参数，这些都是形参的种类。

# 一、 位置参数 (必传参数)
"""  
也叫必传参数，顺序参数，是最重要的，也是必须在调用函数时明确提供的参数！位置参数必须按先后顺序，一一对应，个数不多不少的传递！

"""

# 二、 默认参数
"""  
在函数定义时，如果给某个参数提供一个默认值，这个参数就变成了默认参数，不再是位置参数了。
在调用函数的时候，我们可以给默认参数传递一个自定义的值，也可以使用默认值。
默认参数必须在位置参数后面！  
def power(x, n = 2):
    return x**n

    
使用参数名传递参数
位置参数都是按顺序先后传入,而且必须在默认参数前面。但如果在位置参数传递时，给实参指定位置参数的参数名，那么位置参数也可以不按顺序调用
def student(name, age, classroom, tel, address="..."):
    pass
student(classroom=101, name="Jack", tel=66666666, age=20)       


默认参数尽量指向不变的对象！
def func(a=[]):
    a.append("A")
    return a

print(func()) # ['A']
print(func()) # ['A', 'A']
print(func()) # ['A', 'A', 'A']

"""

# 三、 动态参数
"""  
动态参数就是传入的参数的个数是动态的，可以是1个、2个到任意个，还可以是0个。在不需要的时候，你完全可以忽略动态函数，不用给它传递任何值。

Python的动态参数有两种，分别是*args和**kwargs，这里面的关键是一个和两个星号的区别，
而不是args和kwargs在名字上的区别，实际上你可以使用*any或**whatever的方式。但就如self一样，默认大家都使用*args和**kwargs。

# 注意：动态参数，必须放在所有的位置参数和默认参数后面！
def func(name, age, sex='male', *args, **kwargs):
    pass

"""
# 1.*args
# 一个星号表示接收任意个参数。调用时，会将实际参数打包成一个元组传入形式参数。如果参数是个列表，会将整个列表当做一个参数传入。例如：
def func(*args):
    for arg in args:
        print(arg)

func('a', 'b', 'c') #a  b  c
li = [1, 2, 3]
func(li) # [1, 2, 3]

"""  
通过循环args，我们可以获得传递的每个参数。但是li这个列表，我们本意是让它内部的1,2,3分别当做参数传递进去，但实际情况是列表本身被当做一个整体给传递进去了。
使用一个星号！调用函数，传递实参时，在列表前面添加一个星号就可以达到目的了。
实际情况是，不光列表，任何序列类型数据对象，比如字符串、元组都可以通过这种方式将内部元素逐一作为参数，传递给函数。而字典，则会将所有的key逐一传递进去。

"""
func(*li) # 1  2  3



# 2.**kwargs
# 两个星表示接受键值对的动态参数，数量任意。调用的时候会将实际参数打包成字典。例如：
def func(**kwargs):
    for kwg in kwargs:
        print(kwg, kwargs[kwg])
        print(type(kwg))

func(k1='v1', k2=[0, 1, 2])
print("=================================")
dic = {
    'k1': 'v1',
    'k2': 'v2'
}
func(**dic)


# 3.“万能”参数
"""  
当*args和**kwargs组合起来使用，理论上能接受任何形式和任意数量的参数，在很多代码中我们都能见到这种定义方式。
需要注意的是，*args必须出现在**kwargs之前。
"""
print("=======================万能参数====================")
def func2(a, b, c=1,*args, **kwargs):
    for arg in args:
        print(arg)

    for kwg in kwargs:
        print(kwg, kwargs[kwg])


lis = ['aaa', 'bbb', 'ccc']
dic = {
    'k1': 'v1',
    'k2': 'v2'
}

func2(1, 2, *lis, **dic,)

# 4.关键字参数

# 对于*args和**kwargs参数，函数的调用者可以传入任意不受限制的参数。
# 关键字参数前面需要一个特殊分隔符*和位置参数及默认参数分隔开来，*后面的参数被视为关键字参数。
# 在函数调用时，关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错

def student(name, age, *, sex):
    print(name,age,sex)
# sex 此时为关键字参数
student(name="jack", age=18, sex='male') #jack 18 male
# student(name="ken", age=8)

# 如果函数定义中已经有了一个*args参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了。
def student(name, age=10, *args, sex, classroom, **kwargs):
    print("+++++++++++++++++++++++++++++++")
    print(name,age,args,sex,classroom,kwargs)

student(name="jack", age=18, sex='male', classroom="202", k1="v1") #jack 18 () male 202 {'k1': 'v1'}