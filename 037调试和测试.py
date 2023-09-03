"""  
没有一次性写好的代码，也没有不用修改、优化、测试、扩展的代码！无论你事先多有把握，
思考了多久，设计得多完善，总会存在各种各样，你意想不到的问题，或者说缺陷，甚至是Bug。
这些都需要你在代码编写过程中或者后期维护升级中，不断的对程序进行调试和测试。

"""

# 一、 调试
"""  
1. 初学者简单粗暴的方法：print大法
2. 断言assert
Python内置了一个assert关键字，表示断言。凡是用print()来辅助查看的地方，都可以用断言来替代。
它会对后面的表达式进行判断，如果表达式为True，那就什么都不做，程序接着往下走；如果False，那么就会弹出异常。
比如下面的例子，断言此处a的值必定大于5，如果不是，那么说明前面的代码有问题，程序在此中断！
a = 1
pass
assert a > 5
pass

assert是一个非常有用的技巧，通过选择关键因子，对因子的状态进行判定，可以将程序一块一块的进行划分，逐步的缩小问题范围。
但是，程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert。
关闭后，所有的assert语句相当于pass语句。

3. 日志logging
logging是Python内置的一个日志模块，不但可以将信息在屏幕上打印，还可以输出到文件，保留下来。使用logging之前，需要先通过import logging导入该模块。
import logging
logging.basicConfig(level=logging.INFO)
def func(s):
    logging.info("s的数据类型为 %s" % type(s))
    return s/10

func("100")

logging允许你指定记录信息的级别，有DEBUG，INFO，WARNING，ERROR等几种级别，级别参数level会忽略比它低的级别信息。
当指定level=INFO时，logging.DEBUG就不起作用了。同理，指定level=WARNING后，DEBUG和INFO就不起作用了。
logging.basicConfig(level=logging.INFO)这行就是指定只有INFO以上级别的信息才会被记录下来。

4. pdb模块
除了上面的方法外，Python还专门提供了一个pdb模块，可以单步或断点调试程序。
运行方式：$ python -m pdb 文件名。但这依然不是好的解决方案，因为它不够简单直观。我们通常更多使用的还是IDE的调试功能，比如Pycharm的调试功能。





"""




# 二、 单元测试之unittest

"""  
单元测试是用来对一个模块、一个函数或者一个类进行正确性检验的工作。你的代码可能在语法、词法和运行过程中没有问题了，
但是并不能代表它就完全符合你的设计预期，很有可能你希望得到A，它给你的结果却是B。
这就需要我们对程序进行单元测试。单元测试测的不是语法问题，而是业务逻辑是否正确的问题。单元测试是软件开发过程中非常重要的一个环节。




"""