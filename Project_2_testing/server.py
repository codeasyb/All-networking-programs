import socket
import select


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[S]: {}".format(ls))

host = socket.gethostname()
host_ip = socket.gethostbyname(host)
port = 12000
ls_addr = (host_ip, port)

ls.bind(ls_addr)
ls.listen(4)

while True:
	conn, addr = ls.accept()

	client = conn.recv(1024).decode("utf-8")
	print("[C]: {}".format(client))





