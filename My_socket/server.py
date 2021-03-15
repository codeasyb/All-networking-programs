import socket as sock
import sys

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
s.bind(("172.31.199.4", 2222))
s.listen(1)

while True:
	conn, addr = s.accept()
	print(f"Connected to {addr}")
	cmessage = conn.recv(1024).decode("utf-8")
	print(f"Client says: {cmessage}")

	smessage = "hello from server"
	conn.send(smessage.encode("utf-8"))

	user = input("Do you want to stay up(yes/no): ")
	if user == "yes":
		continue
	elif user == "no":
		print("Connection closed")
		break