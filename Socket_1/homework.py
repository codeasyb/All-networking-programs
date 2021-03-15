import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = str(self.request.recv(1024), 'ascii')
            cur_thread = threading.current_thread()
            if len(data) <= 0:
                break;
            # full_msg += self.decode("ascii")
            chara = [ord(c) for c in data]
            message = str(('_'.join(map(str, chara))))
            response = bytes("{}: {}".format(cur_thread.name, message), 'ascii')
            self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

# this function will read file from the same directory this file will be executed
def readeFile():
    try:
        file = open('HW1test.txt','r')
        fileContent = file.read()
        for word in fileContent.split():
            print(word)
    finally:
        file = open('HW1out.txt', 'w')
        for word in fileContent.split():
            file.write(word + "\n")


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        client(ip, port, "HELLO")
        # client(ip, port, "hello")
        # client(ip, port, "world")

        readeFile()

        server.shutdown()






# things to know 

# who keeps the mapping between IP and the server