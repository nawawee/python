#Server
from socket import *
host = "127.0.0.1"
port = 9000
sock = (host,port)
bufsize = 1024
print("*********Server side************")

server = socket(AF_INET,SOCK_DGRAM)
print("Socket server created:", sock)

server.bind((sock))
print('.............Connection established from address:',sock)

l = 1
f = open('E:\Python\chat\UDPPython\data_save.txt','w')

while True:
    data,info = server.recvfrom(bufsize)
    if not data:
        break
    print("Received :",sock,":"+data.decode())
    f.write('Client :%s\n' % (data))
    message = raw_input("Enter server message: ")
    server.sendto(message.encode(),info)
    f.write('Server :%s\n' % (message))
    if message == "bye" :
        break

server.close()