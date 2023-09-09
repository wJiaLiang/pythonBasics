#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = '' #发件人的邮箱
receivers = ['','']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试使用的是py3,基于163的smt邮箱服务', 'plain', 'utf-8')
message['From'] = "{}".format(sender)        # 发送者
message['To'] =  ",".join(receivers)         # 接收者
 
subject = 'SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

mail_host="smtp.163.com"        #设置服务器
mail_user=""    #用户名         # 授权邮箱服务商的邮箱用户名
mail_pass=""    #口令
 
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件",e)