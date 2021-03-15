import os
import sys
import socket as soc

sc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
host = sc.gethostname;
host_ip = sc.gethostbyname(host)
server = (host_ip,  sys.argv[1])
sc.connect(server)

print("Connection established")

message = "command line arguments are cool"
sc.send(message.encode("utf-8"))

incomming = sc.recv(1024).decode("utf-8")
print(f"incomming message: {incomming}")

