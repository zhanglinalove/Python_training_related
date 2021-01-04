'''
作业:
不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。

实现困难点:
自己实现过程中，遇到的问题: 主要是对于多线程的代码，相关的类库，均不熟悉。


'''

import socket,time

class  MyClient():
    def __init__(self):
        print("Prepare for connecting.....")

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost',50000))
        sock.sendall(b'Hi, Server')  
        self.response = sock.recv(8192)

        print(f"Server:{self.response}")

        self.s = input("Server: Do you want get the 'thinking in Python' file ?(y/n):")
        if self.s == 'y':
            while True:
                self.name = input("Server: input your name:")
                sock.sendall(bytes(f'name:{self.name.strip()}',encoding="utf-8")) 
                self.response = sock.recv(8192)

                if self.response == 'valid':
                    break
                else:
                    print("Server: Invalid username")
            
            while True:
                self.pwd = input("Server: input your password:")
                sock.sendall(f'name:{self.pwd.strip()}'.encode("utf-8"))
                self.response = sock.recv(8192)
                if self.response == 'valid':
                    print("please wait......")
                    f  = open("b.pdf",'wb')
                    while True:
                        data = sock.recv(1024)
                        if data == "EOF":
                            break
                        f.write(data)
                        f.flush()
                        f.close()
                        print('download finished!')
                        break

                else:
                    print("Server: Invalid password")

        sock.sendall("bye")
        sock.close()
        print("Disconnected!")

       
if __name__ == "__main__":
    client = MyClient()
    client.connect()