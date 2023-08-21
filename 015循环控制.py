# 循环控制，就是让程序循环运行某一段代码直到满足退出的条件，才退出循环。

# Python用关键字for和while来进行循环控制，但是没有其它语言的do...while语句。

# 一、while循环
"""  
语法格式：

while 判断表达式：
    内部代码块
"""

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum)) #1 到 100 之和为: 5050

# 二、while的else从句：
"""  
while循环还可以增加一个else从句。当while循环正常执行完毕，会执行else语句。
但如果是被break等机制强制提前终止的循环，不会执行else语句。注意else与while平级的缩进方式！

"""
number = 10
i = 0
while i < number:
    print(i)
    i += 1
else:
    print("执行完毕！",i)

print("=================================")
# 下面是被打断的while循环，else不会执行：
number1 = 10
i1 = 0
while i1 < number1:
    print(i1)
    i1 += 1
    if i1 == 7:
        break           
else:
    print("执行完毕！",i1) #不会执行

print("for=========for============for==========")

# 三、for循环
# 虽然与while一样都是循环的关键字，但for循环通常用来遍历可迭代的对象，如一个列表或者一个字典。其一般格式如下
"""  
for <variable> in <sequence>:
    <statements>
"""
# for ... in ....:属于固定套路。其实我们在前面的章节已经或多或少的介绍过for的用法，尤其是遍历一些数据类型的时候。

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum) #55

# 四、for循环的else 子句：
# 与while一样，for循环也可以有else子句。同样是正常结束循环时，else子句执行。被中途break时，则不执行。

# 循环的嵌套
# 这是一个判断质数的程序
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# break语句

"""  
通常情况下的循环要么执行出错，要么死循环，要么就只能老老实实等它把所有的元素循环一遍才能退出。
如果想在循环过程中退出循环，怎么办？用break语句！

break只能用于循环体内。其效果是直接结束并退出当前循环，剩下的未循环的工作全部被忽略和取消。
注意当前两个字，Python的break只能退出一层循环，对于多层嵌套循环，不能全部退出。
"""
var = 10                    # 第二个实例
while var > 0:              
    print ('当期变量值为 :', var)
    var -= 1
    if var == 5:
      break

# continue语句
"""  
与break不同，continue语句用于跳过当前循环的剩余部分代码，直接开始下一轮循环。它不会退出和终止循环，只是提前结束当前轮次的循环。
同样的，continue语句只能用在循环内。
"""
var1 = 10                    # 第二个实例
while var1 > 0:              
    var1 -= 1
    if var1 == 5:             # 变量为 5 时跳过输出
      continue
    print('continue语句当前变量值 :', var1)


# Python没有goto语法
