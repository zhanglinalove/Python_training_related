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





