"""  
Python官方的PyPi仓库为我们提供了一个统一的代码托管仓库，所有的第三方库，甚至你自己写的开源模块，都可以发布到这里，让全世界的人分享下载。
当然，除了Python官方的仓库，也有一些其他公司提供的仓库，还有一些私有的或针对内部的仓库。

Python有两个著名的包管理工具easy_install和pip。在Python2.7的安装包中，easy_install是默认安装的，而pip需要我们手动安装。
随着Python版本的提高，easy_install已经逐渐被淘汰，但是一些比较老的第三方库，在现在仍然只能通过easy_install进行安装。
目前，pip已经成为主流的安装工具，自Python2 >=2.7.9或者Python3.4以后默认都安装有pip。

Python有2、2.7、3、3.6一样，pip也有pip、pip2、pip3之分。
pip是从属于Python的，对应的pip负责给对应的Python安装第三方模块。我们不要关心pip后面跟的数字，核心的问题是这个pip命令对应的是哪个Python解释器，
一个萝卜一个坑，想要为哪个Python解释器安装第三方库，就要调用它名下对应的pip。

cmd环境中，输入pip -V(大写V)：


# 一、安装pip

如果很不巧，你的Python版本下恰好没有pip这个工具，怎么办呢？解决办法很多！

使用easy_install安装： 各种进入到easy_install脚本的目录下，然后运行easy_inatall pip
使用get-pip.py安装： 在下面的url下载get-pip.py脚本 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 然后运行：python get-pip.py 这个脚本会同时安装setuptools和wheel工具。
在linux下使用包管理工具安装pip： 例如，ubuntu下：sudo apt-get install python-pip。Fedora系下：sudo yum install python-pip
在windows下安装pip： 在C:\python27\scirpts下运行easy_install pip 进行安装。

    2. 指定版本安装
    安装特定版本的package，通过使用==, >=, <=, >, <来指定一个版本号。 pip install 'Markdown<2.0' pip install 'Markdown>2.0,<2.0.3

    3. 卸载已安装的库
    pip uninstall pillow

    4. 列出已经安装的库
    pip list

    5. 将已经安装的库列表保存到文本文件中
    pip freeze > requirements.txt
    这个功能非常常用、好用！经常被用作项目环境依赖文件。

    6. 根据依赖文件批量安装库
    pip install -r requirements.txt

    7. 使用wheel文件安装
    除了使用上面的方式联网进行安装外，还可以将安装包也就是wheel格式的文件，下载到本地，然后使用pip进行安装。
    比如我在PYPI上提前下载的pillow库的wheel文件，后缀名为whl。




pip源的选择
很多时候，比如网络不给力，连接超时、防火墙阻挡等等各种原因，我们可能无法从Python官方的PyPi仓库进行pip安装，
这时候可以选择国内的第三方源，推荐使用豆瓣源，速度不错。

使用方法：
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pillow
需要注意的是，除了最后的pillow用你所期望的库名替代外，前面的参数都是固定写法，包括参数顺序。





"""