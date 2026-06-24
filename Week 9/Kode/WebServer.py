from socket import *
import sys

def start_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverPort = 6789
    
    try:
        serverSocket.bind(('', serverPort))
    except OSError as e:
        print(f"Gagal bind ke port {serverPort}: {e}")
        return

    serverSocket.listen(1)
    print(f'Server berjalan di port {serverPort}...')
    print('Tekan Ctrl+C untuk menghentikan server secara aman.')

    try:
        while True:
            print('\nReady to serve...')
            connectionSocket, addr = serverSocket.accept()
            
            try:
                message = connectionSocket.recv(1024).decode()
                
                if not message:
                    connectionSocket.close()
                    continue
                    
                filename = message.split()[1]
                
                # Mencoba membaca file yang diminta
                with open(filename[1:], 'r') as f:
                    outputdata = f.read()
                
                # Header 200 OK
                header = "HTTP/1.1 200 OK\r\n"
                header += "Content-Type: text/html\r\n"
                header += f"Content-Length: {len(outputdata)}\r\n"
                header += "\r\n"
                
                connectionSocket.send(header.encode())
                connectionSocket.send(outputdata.encode())
                print(f"Berhasil mengirim: {filename}")

            except (IOError, IndexError):
                error_html = """
                <!DOCTYPE html>
                <html lang="id">
                <title>Error Not Found </title>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body {
                            margin: 0;
                            display: flex;
                            flex-direction: column;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            background-color: #ffffff;
                            color: #222;
                            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                            text-align: center;
                        }
                        h1 {
                            font-weight: 100;
                            font-size: 8rem;
                            margin: 0;
                            line-height: 1;
                        }
                        p {
                            font-weight: 300; 
                            font-size: 1.2rem;
                            color: #888;
                            letter-spacing: 1px;
                            margin-top: -10px;
                        }
                    </style>
                </head>
                <body>
                    <h1>404</h1>
                    <p>Error Not Found.</p>
                </body>
                </html>
                """
                
                print(f"File tidak ditemukan: {filename if 'filename' in locals() else 'Unknown'}")
                
                header = "HTTP/1.1 404 Error Not Found\r\n"
                header += "Content-Type: text/html\r\n"
                header += f"Content-Length: {len(error_html)}\r\n"
                header += "\r\n"
                
                connectionSocket.send(header.encode())
                connectionSocket.send(error_html.encode())
            
            connectionSocket.close()

    except KeyboardInterrupt:
        print("\n\nMenghentikan server...")
    finally:
        serverSocket.close()
        print("Server socket telah ditutup. Sampai jumpa!")
        sys.exit(0)

if __name__ == "__main__":
    start_server()