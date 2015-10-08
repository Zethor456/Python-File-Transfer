# File Transfer System
# import socket API, as that is how we are handling and creating a
# client/server relationship
import socket
import sys
import re
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost',4040) # change localhost and 4040 to your IP and Port #
socket.connect(server)

print "Connected to: ",server

running = True
while running:
    path = socket.recv(4096) # get the current directory from the server
    raw_cmd = raw_input(path+">")
    cmd = raw_cmd.split()

    # we store the user input in a list
    if cmd[0] == "ls":
        socket.send(cmd[0])
        listElements = socket.recv(4096)
        print listElements
        #print ("End ls")
    elif cmd[0] == "cd":
        socket.send(raw_cmd)
    elif cmd[0] == "mkdir":
        socket.send(raw_cmd)
    elif cmd[0] == "get":
        target = cmd[1]
        filename = re.search(r'\w+\.?\w+?$',target).group(0)
        f = open(filename,"wb")
        socket.send(raw_cmd)
        chunk = socket.recv(4096)
        while(chunk != "EOF"):
            #print("got stuff ",sys.getsizeof(chunk))
            #print(chunk)
            f.write(chunk)
            socket.send("ACK")
            chunk = socket.recv(4096)
        f.close()
    elif cmd[0] == "put":
        f = open(cmd[1],"rb")
        raw_cmd = cmd[0]+" "+re.search(r'\w+\.?\w+?$',cmd[1]).group(0)
        socket.send(raw_cmd)
        chunk = f.read(4096)
        while(chunk):
            socket.send(chunk)
            if socket.recv(4096) != "ACK":
                print "Failed transfer"
            chunk = f.read(4096)
        f.close()
        socket.send('EOF')
    elif cmd[0] == "exit":
        socket.send("terminate")
        socket.close() 
        running = False
    else:
        print ("Unkown command: "+cmd[0])
        socket.send(cmd[0])
    socket.send("ACK")
