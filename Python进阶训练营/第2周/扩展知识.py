
'''
    1、List 集中输出序号及数值的几种方式与方法。
'''
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    list = ['html', 'js', 'css', 'python']

    # 方法1
    print ('遍历列表方法1：')
    for i in list:
        print ("序号：%s   值：%s" % (list.index(i) + 1, i))

    print ('\n遍历列表方法2：')
    # 方法2
    for i in range(len(list)):
        print ("序号：%s   值：%s" % (i + 1, list[i]))

    # 方法3
    print('\n遍历列表方法3：')
    for i, val in enumerate(list):
        print ("序号：%s   值：%s" % (i + 1, val))

    # 方法3
    print ('\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：')
    for i, val in enumerate(list, 2):
        print ("序号：%s   值：%s" % (i + 1, val))


'''
   2、关于Socket实现客户端与服务器端，实现文件传输功能的案例: http://www.cppcns.com/jiaoben/python/283521.html
   设计思路的梳理:
   ①服务端读文件，并将读取的数据，写到客户端
   ②客户端接收到服务端，传递的数据之后，将其写入到对应的文件中
   ③客户端接收完成服务端，传递的数据之后，给服务端返回一个标志位
'''


'''
 助教提供的Python编写规范的参考文档:
 https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/
'''