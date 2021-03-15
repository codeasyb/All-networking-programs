import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1111))
s.listen(1)

while True:
	conn, addr = s.accept()
	print(f"Connection to: {addr}")

	try:
		file = open("test.txt", "rb")
		conn.send(file.encode())
		print(f"File sent: {file.name}")
		# conn.send(file.encode())
	except:
		print("Error managing file operation")