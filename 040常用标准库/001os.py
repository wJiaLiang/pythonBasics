# os模块是Python标准库中的一个用于访问操作系统相关功能的模块，os模块提供了一种可移植的使用操作系统功能的方法。
# 使用os模块中提供的接口，可以实现跨平台访问。但是，并不是所有的os模块中的接口在全平台都通用，
# 有些接口的实现是一来特定平台的，比如linux相关的文件权限管理和进程管理。

# 在使用os模块的时候，如果出现了问题，会抛出OSError异常，表明无效的路径名或文件名，或者路径名(文件名)无法访问，或者当前操作系统不支持该操作。


# 1. 系统相关
# os模块提供了一些操作系统相关的变量，可以在跨平台的时候提供支持，便于编写移植性高，可用性好的代码。
# 所以在涉及操作系统相关的操作时，请尽量使用本模块提供的方法，而不要使用当前平台特定的用法或格式，否则一旦移植到其他平台，可能会造成难以解决的困扰。

"""  
方法和变量	     用途
os.name	        查看当前操作系统的名称。windows平台下返回‘nt’，Linux则返回‘posix’。
os.environ	    获取系统环境变量
os.sep	        当前平台的路径分隔符。在windows下，为‘\’，在POSIX系统中，为‘/’。
os.altsep	    可替代的路径分隔符，在Windows中为‘/’。
os.extsep	    文件名和文件扩展名之间分隔的符号，在Windows下为‘.’。
os.pathsep	    PATH环境变量中的分隔符，在POSIX系统中为‘:’，在Windows中为‘;’。
os.linesep	    行结束符。在不同的系统中行尾的结束符是不同的，例如在Windows下为‘\r\n’。
os.devnull	    在不同的系统上null设备的路径，在Windows下为‘nul’，在POSIX下为‘/dev/null’。
os.defpath	    当使用exec函数族的时候，如果没有指定PATH环境变量，则默认会查找os.defpath中的值作为子进程PATH的值。

""" 
import os
print(os.name,"\n")
print(os.environ,"\n")
print(os.sep,'\n')
print(os.pathsep,'\n')
print(os.linesep,'\n')
print(os.devnull,'\n')
print(os.defpath,'\n')

# 2. 文件和目录操作
"""  
os模块中包含了一系列文件操作相关的函数，其中有一部分是Linux平台专用方法。
Linux是用C写的，底层的libc库和系统调用的接口都是C API，Python的os模块中包括了对这些接口的Python实现，通过Python的os模块，
可以调用Linux系统的一些底层功能，进行系统编程。关于Linux的相关方法，内容较为复杂，
可根据需要自行查阅官方文档，这里只介绍一些常用的，各平台通用的方法。

方法和变量	                     用途
os.getcwd()	                    获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")	            改变当前脚本工作目录；相当于shell下cd
os.curdir	                    返回当前目录: ('.')
os.pardir	                    获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')	    可生成多层递归目录
os.removedirs(‘dirname1’)	    递归删除空目录（要小心）
os.mkdir('dirname')	            生成单级目录
os.rmdir('dirname')	            删除单级空目录，若目录不为空则无法删除并报错
os.listdir('dirname')	        列出指定目录下的所有文件和子目录，包括隐藏文件
os.remove('filename')	        删除一个文件
os.rename("oldname","new")	    重命名文件/目录
os.stat('path/filename')	    获取文件/目录信息
os.path.abspath(path)	        返回path规范化的绝对路径
os.path.split(path)	            将path分割成目录和文件名二元组返回
os.path.dirname(path)	        返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)	        返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。
os.path.exists(path或者file)	如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)	            如果path是绝对路径，返回True
os.path.isfile(path)	        如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)	            如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])	将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)	        返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)	    返回path所指向的文件或者目录的最后修改时间
os.path.getsize(filename)	返回文件包含的字符数量

"""
cp = os.getcwd()
print(cp)
print(os.path.join(cp,"/a/b"))
path = "D:\z_my\z_project\pythonBasics"
print(os.path.getatime(path))

# os.walk(top, topdown=True, onerror=None, followlinks=False)
"""  
walk方法是os模块中非常重要和强大的一个方法。可以帮助我们非常便捷地以递归方式自顶向下或者自底向上的方式遍历目录树，
对每一个目录都返回一个三元元组(dirpath, dirnames, filenames)。

三元元组(dirpath，dirnames，filenames)：
dirpath - 遍历所在目录树的位置，是一个字符串对象
dirnames - 目录树中的子目录组成的列表，不包括("."和"..")
filenames - 目录树中的文件组成的列表

如果可选参数topdown = True或者没有指定，则采用自顶向下的方式进行目录遍历，也就是从父目录向子目录逐步深入遍历，
如果topdown = False，则采用自底向上的方式遍历目录，也就是先打印子目录再打印父目录的方式。

"""
try:
    for root, dirs, files in os.walk(r"D:\z_my\z_project\pythonBasics\027文件读写"):
        print("\033[1;31m-"*8, "directory", "<%s>\033[0m" % root, "-"*10)
        for directory in dirs:
            print("\033[1;34m<DIR>    %s\033[0m" % directory)
        for file in files:
            print("\t%s" % file)
except OSError as ex:
    print(ex)



# 3. 执行命令
"""  
在早期的Python版本中，通常使用os模块的system或者popen等方法执行操作系统的命令。但是，最近Python官方逐渐弃用了这些命令，
而是改用内置的subprocess模块执行操作系统相关命令。由于目前还有很多人仍然在使用os的system和popen方法，在此简要介绍一下。

os.system(command)
运行操作系统命令，直接显示结果。但返回值是0或-1，不能获得显示在屏幕上的数据。 command是要执行的命令字符串。
os.system('ipconfig /all')


os.popen(command, [mode, [bufsize]])
开启一个子进程执行command参数指定的命令，在父进程和子进程之间建立一个管道pipe，用于在父子进程间通信。
该方法返回一个文件对象，可以对这个文件对象进行读或写，取决于参数mode，如果mode指定了只读，那么只能对文件对象进行读，
如果mode参数指定了只写，那么只能对文件对象进行写操作。

简而言之，popen也可以运行操作系统命令，并通过read()方法将命令的结果返回，不像system只能看不能存，这个能存！
ret = os.popen('ipconfig')
ret.read()
"""