import socket

while not self.queue.empty():
        try:
            s = socket.socket()
            s.connect((HOST,PORT))
        except:
            print("connection error")
            break
        file_path = self.queue.get()
        file = open(file_path,'rb')
        dados = ['User',
                'someothertext',
                file_path,
                file.read()
                ]
        temp = open(os.path.join(SaveDirectory,'temp'),'wb')
        marshal.dump(dados,temp)
        temp.close()
        file = open(os.path.join(SaveDirectory,'temp'),'rb')
        l = file.read(1024)
        while l:
            try:
                s.send(l)
                l = file.read(1024)
            except:
                print("error while sending")
                break


        temp.close()
        file.close()

        os.remove(os.path.join(SaveDirectory,'temp'))

        self.queue.task_done()

        s.close()
        print(u"OK")