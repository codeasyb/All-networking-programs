import socket
import os
import sys
import marshal

FilePath = os.path.realpath(os.path.dirname(sys.argv[0]))

s = socket.socket()
s.bind(("localhost",8000))
s.listen(5) #Tipo, 5 conexoes no maximo {ao mesmo tempo}

i=0
nome = 'file_'
while (True):
    sc, address = s.accept()
    nome = 'file_%s' % i
    temp = open(os.path.join(FilePath,'server_received/%s'% nome) ,'wb')
    i=i+1
    l = sc.recv(1024)
    while (l):
        temp.write(l)
        l = sc.recv(1024)
    temp.close()
    temp = open(os.path.join(FilePath,'server_received/%s'% nome) ,'rb') #abrir como binario
    #Here I can unpack my dictionary.
    dados = marshal.load(temp)
    temp.close()
    #removing the file I received
    os.remove(os.path.join(FilePath,'server_received/%s'% nome))
    print(dados[0], dados[1], dados[2])
    arq  = open(os.path.join(FilePath,'server_received/%s'% dados[2].split('\\')[-1]),'wb')
    arq.write(dados[3])
    arq.close()


sc.close()
s.close()