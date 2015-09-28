import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',4040))

#the binary string initialized via b"" is due to
#some kind of compatibility issue between python 2 & 3
PING = b"ping"

socket.send(PING)
response = socket.recv(512)
print response
socket.close()