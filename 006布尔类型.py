# 对于错、0和1、正与反，都是传统意义上的布尔类型。

# 但在Python语言中，布尔类型只有两个值，True与False。请注意，是英文单词的对与错，并且首字母要大写，不能其它花式变型。

# Python内置的bool()函数可以用来测试一个表达式的布尔值结果。

# 你会发现很多想当然的结果居然是错的。0、0.0、-0.0、空字符串、空列表、空元组、空字典，这些都被判定为False。而-1、"False"也被判断为True。


# 布尔类型可以进行and、or和not运算。

# and运算是与运算，只有所有都为True，and运算的结果才是True：
# or运算是或运算，只要其中有一个为True，or运算结果就是True：
# not运算是非运算，它是单目运算符，把True变成False，False变成True：
# 再开下脑洞，布尔类型还能做别的运算吗？试试就知道了！
True > False  # True
True < False  # False
True >=False  #True
True -1     #0
True + 1   #2
True *3    #3
False -1   #-1
# 比较运算，四则运算都没有问题。并且在做四则运算的时候，明显把True看做1，False看做0

# 空值：None
# 空值不是布尔类型，严格的来说放在这里是不合适的，只不过和布尔关系比较紧密。
# 空值是Python里一个特殊的值，用None表示（首字母大写）。None不能理解为0，因为0是整数类型，而None是一个特殊的值。None也不是布尔类型，而是NoneType。

# 我们平时最容易犯的错误就是获得了一个None值，却对它进行各种方法调用，例如：
list1 = ["a", "b",None]
for char in list1:
    print(char.join("A"))  # 报错




