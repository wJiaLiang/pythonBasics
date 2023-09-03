"""  
ZIP是通用的归档和压缩格式。zipfile模块提供了通用的创建、读取、写入、附加和显示压缩文件的方法，你可以简单地把它理解为Python中的zip解压缩软件。
该模块可以解密带有密码的压缩文件，但不提供附加密码的压缩功能。


定义的类和异常

class zipfile.ZipFile
模块最重要的类。用于读写ZIP文件。

class zipfile.PyZipFile
创建包含Python库的ZIP归档文件的类


class zipfile.ZipInfo(filename='NoName', date_time=(1980, 1, 1, 0, 0, 0))
用于显示ZIP文件信息的类。ZIP对象的getinfo()或infolist()方法会返回一个该类的实例。filename是ZIP文件的完整名称。
date_time是一个包含6个元素的元组，描述文件最近修改时间。

zipfile.is_zipfile(filename)
如果文件是个ZIP文件则返回True，否则False。


zipfile.ZIP_STORED
未压缩的归档文件的数字常数。


zipfile.ZIP_DEFLATED
常用的ZIP压缩方法。


zipfile.ZIP_BZIP2
BZIP2压缩方法的数字常量。


zipfile.ZIP_LZMA
LZMA压缩方法的数字常量。

exception zipfile.BadZipFile
ZIP文件被损坏异常。3.2版本新增。


exception zipfile.LargeZipFile
当需要ZIP64功能，但未开启该功能时弹出异常。



ZipFile对象
class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True)
打开一个ZIP文件。返回的也是一个类似文件的ZipFile对象，可以读写。


..........

"""