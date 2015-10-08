# File Transfer System
# import os as that is the API used to manipulate user directories
# it is cross platform (as is the socket API)
import socket
import os
import sys
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost',4040)) # change localhost and 4040 to IP and PORT# of server
serversocket.listen(5)


while True:
	c, addr = serversocket.accept()
	print 'Connected to ', addr
	running = True
	while running:
		c.send(os.getcwd()) # client needs to get the current directory, so we send it here
		raw_msg = c.recv(4096)
		if not raw_msg:
			print "Client disconnected"
			c.close()
			break
		msg = raw_msg.split()
		cmd = msg[0]
		print 'Received cmd ', cmd
		if cmd == "ls":
			lsDir = os.listdir(os.getcwd())
			#Check for empty directory
			if not lsDir: string = "*empty*"
			else:
				string = '\n'.join(lsDir)
				print "string: ",string
			c.send(string)
		elif cmd == "cd":
			target = msg[1]
			os.chdir(target)
		elif cmd == "mkdir":
			target = msg[1]
			newDir = os.getcwd() + "/" + target
			os.mkdir(newDir)
		elif cmd == "get":
			target = msg[1]
			f = open(target,"rb");
			chunk = f.read(4096)
			while(chunk):
				#print("sending stuff ",sys.getsizeof(chunk))
				c.send(chunk)
				if c.recv(4096) != "ACK":
					print "Failed transfer"
				chunk = f.read(4096)
			f.close()
			c.send('EOF')
		elif cmd == "put":
			target = msg[1]
			f = open(target,"wb");
			print("file ok")
			chunk = c.recv(4096)
			while(chunk != 'EOF'):
				print("got stuff")
				f.write(chunk)
				c.send("ACK")
				chunk = c.recv(4096)
			f.close()
		elif cmd == "terminate":
			c.close() 
			running = False
		else:
			print("Received unkown cmd: "+cmd)
