import socket
import threading
import time
import random
import os
import sys

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	localhost = socket.gethostname()
	server_ip = socket.gethostbyname(localhost)
	port = 12345
except sock.error as err:
	print(f"Erro connecting to {localhost}")

# connect to the address
server_address = (server_ip, port)
sock.connect(server_address)
print(f"[C] Connected to {localhost} at {server_ip}")

# send the packet
message = "HELLO"
print(f"[C] Packet sent: [{message}]")
sock.send(message.encode("ascii"))

# recv the packet from the server
response = sock.recv(1024).decode('ascii')
print(f"[S] Response from server: {response}")
print("Now wait for file to be read.")

# funtion to open for read and write
def readFile():
	try:
		file = open('HW1test.txt', 'r') 	# open file for read
		fileContent = file.read()
		print("-------------")
		for word in fileContent.split():
			print(word)
		print("-------------")
	finally:
			file = open('HW1out.txt', 'w') # open file for write
			for word in fileContent.split():
				file.write(word + '\n')
			print("---------------------------------------------")
			print(f"{str(file.name)} saved in current directory.")
			print("---------------------------------------------")

# time for fun
time.sleep(random.random()*5)
t1 = threading.Thread(name='readFile', target=readFile)
t1.start()
time.sleep(random.random()*1)

print("\nDone, Have a good day, but wait!")
time.sleep(random.random()*3)

# help to open file
flag = input("Do you want to open the file(yes/no)? ")

if flag == "yes":
	hwFile = os.path.abspath('.//HW1out.txt')
	os.system(f"open {hwFile}")
elif flag == "no":
	print("No worries, do it yourself.")
else:
	print(f"File does not exits")












