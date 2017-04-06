from socket import *
addr = ("127.0.0.1",9000)
bufsize = 1024
print("**********Client Side*************")

server = socket(AF_INET,SOCK_DGRAM)
data = "Hello"
server.sendto(data.encode(),addr)
server.close()