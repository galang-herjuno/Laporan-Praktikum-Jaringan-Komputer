from socket import *

# Konfigurasi Port
serverPort = 12000

# Create socket TCP (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind socket ke port
serverSocket.bind(('', serverPort))

# Listen untuk koneksi masuk
serverSocket.listen(1)
print('The server is ready to receive (TCP Reverse)')

while True:
    # Accept koneksi masuk
    connectionSocket, addr = serverSocket.accept()
    
    # Receive message dari client
    sentence = connectionSocket.recv(1024).decode()
    
    reversedSentence = sentence[::-1]
    
    # Send hasil reverse ke client
    connectionSocket.send(reversedSentence.encode())
    
    # Menutup koneksi untuk request ini
    connectionSocket.close()