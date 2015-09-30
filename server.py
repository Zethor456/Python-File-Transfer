import socket
import os
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost',4040))
serversocket.listen(5)


while True:
	c, addr = serversocket.accept()
	print 'Connected to ', addr
	running = True
	while running:
		raw_msg = c.recv(4096)
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
			print os.getcwd()
		elif cmd == "mkdir":
			target = msg[1]
			newDir = os.getcwd() + "/" + target
			os.mkdir(newDir)
		elif cmd == "get":
			target = msg[1]
			f = open(target,"r");
			chunk = f.read(4096)
			while(chunk):
				print("sending stuff")
				c.send(chunk)
				chunk = f.read(4096)
			f.close
		elif cmd == "put":
			target = msg[1]
			f = open(target,"wb");
			print("file ok")
			chunk = c.recv(4096)
			while(chunk):
				print("got stuff")
				f.write(chunk)
				chunk = c.recv(4096)
			f.close()
		elif cmd == "terminate":
			c.close()
			running = False
		else:
			print("Received unkown cmd: "+cmd)
