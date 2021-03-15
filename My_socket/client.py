import socket 
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_name = socket.gethostbyname(socket.gethostname())
port = 2222

s.connect((ip_name, port))

msg = "hello"
s.send(msg.encode("utf-8"))

server = s.recv(1024).decode("utf-8")
print(f"{server.upper()}")
