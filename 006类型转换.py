# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。
"""  
Python 数据类型转换可以分为两种：
    隐式类型转换 - 自动完成
        1.较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。
    显式类型转换 - 需要使用类型函数来转换
"""
# 1 隐式类型转换
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print("num_new 值为:", num_new)  # 124.23
print("num_new 数据类型为:", type(num_new))  # <class 'float'>


# 2 显式类型转换

# int() 强制转换为整型：
a = int(True)  # 1
b = int(False)  # 0
x = int(1)    # x 输出结果为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3
print(a, b, x, y, z)

# float() 强制转换为浮点型：
a1 = float(True)  # 1.0
b1 = float(False)  # 0.0
x1 = float(1)     # x 输出结果为 1.0
y1 = float(2.8)   # y 输出结果为 2.8
z1 = float("3")   # z 输出结果为 3.0
w1 = float("4.2")  # w 输出结果为 4.2
print(a1, b1, x1, y1, z1)

# str() 强制转换为字符串类型：
a2 = str(True)  # 'True'
b2 = str(False)  # 'False'
x2 = str("s1")  # x 输出结果为 's1'
y2 = str(2)    # y 输出结果为 '2'
z2 = str(3.0)  # z 输出结果为 '3.0'
print(a2, b2, x2, y2, z2)

# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
"""  
函数	                描述

int(x [,base])          将x转换为一个整数
float(x)                将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)                  将对象 x 转换为字符串
repr(x)                 将对象 x 转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                tuple(s)
list(s)                 将序列 s 转换为一个列表
set(s)                  转换为可变集合
dict(d)                 创建一个字典。d 必须是一个 (key, value)元组序列。
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串



"""
