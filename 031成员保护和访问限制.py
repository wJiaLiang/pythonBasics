# 在类的内部，有各种变量和方法。这些数据成员，可以在类的外部通过实例或者类名进行调用，例如：
class People:
    title = "人类"
    def __init__(self, name, age):
        self.__name = name  # 无法从外部访问
        self.age = age
    def print_age(self):
        print('%s: %s' % (self.__name, self.age))

obj = People("jack", 12)
obj.age = 18
obj.print_age()
print(People.title)

"""  
上面的调用方式是我们大多数情况下都需要的，但是往往我们也不希望所有的变量和方法能被外部访问，需要针对性地保护某些成员，限制对这些成员的访问。
这样的程序才是健壮、可靠的，也符合业务的逻辑。

在类似JAVA的语言中，有private关键字，可以将某些变量和方法设为私有，阻止外部访问。
但是，Python没有这个机制，Python利用变量和方法名字的变化，实现这一功能。


在Python中，如果要让内部成员不被外部访问，可以在成员的名字前加上两个下划线__，这个成员就变成了一个私有成员（private）。
私有成员只能在类的内部访问，外部无法访问。

那外部如果要对__name 和 __age进行访问和修改呢？在类的内部创建外部可以访问的get和set方法！

"""
class People2:
    title = "人类"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_age(self):
        print('%s: %s' % (self.__name, self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

obj2 = People2("jack", 18)
obj2.get_name()
obj2.set_name("tom")

"""  
这样做，不但对数据进行了保护的同时也提供了外部访问的接口，而且在get_name,set_name这些方法中，
可以额外添加对数据进行检测、处理、加工、包裹等等各种操作，作用巨大！

比如下面这个方法，会在设置年龄之前对参数进行检测，如果参数不是一个整数类型，则抛出异常。

那么，以双下划线开头的数据成员是不是一定就无法从外部访问呢？其实也不是！本质上，从内部机制原理讲，
外部不能直接访问__age是因为Python解释器对外把__age变量改成了_People__age，也就是_类名__age（类名前是一个下划线）。
因此，投机取巧的话，你可以通过_ People__age在类的外部访问__age变量：

print(obj._People__name)

也就是说：Python的私有成员和访问限制机制是“假”的，没有从语法层面彻底限制对私有成员的访问。这一点和常量的尴尬地位很相似。

"""
print(obj2._People2__name) #tom


# 拓展：由于Python内部会对双下划线开头的私有成员进行名字变更，所以会出现下面的情况：
class People:
    title = "人类"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_age(self):
        print('%s: %s' % (self.__name, self.__age))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


obj = People("jack", 18)
obj.__name = "tom"          # 注意这一行
print("obj.__name:  ", obj.__name)
print("obj.get_name():  ", obj.get_name())

# 一定要注意，此时的obj.__name= 'tom'，相当于给obj实例添加了一个新的实例变量__name,而不是对原有私有成员__name的重新赋值。

"""  
此外，有些时候，你会看到以一个下划线开头的成员名，比如_name，这样的数据成员在外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的标识符时，意思就是，“虽然我可以被外部访问，但是，请把我视为私有成员，不要在外部访问我！”。

还有，在Python中，标识符类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊成员，特殊成员不是私有成员，可以直接访问，要注意区别对待。
同时请尽量不要给自定义的成员命名__name__或__iter__这样的标识，它们都是Python中具有特殊意义的魔法方法名

类的成员与下划线总结：
    _name、_name_、_name__:建议性的私有成员，不要在外部访问。
    __name、 __name_ :强制的私有成员，但是你依然可以蛮横地在外部危险访问。
    __name__:特殊成员，与私有性质无关，例如__doc__。
    name_、name__:没有任何特殊性，普通的标识符，但最好不要这么起名。

"""


