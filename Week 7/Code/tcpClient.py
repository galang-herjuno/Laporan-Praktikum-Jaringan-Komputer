from socket import *

#port
serverName = 'Galang-Herjuno'
serverPort = 12000

#create client socket 
clientSocket = socket(AF_INET, SOCK_STREAM)

#connect ke server
clientSocket.connect((serverName, serverPort))

#send message to server
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())

#receive modified sentence from server
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())

#menutup koneksi
clientSocket.close()