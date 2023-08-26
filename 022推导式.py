"""  
Python语言有一种独特的推导式语法，相当于语法糖的存在，可以帮你在某些场合写出比较精简酷炫的代码。
但没有它，也不会有太多的影响。Python语言有几种不同类型的推导式，下面逐一介绍：
"""

# 1. 列表推导式
# 列表推导式是一种快速生成列表的方式。其形式是用方括号括起来的一段语句，如下例子所示：
lis = [x * x for x in range(1, 10)]
print(lis)  #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# 列表推导式要这么理解，首先执行for循环，对于每一个x，代入x*x中进行运算，将运算结果逐一添加到一个新列表内，循环结束，得到最终列表。
# 列表推导式有多种花样用法：
    # 增加条件语句
lis2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(lis2) # [4, 16, 36, 64, 100]

    # 多重循环
lis3 = [a + b for a in '123' for b in 'abc']
print(lis3) #['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']



# 2. 字典推导式
# 既然使用中括号[]可以编写列表推导式，那么使用大括号呢？你猜对了！使用大括号{}可以制造字典推导式！
dic = {x: x**2 for x in (2, 4, 6)}
print(dic) #{2: 4, 4: 16, 6: 36
# 注意x: x**2的写法，中间的冒号，表示左边的是key右边的是value。


# 3. 集合推导式
# 大括号除了能用作字典推导式，还可以用作集合推导式，两者仅仅在细微处有差别。
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'d', 'r'}


# 4、 还有圆括号！是不是元组推导式？想法不错，但事实却没有 圆括号在Python中被用作生成器的语法了，没有元组推导式。

tup = (x for x in range(9))
print(tup)    # <generator object <genexpr> at 0x000001AFE01E8430
print(type(tup))  # <class 'generator'>

# 要通过类似方法生成元组，需要显式调用元组的类型转换函数tuple()，如下所示：
tup2 = tuple(x for x in range(9))
print(tup2)  # (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(type(tup2)) # <class 'tuple'>


# 测试
result = [lambda x: x + i for i in range(10)]
print(result)
print(result[0](10))

# result 会返回 10 个匿名函数的列表,生产列表的过程中匿名函数并没有调用， range 执行完成后 i 的值为9，所以返回19

result = [lambda x, i=i: x + i for i in range(10)]
print(result[0](10)) #10