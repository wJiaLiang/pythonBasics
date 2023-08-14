# 一、 input输入函数

# input函数：获取用户输入，保存成一个字符串。input函数的返回值是一个字符串类型。
# 哪怕你输入的是个数字1，返回给你的只会是字符串“1”，而不是 整数1


"""  
>>> age  = input("please input your age: ")
please input your age: 18
>>> age
'18'
>>> type(age)
<class 'str'>
type是Python内置的函数之一，非常有用，用于查看对象的数据类型

比如将字符串转换成数字类型：
age = int(age)   # 将字符串转化为整数



# 使用int()转换前应该先判断，否则报错
if age.isdigit():   # 使用isdigit函数判断输入是否全是数字格式
    age = int(age)   # 将字符串转化为整数
    print("你的年龄是： ", age)
else:
    print("输入不合法！")


去除开头的空白lstrip,去除结尾的空白rstrip以及去除两端的空白strip
inp = inp.strip()  # strip的用法在字符串数据类型有讲述
print(inp)


"""
age  = input("please input your age: ")
if age.isdigit():   # 使用isdigit函数判断输入是否全是数字格式
    age = int(age)   # 将字符串转化为整数
    print("你的年龄是： ", age)
else:
    print("输入不合法！")


# nput函数有时可以巧妙地用于阻塞或暂停程序
print("程序前面部分执行完毕......")
input("请按回车继续......")       # 在这里程序会暂停，等待你的回车动作
print("继续执行程序的后面部分......")
# 此时的input函数不会将输入保存下来，只是用作暂停程序动作。



# 二、 print输出函数
# print函数用于将内容格式化显示在标准输出上，主要指的是屏幕显示器。
# print可以接受多个字符串，字符串类型的变量或者可print的对象。每个字符串用逗号“,”隔开，连成一串输出。
# print会依次打印每个字符串，同时，每遇到一个逗号“,”就输出一个空格
"""  
>>> a = "i am"
>>> b = "student"
>>> print(a,"a" , b)
i am a student      # 自动以空格分隔
>>> print(a+"a"+b)
i amastudent        # 无分隔

"""

# 三、 print格式化输出
# 一种就是类似C语言的printf的%百分号格式化输出，也是Python最基础最常用的格式化输出方式。
# 另一种就是str.format()的方式，在后面的章节会连同颜色控制一块介绍。
"""  
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
首先构造一个字符串"我叫 %s 今年 %d 岁!"，将其中需要用别的变量或值替代的部分，用%百分符加一个数据类型代号，
比如%s、%d来代替。然后在字符串的后面用%加一个同样数量变量或值的元组。

也就是前面字符串中有多少个%符号，后面就要提供多少个参数值，每个参数值之间用逗号隔开，所有参数用圆括号括起来。
每个参数与前面的%一一对应，并且数据类型也要能够合法对应。

"""
print ("我叫 %s 今年 %d 岁!" % ('小明', 12))



# 格式化操作符辅助指令:
