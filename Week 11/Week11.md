# Tugas Praktikum Week 11 | Dynamic Host Configuration Protocol (DHCP)

Nama : Galang Herjuno Mulya  
NIM : 103072430006  
Kelas : IF-04-01

---

## Struktur Folder

1. `Assets/` berisi screenshot proses release, renew, dan detail DHCP handshake.

---

## Tujuan Praktikum

Mahasiswa dapat memahami proses pengalamatan dinamis menggunakan DHCP, mulai dari pelepasan alamat IP, permintaan alamat baru, hingga analisis empat tahapan handshake DHCP di Wireshark.

---

## Pengantar

DHCP digunakan untuk membagikan konfigurasi jaringan secara otomatis kepada host. Pada praktikum ini, saya menjalankan perintah `ipconfig /release` dan `ipconfig /renew` untuk memicu transaksi DHCP, kemudian mengamati hasilnya di Wireshark agar bisa melihat bagaimana paket Discover, Offer, Request, dan ACK terbentuk.

---

## Langkah Percobaan

1. Jalankan `ipconfig /release` untuk melepaskan alamat IP.
2. Jalankan `ipconfig /renew` untuk meminta alamat IP baru.
3. Buka Wireshark dan gunakan filter `dhcp`.
4. Pilih paket DHCP Discover, Offer, Request, dan ACK untuk dianalisis.

---

## Output / Hasil Percobaan

### Proses Release IP
<img src="./Assets/ip relase.png" alt="Tampilan Proses Release IP" style="width:400px"><br>

### Proses Renew IP
<img src="./Assets/ip renew.png" alt="Tampilan Proses Renew IP" style="width:400px"><br>

### Struktur Detail Paket DHCP Handshake
<img src="./Assets/Handshake DHCP.png" alt="Tampilan Struktur Detail Paket DHCP" style="width:400px"><br>

---

## Analisis DHCP

### 1. UDP sebagai Transport DHCP
Pesan DHCP dikirim melalui UDP, bukan TCP. Hal ini karena DHCP dirancang untuk komunikasi yang ringan dan cepat dalam proses inisialisasi jaringan.

### 2. Port yang Digunakan
DHCP menggunakan port sumber dan tujuan yang khas, yaitu client memakai port 68 dan server memakai port 67. Kombinasi ini dipakai konsisten pada proses Discover, Offer, Request, dan ACK.

### 3. Alamat MAC Host
Dalam pesan DHCP, alamat MAC host dicantumkan sebagai identitas layer link. Pada tahap awal, host belum memiliki alamat IP valid sehingga identifikasi perangkat masih mengandalkan MAC address.

### 4. Source IP dan Destination IP pada Discover
Pada pesan DHCP Discover, source IP biasanya bernilai `0.0.0.0` dan destination IP bernilai `255.255.255.255`. Ini terjadi karena host belum memiliki alamat IP dan harus menyebarkan permintaan secara broadcast agar server DHCP manapun bisa merespons.

### 5. Alamat IP yang Ditawarkan
Pada DHCP Offer, server akan menawarkan alamat IP yang masih tersedia untuk host. Alamat ini merupakan hasil peminjaman sementara yang nantinya harus dikonfirmasi melalui DHCP Request.

### 6. Lease Time
Lease time pada DHCP ACK menunjukkan lama sewa alamat IP yang diberikan server. Nilai ini penting karena menentukan kapan host harus memperbarui sewa alamat agar tetap terhubung ke jaringan.

### 7. Perbedaan DHCP Discover dan DHCP Request
DHCP Discover digunakan untuk mencari server DHCP yang tersedia di jaringan, sedangkan DHCP Request digunakan untuk meminta secara spesifik alamat IP yang sudah ditawarkan oleh server. Jadi, Discover bersifat pencarian, sedangkan Request bersifat konfirmasi.

---

## Kesimpulan

Berdasarkan praktikum ini, DHCP bekerja melalui pertukaran pesan UDP yang sederhana tetapi penting untuk konfigurasi jaringan otomatis. Proses release dan renew memperlihatkan bagaimana host melepaskan lalu memperoleh alamat IP baru, sedangkan Wireshark membantu membuktikan empat tahapan DHCP handshake secara jelas.

## Ends Of File
 [Kembali ke Halaman Utama](../README.md) 
