import socket
import os
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost',4040))
serversocket.listen(5)

currDirectory = os.getcwd()
while True:
	c, addr = serversocket.accept()
	print 'Connected to ', addr
	msg = c.recv(4096)
	if msg == "ls":
		print os.listdir(currDirectory)
	if msg == "cd":
		currDirectory = c.recv(4096)
		print os.listdir(currDirectory)
	if msg == "mkdir":
		toAdd = c.recv(4096)
		newDir = currDirectory + "/" + toAdd
		os.mkdir(newDir)
