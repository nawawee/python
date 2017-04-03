from socket import *
host = raw_input("Enter Server IP: ")
port = input("Enter Server Port: ")
addr = (host,port)
bufsize = 1024
print("*************Client side*************")

client = socket(AF_INET,SOCK_STREAM)
client.connect((addr))
print('.................Connection established to server:',addr,' now......')

while True:
    message = raw_input("Enter client message: ")
    client.send(str.encode(message))
    data = client.recv(bufsize).decode()
    print("Received from server:",data)
    if data == "bye":
        break
client.close()