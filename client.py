import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',4040))

cmd = raw_input("Enter the command you want to send: ")
if cmd == "ls":
    socket.send(cmd);
