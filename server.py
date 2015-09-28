import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost',4040))

#queue up to 5 requests
serversocket.listen(5)

aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#while 1:
#TODO loop accepting new clients

#accept() returns a new client socket
(client, address) = serversocket.accept()

#TODO methods to process incoming client requests
#basically just a loop and a case statement

msg = client.recv(512)
print (msg)
data = b"ACK"
client.send(data)
print ('connected to client!')


client.close()
serversocket.close()

	