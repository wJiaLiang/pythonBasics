# Json是一种轻量级的数据交换格式。Json源自JavaScript语言，易于人类的阅读和编写，同时也易于机器解析和生成，是目前应用最广泛的数据交换格式。

"""  
数据交换格式是不同平台、语言中进行数据传递的通用格式。比如Python和Java之间要对话，
你直接传递给Java一个dict或list吗？Java会问，这是什么鬼？虽然它也有字典和列表数据类型，但两种字典不是一个“物种”，根本无法相互理解。
这个时候就需要用Json这种交换格式了，Python和Java都能理解Json。那么别的语言为什么能理解Json呢？
因为这些语言都内置或提供了Json处理模块，比如Python的json模块。（额外强调一点，在Python中json是全部小写的，包括模块和方法名。）


Json是跨语言，跨平台的，但只能对Python的基本数据类型做操作，对Python的类就无能为力。
JSON格式和Python中的字典非常像。但是，json的数据要求用双引号将字符串引起来，并且不能有多余的逗号。
这是因为在别的语言中，双引号引起来的才是字符串，单引号引起来的是字符；
Python程序员习惯性的在列表、元组或字典的最后一个元素的后面加个逗号，这在json中是不允许的，需要特别注意。


类型转换
将数据从Python转换到json格式，在数据类型上会有变化，如下表所示：

Python	                                JSON
dict	                                object
list,tuple	                            array
str	                                    string
int,float, int- & float-derived Enums	number
True	                                true
False	                                false
None	                                null


反过来，从json格式转化为Python内置类型，见下表：
JSON	Python
object	dict
array	list
string	str
number (int)	int
number (real)	float
true	True
false	False
null	None


# 使用方法
json模块的使用其实很简单，对于绝大多数场合下，我们只需要使用下面四个方法就可以了：
方法	             功能
json.dump(obj, fp)	将python数据类型转换并保存到json格式的文件内。
json.dumps(obj)	    将python数据类型转换为json格式的字符串。 
json.load(fp)	    从json格式的文件中读取数据并转换为python的类型。
json.loads(s)	    将json格式的字符串转换为python的类型。



"""
import json
a = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(a) #["foo", {"bar": ["baz", null, 1.0, 2]}]

# 需要注意的是json模块不支持bytes类型，要先将bytes转换为str格式。

b = b'xixi'
k = json.dumps(b)
k = json.dumps(b.decode())
print(k)