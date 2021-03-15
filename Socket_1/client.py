import socket
import random
import threading

# try and catch for establishing a connection the server
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Connection established")	
except socket.error as err:
	print('{}'.format("Error connecting"), err)

# try and catch for sending a packet after connection
try:
	s.connect((socket.gethostname(), 1000))
	sendmessage = socket.sendall(bytes("HELLO", "ascii")) # sending packets in ascii code
	msg = str(socket.recv(1024), 'ascii')
	print("Message sent: {}".format(sendmessage))
	print("Receive back: {}".format(msg))
except socket.error as packeterror:
	print('{}'.format("Error sending the packet"), packeterror)










# HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])

# # Create a socket (SOCK_STREAM means a TCP socket)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     # Connect to server and send data
#     sock.connect((HOST, PORT))
#     sock.sendall(bytes(data + "\n", "utf-8"))

#     # Receive data from the server and shut down
#     received = str(sock.recv(1024), "utf-8")

# print("Sent:     {}".format(data))
# print("Received: {}".format(received))