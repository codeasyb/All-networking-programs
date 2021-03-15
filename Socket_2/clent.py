import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 4321))



#s.send(bytes("HELLO", "utf-8"))

full_msg = ''
while True:
	msg = s.recv(1)                    # receiving 1 byte arbitrary of times
	#print(ord(msg), len(msg))
	if len(msg) <= 0:
		break;
	full_msg += msg.decode("utf-8")    # decode the message when received
	chara = [ord(c) for c in full_msg] # using advanced for loop to convert into ASCII codee

print('_'.join(map(str, chara)))	   # map the characters recieved into a string of ASCII code

try:
	file = open('HW1test.txt','r')
	fileContent = file.read()
	for word in fileContent.split():
	    print(word)
finally:
	file = open('outfile.txt', 'w')
	for word in fileContent.split():
		file.write(word + "\n")



# def read():
# 	try:
# 		file = open('HW1test.txt','r')
# 		fileContent = file.read()
# 		for word in fileContent.split():
# 	    		print(word)
# 	finally:
# 		file = open('outfile.txt', 'w')
# 		for word in fileContent.split():
# 			file.write(word + "\n")



# def readFile():
# 	try:
# 		file = open('HW1test.txt', 'r')
# 		fileContent = file.read()
# 		for word in fileContent.split():
# 				print(word) 
# 	finally:
# 		file.close()


#t1.threading.Thread(server='read', target=read)
#t1.start()


#input("Enter to exit\n")
#exit()