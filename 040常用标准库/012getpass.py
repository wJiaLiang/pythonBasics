# getpass模块大概是标准库中最简单的一个模块了。getpass模块用于输入密码时，隐藏密码字符。

"""  
我们都知道，密码是非常重要不能展示给他人观看的事物。做演示的时候，如果你的密码以明文的方式在显示设备上打印出来了，那就太糟糕了。
所以不管是在普通软件中还是浏览器上，我们输入的密码通常都以圆点或者星号替代，有的甚至根本就不显示密码输入过程。

那么如何在Python中也实现这一功能呢？使用getpass模块！

getpass模块简单到只有两个方法：

getpass.getpass(prompt='Password: ', stream=None)
提示用户输入密码。可自定义提示符。可从stream中读取密码。

getpass.getuser()
获取当前用户名。按顺序从LOGNAME, USER, LNAME或者USERNAME这些环境变量中查询。




总结：getpass模块只能用于命令行界面！^_^



"""