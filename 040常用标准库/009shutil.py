# shutil可以简单地理解为sh + util，shell工具的意思。shutil模块是对os模块的补充，主要针对文件的拷贝、删除、移动、压缩和解压操作。

# shutil模块的主要方法
"""  
1. shutil.copyfileobj(fsrc, fdst[, length=16*1024])
copy文件内容到另一个文件，可以copy指定大小的内容。这个方法是shutil模块中其它拷贝方法的基础，其它方法在本质上都是调用这个方法。
代码很简单，一看就懂。但是要注意，其中的fsrc，fdst都是使用open()方法打开后的文件对象。


2. shutil.copyfile(src, dst)
拷贝整个文件。


3. shutil.copymode(src, dst)
仅拷贝权限。内容、组、用户均不变。


4. shutil.copystat(src, dst)
仅复制所有的状态信息，包括权限，组，用户，时间等。


5. shutil.copy(src,dst)
同时复制文件的内容以及权限，也就是先copyfile()然后copymode()。


6. shutil.copy2(src, dst)
同时复制文件的内容以及文件的所有状态信息。先copyfile()后copystat()。

7. shutil.ignore_patterns(*patterns)
忽略指定的文件。通常配合下面的copytree()方法使用。

8. shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,ignore_dangling_symlinks=False)
递归地复制目录及其子目录的文件和状态信息
symlinks：指定是否复制软链接。小心陷入死循环。
ignore：指定不参与复制的文件，其值应该是一个ignore_patterns()方法。
copy_function：指定复制的模式


9. shutil.rmtree(path[, ignore_errors[, onerror]])
递归地删除目录及子目录内的文件。注意！该方法不会询问yes或no，被删除的文件也不会出现在回收站里，请务必小心！


10. shutil.move(src, dst)
递归地移动文件，类似mv命令，其实就是重命名。

11. shutil.which(cmd)
类似linux的which命令，返回执行该命令的程序路径。Python3.3新增

12. shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
创建归档或压缩文件。
base_name：压缩后的文件名。如果不指定绝对路径，则压缩文件保存在当前目录下。这个参数必须指定。
format：压缩格式，可以是“zip”, “tar”, “bztar” ，“gztar”，“xztar”中的一种。这个参数也必须指定。
root_dir：设置压缩包里的根目录，一般使用默认值，不特别指定。
base_dir：要进行压缩的源文件或目录。
owner：用户，默认当前用户。
group：组，默认当前组。
logger：用于记录日志，通常是logging.Logger对象。

13. shutil.unpack_archive(filename[, extract_dir[, format]])
解压缩或解包源文件。
filename是压缩文档的完整路径
extract_dir是解压缩路径，默认为当前目录。
format是压缩格式。默认使用文件后缀名代码的压缩格式。

shutil模块的压缩和解压功能，在后台是通过调用zipfile和tarfile两个模块来进行的。




"""

