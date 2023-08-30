# Python内置的@property装饰器可以把类的方法伪装成属性调用的方式。
# 也就是本来是Foo.func()的调用方法，变成Foo.func的方式。在很多场合下，这是一种非常有用的机制。



class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @age.deleter
    def age(self):
        print("删除年龄数据！")

obj = People("jack", 18)
print(obj.age) # 获取值
obj.age = 19   # 重新赋值
print("obj.age:  ", obj.age)
del obj.age    # 重新赋值

"""  
那么如何将一个普通的方法转换为一个“伪装”的属性呢？

1、首先，在普通方法的基础上添加@property装饰器，例如上面的age()方法。
这相当于一个get方法，用于获取值,决定类似"result = obj.age"执行什么代码。该方法仅有一个self参数。

2、写一个同名的方法，添加@xxx.setter装饰器（xxx表示和上面方法一样的名字），比如例子中的第二个方法。
这相当于编写了一个set方法，提供赋值功能，决定类似"obj.age = ...."的语句执行什么代码。

3、再写一个同名的方法，并添加@xxx.delete装饰器，比如例子中的第三个方法。
用于删除功能，决定"del obj.age "这样的语句具体执行什么代码。

简而言之，就是分别将三个方法定义为对同一个属性的获取、修改和删除。
还可以定义只读属性，也就是只定义getter方法，不定义setter方法就是一个只读属性。
"""

# 二、property()函数
# 除了使用装饰器的方式将一个方法伪装成属性外，Python内置的builtins模块中的property()函数，为我们提供了第二种设置类属性的手段。

class People2:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    def del_age(self):
        print("删除年龄数据！")

    # 核心在这句
    age = property(get_age, set_age, del_age, "年龄")


obj2 = People2("jack", 22)
print(obj2.age) # 22
obj2.age = 33
print("obj.age:  ", obj2.age) # obj.age:   33
del obj2.age  # 删除年龄数据！
print(obj2.age.__doc__)
help(People2.age)

"""  
通过语句age = property(get_age, set_age, del_age, "年龄")将一个方法伪装成为属性。其效果和装饰器的方法是一样的。
property()函数的参数：
第一个参数是方法名，调用 实例.属性 时自动执行的方法
第二个参数是方法名，调用 实例.属性 ＝ XXX时自动执行的方法
第三个参数是方法名，调用 del 实例.属性 时自动执行的方法
第四个参数是字符串，调用 实例.属性  __doc__时的描述信息。

"""