import socket 
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1200))
s.listen(1)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established")

	d = {1: "Hey", 2: " there"}
	msg = pickle.dump(d)

	msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

	clientsocket.send(msg)