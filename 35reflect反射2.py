# 考虑有这么一个场景：需要根据用户输入url的不同，调用不同的函数，实现不同的操作，
# 也就是一个WEB框架的url路由功能。路由功能是web框架里的核心功能之一，例如Django的urls。

# 首先，有一个commons.py文件，它里面有几个函数，分别用于展示不同的页面。这其实就是Web服务的视图文件，用于处理实际的业务逻辑。
# commons.py
def login():
    print("这是一个登陆页面！")
def logout():
    print("这是一个退出页面！")
def home():
    print("这是网站主页面！")


# 其次，有一个visit.py文件，作为程序入口，接收用户输入，并根据输入展示相应的页面。

# visit.py

import commons
def run():
    inp = input("请输入您想访问页面的url：").strip()
    if inp == "login":
        commons.login()
    elif inp == "logout":
        commons.logout()
    elif inp == "home":
        commons.home()
    else:
        print("404")
if __name__ == '__main__':
    run()

# 这就实现了一个简单的url路由功能，根据不同的url，执行不同的函数，获得不同的页面。
# 如果commons文件里有成百上千个函数呢(这很常见)？难道在visit模块里写上成百上千个elif？显然这是不可能的！那么怎么办？

# 仔细观察visit.py中的代码，会发现用户输入的url字符串和相应调用的函数名好像！如果能用这个字符串直接调用函数就好了！
# 但是，前面已经说了字符串是不能用来调用函数的。
# 为了解决这个问题，Python提供了反射机制，帮助我们实现这一想法，其主要就表现在getattr()等几个内置函数上!


def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    func = getattr(commons,inp)
    func() 

if __name__ == '__main__':
    run()
# getattr()函数的使用方法：接收2个参数，前面的是一个类或者模块，后面的是一个字符串，注意了！是个字符串！
# 这个过程就相当于把一个字符串变成一个函数名的过程。这是一个动态访问的过程，一切都不写死，全部根据用户输入来变化。



# 如果用户输入一个非法的url，比如jpg，由于在commons里没有同名的函数，肯定会产生运行错误
# python提供了一个hasattr()的内置函数，用法和getattr()基本类似，它可以判断commons中是否具有某个成员，返回True或False。
def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    if hasattr(commons,inp):
        func = getattr(commons,inp)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()
# Python的四个重要内置函数：getattr()、hasattr()、delattr()和setattr()较为全面的实现了基于字符串的反射机制。
# delattr()和setattr()就不做多解释，相信从字面意思看，你也该猜到它们的用途和用法了。
# 它们都是对内存中的模块进行操作，并不会对源文件进行修改。



# Python内置的__import__(字符串参数)函数解决这个问题。通过它，可以实现类似getattr()的反射功能。
# __import__()方法会根据字符串参数，动态地导入同名的模块。
# 注意字符串的拼接
# 对于lib.xxx.xxx.xxx这一类的模块导入路径，__import__()默认只会导入最开头的圆点左边的目录，也就是lib,只要加上fromlist = True参数即可

def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    modules, func = inp.split("/")
    obj = __import__("lib." + modules, fromlist=True)  # 注意fromlist参数
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("404") 
if __name__ == '__main__':
    run()