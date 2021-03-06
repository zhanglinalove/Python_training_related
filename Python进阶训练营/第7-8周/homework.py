#作业一：

#区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.deque


一、从使用内存的角度来进行划分，如下的情况:
可变数据类型:list, dict,collections.deque
不可变数据类型:tuple, str, 

二、序列分类:
容器序列:list, tuple, dict, collections.deque
扁平序列:str



作业二：
自定义一个 python 函数，实现 map() 函数的功能。

def square(x):
    return x ** 2


def my_map(func, *iterables):
    try:
        i = 0
        while 1:
            print([j for j in iterables])
            print([j[i] for j in iterables])
            yield func(*[j[i] for j in iterables])
            i += 1
    except IndexError:
        pass
print(list(my_map(square, range(10))))


作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import time
def timer(func):
    def inner(*args, **kwargs):
        beginTime = time.time()
        print(f'函数开始时间:{beginTime}')
        ret = func(*args, **kwargs)
        endTime = time.time()
        print(f'函数结束时间:{endTime}')
        print(f'函数的计算时间是:{endTime - beginTime}')
        return ret

    return inner


@timer
def my_count(b):
    a = 0
    for i in range(b):
        a += i
    return f"1到{b}累计的和={a}"


count1 = my_count(10)
print(count1)
