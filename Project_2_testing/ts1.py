import socket

s = socket.socket()

host = socket.gethostname()
host_ip = socket.gethostbyname(host)
print("[HOST]: {}".format(host))
print("[HOSTIP]: {}".format(host_ip))

address = (host_ip, 12001)
s.bind(address)
s.listen(2)

while True:
	conn, addr = s.accept()
	ls_server = conn.recv(1028).decode("utf-8")
	print("[LS]: {}".format(ls_server))