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
	if msg == "get":
		filenme = c.recv(1024)
		sentfile = open("Test.txt","r");
		chunk = sentfile.read(4096)
		while(chunk):
			print("sent stuff")
			c.send(chunk)
			
			chunk = sentfile.read(4096)
		sentfile.close	
		c.shutdown(socket.SHUT_WR)
		print c.recv(4096)
		c.close
	if msg == "put":
		print("got here")
		filenme = c.recv(4096)
		print("got here")
		f = open(filenme,"wb");
		print("file ok")
		chunk = c.recv(4096)
		while(chunk):
			print("got stuff")
			f.write(chunk)
			chunk = c.recv(4096)
		f.close()
		c.recv(1024);
		c.close	
