# Tugas Praktikum Week 13 | Ethernet II dan Address Resolution Protocol (ARP)

Nama : Galang Herjuno Mulya  
NIM : 103072430006  
Kelas : IF-04-01

---

## Struktur Folder

1. `Assets/` berisi screenshot frame Ethernet II, cache ARP, dan traffic ARP.

---

## Tujuan Praktikum

Mahasiswa dapat memahami struktur frame Ethernet II dan proses kerja ARP dalam menerjemahkan alamat IP menjadi alamat MAC pada jaringan lokal.

---

## Pengantar

Pada praktikum ini, saya melakukan investigasi terhadap protokol Link Layer, khususnya Ethernet II dan ARP. Dengan menghapus cache ARP, saya dapat memaksa host melakukan resolusi alamat fisik sehingga proses Request dan Reply dapat diamati di Wireshark.

---

## Langkah Percobaan

1. Buka Wireshark dan filter traffic yang relevan.
2. Amati struktur frame Ethernet II pada paket HTTP.
3. Jalankan `arp -a` untuk melihat cache ARP.
4. Jalankan `arp -d *` jika perlu mengosongkan cache.
5. Amati paket ARP Request dan ARP Reply di Wireshark.

---

## Output / Hasil Percobaan

### Analisis Struktur Frame Ethernet II
<img src="./Assets/frame ethernet.png" alt="Tampilan Detail Frame Ethernet II" style="width:400px"><br>

### Tabel Cache ARP Lokal
<img src="./Assets/caching arp.png" alt="Tampilan Cache ARP Lokal" style="width:400px"><br>

### Protokol ARP Beraksi di Wireshark
<img src="./Assets/aksi arp.png" alt="Tampilan Traffic ARP Request dan Reply" style="width:400px"><br>

---

## Analisis Ethernet II

### 1. Source MAC dan Destination MAC
Frame Ethernet II membawa alamat MAC sumber dan tujuan sebagai identitas layer link. Pada trace, destination MAC biasanya mengarah ke gateway atau perangkat tujuan di jaringan lokal, bukan langsung ke server internet jauh.

### 2. Field Type
Field Type pada Ethernet II menunjukkan protokol layer di atasnya. Jika nilai Type adalah `0x0800`, berarti payload yang dibawa adalah IPv4.

### 3. Ukuran Frame
Ukuran frame Ethernet bervariasi tergantung payload yang dibawa. Frame minimal dan maksimal dapat berbeda tergantung jenis paket dan besarnya data pada layer atas.

---

## Analisis ARP

### 1. ARP Request
ARP Request digunakan untuk mencari MAC Address dari alamat IP tertentu di jaringan lokal. Karena target MAC belum diketahui, paket ini dikirim sebagai broadcast ke semua host dalam segmen jaringan.

### 2. ARP Reply
ARP Reply dikirim sebagai unicast ke host yang mengirim permintaan. Balasan ini berisi pasangan alamat IP dan MAC Address milik host target.

### 3. Opcode ARP
Opcode pada pesan ARP menunjukkan jenis pesan. Nilai `1` menandakan Request, sedangkan nilai `2` menandakan Reply.

### 4. ARP Cache
Setelah satu kali resolusi berhasil, hasil pemetaan IP ke MAC biasanya disimpan pada ARP cache. Karena itu, host tidak selalu mengirim ARP Request baru setiap kali mengirim paket ke host yang sama.

---

## Pertanyaan Modul

### Bagian 1: Ethernet II

1. **Berapa nilai alamat MAC Sumber (Source MAC Address) dan alamat MAC Tujuan (Destination MAC Address) dari frame Ethernet II tersebut? Apakah alamat MAC tujuan merujuk langsung ke server gaia atau ke router gateway Anda?**
   - **Jawaban:** Source MAC adalah MAC address dari komputer lokal, sedangkan Destination MAC biasanya mengarah ke router gateway pada jaringan lokal.

2. **Periksa field Type pada frame Ethernet tersebut. Berapa nilai heksadesimal yang tertera dan apa arti dari nilai tersebut terkait protokol layer di atasnya?**
   - **Jawaban:** Jika field Type bernilai `0x0800`, maka payload yang dibawa adalah protokol IPv4.

3. **Berapakah ukuran total panjang frame Ethernet terkecil dan terbesar yang Anda temukan sepanjang trace transaksi tersebut?**
   - **Jawaban:** Ukuran frame terkecil dan terbesar bergantung pada paket yang tertangkap, namun secara umum frame Ethernet akan berbeda sesuai panjang payload yang dibawa.

### Bagian 2: Protokol ARP

4. **Periksa paket ARP Request (permintaan). Berapa nilai alamat MAC Tujuan (Destination MAC) yang digunakan? Jelaskan mengapa paket ini harus dikirimkan secara Broadcast (`ff:ff:ff:ff:ff:ff`)!**
   - **Jawaban:** Destination MAC pada ARP Request adalah `ff:ff:ff:ff:ff:ff` karena host belum mengetahui MAC address tujuan dan harus menyiarkan permintaan ke seluruh jaringan lokal.

5. **Periksa paket ARP Reply (balasan). Apakah paket balasan ini dikirimkan secara Broadcast atau Unicast? Jelaskan analisis Anda berdasarkan detail alamat MAC-nya!**
   - **Jawaban:** ARP Reply dikirimkan secara unicast ke host yang meminta, karena alamat tujuan sudah diketahui dari paket permintaan.

6. **Buka detail isi pesan di dalam paket ARP Request. Field apa atau opcode bernilai berapa yang menandakan bahwa paket tersebut merupakan sebuah Request (permintaan)?**
   - **Jawaban:** Opcode bernilai **1** menandakan bahwa paket tersebut adalah ARP Request.

7. **Apakah komputer Anda langsung mengirimkan pesan ARP baru ketika ingin mengirimkan paket data kedua menuju host yang sama? Jelaskan hubungannya dengan cara kerja ARP Cache!**
   - **Jawaban:** Tidak selalu. Jika entri alamat masih ada di ARP cache dan belum kedaluwarsa, host dapat memakai hasil resolusi sebelumnya tanpa mengirim ARP Request baru.

---

## Kesimpulan

Berdasarkan praktikum ini, Ethernet II membantu kita melihat identitas layer link, sedangkan ARP berfungsi untuk menerjemahkan alamat IP ke MAC Address di jaringan lokal. Dengan Wireshark, proses broadcast request, unicast reply, dan penggunaan ARP cache dapat diamati dengan jelas.

## Ends Of File
 [Kembali ke Halaman Utama](../README.md) 
