# Python的字典数据类型是基于hash散列算法实现的，采用键值对(key:value)的形式，根据key的值计算value的地址，具有非常快的查取和插入速度。

# 字典包含的元素个数不限，值的类型可以是任何数据类型！但是字典的key必须是不可变的对象，例如整数、字符串、bytes和元组，最常见的还是将字符串作为key。
# 列表、字典、集合等就不可以作为key。同时，同一个字典内的key必须是唯一的，但值则不必。

# 从Python3.6开始，字典是有序的！它将保持元素插入时的先后顺序！请务必清楚！

# 字典可精确描述为不定长、可变、散列的集合类型。字典元素在内存中的存储方式是不连续的，也没有链接关系，所以千万不要用列表的序列性质来套字典的性质。


# 字典的每个键值对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ，例如：
# d = {key1 : value1, key2 : value2 }

#  一、 创建字典
# 1、使用大括号 { } 创建空字典：
# 2、使用dict()函数 是Python内置的创建字典的方法。
"""  
dicvalue = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict([('a', 1), ('b', 2), ('c', 3)])
dict(sape=4139, guido=4127, jack=4098)
"""
print({'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}) #{'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict([('a', 1), ('b', 2), ('c', 3)]))   #{'a': 1, 'b': 2, 'c': 3}
print(dict(sape=4139, guido=4127, jack=4098)) #{'sape': 4139, 'guido': 4127, 'jack': 4098}


# 二、访问字典
"""  
虽然现在的字典在访问时有序了，但字典依然是集合类型，不是序列类型，因此没有索引下标的概念，更没有切片的说法。
但与list类似的地方是，字典采用把相应的键放入方括号内获取对应值的方式取值。
dic = {'Name': 'Jack','Age': 7, 'Class': 'First'}
print ("dic['Name']: ", dic['Name'])

"""
dic = {'Name': 'Jack','Age': 7, 'Class': 'First'}
print ("dic['Name']: ", dic['Name']) #dic['Name']:  Jack

# 三、增加和修改
"""  
增加就是往字典插入新的键值对，修改就是给原有的键赋予新的值。由于一个key只能对应一个值，所以，多次对一个key赋值，后面的值会把前面的值冲掉。
"""
dic1 = {'Name': 'Jack','Age': 7, 'Class': 'First'}
dic1['Name'] = "beijin"
dic1["address"] = "guangzhou"
dic1['Age'] = 22
print(dic1)
# 要统计字典内键的个数，可以使用Python内置的len()函数：
print(len(dic1))

# 四、删除字典元素、清空字典和删除字典
# 使用del关键字删除字典元素或者字典本身，使用字典的clear()方法清空字典。

dic2 = {'Name': 'Jack', 'Age': '20', 'Class': 'First', 'sex': 'male'}
del dic2["Name"]    # 删除指定的键
dic2.clear()        # 清空字典
del dic2            # 删除字典本身


# 五、 字典的重要方法
# 下表中列出了字典的重要内置方法。其中的get、items、keys和values是核心中的核心，必须熟练掌握！

# clear()	删除字典内所有元素
# copy()	返回一个字典的浅复制
# fromkeys()	创建一个新字典，以序列seq中元素做字典的键
# get(key)	返回指定键的值，如果键不在字典中，则返回default值
# items()	以列表返回可遍历的(键, 值) 元组对
# keys()	以列表返回字典所有的键
# values()	以列表返回字典所有的值
# pop(key)	删除并返回指定key的值
# popitem()	删除并返回字典的最后一个键值对，不接受参数。
# setdefault(key, default=None)	和get()类似,但如果键不存在于字典中，将会添加键并将值设为default
# update(dict2)	把字典dict2的键/值对更新到dict里
dic3 = {'Name': 'Jack', 'Age': 7, 'Class': 'First'}
dic3.get('sex')  # 访问不存在的key，没有报错，但是IDLE不会显示Nones
dic3['sex']       # 报错
dic3.items()    #dict_items([('Name', 'Jack'), ('Age', 7), ('Class', 'First')])


# 六、遍历字典
# 从Python3.6开始遍历字典获得的键值对是有序的！以下的遍历方法必须全部熟练掌握。
dic4 = {'Name': 'Jack', 'Age': 7, 'Class': 'First'}
# 1  直接遍历字典获取键，根据键取值
for key in dic:
    print(key, dic[key])

# 2  利用items方法获取键值，速度很慢，少用！
for key,value in dic.items():
    print(key,value)

#3  利用keys方法获取键
for key in dic.keys():
    print(key, dic[key])
    
#4  利用values方法获取值，但无法获取对应的键。
for value in dic.values():
    print(value)

