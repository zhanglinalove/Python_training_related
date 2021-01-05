'''
作业说明:
本次作业的实现方式，是参考了该文章http://www.cppcns.com/jiaoben/python/283521.html 模仿实现的

实现前期遇到了很多问题:
①设计的目标不明确
②Socket相关的方法非常不熟悉，不知道如何下手
③报错以后，不知道具体原因无法解决

最终解决方案:
①在网络上寻找答案，理解设计思路与方法
②模仿代码的书写方式
③理解之后，对于其中的不合理的地方，进行了调整
④报错实现找不出答案的时候，咨询了老师
⑤BrokenPipeError: [Errno 32] Broken pipe 的报错，主要是服务端、或者是客户端一端掉线了

'''

#导入对应的模块
import socket
import os
from pathlib import *

#创建套接字

def echo_client(filepath):
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('localhost',50000))


    filename = input("请输入要下载的文件:\n")

    tcp_client_socket.send(filename.encode())
    try:
        with open(filepath.joinpath(filename) ,"wb") as file:
            while True:
                file_data = tcp_client_socket.recv(1024)
                if file_data:
                    file.write(file_data)
                else:
                    break
        print("下载成功！")
    except Exception as e:
        print("下载异常", e)

    tcp_client_socket.close()

if __name__ == '__main__':
    path = os.getcwd()
    filepath = Path(path)
    echo_client(filepath)





