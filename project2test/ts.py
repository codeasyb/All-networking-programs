import sys
import socket as soc

sc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
print("connected")

host = soc.gethostname()
host_ip = soc.gethostbyname(host)
address = (host_ip, int(sys.argv[1]))
sc.bind(address)
sc.listen(1)

while True:
	conn, addr = sc.accept()
	message = conn.recv(1024).decode("utf-8")
	print("[C] {message}")

	send = "Yes they are cool"
	conn.send(send).encode("utf-8")

	
