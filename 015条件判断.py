# 条件判断是通过一条或多条判断语句的执行结果（True或者False）来决定执行的代码块。
# 在Python语法中，使用if、elif和else三个关键字来进行条件判断。

"""  
条件判断的使用原则：
    每个条件后面要使用冒号（:）作为判断行的结尾，表示接下来是满足条件（结果为True）后要执行的语句块。
    除了if分支必须有，elif和else分支都可以根据情况省略。
    使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
    顺序判断每一个分支，任何一个分支首先被命中并执行，则其后面的所有分支被忽略，直接跳过！
    在Python中没有switch – case语句。

    if/else语句可以嵌套，也就是把 if...elif...else 结构放在另外一个 if...elif...else 结构中。形如下面的结构：

"""
number = 20
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")