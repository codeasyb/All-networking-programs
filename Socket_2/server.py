import socket
import socketserver

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 4321))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")
	clientsocket.send(bytes("HELLO", "utf-8"))
	clientsocket.close()
