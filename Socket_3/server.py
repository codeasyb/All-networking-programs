
import socket as soc

try:
	s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
	print("[S]: Server socket created.")
except soc.error as err:
	print('{} \n'.format("socket open error ", err))

s.bind((soc.gethostname(), 1234))
s.listen(1)


host = soc.gethostname()
print(f"[S]: Server host name is {host}")


localhost_ip = soc.gethostbyname(host)
print(f"[S]: Server IP address is {localhost_ip}")


clientsocket, addr = s.accept()
print(f"[S]: Got a connection request from a client at {addr}")

msg = "Welcome my boy"
clientsocket.send(msg.encode('utf-8'))


s.close
exit()

