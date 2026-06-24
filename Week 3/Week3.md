# Tugas Praktikkum Week 3 | Protokol HTTP

Praktikum week 3 membahas cara kerja protokol HTTP melalui pengamatan langsung di Wireshark. Disini saya fokus melihat bagaimana browser dan server saling bertukar request dan response, serta bagaimana header HTTP memengaruhi proses pengambilan data.

### 1. Persiapan Filter Wireshark
Langkah pertama yang dilakukan adalah menyiapkan display filter `http` pada Wireshark supaya paket yang tampil hanya traffic HTTP. Dengan cara ini, proses analisis menjadi lebih terarah karena paket lain yang tidak relevan bisa diabaikan.

#### Tampilan Filter HTTP
<img src="./Assets/Http1.png" alt="Tampilan Filter HTTP" style="width:400px"><br>

### 2. Basic HTTP GET/Response Interaction
Pada tahap ini, browser digunakan untuk mengakses `file1.html` ke server `gaia.cs.umass.edu`. Dari hasil capture di Wireshark, terlihat adanya request `GET` dari client dan response `200 OK` dari server. Interaksi ini menunjukkan alur dasar HTTP saat browser meminta halaman web lalu server mengirimkan isi halaman tersebut.

#### Tampilan Traffic HTTP GET dan Response OK
<img src="./Assets/Http2.png" alt="Tampilan Traffic HTTP GET dan Response OK" style="width:400px"><br>

### 3. HTTP Conditional GET/Response Interaction
Bagian ini mengamati mekanisme caching melalui request conditional GET saat membuka `file2.html`. Browser mengirimkan header seperti `If-Modified-Since` untuk mengecek apakah konten masih sama dengan versi terakhir yang sudah disimpan. Jika file belum berubah, server dapat merespons lebih efisien tanpa mengirim ulang seluruh isi dokumen.

#### Tampilan Traffic Conditional GET
<img src="./Assets/http3.png" alt="Tampilan Traffic Conditional GET" style="width:400px"><br>

### 4. Mengambil Dokumen HTML yang Panjang
Pada percobaan ini, file `file3.html` digunakan untuk melihat bagaimana dokumen HTML yang panjang dapat diteruskan melalui beberapa paket TCP. Dari hasil analisis di Wireshark, terlihat bahwa pengiriman data tidak selalu selesai dalam satu paket, melainkan dapat terbagi menjadi beberapa segmen sesuai mekanisme transport layer.

#### Tampilan Paket Terfragmentasi
<img src="./Assets/http4.png" alt="Tampilan Paket Terfragmentasi" style="width:400px"><br>

### 5. Dokumen HTML dengan Embedded Objects
Tahap terakhir mengamati halaman HTML yang memiliki embedded object, misalnya gambar logo yang ikut dimuat bersama halaman utama. Saat browser membuka halaman tersebut, Wireshark akan menampilkan lebih dari satu request HTTP karena objek-objek tambahan harus diambil satu per satu dari server.

#### Tampilan Traffic Embedded Objects
<img src="./Assets/http5.png" alt="Tampilan Traffic Embedded Objects" style="width:400px"><br>

## Ends Of File
 [Kembali ke Halaman Utama](../README.md) 
