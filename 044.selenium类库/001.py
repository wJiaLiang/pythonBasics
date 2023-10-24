from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep

#1.创建Chrome或Firefox浏览器对象，这会在电脑上在打开一个浏览器窗口 "D:\z_install\Firefox\F\geckodriver"
browser = webdriver.Firefox()
browser.set_window_size(1000,600)

# browser = webdriver.Chrome()

#2.通过浏览器向服务器发送URL请求。如果能打开百度网站，说明安装成功。
# browser.get("https://www.baidu.com/")
browser.get("https://www.baidu.com/")

# 获取title 标签内容
t = browser.title
print(t)
now_url  = browser.current_url
print(now_url) #当前页面的url;
# print(browser.page_source) # 网页源码

# 选择多个标签;
domli = browser.find_elements(By.CSS_SELECTOR,"#hotsearch-content-wrapper li .title-content-title")
# print(domli)
for i,value in enumerate(domli):
    print(value.text) # 标签内的文字
    if i == 2:
        print(value.text)

input = browser.find_element(By.ID,"kw") #获取id 为 kw的元素;
input.send_keys('selenium') #输入框录入数据
btn = browser.find_element(By.ID,"su").click() # 点击搜索按钮

print(input.get_attribute("value")) # 获取input内输入的文字;

