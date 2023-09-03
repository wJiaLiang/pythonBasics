"""  
既然有压缩模块zipfile，那有一个归档模块tarfile也是很自然的。tarfile模块用于解包和打包文件，包括被gzip，bz2或lzma压缩后的打包文件。
如果是.zip类型的文件，建议使用zipfile模块，更高级的功能请使用shutil模块。

定义的类和异常
tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)

返回一个TarFile类型的对象。本质上就是打开一个文件对象。Python随处可见这种文件对象类型的设计，你很容易就明白，不是吗？
name是文件名或路径。
bufsize用于指定数据块的大小，默认为20*512字节。
mode是打开模式，一个类似filemode[:compression]格式的字符串，可以有下表所示的组合，默认为“r”。

........



"""