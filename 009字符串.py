"""  
字符串是Python中最常用的数据类型之一，使用单引号或双引号来创建字符串，使用三引号创建多行字符串。
字符串要么使用两个单引号，要么两个双引号，不能一单一双！Python不支持单字符类型，单字符在Python中也是作为一个字符串使用。

字符串是不可变的序列数据类型，不能直接修改字符串本身，和数字类型一样！
Python3全面支持Unicode编码，所有的字符串都是Unicode字符串，所以传统Python2存在的编码问题不再困扰我们，可以放心大胆的使用中文。

虽然字符串本身不可变，但可以像列表序列一样，通过方括号加下标的方式，访问或者获取它的子串，当然也包括切片操作。
这一切都不会修改字符串本身，当然也符合字符串不可变的原则。
"""

# 一、字符串的运算：

# 下表实例变量a值为字符串 "Hello"，b变量值为 "Python"：
"""  
+	字符串连接(运算速度慢，慎用)	a + b	    'HelloPython'
*	重复输出字符串，相当于乘法	a * 2	        'HelloHello'
[]	通过索引获取字符串中的字符	a[1]	        'e'
[ : ]	截取字符串中的一部分，切片	a[1:4]	    'ell'
in	成员运算符 - 如果字符串中包含给定的字符返回True	        "H" in a	True
not in	成员运算符 - 如果字符串中不包含给定的字符返回True	"M" not in a	True
r/R	原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 
原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	print(r'\n')	\n

"""

# 二、Python转义字符：
# 编程语言里，有很多特殊字符，它们起着各种各样的作用。
# 有些特殊字符没有办法用普通字符表示，需要进行转义。python用反斜杠(\)转义字符。如下表：

#  \(在行尾时)	    续行符
#  \\	    反斜杠符号
#  \'	    单引号
#  \"	    双引号
#  \a	    响铃
#  \b	    响铃
#  \e	    转义
#  \000	    空
#  \n	    换行
#  \v	    纵向制表符
#  \t	    横向制表符
#  \r	    回车
#  \f	    换页
#  \oyy	   八进制数，yy代表的字符，例如：\o12代表换行
#  \xyy	   十六进制数，yy代表的字符，例如：\x0a代表换行
#  \033	   颜色控制

print("line1 \
... line2 \
... line3") # line1 ... line2 ... line3

print("\\") #/

a = "abaa\'  as"
print(a)    # abaa'  as

print("\a")  # 执行后电脑有响声。

print("Hello \b World!") #  Hello World!

print("Hello \v World!")  
# Hello 
    #    World!
print("Hello \t World!")  # Hello    World!

print("\110")

print("\x1c")

# 换页插入到字符窜
aa = '插入到字符窜'
print(f'换页{aa}')

# 三、“多行字符串”

# 在字符串中，可以使用三引号（三单或三双引号都可以）编写跨行字符串，在其中可以包含换行符、制表符以及其他特殊字符。例如：



# 四、字符串内置方法
""" 把字符串的第一个字符大写 
    string.capitalize()	

   返回一个原字符串居中,并使用空格填充至长度width的新字符串
   string.center(width)	

   返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
   string.count(str, beg=0, end=len(string))	

   Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象
   bytes.decode(encoding='UTF-8', errors='strict')	

   以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
   string.encode(encoding='UTF-8', errors='strict')

   检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。
   endswith(suffix, beg=0, end=len(string))

   把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
    expandtabs(tabsize=8)

    检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
   find(str, beg=0, end=len(string))

   跟find()方法一样，只不过如果str不在字符串中会报一个异常。
    index(str, beg=0, end=len(string))

    如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
    isalnum()

    如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
    isalpha()

    如果字符串只包含数字则返回 True 否则返回 False..
    isdigit()

    如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
    islower()

    如果字符串中只包含数字字符，则返回 True，否则返回 False
    isnumeric()

    如果字符串中只包含空白，则返回 True，否则返回 False.
    isspace()

    如果字符串是标题化的(见 title())则返回 True，否则返回 False
    istitle()

    如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
    isupper()

    以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    join(seq)

    返回字符串长度
    len(string)

    返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
    ljust(width[, fillchar])

    转换字符串中所有大写字符为小写.
    lower()

    截掉字符串左边的空格或指定字符。
    lstrip()

    创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
    maketrans()

    返回字符串 str 中最大的字母。
    max(str)

    返回字符串 str 中最小的字母。
    min(str)

    把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
    replace(old, new [, max])

    类似于 find()函数，不过是从右边开始查找.
    rfind(str, beg=0,end=len(string))

    类似于 index()，不过是从右边开始.
    rindex( str, beg=0, end=len(string))

    返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
    rjust(width,[, fillchar])

    删除字符串末尾的空格或指定字符。
    rstrip()

    以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
    split(str="", num=string.count(str))

    按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    splitlines([keepends])

    检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
    startswith(substr, beg=0,end=len(string))

    在字符串上执行 lstrip()和 rstrip()
    strip([chars])

    将字符串中大写转换为小写，小写转换为大写
    swapcase()

    返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
    title()

    根据 table 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
    translate(table, deletechars="")

    转换字符串中的小写字母为大写
    upper()

    返回长度为 width 的字符串，原字符串右对齐，前面填充0
    zfill (width)

    检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
    isdecimal()


"""

# str.format()格式化方法
    # 去除复杂的参数，简单的format格式化方法基本有两类：

    # 1.{0}、{1}、{2}:这一类是位置参数，引用必须按顺序，不能随意调整，否则就乱了。例如：
    # tpl = "i am {0}, age {1}, really {0}".format("seven", 18)

    # 2.{name}、{age}、{gender}：这一类是关键字参数，引用时必须以键值对的方式，可以随意调整顺序。例如：
    # tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)

tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
print(tpl)

tpl2 = "i am {name}, age {age}, really {name}".format(name="seven", age=22)
print(tpl2)




# 五、字符串颜色控制
    # 颜色是用转义序列控制的，转义序列是以ESC开头，在代码中用\033表示(ESC的ASCII码用十进制表示就是27，等于用八进制表示的33，\0表示八进制)。
    # 注意：颜色控制只在终端界面中有效。
    # 格式：\033[显示方式;前景色;背景色m正文\033[0m



# 六、字符编码
# 计算机只能处理数字01，如果要处理文本，就必须先把文本转换为数字01，这种转换方式就称为字符编码。

""" 
ASCII编码：早期专门为英语语系编码，只有255个字符，每个字符需要8位也就是1个字节。不兼容汉字。

Unicode编码：又称万国码，国际组织制定的可以容纳世界上所有文字和符号的字符编码方案。用2个字节来表示汉字。

UTF-8编码：为了节省字节数，在Unicode的基础上进行优化的编码。用1个字节表示英文字符，3个字符表示汉字。天生兼容ASCII编码，所以最为流行。

GB2312：我国早期自己制定的中文编码，世界范围内不通用。

GBK： 全称《汉字内码扩展规范》，向下与GB2312兼容，向上支持ISO10646.1国际标准，是前者向后者过渡过程中的一个承上启下的产物。windows中文版的汉字编码用的就是GBK。也非世界范围通用的编码

其它编码：非以上类型者的统称。属于能不用就不要碰的编码。


另外有这么几条规则，你要记住：
操作系统运行时，在内存中，统一使用的都是Unicode编码，当需要将数据保存到硬盘或者网络传输的时候，就转换为UTF-8编码，进行保存和传输。

用文本编辑器的时候，从文件系统或者说硬盘上读取的UTF-8编码字符被转换为Unicode字符到内存里，供程序或者操作系统使用。
编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8传输到客户的浏览器。


"""



