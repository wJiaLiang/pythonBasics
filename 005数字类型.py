# 数字类型是不可变类型。所谓的不可变类型，指的是类型的值一旦有不同了，那么它就是一个全新的对象。
# 数字1和2分别代表两个不同的对象，对变量重新赋值一个数字类型，会新建一个数字对象。

# 还是要强调一下Python的变量和数据类型的关系，变量只是对某个对象的引用或者说代号、名字、调用等等，
# 变量本身没有数据类型的概念。类似1，[2, 3, 4]，“haha”这一类对象才具有数据类型的概念。

a = 1 # 创建数字对象1
a = 2 # 创建数字对象2，并将2赋值给变量a，a不再指向数字对象1

# 这里，发生了变化的是变量a的指向，而不是数字对象1变成了数字对象2。初学者可能会比较迷糊，但不要紧，我们努力去明白它。


# Python 支持三种不同的数字类型，整数、浮点数和复数：


# 1. 整数(Int) ：
# 通常被称为整型，是正或负整数，不带小数点。Python3的整型可以当作Long类型（更长的整型）使用，所以 Python3没有Python2的Long类型。

# 表示数字的时候，有时我们还会用八进制或十六进制来表示：
# 十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2。
# 八进制用0o前缀和0-7表示，例如0o12
# Python的整数长度为32位，并且通常是连续分配内存空间的。


"""  





"""