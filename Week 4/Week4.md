# Tugas Praktikkum Week 4 | Domain Name System (DNS)

Praktikum week 4 membahas cara kerja Domain Name System atau DNS. Pada modul ini saya melakukan beberapa percobaan menggunakan `nslookup`, melihat cache DNS lokal, lalu mengamati traffic DNS di Wireshark untuk memahami alur query dan response.

### 1. Uji Coba Perintah Nslookup Dasar
Pada tahap awal, saya menjalankan perintah `nslookup` untuk mencari alamat IP dari `www.mit.edu`. Hasil dari perintah ini menunjukkan bagaimana komputer mengirim query DNS ke server yang sedang digunakan lalu menerima balasan berisi alamat IP tujuan.

#### Tampilan Command Prompt Nslookup MIT
<img src="./Assets/nslookupmit.png" alt="Tampilan Command Prompt Nslookup MIT" style="width:400px"><br>

### 2. Mencari DNS Otoritatif dengan Opsi Type NS
Percobaan berikutnya menggunakan `nslookup -type=NS mit.edu` untuk melihat name server yang berwenang pada domain tersebut. Dari hasil ini kita bisa mengetahui server DNS mana yang bertanggung jawab mengelola domain MIT.

#### Tampilan Query DNS Otoritatif
<img src="./Assets/dns1.png" alt="Tampilan Query DNS Otoritatif" style="width:400px"><br>

### 3. Query DNS Spesifik ke Server Tertentu
Pada bagian ini saya melakukan query DNS dengan server tertentu agar proses pencarian alamat domain tidak hanya bergantung pada DNS default. Tujuannya adalah melihat apakah hasil resolver tetap konsisten meskipun server DNS yang dituju berbeda.

#### Tampilan Query ke Server Spesifik
<img src="./Assets/wiresharkdns.png" alt="Tampilan Query ke Server Spesifik" style="width:500px"><br>

### 4. Melihat dan Mengosongkan Cache DNS Lokal
Saya juga memeriksa cache DNS lokal menggunakan `ipconfig /displaydns`, lalu mengosongkannya dengan `ipconfig /flushdns`. Langkah ini berguna untuk memastikan bahwa query DNS berikutnya benar-benar dikirim ulang ke server, bukan diambil dari cache.

#### Tampilan Proses Flush DNS
<img src="./Assets/flushdns.png" alt="Tampilan Proses Flush DNS" style="width:400px"><br>

### 5. Tracing Paket DNS Melalui Wireshark
Bagian terakhir adalah mengamati paket DNS yang muncul saat melakukan browsing ke `www.ietf.org`. Dari sini terlihat paket query dan response DNS yang dikirim untuk menerjemahkan nama domain menjadi alamat IP.

#### Tampilan Paket DNS Query dan Response
<img src="./Assets/ipconfigall.png" alt="Tampilan Paket DNS Query dan Response" style="width:500px"><br>

### Pertanyaan Modul

1. **Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP atau TCP?**
   - **Jawaban:** Pada praktik umum DNS seperti ini, pesan permintaan dan balasan DNS dikirim melalui **UDP**. Hal ini karena DNS standar memakai port 53 UDP untuk query ringan dan cepat.

2. **Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?**
   - **Jawaban:** Port tujuan pada pesan permintaan DNS adalah **53**. Port sumber pada pesan balasan adalah **53** juga, karena balasan datang dari server DNS yang sama.

3. **Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal Anda? Apakah kedua alamat IP tersebut sama?**
   - **Jawaban:** Alamat IP tujuan pada pesan permintaan DNS adalah alamat server DNS yang digunakan oleh komputer. Berdasarkan `ipconfig`, alamat IP server DNS lokal biasanya sama dengan alamat tujuan query jika resolver lokal memang server yang dipakai secara langsung. Jika memakai DNS router atau DNS ISP, maka keduanya akan sesuai dengan server yang tercantum di konfigurasi jaringan.

4. **Periksa pesan permintaan DNS. Apa jenis atau type dari pesan tersebut? Apakah pesan permintaan tersebut mengandung jawaban atau answers?**
   - **Jawaban:** Untuk query awal ke domain web biasa, type yang paling umum adalah **A** untuk mencari alamat IPv4. Pesan permintaan tidak mengandung answers karena fungsi request hanya mengajukan pertanyaan, bukan mengirim jawaban.

5. **Periksa pesan balasan DNS. Berapa banyak jawaban atau answers yang terdapat di dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?**
   - **Jawaban:** Jumlah answers bergantung pada domain yang diminta. Pada kasus domain web umum, biasanya balasan berisi satu atau lebih record A/CNAME. Isi setiap jawaban biasanya meliputi nama domain, tipe record, TTL, dan alamat IP tujuan.

6. **Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?**
   - **Jawaban:** Ya, alamat IP pada paket TCP SYN umumnya sesuai dengan alamat IP hasil balasan DNS. Ini menunjukkan bahwa browser langsung memakai hasil resolusi DNS untuk membuka koneksi TCP ke server yang benar.

7. **Halaman web yang sebelumnya Anda akses memuat beberapa gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin mengakses suatu gambar?**
   - **Jawaban:** Tidak selalu. Jika gambar masih berada pada domain yang sama, host biasanya tidak perlu melakukan query DNS baru karena alamat IP server sudah diketahui dan sering disimpan di cache. Query baru hanya diperlukan jika domain atau host tujuan berubah, atau cache DNS sudah kedaluwarsa.

## Ends Of File
 [Kembali ke Halaman Utama](../README.md) 
