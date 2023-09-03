# logging

# 1.1 logging使用场景
"""  
日志是什么？这个不用多解释。百分之九十的程序都需要提供日志功能。Python内置的logging模块，
为我们提供了现成的高效好用的日志解决方案。但是，不是所有的场景都需要使用logging模块，下面是Python官方推荐的使用方法：


任务场景	                        最佳工具
普通情况下，在控制台显示输出	      print()
报告正常程序操作过程中发生的事件	  logging.info()(或者更详细的logging.debug())
发出有关特定事件的警告	             warnings.warn()或者logging.warning()
报告错误	                        弹出异常
在不引发异常的情况下报告错误	     logging.error(), logging.exception()或者logging.critical()

logging模块定义了下表所示的日志级别，按事件严重程度由低到高排列（注意是全部大写！因为它们是常量。）：

级别	    级别数值	      使用时机
DEBUG	    10	             详细信息，常用于调试。
INFO	    20	             程序正常运行过程中产生的一些信息。
WARNING	    30	             警告用户，虽然程序还在正常工作，但有可能发生错误。
ERROR	    40	             由于更严重的问题，程序已不能执行一些功能了。
CRITICAL	50	             严重错误，程序已不能继续运行。

"""
# 在什么都不配置和设定的情况下，logging会简单地将日志打印在显示器上，如下例所示：

import logging
logging.warning('Watch out!')  # 消息会被打印到控制台上
logging.info('I told you so')  # 这行不会被打印，因为级别低于默认级别

# 默认情况下，打印出来的内容包括日志级别、调用者和具体的日志信息。所有的这些内容都是可以自定义的，在后面我们会细说。


# 1.3 记录到文件内
# 要把日志输出到文件内，就不能使用上面的方法了，但是logging模块同样给我们提供了一个相对便捷的手段，那就是logging.basicConfig()方法。
import logging
logging.basicConfig(filename='example.log',filemode='w',level=logging.WARNING)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

