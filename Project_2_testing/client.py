import socket

s = socket.socket()

host = socket.gethostname()
host_ip = socket.gethostbyname(host)
print("[HOST]: {}".format(host))
print("[HOSTIP]: {}".format(host_ip))

address = (host_ip, 12000)
s.connect(address)


s.send("Hello".encode("utf-8"))
