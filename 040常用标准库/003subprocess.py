"""  
subprocess模块主要用于创建子进程，并连接它们的输入、输出和错误管道，获取它们的返回状态。
通俗地说就是通过这个模块，你可以在Python的代码里执行操作系统级别的命令，比如“ipconfig”、“du -sh”等等。subprocess模块替代了一些老的模块和函数，比如：

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)
功能：执行args参数所表示的命令，等待命令结束，并返回一个CompletedProcess类型对象。
1、args：表示要执行的命令。必须是一个字符串，字符串参数列表。
2、stdin、stdout和stderr：子进程的标准输入、输出和错误。
    其值可以是subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者None。
    subprocess.PIPE表示为子进程创建新的管道。subprocess.DEVNULL表示使用os.devnull。默认使用的是None，表示什么都不做。另外，stderr可以合并到stdout里一起输出。
3、timeout：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出TimeoutExpired异常。
4、check：如果该参数设置为True，并且进程退出状态码不是0，则弹出CalledProcessError异常。
5、encoding:如果指定了该参数，则stdin、stdout和stderr可以接收字符串数据，并以该编码方式编码。否则只接收bytes类型的数据。
5、shell：如果该参数为True，将通过操作系统的shell执行指定的命令。



"""
import os
import subprocess
# subprocess.run("exit 1", shell=True, check=True)
subprocess.run(["ls", "-l"])
