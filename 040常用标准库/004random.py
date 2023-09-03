# random模块用于生成伪随机数。

"""  
真正意义上的随机数（或者随机事件）是按照实验过程中表现的分布概率随机产生的，其结果是不可预测的。
而计算机中的随机数是所谓的随机函数按照一定算法模拟产生的，其结果是确定的，是可预测的。
所以用计算机随机函数所产生的“随机数”并不随机，是伪随机数，绝对不可以用来生成密码。


1.计算机的伪随机数是由随机种子根据一定的计算方法计算出来的数值。所以，只要计算方法一定，随机种子一定，那么产生的随机数就是固定的。
2.如果用户不设置随机种子，那么随机种子默认来自系统时钟。

# 1. 基本方法
random.seed(a=None, version=2)
初始化随机数生成器。如果未提供a或者a=None，则使用系统时间为种子。如果a是一个整数，则作为新的种子。

random.getstate()
返回当前生成器的内部状态

random.setstate(state)
传入一个先前利用getstate方法获得的状态对象，使得生成器恢复到这个状态。

random.getrandbits(k)
返回一个不大于K位的Python整数（十进制），比如k=10，则结果是0~2^10之间的整数。

# 2. 针对整数的方法
random.randrange(stop)
random.randrange(start, stop[, step])
random.randint(a, b)
返回一个a <= N <= b的随机整数N。等同于randrange(a, b+1)。


# 3. 针对序列类型的方法
random.choice(seq)
从非空序列seq中随机选取一个元素。如果seq为空则弹出IndexError异常。
random.choices(population, weights=None, *, cum_weights=None, k=1)
3.6版本新增。从population集群中随机抽取K个元素。weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在。

random.shuffle(x[, random])
随机打乱序列x内元素的排列顺序，俗称“洗牌”。只能用于可变的序列，对于不可变序列，请使用下面的sample()方法。

random.sample(population, k)
从population样本或集合中随机抽取K个不重复的元素形成新的序列。常用于不重复的随机抽样。返回的是一个新的序列，不会破坏原有序列。
比如从一个整数区间随机抽取一定数量的整数random.sample(range(10000000), k=60)，这非常有效和节省空间。 
如果k大于population的长度，则弹出ValueError异常。

# 4. 真值分布
random模块最高端的功能其实在这里。
random.random()
返回一个介于左闭右开[0.0, 1.0)区间的浮点数。

random.uniform(a, b)
返回一个介于a和b之间的浮点数。如果a>b，则是b到a之间的浮点数。这里的a和b都有可能出现在结果中。

.........


# 6. 重要的例子
from random import *
random()              # 随机浮点数:  0.0 <= x < 1.0
uniform(2.5, 10.0)                   # 随机浮点数:  2.5 <= x < 10.0
randrange(10)                        # 0-9的整数：
randrange(0, 101, 2)                 # 0-100的偶数
choice(['win', 'lose', 'draw'])      # 从序列随机选择一个元素

deck = 'ace two three four'.split()
shuffle(deck)    # 对序列进行洗牌，改变原序列
sample([10, 20, 30, 40, 50], k=4)    # 不改变原序列的抽取指定数目样本，并生成新序列


"""
import random

print(random.random()) # 0.20757954971925985
print(random.uniform(2.5, 10.0)) # 8.486299644619768

