"""  
当今市面上有很多主流的消息中间件，如老牌的ActiveMQ、RabbitMQ、ZeroMQ，炙手可热的Kafka，
还有阿里巴巴自主开发的Notify、MetaQ、RocketMQ等。这些都是大型的重量级消息队列，通常应用于商业生产环境。
但是，如果只是小型服务或者任务量不大，再或者学习、实验、测试等情况下，你有必要去搭建或者购买一个本身就已经很庞大的消息服务么？杀鸡焉用牛刀，当然不需要！

Python为我们内置了一个微型轻量级的消息队列模块，queue！queue模块主要用于多生产者和消费者模式下的队列实现，
特别适合多线程时的消息交换。它实现了常见的锁语法，临时阻塞线程，防止竞争，这有赖于Python对线程的支持。


queue模块实现了三种队列：
FIFO：先进先出队列，类似管道。元素只能从队头方向一个一个的弹出，只能从队尾一个一个的放入。
LIFO：后进先出队列，也就是栈。元素永远只能在栈顶出入。
priority queue：优先级队列，每个元素都带有一个优先值，值越小的越早出去。值相同的，先进入队列的先出去。


queue模块定义了下面几个类和异常（一定要注意大小写！） ：

#1、 class queue.Queue(maxsize=0)：
FIFO队列构造器。maxsize是队列里最多能同时存在的元素个数。如果队列满了，则会暂时阻塞队列，直到有消费者取走元素。
maxsize的值如果小于或等于零，表示队列元素个数不设上限，理论上可无穷个，但要小心，内存不是无限大的，这样可能会让你的内存溢出。


#2、 class queue.LifoQueue(maxsize=0)
LIFO队列构造器。maxsize是队列里最多能同时放置的元素个数。如果队列满了，则会暂时阻塞队列，直到有消费者取走元素。
maxsize的值如果小于或等于零，表示队列元素个数不设上限，可无穷个。


# 3、class queue.PriorityQueue(maxsize=0)
优先级队列构造器。maxsize是队列里最多能同时放置的元素个数。如果队列满了，则会暂时阻塞队列，直到有消费者取走元素。
maxsize的值如果小于或等于零，表示队列元素个数不设上限，可无穷个。通常在这类队列中，
元素的优先顺序是按sorted(list(entries))[0]的结果来定义的，而元素的结构形式通常是(priority_number, data)类型的元组。

exception queue.Empty
从空的队列里请求元素的时候，弹出该异常。

exception queue.Full
往满的队列里放入元素的时候，弹出该异常。



Queue对象
三种队列类的对象都提供了以下通用的方法：

Queue.qsize()
返回当前队列内的元素的个数。注意，qsize()大于零不等于下一个get()方法一定不会被阻塞，qsize()小于maxsize也不表示下一个put()方法一定不会被阻塞。

Queue.empty()
队列为空则返回True，否则返回False。同样地，返回True不表示下一个put()方法一定不会被阻塞。返回False不表示下一个get()一定不会被阻塞。

Queue.full()
与empty()方法正好相反。同样不保证下一步的操作不被阻塞。

Queue.put(item, block=True, timeout=None)
item参数表示具体要放入队列的元素。block和timeout两个参数配合使用。其中，如果block=True，timeout=None，队列阻塞，直到有空槽出现；
当block=True，timeout=正整数N，如果在等待了N秒后，队列还没有空槽，则弹出Full异常；
如果block=False，则timeout参数被忽略，队列有空槽则立即放入，如果没空槽，则弹出Full异常。


Queue.put_nowait(item)
等同于put(item, False)

Queue.get(block=True, timeout=None)
从队列内删除并返回一个元素。如果block=True, timeout=None，队列会阻塞，直到有可供弹出的元素。
如果timeout指定为一个正整数N，则在N秒内如果队列内没有可供弹出的元素，则抛出Empty异常。如果block=False，timeout参数会被忽略，
此时队列内如果有元素则直接弹出，无元素可弹，则抛出Empty异常。


Queue.get_nowait()
等同于get(False).
下面的两个方法用于跟踪排队的任务是否被消费者守护线程完全处理。

Queue.task_done()
表明先前的队列任务已完成。由消费者线程使用。

Queue.join()
阻塞队列，直到队列内的所有元素被获取和处理。



"""
