# 什么是Hash
"""  
Hash，译做“散列”，也有直接音译为“哈希”的。把任意长度的输入，通过某种hash算法，
变换成固定长度的输出，该输出就是散列值，也称摘要值。该算法就是哈希函数，也称摘要函数。

通过摘要函数对任意长度的数据计算出固定长度的摘要digest，目的是为了提供一个验证文件未被篡改的方法。
摘要函数是一个单向函数，计算digest很容易，但通过digest反推原始数据却非常困难。而且，最关键的是，对原始数据做一个比特位的修改，都会导致计算出的摘要完全不同。

要注意，摘要算法不是加密算法，不能用于加密数据（因为无法通过摘要反推明文），只能用于防止数据被篡改，
但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。

MD5是最常见的摘要算法，速度很快，生成结果是固定的16字节，通常用一个32位的16进制字符串表示。
SHA1算法更安全点，它的结果是20字节长度，通常用一个40位的16进制字符串表示。
而比SHA1更安全的算法是SHA256和SHA512等等，不过越安全的算法越慢，并且摘要长度更长。

"""

# hashlib模块
# Python内置的hashlib模块为我们提供了多种安全方便的摘要方法，我们不必求助他人。
"""  
当前，在大部分操作系统下，hashlib模块支持md5(),sha1(), sha224(), sha256(), sha384(), sha512(), blake2b()，blake2s()，
sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256()等多种hash构造方法。
这些构造方法在使用上通用，返回带有同样接口的hash对象，对算法的选择，差别只在于构造方法的选择。例如sha1()能创建一个SHA-1对象，
sha256()能创建一个SHA-256对象。然后就可以使用通用的update()方法将bytes类型的数据添加到对象里，最后通过digest()或者hexdigest()方法获得当前的摘要。

下面是获得bytes类型字符串b'Nobody inspects the spammish repetition'的摘要的过程：
"""
import hashlib
m = hashlib.sha256()                # 通过构造函数获得一个hash对象
m.update(b'Nobody inspects')        # 使用hash对象的update方法添加消息
m.update(b' the spammish repetition')   # 同上
m.digest()                  # 获得bytes类型的消息摘要

# 更简洁的用法：
hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()

"""  
hashlib.new(name[, data])
h.hexdigest()

"""

# 1. hashlib模块的两个常量属性：

# hashlib.algorithms_guaranteed
# 所有平台中，模块支持的hash算法列表

# hashlib.algorithms_available
# 当前Python解释器环境中，模块支持的hash算法列表
print(hashlib.algorithms_guaranteed)


# 2. hash对象的两个常量属性
# hash.digest_size
# hash结果的长度

# hash.block_size
# hash内部块的大小



# 3. hash对象的属性
# hash.name
# hash算法名称字符串

# 4. hash对象的方法
# hash.update(arg)

"""  
更新hash对象。连续的调用该方法相当于连续的追加更新。例如m.update(a); m.update(b)相当于m.update(a+b)。
注意，当数据规模较大的时候，Python的GIL在此时会解锁，用于提高计算速度。

一定要理解update()的作用，由于消息摘要是只针对当前状态产生的，所以每一次update后，再次计算hexdigest()的值都会不一样。

hash.digest()
返回bytes格式的消息摘要

hash.hexdigest()
与digest方法类似，不过返回的是两倍长度的字符串对象，所有的字符都是十六进制的数字。通常用于邮件传输或非二进制环境中。通常我们比较摘要时，比较的就是这个值！

hash.copy()
返回一个hash对象的拷贝


"""

#使用场景

# 加盐：额外给原始数据添加一点自定义的数据，使得生成的消息摘要不同于普通方式计算的摘要。

md5 = hashlib.md5()
s = "password" + "aaabbbccc"
md5.update(s.encode())
print(md5.hexdigest()) #b2d4e972d9ab62863fb3f76c1962b1bcs

