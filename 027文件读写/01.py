"""  
Python内置了一个open()方法，用于对文件进行读写操作。
使用open()方法操作文件就像把大象塞进冰箱一样，可以分三步走，一是打开文件，二是操作文件，三是关闭文件。

open()方法的返回值是一个file对象，可以将它赋值给一个变量（文件句柄）。其基本语法格式为:
f = open(filename, mode)


Python中，所有具有read和write方法的对象，都可以归类为file类型。
而所有的file类型对象都可以使用open方法打开，close方法结束和被with上下文管理器管理。这是Python的设计哲学之一。

filename：一个包含了你要访问的文件名称的字符串值，通常是一个文件路径。
mode：打开文件的模式，有很多种，默认是只读方式r。

"""
# # 打开一个文件
f = open("D:/z_my/z_project/pythonBasics/027文件读写/test.md","w",encoding='utf-8')
# 写输入数据
f.write("Python 是个很牛逼的语言\n很不错的\n")
# 关闭打开的文件
f.close()



# 一、 b模式：
"""  
二进制模式，通常用来读取图片、视频等二进制文件。注意，它在读写的时候是以bytes类型读写的，因此获得的是一个bytes对象而不是字符串。
在这个读写过程中，需要自己指定编码格式。在使用带b的模式时一定要注意传入的数据类型，确保为bytes类型。

t = "Python 是个很牛逼的语言,\n 很不错的 \n"
b = bytes(t,encoding='utf-8')
f = open("D:/z_my/z_project/pythonBasics/027文件读写/test.md","wb")
# 写输入数据  b 是bytes类型
f.write(b)
# 关闭打开的文件
f.close()

"""

# 二、 + 模式：
# 对于w+模式，在读写之前都会清空文件的内容，建议不要使用！
# 对于a+模式，永远只能在文件的末尾写入，有局限性，建议不要使用！
# 对于r+模式，也就是读写模式，配合seek()和tell()方法，可以实现更多操作。

# 三、 编码问题
# 要读取非UTF-8编码的文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# f = open('gbk.txt', 'r', encoding='gbk')
# a = f.read()
"""  
遇到有些编码不规范的文件，可能会抛出UnicodeDecodeError异常，这表示在文件中可能夹杂了一些非法编码的字符。
遇到这种情况，可以提供errors参数，表示如果遇到编码错误后如何处理。
f = open('gbk.txt', 'r', encoding='gbk', errors='ignore') 忽略错误
"""

# 四、 文件对象操作
# 每当我们用open方法打开一个文件时，将返回一个文件对象。这个对象内置了很多操作方法。下面假设，已经打开了一个f文件对象。

# 1. f.read(size)
# 读取一定大小的数据, 然后作为字符串或字节对象返回。size是一个可选的数字类型的参数，用于指定读取的数据量。
# 当size被忽略了或者为负值，那么该文件的所有内容都将被读取并且返回。
# 如果文件体积较大，请不要使用read()方法一次性读入内存，而是read(512)这种一点一点的读。

# 2. f.readline()
# 从文件中读取一行n内容。换行符为'\n'。如果返回一个空字符串，说明已经已经读取到最后一行。
# 这种方法，通常是读一行，处理一行，并且不能回头，只能前进，读过的行不能再读了。
f = open("D:/z_my/z_project/pythonBasics/027文件读写/test.md", "r",encoding='utf-8')
str = f.readline()
print(str)
f.close()
print("\n")


# 3. f.readlines()
# 将文件中所有的行，一行一行全部读入一个列表内，按顺序一个一个作为列表的元素，并返回这个列表。
# readlines 方法会一次性将文件全部读入内存，所以也存在一定的风险。但是它有个好处，每行都保存在列表里，可以随意存取。
f1 = open("D:/z_my/z_project/pythonBasics/027文件读写/test.md", "r",encoding="utf-8")
a = f1.readlines()
print(a) #['Python 是个很牛逼的语言\n', '很不错的\n']
f1.close()


# 4. 遍历文件
# 实际上，更多的时候，我们将文件对象作为一个迭代器来使用。

f2 = open("D:/z_my/z_project/pythonBasics/027文件读写/test.md", "r",encoding="utf-8")

for line in f2:
    print(line, end=',')
f2.close()

# 这个方法很简单, 不需要将文件一次性读出，但是同样没有提供一个很好的控制，与readline方法一样只能前进，不能回退。
"""  
几种不同的读取和遍历文件的方法比较：如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便。普通情况，使用for循环更好，速度更快。


"""


# 5. f.write()
"""  
将字符串或bytes类型的数据写入文件内。write()动作可以多次重复进行，
其实都是在内存中的操作，并不会立刻写回硬盘，直到执行close()方法后，才会将所有的写入操作反映到硬盘上。
在这过程中，如果想将内存中的修改，立刻保存到硬盘上，可以使用f.flush()方法，但这可能造成数据的不一致。

# 打开一个文件
f = open("/tmp/foo.txt", "w")
f.write("Python 是一种非常好的语言。\n我喜欢Python!!\n")
# 关闭打开的文件
f.close()
"""

# 6. f.tell()
# 返回文件读写指针当前所处的位置,它是从文件开头开始算起的字节数。一定要注意了，是字节数，不是字符数。

# 7. f.seek()
# 如果要改变位置指针的位置, 可以使用f.seek(offset, from_what)方法。seek()经常和tell()方法配合使用。
# from_what的值，如果是0表示从文件开头计算，如果是1表示从文件读写指针的当前位置开始计算，2表示从文件的结尾开始计算，默认为0，例如：
# offset：表示偏移量。
    # seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    # seek(x,1) ： 表示从当前位置往后移动x个字符
    # seek(-x,2)：表示从文件的结尾往前移动x个字符

# 8. f.close()
"""  
关闭文件对象。当处理完一个文件后，调用f.close()来关闭文件并释放系统的资源。文件关闭后，如果尝试再次调用该文件对象，则会抛出异常。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了，或者更糟糕的结果。也就是说大象塞进冰箱后，一定不要忘记关上冰箱的门。


"""


# 五、 with关键字
"""  
with关键字用于Python的上下文管理器机制。为了防止诸如open这一类文件打开方法在操作过程出现异常或错误，或者最后忘了执行close方法，
文件非正常关闭等可能导致文件泄露、破坏的问题。Python提供了with这个上下文管理器机制，保证文件会被正常关闭。在它的管理下，不需要再写close语句。注意缩进。

with open('test.txt', 'w') as f:
    f.write('Hello, world!')

with支持同时打开多个文件：
with open('log1') as obj1, open('log2','w') as obj2:
    s=obj1.read()
    obj2.write(s)

"""


