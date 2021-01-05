import socket
import os 
from pathlib import *
import time

def echo_server():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(('localhost',50000))

    tcp_server_socket.listen(2)
    print("服务端已开启，等待客户端连接......")

    while True:
        client_socket,client_ip = tcp_server_socket.accept();
        print("客户端",client_ip,"连接")

        file_name_data = client_socket.recv(1024)
        file_name = file_name_data.decode("utf-8")
        try:
            with open('/Users/zhanglina/Desktop/'+ file_name ,'rb') as file:
                while True:
                    file_data = file.read(1024)
                    time.sleep(100)
                    print("读取文件内容是:",file_data.decode("utf-8"))

                    if file_data:
                        client_socket.sendall(file_data)
                    else:
                        print(file_name,"传输成功")
                        break
        except Exception as e:
            print("传输异常",e)

if __name__ == '__main__':
    echo_server()
 
    




