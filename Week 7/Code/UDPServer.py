from socket import *

serverPort = 12000
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverPort))

print('The server is ready to receive')

while True:
    message, clientAddress = serversocket.recvfrom(2048)
    
    modifiedMessage = message.decode().upper()
    kata_terbalik = modifiedMessage[::-1]
    serversocket.sendto(kata_terbalik.encode(), clientAddress)