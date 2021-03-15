
import socket as soc
import threading
import socketserver

# Making a handshake with the server 
try:
	s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
	s.bind((soc.gethostname(), 1000))
	s.listen(1)
	print("[S]: handshake Established")
except soc.error as err:
	print("[S]: Error connecting to the server")


clientsocket, address = s.accept()
print(f"Connection to {address} established")


# Now we going catch error for sending message back to the client
try:
	full_msg = ''
	while True:
		msg = s.recv(1).strip() 		   			# receiving 1 byte arbitrary of times
		#print(ord(msg), len(msg))
		if len(msg) <= 0:
			break;
		full_msg += clientsocket.decode("ascii")    # decode the message when received
		chara = [ord(c) for c in full_msg] 			# using advanced for loop to convert into ASCII codee

	print('_'.join(map(str, chara)))	   			# map the characters recieved into a string of ASCII code
except soc.error as servererror:
	print("Error sending message.")




# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

#     def handle(self):
#         data = str(self.request.recv(1024), 'ascii')
#         # cur_thread = threading.current_thread()
#         response = bytes("{}".format(data.lower()), 'ascii')
#         self.request.sendall(response)

# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass


# if __name__ == "__main__":
# 	 # Port 0 means to select an arbitrary unused port
#     HOST, PORT = "localhost", 1000

#     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
#     with server:
#         ip, port = server.server_address

#         # Start a thread with the server -- that thread will then start one
#         # more thread for each request
#         server_thread = threading.Thread(target=server.serve_forever)
#         # Exit the server thread when the main thread terminates
#         server_thread.daemon = True
#         server_thread.start()


#         server.shutdown()







