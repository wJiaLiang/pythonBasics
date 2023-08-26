
# 在介绍迭代器之前，先说明下迭代的概念：

# 一、 迭代：通过for循环遍历对象的每一个元素的过程。
# Python的for语法功能非常强大，可以遍历任何可迭代的对象。
# 在Python中，list/tuple/string/dict/set/bytes都是可以迭代的数据类型。

# 可以通过collections模块的Iterable类型来判断一个对象是否可迭代：
from collections.abc import Iterable
isRes = isinstance('abc', Iterable)
print(isRes) # True


# 二、迭代器
# 迭代器是一种可以被遍历的对象，并且能作用于next()函数。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往后遍历不能回溯，不像列表，你随时可以取后面的数据，也可以返回头取前面的数据。迭代器通常要实现两个基本的方法：iter() 和 next()。

lis=[1,2,3,4]
it = iter(lis)             # 使用Python内置的iter()方法创建迭代器对象
print(next(it))            # 1 使用next()方法获取迭代器的下一个元素
print(next(it))            # 2   当后面没有元素可以next的时候，弹出错误

it = iter(lis)          # 创建迭代器对象
for x in it:            # 使用for循环遍历迭代对象
    print (x, end=" ") 

# 很多时候，为了让我们自己写的类成为一个迭代器，需要在类里实现__iter__()和__next__()方法。

print("\n")
for i in [22,44,55]:
    print(i)
"""  
总结：Python的迭代器表示的是一个元素流，可以被next()函数调用并不断返回下一个元素，直到没有元素时抛出StopIteration错误。
可以把这个元素流看做是一个有序序列，但却不能提前知道序列的长度，只能不断通过next()函数得到下一个元素，所以迭代器可以节省内存和空间。
"""

# 三、 迭代器(Iterator)和可迭代(Iterable)的区别：
# 凡是可作用于for循环的对象都是可迭代类型；

# 凡是可作用于next()函数的对象都是迭代器类型；

# list、dict、str等是可迭代的但不是迭代器，因为next()函数无法调用它们。可以通过iter()函数将它们转换成迭代器。

# Python的for循环本质上就是通过不断调用next()函数实现的。






