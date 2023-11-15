"""  
与time模块相比，datetime模块提供的接口更直观、易用，功能也更加强大。
导入方式： import datetime
datetime模块定义了以下几个类（注意：这些类的对象都是不可变的！）。


类名	描述
datetime.date	日期类
datetime.time	时间类
datetime.datetime	日期与时间类
datetime.timedelta	表示两个date、time、datetime实例之间的时间差
datetime.tzinfo	时区相关信息对象的抽象基类。
datetime.timezone	Python3.2中新增的功能，实现tzinfo抽象基类的类，表示与UTC的固定偏移量


使用datetime模块主要就是对其前四个类的操作。另外，datetime模块中还定义了两个常量：

datetime.MINYEAR：
datetime.date或datetime.datetime对象所允许的年份的最小值，该值为1。

datetime.MAXYEAR：
datetime.date或datetime.datetime对象所允许的年份的最大值，该值为9999。




"""


# 一、datetime.date类
"""  
datetime模块中包含如下类：
date	        日期对象,常用的属性有year, month, day
time	        时间对象
datetime	    日期时间对象,常用的属性有hour, minute, second, microsecond
datetime_CAPI	日期时间对象C语言接口
timedelta	    时间间隔，即两个时间点之间的长度
tzinfo	        时区信息对象

"""
# 一、datetime.date类
# 定义：class datetime.date(year, month, day)
"""  
datetime模块下的日期类，只能处理年月日这种日期时间，不能处理时分秒。

在构造datetime.date对象的时候需要传递下面的参数：
参数名称	取值范围
year	[MINYEAR, MAXYEAR]
month	[1, 12]
day	    [1, 指定年份的月份中的天数]


"""
import datetime
print(datetime.datetime.now())  # 获取当前日期和时间 2023-11-08 21:58:00.048240
current_datetime = datetime.datetime.now()
print(current_datetime.strftime("%Y-%m-%d %H"))  # 格式化日期 2023-11-08 21
print(datetime.date.today())  # 获取当前日期 2023-11-08
print('-----------------------------------------')
instanced = datetime.date(2023, 9, 3)
print(instanced)  # 2023-09-03

print(datetime.date.max)
print(datetime.date.min)
print(datetime.date.today())  # 当前的日期

print("--------实例属性和方法--------------")
print(instanced.year)
print(instanced.month)
print(instanced.day)
print(instanced.isoformat())
print(instanced.weekday())  # 返回日期是星期几，[0, 6]，0表示星期一


# 二、 datetime.time类
# 定义：class datetime.time(hour, [minute[, second, [microsecond[, tzinfo]]]])
# datetime模块下的时间类，只能处理时分秒。

"""  
在构造datetime.time对象的时候需要传递下面的参数：

参数名称	     取值范围
hour	        [0, 23]
minute	        [0, 59]
second	        [0, 59]
microsecond	    [0, 1000000]
tzinfo	        tzinfo的子类对象，如timezone类的实例

主要属性和方法：
time.max	            time类所能表示的最大时间：time(23, 59, 59, 999999)
time.min	        time类所能表示的最小时间：time(0, 0, 0, 0)
time.resolution	    时间的最小单位，即两个不同时间的最小差值：1微秒
t.hour	            时
t.minute	        分
t.second	        秒
t.microsecond	    微秒
t.tzinfo	        返回传递给time构造方法的tzinfo对象，如果该参数未给出，则返回None
t.replace(hour[, minute[, second[, microsecond[, tzinfo]]]])	生成并返回一个新的时间对象，原时间对象不变
t.isoformat()	    返回一个‘HH:MM:SS.%f’格式的时间字符串
t.strftime()	    返回指定格式的时间字符串，与time模块的strftime(format, struct_time)功能相同
"""
print("============================")
t = datetime.time(10, 22, 30)
print(datetime.time.resolution)  # 0:00:00.000001
print(datetime.time.max)  # 23:59:59.999999
print(t.hour)  # 10
print(t.minute)
print(t.second)
print(t.microsecond)


# 三、 datetime.datetime类
# 一定要注意这是datetime模块下的datetime类，千万不要搞混了！
# datetime模块下的日期时间类，你可以理解为datetime.time和datetime.date的组合类。


# 四、 datetime.timedelta类
# 定义：class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, hours=0, weeks=0)
# timedelta对象表示两个不同时间之间的差值。可以对datetime.date, datetime.time和datetime.datetime对象做算术运算。

"""  
类方法/属性名称	                          描述
timedelta.min	                         timedelta(-999999999)
timedelta.max	                         timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
timedelta.resolution	                 timedelta(microseconds=1)
td.days	                                 天 [-999999999, 999999999]
td.seconds	                             秒 [0, 86399]
td.microseconds	                         微秒 [0, 999999]
td.total_seconds()	                     时间差中包含的总秒数，等价于: td / timedelta(seconds=1)


"""
dt = datetime.datetime.now()  # 当前时间
tt = datetime.timedelta(3)              # 3天后
print(dt + tt)  # 2023-09-06 16:20:15.367589
dd = datetime.timedelta(hours=-3)       # 3小时前
print(dt+dd)  # 2023-09-03 13:21:22.532971
