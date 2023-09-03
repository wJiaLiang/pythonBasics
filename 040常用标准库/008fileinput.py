"""  
fileinput模块用于对标准输入或多个文件进行逐行遍历。这个模块的使用非常简单，相比open()方法批量处理文件，fileinput模块可以对文件、行号进行一定的控制。

基本方法
fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
创建并返回一个FileInput类的实例。files指定要处理的文件，可以是一个多元元组，表示按顺序批量处理元组内文件。
inplace参数最关键，可设置是否对源文件进行修改；backup则用于指定对源文件进行备份的后缀名；
mode用于指定文件读写方式，和open()方法的定义一样， 默认为只读‘r’。同样的，fileinput.input()方法也可以作为一个上下文管理器使用，如下所示：

with fileinput.input(files=('spam.txt', 'eggs.txt')) as f:
    for line in f:
        process(line)

这将保证input会在with语句结束之后被关闭，无论期间是否抛出过异常，确保文件安全。

主要属性:

fileinput.filename()
返回当前正在处理的文件名（也就是包含了当前正在处理的文本行的文件）

fileinput.fileno()
返回当前文件的总行数。

fileinput.lineno()
返回当前的行数，这个行数是累计的。多个文件的行数会累加起来。

fileinput.filelineno()
返回当前正在处理的文件的当前行数。每次处理完一个文件并开始处理下一个文件时，该值会重置为1，重新开始计数。

fileinput.isfirstline()
当前行是当前文件的第一行时返回True，否则False

fileinput.isstdin()
当前操作对象为sys.stdin时返回True否则False。

fileinput.nextfile()
关闭当前的文件，跳到下一个文件，跳过的行不计数。

fileinput.close()
关闭整个文件链，结束迭代。

现在有一个1.txt文件，内容如下：
愿圣光与你同在！
为了部落！
兽人永不为奴！
你们这是自寻死路！
复活吧我的勇士！
为你而战我的女士！

我们的需求是为每一行添加“#行号”

import fileinput
with fileinput.input(files="d:\\1.txt") as f:
    for line in f:
        line = line.rstrip()
        num = fileinput.lineno()
        print("#%d\t%s" % (num, line))

如果你想同步修改源文件，添加inplace=True参数即可，但一定要小心，请确认自己的行为，防止误操作！

"""