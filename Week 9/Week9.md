# Tugas Praktikum Week 9 | Internet Protocol (IP)

Nama : Galang Herjuno Mulya  
NIM : 103072430006  
Kelas : IF-04-01

---

## Struktur Folder

1. `Kode/` berisi source code `WebServer.py`.
2. `Assets/` berisi screenshot hasil server dan output browser.

---

## Tujuan Praktikum

Mahasiswa dapat memahami konsep dasar Internet Protocol melalui eksperimen sederhana berupa web server TCP yang melayani file HTML dan menampilkan halaman error ketika file tidak ditemukan.

---

## Pengantar

Internet Protocol merupakan lapisan jaringan yang bertugas membawa datagram dari sumber ke tujuan. Pada praktikum ini, implementasi yang digunakan adalah web server sederhana berbasis socket TCP. Walaupun fokus modul ada pada IP, server ini tetap berguna untuk melihat alur koneksi, pengambilan file, dan respon HTTP yang dikirim ke browser.

---

## Penjelasan Web Server

```python
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
                
                with open(filename[1:], 'r') as f:
                    outputdata = f.read()
                
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
```

Program `WebServer.py` berfungsi sebagai web server sederhana yang menerima request dari browser, membaca file HTML yang diminta, lalu mengirimkan response `200 OK`. Jika file tidak tersedia, server akan mengirimkan halaman `404 Error Not Found`.

### Penjelasan per potongan kode WebServer.py:

- Import modul socket dan sys:
  ```python
  from socket import *
  import sys
  ```
  Digunakan untuk membuat socket TCP dan keluar dari program secara aman.

- Membuat socket TCP:
  ```python
  serverSocket = socket(AF_INET, SOCK_STREAM)
  ```
  Socket dibuat menggunakan protokol TCP.

- Mengaktifkan reuse address:
  ```python
  serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  ```
  Agar port bisa dipakai ulang saat server dijalankan berkali-kali.

- Menentukan port server:
  ```python
  serverPort = 6789
  ```

- Melakukan bind dan listen:
  ```python
  serverSocket.bind(('', serverPort))
  serverSocket.listen(1)
  ```
  Server diikat ke port 6789 dan siap menerima koneksi.

- Menerima request dari browser:
  ```python
  connectionSocket, addr = serverSocket.accept()
  message = connectionSocket.recv(1024).decode()
  ```
  Server membaca request HTTP yang dikirim browser.

- Mengambil nama file:
  ```python
  filename = message.split()[1]
  ```
  Bagian path file diambil dari request line HTTP.

- Membaca file HTML:
  ```python
  with open(filename[1:], 'r') as f:
      outputdata = f.read()
  ```
  File dibuka dari direktori lokal dan isinya dibaca.

- Mengirim response sukses:
  ```python
  header = "HTTP/1.1 200 OK\r\n"
  header += "Content-Type: text/html\r\n"
  header += f"Content-Length: {len(outputdata)}\r\n"
  header += "\r\n"
  connectionSocket.send(header.encode())
  connectionSocket.send(outputdata.encode())
  ```
  Header dan isi file dikirim ke browser.

- Mengirim halaman error:
  ```python
  header = "HTTP/1.1 404 Error Not Found\r\n"
  ```
  Jika file gagal dibaca, server mengirimkan halaman error 404.

## Penjelasan index.html

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Server</title>
</head>
<body>

    <h1>Congrats!</h1>
    <p>Socket anda sudah berhasil dijalankan.</p>

</body>
</html>
```

File `index.html` adalah halaman yang akan ditampilkan oleh web server ketika browser meminta halaman utama. Isi file ini sederhana, hanya menampilkan pesan bahwa socket berhasil dijalankan.

---

## Output / Hasil Percobaan

### Menyiapkan server
<img src="./Assets/Prepare the server.png" alt="Menyiapkan server" style="width:400px"><br>

### Output browser
<img src="./Assets/output.png" alt="Output browser" style="width:400px"><br>

---

## Analisis Awal

| No | Komponen yang Dianalisis | Hasil Analisis |
| --- | --- | --- |
| 1 | Port server yang digunakan | 6789 |
| 2 | Jenis socket yang digunakan | TCP / `SOCK_STREAM` |
| 3 | Respons ketika file ada | `HTTP/1.1 200 OK` |
| 4 | Respons ketika file tidak ada | `HTTP/1.1 404 Error Not Found` |
| 5 | Isi halaman utama | Pesan `Congrats!` |

---

## Kesimpulan

Berdasarkan praktikum ini, web server sederhana dapat melayani file HTML menggunakan socket TCP. Browser mengirim request, server membaca file lokal, lalu mengirimkan response HTTP yang sesuai. Jika file tidak ditemukan, server mengembalikan halaman error 404 sehingga alur komunikasi client-server tetap berjalan dengan jelas.

## Ends Of File
 [Kembali ke Halaman Utama](../README.md) 
