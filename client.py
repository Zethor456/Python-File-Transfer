import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',4040))

input = raw_input("Enter the command you want to send: ")
cmd = input.split()
if cmd[0] == "ls":
    socket.send(cmd[0])
if cmd[0] == "cd":
    socket.send(cmd[0])
    socket.send(cmd[1])
if cmd[0] == "mkdir":
    socket.send(cmd[0])
    socket.send(cmd[1])
