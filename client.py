import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost',4040)
socket.connect(server)
print "Connected to: ",server

running = True
while running:
    path = socket.recv(4096)
    raw_cmd = raw_input(path+">")
    cmd = raw_cmd.split()
    if cmd[0] == "ls":
        socket.send(cmd[0])
        listElements = socket.recv(4096)
        print listElements
    elif cmd[0] == "cd":
        socket.send(raw_cmd)
    elif cmd[0] == "mkdir":
        socket.send(raw_cmd)
    elif cmd[0] == "get":
        print("Sending ",raw_cmd)
        target = cmd[1]
        f = open(target,"wb")
        socket.send(raw_cmd)
        chunk = socket.recv(4096)
        while(chunk != "EOF"):
            print("got stuff")
            print(chunk)
            f.write(chunk)
            socket.send("ACK")
            chunk = socket.recv(4096)
        f.close()
    elif cmd[0] == "put":
        f = open(cmd[1],"r")
        socket.send(raw_cmd)
        chunk = f.read(4096)
        while(chunk):
            socket.send(chunk)
            if socket.recv(4096) != "ACK":
                print "Failed transfer"
            chunk = f.read(4096)
        f.close
        socket.send('EOF')
    elif cmd[0] == "exit":
        socket.send("terminate")
        socket.close()
        running = False
    else:
        print ("Unkown command: "+cmd[0])