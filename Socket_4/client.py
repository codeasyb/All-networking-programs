import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1500))

while True:
	full_msg = ''
	new_msg = True
	while True:
		msg = s.recv(16)
		if new_msg:
			print(f"new mesage length: {msg[:HEADERSIZE]}")
			msglen = int(msg[:HEADERSIZE]) # get the size of the message
			new_msg = False

		full_msg += msg.decode("utf-8")

		if len(full_msg)-HEADERSIZE == msglen:
			print("full message received")
			print(full_msg[HEADERSIZE:])
			new_msg = True
			full_msg = ''

	print(full_msg)