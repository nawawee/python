#Client
from socket import *

host = raw_input("Enter Server IP: ")
port = input("Enter Server Port: ")
bufsize = 1024
sock = (host,port)
print("*************Client side*************")

server = socket(AF_INET,SOCK_DGRAM)
print("Socket server created:", sock)

print('.................Connection established to server:',sock,' now......')

while True:
    data = raw_input("Enter Client message: ")
    server.sendto(data.encode(),sock)

    message,addr = server.recvfrom(bufsize)
    print("Received :"+message.decode())

    if message == "bye" :
        break

server.close()