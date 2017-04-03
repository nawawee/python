from socket import *
host = "127.0.0.1"
port = 9000
addr = (host,port)
bufsize = 1024
print("*********Server side************")

server = socket(AF_INET,SOCK_STREAM)
print("Socket server created:", addr)

server.bind((addr))
server.listen(5)

conn,addr = server.accept()
print('.............Connection established from address:',addr)

while True:
    data = conn.recv(bufsize).decode()
    if not data:
        break
    print("Received data from client",addr,":",data)
    message = raw_input("Enter server message: ")
    conn.send(str.encode(message))

conn.close()