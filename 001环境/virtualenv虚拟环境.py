
"""  

在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.10。所有第三方的包都会被pip安装到Python3的site-packages目录下。
如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？
这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。venv就是用来为一个应用创建一套“隔离”的Python运行环境。

首先，我们假定要开发一个新的项目project101，需要一套独立的Python运行环境，可以这么做：


第一步，创建目录，这里把venv命名为proj101env，因此目录名为proj101env：
第二步，创建一个独立的Python运行环境：
proj101env$ python3 -m venv .

查看当前目录，可以发现有几个文件夹和一个pyvenv.cfg文件：

命令python3 -m venv <目录>就可以创建一个独立的Python运行环境。观察bin目录的内容，里面有python3、pip3等可执行文件，实际上是链接到Python系统目录的软链接。

第三步、继续进入bin目录，Linux/Mac用source activate，Windows用activate.bat激活该venv环境：

proj101env$ cd bin
bin$ source activate
(proj101env) bin$


在venv环境下，用pip安装的包都被安装到proj101env这个环境下，具体目录是proj101env/lib/python3.x/site-packages，
因此，系统Python环境不受任何影响。也就是说，proj101env环境是专门针对project101这个应用创建的。


退出当前的proj101env环境，使用deactivate命令：
(proj101env) bin$ deactivate

此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。

venv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python链接或复制一份到venv的环境，
用命令source activate进入一个venv环境时，venv会修改相关环境变量，让命令python和pip均指向当前的venv环境。

如果不再使用某个venv，例如proj101env，删除它也很简单。首先确认该venv没有处于“激活”状态，然后直接把整个目录proj101env删掉就行。




"""