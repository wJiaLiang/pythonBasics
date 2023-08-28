# 封装
"""  
封装是指将数据与具体操作的实现代码放在某个对象内部，使这些代码的实现细节不被外界发现，
外界只能通过接口使用该对象，而不能通过任何形式修改对象内部实现，正是由于封装机制，
程序在使用某一对象时不需要关心该对象的数据结构细节及实现操作的方法。
使用封装能隐藏对象实现细节，使代码更易维护，同时因为不能直接调用、修改对象内部的私有信息，在一定程度上保证了系统安全性。
类通过将函数和变量封装在内部，实现了比函数更高一级的封装。


"""

# 继承

"""  
继承来源于现实世界，一个最简单的例子就是孩子会具有父母的一些特征，即每个孩子都会继承父亲或者母亲的某些特征，
当然这只是最基本的继承关系，现实世界中还存在着更复杂的继承。
继承机制实现了代码的复用，多个类公用的代码部分可以只在一个类中提供，而其他类只需要继承这个类即可。

在OOP程序设计中，当我们定义一个新类的时候，新的类称为子类（Subclass），而被继承的类称为基类、父类或超类（Base class、Super class）。
继承最大的好处是子类获得了父类的全部变量和方法的同时，又可以根据需要进行修改、拓展。其语法结构如下：

Python支持多父类的继承机制，所以需要注意圆括号中基类的顺序，若是基类中有相同的方法名，并且在子类使用时未指定，
Python会从左至右搜索基类中是否包含该方法。一旦查找到则直接调用，后面不再继续查找。

Python3的继承机制:

子类在调用某个方法或变量的时候，首先在自己内部查找，如果没有找到，则开始根据继承机制在父类里查找。
根据父类定义中的顺序，以深度优先的方式逐一查找父类！


在类A中，没有show()这个方法，于是它只能去它的父类里查找，它首先在B类中找，结果找到了，于是直接执行B类的show()方法。
可见，在A的定义中，继承参数的书写有先后顺序，写在前面的被优先继承。

"""

class H:
    def show(self):
        print("i am H")
    pass

class D(H):
    pass

class C(D):
    pass

class B(C):
    pass

class G(H):
    pass

class F(G):
    pass

class E(F): 
    def show(self):
        print("i am E")
    pass

class A(B, E):
    pass

a = A()
a.show()


# super()函数：
# 我们都知道，在子类中如果有与父类同名的成员，那就会覆盖掉父类里的成员。
# 那如果你想强制调用父类的成员呢？使用super()函数！这是一个非常重要的函数，最常见的就是通过super调用父类的实例化方法__init__！
# 语法：super(子类名, self).方法名()，需要传入的是子类名和self，调用的是父类里的方法，按父类的方法需要传入参数。

class A:
    def __init__(self, name):
        self.name = name
        print("父类的__init__方法被执行了！")
    def show(self):
        print("父类的show方法被执行了！")

class B(A):
    def __init__(self, name, age):
        super(B, self).__init__(name=name)
        self.age = age

    def show(self):
        super(B, self).show()

obj = B("jack", 18)
obj.show()


# 多态
class Animal:
    def kind(self):
        print("i am animal")

class Dog(Animal):
    def kind(self):
        print("i am a dog")

class Cat(Animal):
    def kind(self):
        print("i am a cat")

class Pig(Animal):
    def kind(self):
        print("i am a pig")

# 这个函数接收一个animal参数，并调用它的kind方法
def show_kind(animal):
    animal.kind()

d = Dog()
c = Cat()
p = Pig()

show_kind(d) # i am a dog
show_kind(c) # i am a cat
show_kind(p) # i am a pig
"""  
狗、猫、猪都继承了动物类，并各自重写了kind方法。show_kind()函数接收一个animal参数，并调用它的kind方法。
可以看出，无论我们给animal传递的是狗、猫还是猪，都能正确的调用相应的方法，打印对应的信息。这就是多态。

实际上，由于Python的动态语言特性，传递给函数show_kind()的参数animal可以是 任何的类型，只要它有一个kind()的方法即可。
动态语言调用实例方法时不检查类型，只要方法存在，参数正确，就可以调用。
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

"""
class Job:
    def kind(self):
        print("i am not animal, i am a job")

j = Job()
show_kind(j)


"""  
如果你学过JAVA这一类强类型静态语言，就不会这么觉得了，对于JAVA，必须指定函数参数的数据类型，
只能传递对应参数类型或其子类型的参数，不能传递其它类型的参数，show_kind()函数只能接收animal、dog、cat和pig类型，而不能接收job类型。
就算接收dog、cat和pig类型，也是通过面向对象的多态机制实现的。

"""