import socketserver,time

class MyServer(socketserver.BaseRequestHandler):
   userInfo = {
       "zhangsan":"123",
       "lisi":"123",
       "wangwu":"123"
   }

   def handle(self):
       print(f"Connect from:{self.client_address}")

       while True:
           receivedData = self.request.recv(8192)
           if not receivedData:
               continue
           elif receivedData == "Hi, Server":
                self.request.sendall("hi client")
           elif receivedData.startswith(bytes("name",encoding="utf-8")):
               self.clientName = receivedData
               if MyServer.userInfo.has_key(self.clientName):
                   self.request.sendall("valid")
               else:
                   self.request.sendall("invalid")
           
           elif receivedData.startswith(bytes("pwd",encoding="utf-8")):
               self.clientPwd = receivedData.split(":")[-1]
               if self.clientPwd == MyServer.userInfo[self.clientName]:
                   self.request.sendall("valid")
                   time.sleep(5)

                   sfile = open("PyNet.pdf",'rb')
                   while True:
                       data = sfile.read(1024)
                       if not data:
                           break
                       while len(data)> 0:
                           intSent = self.request.send(data)
                           data = data[intSent:]
                       time.sleep(3)
                       self.request.sendall('EOF')
               else:
                   self.request.sendall("invalid")
           elif receivedData == 'bye':  
                break
       self.request.close() 
       print('Disconnected from', self.client_address )

          
    

if __name__ == '__main__':  
    print('Server is started\nwaiting for connection...\n') 
    srv = socketserver.ThreadingTCPServer(('localhost', 50000), MyServer)  
    srv.serve_forever()


