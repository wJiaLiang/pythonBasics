# 在编程语言中，代码块、函数、类、模块，一直到包，逐级封装，层层调用。
# 在Python中，一个.py文件就是一个模块，模块是比类更高一级的封装。在其他语言，被导入的模块也通常称为库。

# 使用模块还可以避免类名、函数名和变量名发生冲突。相同名字的类、函数和变量完全可以分别存在不同的模块中。
# 但是也要注意尽量不要与内置函数名（类名）冲突。

# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package），包是模块的集合，比模块又高一级的封装。
# 没有比包更高级别的封装，但是包可以嵌套包，就像文件目录一样，如下图：


# 包名通常为全部小写，避免使用下划线。
# 用其它的模块（包、类、函数），就必须先导入对应的模块（包、类、函数）。在Python中，模块（包、类、函数）的导入方式有以下四种：
"""  
import xx.xx
from xx.xx import xx
from xx.xx import xx as rename
from xx.xx import *

对于xx.xx的说明：

由于一个模块可能会被一个包封装起来，而一个包又可能会被另外一个更大的包封装起来，
所以我们在导入的时候，需要提供导入对象的绝对路径，也就是“最顶层的包名.次一级包名.（所有级别的包名）.模块名.类名.函数名”。
类似文件系统的路径名，只是用圆点分隔的。
# 有时候，模块名就在搜索路径根目录下，那么可以直接import 模块名，比如Python内置的一些标准模块，os、sys、time等等。

1. import xx.xx
这会将对象（这里的对象指的是包、模块、类或者函数，下同）中的所有内容导入。如果该对象是个模块，那么调用对象内的类、函数或变量时，需要以module.xxx的方式。
比如，被导入的模块Module_a：

# Module_a.py
def func():
    print("this is module A!") 
在Main.py中导入Module_a：

# Main.py
import module_a
module_a.func()  # 调用方法

2. From xx.xx import xx.xx
从某个对象内导入某个指定的部分到当前命名空间中，不会将整个对象导入。这种方式可以节省写长串导入路径的代码，但要小心名字冲突。
在Main.py中导入Module_a：

# Main.py
from module_a import func
module_a.func()   # 错误的调用方式
func()  # 这时需要直接调用func


3. from xx.xx import xx as rename
为了避免命名冲突，在导入的时候，可以给导入的对象重命名。

# Main.py
from module_a import func as f
def func(): ## main模块内部已经有了func函数
    print("this is main module!")
func()
f()


4. from xx.xx import *
将对象内的所有内容全部导入。非常容易发生命名冲突，请慎用！

# Main.py
from module_a import *
def func():
    print("this is main module!")
func()  # 从module导入的func被main的func覆盖了



模块搜索路径
不管你在程序中执行了多少次import，一个模块只会被导入一次。这样可以防止一遍又一遍地导入模块，节省内存和计算资源。
那么，当使用import语句的时候，Python解释器是怎样找到对应的文件的呢？

Python根据sys.path的设置，按顺序搜索模块。
import sys
print(sys.path)

['d:\\z_my\\z_project\\pythonBasics', 
'D:\\z_proenv\\Python3.10.10\\python310.zip', 
'D:\\z_proenv\\Python3.10.10\\DLLs', 
'D:\\z_proenv\\Python3.10.10\\lib', 
'D:\\z_proenv\\Python3.10.10', 
'D:\\z_proenv\\Python3.10.10\\lib\\site-packages']

当然，这个设置是可以修改的，就像windows系统环境变量中的path一样，可以自定义。
通过sys.path.append('路径')的方法为sys.path路径列表添加你想要的路径。
默认情况下，模块的搜索顺序是这样的：

1、当前执行脚本所在目录
2、Python的安装目录
3、Python安装目录里的site-packages目录
其实就是“自定义”——>“内置”——>“第三方”模块的查找顺序。任何一步查找到了，就会忽略后面的路径，所以模块的放置位置是有区别的。

"""

# 包（Package）：
# 前面我们已经介绍过，包是一种管理模块的手段，采用“包名.子包名.....模块名”的调用形式，非常类似文件系统中的文件目录。但是包不等于文件目录！
# 只有包含__init__.py文件的目录才会被认作是一个包！

"""  
Python会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。 
但是这个方法有风险，有可能导入的模块和已有的模块冲突，或者并不需要导入所有的模块。
为了解决这个问题，需要提供一个精确的模块索引。这个索引要放置在__init__.py中。

如果包定义文件__init__.py中存在一个叫做__all__的列表变量，那么在使用from package import *的时候就把这个列表中的所有名字作为要导入的模块名。

例如在example/p1/__init__.py中包含如下代码:
__all__ = ["x"]
这表示当你使用from example.p1 import *这种用法时，你只会导入包里面的x子模块。

"""


# Python 中的 if __name__ == 'main' 的作用和原理
"""
__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被运行。

由于每个Python模块（Python文件）都包含内置的变量__name__，当运行模块被执行的时候，__name__等于文件名（包含了后缀.py）。
如果import到其他模块中，则__name__等于模块名称（不包含后缀.py）。
而“__main__”等于当前执行文件的名称（包含了后缀.py）。
所以当模块被直接执行时，__name__ == '__main__'结果为真；
而当模块被import到其他模块中时，__name__ == '__main__'结果为假，就是不调用对应的方法。

"""
if __name__ == "__main__":
    print(__name__)

print("name=>", __name__)  # '__main__'
print(type(__name__))  # <class 'str'>
print(type(__name__) == type(""))  # True
print(type(__name__) == type(1))
