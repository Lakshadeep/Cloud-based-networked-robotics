import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.0.103', 8082))

clientsocket.sendall('test1,test2,test3')

data = clientsocket.recv(1024)

clientsocket.close()

print('Received',repr(data))

