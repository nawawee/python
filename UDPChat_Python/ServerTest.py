from socket import *
host = "127.0.0.1"
port = 9000
sock = (host,port)
bufsize = 1024
print("***********Server Side*********")

server = socket(AF_INET,SOCK_DGRAM)
server.bind((sock))
data,info = server.recvfrom(bufsize)
print("Received :",data.decode()," ",info)
server.close()