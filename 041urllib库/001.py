# Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。

"""  
Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。
urllib.request - 打开和读取 URL。
urllib.error - 包含 urllib.request 抛出的异常。
urllib.parse - 解析 URL。
urllib.robotparser - 解析 robots.txt 文件。


urllib.request
urllib.request 定义了一些打开 URL 的函数和类，包含授权验证、重定向、浏览器 cookies等。
urllib.request 可以模拟浏览器的一个请求发起过程。
我们可以使用 urllib.request 的 urlopen 方法来打开一个 URL，语法格式如下：

urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

url：url 地址。
data：发送到服务器的其他数据对象，默认为 None。
timeout：设置访问超时时间。
cafile 和 capath：cafile 为 CA 证书， capath 为 CA 证书的路径，使用 HTTPS 需要用到。
cadefault：已经被弃用。
context：ssl.SSLContext类型，用来指定 SSL 设置。


"""
from urllib.request import urlopen
print(urlopen)

tesUrl = urlopen("https://www.baidu.com/")
# print(tesUrl.read())
print(tesUrl.readline()) #读取一行