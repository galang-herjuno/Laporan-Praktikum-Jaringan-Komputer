# Tugas Praktikum Week 10 | Internet Protocol (IP) - Bagian Traceroute & Fragmentasi

Nama : Galang Herjuno Mulya  
NIM : 103072430006  
Kelas : IF-04-01

---

## Struktur Folder

1. `Asets/` berisi screenshot hasil Tracert dan tampilan utama Wireshark.

---

## Tujuan Praktikum

Mahasiswa dapat menganalisis struktur datagram IPv4, memahami peran field Time-to-Live, serta mengamati bagaimana paket fragmentasi terjadi ketika ukuran datagram melebihi batas MTU.

---

## Pengantar

Pada praktikum ini, saya menggunakan `tracert` untuk melihat jalur hop dari komputer menuju server tujuan. Setelah itu, saya mengamati traffic di Wireshark untuk memahami bagaimana paket UDP dan ICMP digunakan selama proses traceroute, serta bagaimana field IPv4 berubah saat datagram melewati router.

---

## Langkah Percobaan

1. Jalankan perintah `tracert` ke target server `gaia.cs.umass.edu`.
2. Buka Wireshark dan lakukan capture traffic yang muncul selama traceroute.
3. Gunakan filter `udp || icmp` untuk menampilkan paket yang relevan.
4. Pilih paket IPv4 yang sesuai untuk dianalisis pada bagian detail paket.

---

## Output / Hasil Percobaan

### Hasil Tracert / Traceroute pada CLI
<img src="./Asets/Tracert CLI.png" alt="Tampilan Hasil Tracert CLI" style="width:400px"><br>

### Tampilan Jendela Utama Wireshark
<img src="./Asets/Jendela Utama Wireshark.png" alt="Tampilan Jendela Utama Wireshark" style="width:400px"><br>

---

## Analisis IPv4 Dasar

### 1. Alamat IP Sumber dan Tujuan
Pada packet trace traceroute, datagram IPv4 dikirim dari alamat IP komputer lokal menuju server tujuan atau router perantara. Alamat sumber menunjukkan host pengirim, sedangkan alamat tujuan menunjukkan hop berikutnya yang ingin dicapai oleh paket.

### 2. Protokol yang Dibungkus
Field `Protocol` pada header IPv4 menunjukkan protokol layer transport yang dibawa di dalam datagram, misalnya UDP atau ICMP. Pada traceroute, paket awal biasanya menggunakan UDP, sedangkan balasan dari router sering berupa ICMP `Time Exceeded`.

### 3. Total Length, Header Length, dan Payload
Field `Total Length` menyatakan total ukuran datagram IPv4 secara keseluruhan, termasuk header dan payload. `Header Length` biasanya menunjukkan ukuran header IPv4 dasar, yaitu 20 byte jika tidak ada opsi tambahan. Sisa ukurannya merupakan payload yang dibawa oleh datagram tersebut.

### 4. Field Identification
Field `Identification` digunakan untuk membedakan datagram yang dikirim oleh host. Nilainya umumnya berubah pada setiap datagram baru karena setiap paket harus punya identitas unik untuk membantu proses fragmentasi dan reassembly.

### 5. Field Time-to-Live
Field `TTL` pada paket traceroute dipakai untuk membatasi jumlah hop yang dapat dilalui paket. Nilai TTL akan berkurang satu setiap kali melewati router. Saat TTL mencapai nol, router akan membuang paket dan mengirim pesan ICMP `TTL Exceeded` kembali ke pengirim.

### 6. Pesan ICMP TTL-Exceeded
Pesan ICMP `TTL Exceeded` dibungkus dalam datagram IP baru yang dikirim router kembali ke host. TTL pada datagram balasan ini berbeda dari paket awal karena paket balasan merupakan paket baru yang dibuat oleh router, bukan paket yang sama yang sedang melewati jaringan.

---

## Analisis Fragmentasi IP

Fragmentasi IP terjadi ketika ukuran datagram lebih besar daripada MTU pada jalur jaringan. Jika ini terjadi, router akan memecah datagram menjadi beberapa fragmen. Pada header IPv4, informasi seperti `Identification`, `Flags`, dan `Fragment Offset` digunakan untuk mengatur fragmen tersebut agar bisa disusun kembali di host tujuan.

### Hal yang biasanya diamati

| No | Komponen yang Dianalisis | Hasil Analisis |
| --- | --- | --- |
| 1 | Field `Identification` | Sama untuk fragmen dari datagram yang sama |
| 2 | Field `MF` / More Fragments | Menandakan masih ada fragmen lanjutan |
| 3 | Field `Fragment Offset` | Menunjukkan posisi fragmen pada datagram asli |
| 4 | Perilaku reassembly | Fragmen disusun ulang di host tujuan |

---

## Kesimpulan

Berdasarkan praktikum ini, traceroute membantu melihat jalur perjalanan paket menuju server tujuan, sedangkan Wireshark menunjukkan bagaimana field IPv4 berubah selama proses tersebut. Field `TTL` sangat penting karena membatasi umur paket, dan fragmentasi IP diperlukan ketika ukuran datagram melebihi MTU pada jalur jaringan.

## Ends Of File
 [Kembali ke Halaman Utama](../README.md) 
