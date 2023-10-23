from selenium import webdriver

from time import sleep
sleep(1)

#1.创建Chrome或Firefox浏览器对象，这会在电脑上在打开一个浏览器窗口 "D:\z_install\Firefox\F\geckodriver"
# browser = webdriver.Firefox()
browser2 = webdriver.Chrome()

#2.通过浏览器向服务器发送URL请求。如果能打开百度网站，说明安装成功。
# browser.get("https://www.baidu.com/")
browser2.get("https://www.baidu.com/")
browser2.implicitly_wait(0.5)
t = browser2.title
print(t)