import socket

try:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	localhost = socket.gethostname()
	ip = socket.gethostbyname(localhost)
	port = 12345
	server_address = (ip, port)
	server.bind(server_address)
	server.listen(1)
except socket.error as err:
	print(f"Error connecting to {server}")


print(f"[S] Started listening on {ip}, port {port}")

conn, address = server.accept()

print(f"[S] Got a connection from {address[0]}")

while True:
	data = conn.recv(1024).decode("ascii")      		# receive data from client
	print(f"[C] Client says: {data}")		    		# print what the client sent
	chara = [ord(c) for c in data]			    		# convert every character into ASCII VALUE
	message = str('_'.join(map(str, chara)))  			# mapping the characters to string 
	print(f"[S] Server Respond: [{message}]")
	conn.sendall(message.encode('ascii'))
	conn.close()
	
server.close()